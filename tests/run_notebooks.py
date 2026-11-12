"""Chạy tuần tự 3 notebook từ root để kiểm tra luồng đầy đủ.

python tests/run_notebooks.py

Yêu cầu: đã cài requirements (nbclient, nbformat, ipykernel).
Thực thi notebook trong bộ nhớ; không ghi đè notebook gốc.
"""
from pathlib import Path
import os

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [
    ROOT / "notebooks/01_customer_features.ipynb",
    ROOT / "notebooks/02_kmeans_clustering.ipynb",
    ROOT / "notebooks/03_customer_insights.ipynb",
]

# Matplotlib có thể dùng backend không cần màn hình khi chạy trong CI.
os.environ.setdefault("MPLBACKEND", "Agg")


def main():
    for path in NOTEBOOKS:
        print(f"RUN {path.name}", flush=True)
        notebook = nbformat.read(path, as_version=4)
        client = NotebookClient(
            notebook,
            timeout=120,
            kernel_name="python3",
            resources={"metadata": {"path": str(ROOT)}},
            allow_errors=False,
        )
        client.execute()
        print(f"PASS {path.name}", flush=True)

    processed = ROOT / "data/processed"
    for name in (
        "customer_rfm.csv",
        "clustering_scores.csv",
        "customer_segments.csv",
        "segment_profiles.csv",
    ):
        assert (processed / name).is_file(), name

    print("PASS: 3 notebooks executed; 4 output files exist", flush=True)


if __name__ == "__main__":
    main()
