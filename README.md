# FIT4112 – LAB 3 | Customer Segmentation với K-Means

**Học phần:** Khai phá dữ liệu (Data Mining)  
**Case study:** Phân khúc khách hàng từ dữ liệu bán lẻ theo **RFM (Recency – Frequency – Monetary)**  
**Thiết kế:** **Một lab chung – hai lộ trình** dành cho sinh viên **HTTT** (chưa học K-Means) và **PTPM** (đã học K-Means).

> Hai lộ trình có **cùng mục tiêu học tập, cùng rubric 100 điểm, cùng khả năng đạt điểm tối đa**. Sinh viên được chọn lộ trình phù hợp năng lực, không bắt buộc theo lớp.

Tiếp nối [Lab 1: Apriori](https://github.com/TrangLe1912/fit4112_lab_1) và [Lab 2: FP-Growth](https://github.com/TrangLe1912/fit4112_lab_2): hai bài trước tìm **những sản phẩm nào được mua cùng nhau**; bài này trả lời **những khách hàng nào có hành vi mua tương tự nhau**.

## 1. Mục tiêu

Sau Lab 3, sinh viên có thể:
1. Chuyển dữ liệu **dòng giao dịch** thành dữ liệu **mỗi khách hàng một dòng** với các đặc trưng RFM.
2. Giải thích trực quan ý tưởng K-Means, vai trò của chuẩn hóa dữ liệu, số cụm `k`.
3. Chạy K-Means với scikit-learn, thử ít nhất **k = 2, 3, 4** và đọc **Silhouette Score**.
4. Phân tích profile của từng cụm bằng RFM gốc, đặt tên cụm có căn cứ và đề xuất chiến lược.
5. Nêu giới hạn: các cụm là mô tả từ dữ liệu, không phải chân lý hay phân nhóm cố định.

**Không bắt buộc:** viết thuật toán K-Means từ đầu, dashboard Streamlit, phân cụm từ vector luật kết hợp, thử nhiều thuật toán, báo cáo dài.

## 2. Ba notebook chính

| Thứ tự | Notebook | Nội dung |
|---|---|---|
| 01 | [Customer Feature Engineering](notebooks/01_customer_features.ipynb) | Đọc/lọc giao dịch, tính RFM, xuất bảng khách hàng |
| 02 | [K-Means Clustering](notebooks/02_kmeans_clustering.ipynb) | Chuẩn hóa, chọn k, fit K-Means, đánh giá silhouette |
| 03 | [Customer Segmentation Insights](notebooks/03_customer_insights.ipynb) | Thống kê cụm, đặt tên, diễn giải và đề xuất |

Chạy **01 → 02 → 03** trong Jupyter hoặc VS Code. Nếu Notebook 01 còn khó, có thể bắt đầu từ bảng RFM mẫu đã chuẩn bị sẵn trong `data/starter/` để học Notebook 02–03; sau đó quay lại hoàn thiện Notebook 01.

## 3. Hai lộ trình học tập

| | **Foundation – HTTT** | **Applied – PTPM** |
|---|---|---|
| Nền tảng | Lần đầu học K-Means | Đã biết K-Means ở Học máy |
| Hướng dẫn | Code mẫu và giải thích từng bước | Code mẫu + tự chủ thiết kế thử nghiệm |
| Đặc trưng | Dùng RFM với `log1p` và StandardScaler | So sánh *log1p + scaler* với *scaler trực tiếp* |
| Chọn k | Thử k = 2,3,4 và giải thích lựa chọn | Thử k = 2,3,4,5; bảo vệ lựa chọn k, đặc trưng |
| Đầu ra chung | Bảng phân khúc, đặt tên cụm, 2 khuyến nghị | Cùng đầu ra, nhưng có lập luận so sánh cấu hình |
| Điểm tối đa | **100/100** | **100/100** |

Ở Notebook 02, đổi `TRACK = "FOUNDATION"` thành `"APPLIED"` nếu muốn chạy lộ trình nâng cao. Xem [Hướng dẫn hai lộ trình](docs/TRACKS.md).

## 4. Cài đặt

Python 3.11 hoặc 3.12:

```bash
git clone https://github.com/TrangLe1912/fit4112_lab_3.git
cd fit4112_lab_3
python -m venv .venv
```

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

```bash
python -m pip install -r requirements.txt
jupyter lab
```

Trong JupyterLab hoặc VS Code (có Jupyter extension), mở lần lượt 3 notebook và **Run All** hoặc chạy từng cell. Đường dẫn được thiết kế chạy cả khi notebook mở từ thư mục `notebooks/` hoặc thư mục gốc repo.

## 5. Dữ liệu và đầu ra

```text
fit4112_lab_3/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/retail_transactions_demo.csv   # dữ liệu bán lẻ GIẢ LẬP
│   └── starter/customer_rfm.csv           # bảng RFM mẫu cho Foundation
├── notebooks/
│   ├── 01_customer_features.ipynb
│   ├── 02_kmeans_clustering.ipynb
│   └── 03_customer_insights.ipynb
├── docs/
│   ├── TRACKS.md
│   ├── LAB03_STUDENT.md
│   ├── REPORT_TEMPLATE.md
│   └── INSTRUCTOR_GUIDE.md
├── tests/
│   ├── smoke_test.py
│   └── run_notebooks.py
└── .github/workflows/validate.yml
```

Dữ liệu demo có các hồ sơ hành vi khác nhau và vài dòng lỗi có chủ ý để luyện làm sạch. **Không dùng dữ liệu giả lập để suy luận về khách hàng thật.**

Các notebook sinh tệp tại `data/processed/` (được gitignore):
- `customer_rfm.csv` – RFM trước mô hình.
- `customer_segments.csv` – RFM gốc + nhãn cụm.
- `clustering_scores.csv` – chỉ số các cấu hình thử nghiệm.
- `segment_profiles.csv` – mô tả từng cụm.

Có thể dùng dữ liệu thật sau khi nắm chắc quy trình; cần tuân thủ quy định quyền truy cập và bảo vệ dữ liệu khách hàng.

## 6. Bài tập và cách chấm

Xem [Phiếu thực hành Lab 3](docs/LAB03_STUDENT.md), [mẫu báo cáo](docs/REPORT_TEMPLATE.md). Mỗi sinh viên nộp 3 notebook và báo cáo ngắn **tối đa 2 trang**.

| Tiêu chí | Điểm |
|---|---:|
| Chuẩn bị dữ liệu và hiểu RFM | 20 |
| Chạy K-Means đúng và giải thích chuẩn hóa | 20 |
| Thử k, đánh giá cụm và lựa chọn có căn cứ | 25 |
| Diễn giải, đặt tên cụm bằng số liệu RFM | 20 |
| Đề xuất hành động và báo cáo rõ ràng | 15 |
| **Tổng** | **100** |

**Đạt điểm tối đa không phụ thuộc việc chọn Foundation hay Applied.**

## 7. Kiểm thử dành cho giảng viên

```bash
python tests/smoke_test.py
python tests/run_notebooks.py
```

Lệnh thứ hai sẽ chạy cả 3 notebook theo thứ tự (chế độ Foundation mặc định) và báo lỗi nếu một cell thất bại. GitHub Actions cũng có workflow kiểm tra khi push.

## 8. Lỗi thường gặp

- **Chưa có `customer_rfm.csv`:** Notebook 02 có thể đọc trực tiếp bảng mẫu `data/starter/customer_rfm.csv`.
- **Chưa có `customer_segments.csv`:** phải chạy Notebook 02 trước Notebook 03.
- **`ModuleNotFoundError: sklearn`:** cài đúng kernel qua `python -m pip install -r requirements.txt`.
- **Silhouette khác kết quả minh họa:** số liệu phụ thuộc cấu hình, phiên bản và mẫu; cần giải thích lựa chọn, không cần trùng một đáp án duy nhất.
- **Nhãn cụm 0/1/2 khác bạn học:** số nhãn không có ý nghĩa thứ tự; mô tả cụm bằng RFM, **không so số hiệu cụm với nhau**.

**Triết lý lab:** mô hình chỉ là công cụ; trọng tâm là **biến dữ liệu giao dịch thành phân khúc có thể giải thích và hỗ trợ quyết định kinh doanh**.
