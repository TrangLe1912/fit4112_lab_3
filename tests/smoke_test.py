"""Kiểm tra dữ liệu demo và luồng RFM -> K-Means (không cần Jupyter)."""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/retail_transactions_demo.csv"
STARTER = ROOT / "data/starter/customer_rfm.csv"
REF = pd.Timestamp("2026-07-01")


def rebuild_rfm():
    df = pd.read_csv(
        RAW,
        dtype={"InvoiceNo": "string", "StockCode": "string", "CustomerID": "string"},
    )
    assert len(df) == 933, "Đã thay đổi dataset demo ngoài dự kiến"
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    df["CustomerID"] = df["CustomerID"].str.strip()
    valid = (
        df["InvoiceNo"].notna()
        & ~df["InvoiceNo"].str.startswith("C", na=False)
        & df["CustomerID"].notna()
        & df["CustomerID"].ne("")
        & df["Quantity"].gt(0)
        & df["UnitPrice"].gt(0)
        & df["Country"].eq("United Kingdom")
        & df["InvoiceDate"].notna()
        & df["InvoiceDate"].lt(REF)
    )
    clean = df.loc[valid].copy()
    clean["Revenue"] = clean["Quantity"] * clean["UnitPrice"]
    result = (
        clean.groupby("CustomerID")
        .agg(
            LastPurchase=("InvoiceDate", "max"),
            Frequency=("InvoiceNo", "nunique"),
            Monetary=("Revenue", "sum"),
        )
        .reset_index()
    )
    result["Recency"] = (
        REF.normalize() - result["LastPurchase"].dt.normalize()
    ).dt.days
    return result[["CustomerID", "Recency", "Frequency", "Monetary"]].sort_values(
        "CustomerID"
    ).reset_index(drop=True), clean


def main():
    actual, clean = rebuild_rfm()
    expected = pd.read_csv(STARTER, dtype={"CustomerID": "string"})
    expected = expected.sort_values("CustomerID").reset_index(drop=True)

    assert actual.shape == (96, 4)
    assert clean["InvoiceNo"].nunique() > 100
    assert actual["CustomerID"].equals(expected["CustomerID"])
    assert actual["Recency"].equals(expected["Recency"])
    assert actual["Frequency"].equals(expected["Frequency"])
    assert np.allclose(actual["Monetary"], expected["Monetary"], atol=1e-6)
    print("PASS: RFM từ giao dịch khớp dữ liệu starter (96 khách hàng)")

    x = np.log1p(actual[["Recency", "Frequency", "Monetary"]].astype(float))
    scaled = StandardScaler().fit_transform(x)
    for k in (2, 3, 4, 5):
        labels = KMeans(n_clusters=k, random_state=42, n_init=10).fit_predict(
            scaled
        )
        score = silhouette_score(scaled, labels)
        assert np.isfinite(score)
        assert len(set(labels)) == k
        print(f"PASS: k={k} | silhouette={score:.3f}")

    print("PASS: dữ liệu và K-Means đạt kiểm tra cơ bản")


if __name__ == "__main__":
    main()
