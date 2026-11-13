# FIT4112 · Phiếu thực hành Lab 3: Phân cụm khách hàng

**Chủ đề:** Customer Segmentation using RFM & K-Means  
**Hình thức:** Cá nhân, thực hành trong 1 buổi (dự kiến 200 phút)  
**Đầu ra:** 3 notebook đã chạy + báo cáo tối đa 2 trang  
**Lộ trình:** `FOUNDATION` hoặc `APPLIED` – **tự chọn**, cùng điểm tối đa.

## 1. Chuẩn bị

- Tải repo, cài `requirements.txt`, mở Jupyter.
- Chạy lần lượt Notebook 01 → 02 → 03.
- Dữ liệu mặc định là **giả lập**. Nếu thiếu thời gian ở bước 01, dùng bảng RFM trong `data/starter/` cho bước 02 trước, sau đó hoàn thiện 01.

## 2. Hoạt động chung

### A – Từ giao dịch sang RFM (20 điểm)

1. Chạy `01_customer_features.ipynb`.
2. Giải thích mỗi hàng trong bảng RFM đại diện cho gì.
3. Ghi ý nghĩa của Recency, Frequency, Monetary; trình bày cách tính.
4. Giải thích vì sao loại hoá đơn hủy, dòng Quantity/UnitPrice không dương và khách hàng bị thiếu ID.

### B – Phân cụm và chuẩn hóa (20 điểm)

1. Chạy `02_kmeans_clustering.ipynb`.
2. Đọc code `KMeans(n_clusters=k, random_state=42, n_init=10)`.
3. Trả lời: Tại sao không nên dùng RFM thô trực tiếp với khoảng cách Euclidean khi thang đo khác biệt lớn?
4. Ghi cấu hình đặc trưng đã dùng và giá trị k được chọn.

### C – Thử nghiệm, đánh giá (25 điểm)

- **Foundation:** thử `k = 2,3,4` với `log1p + StandardScaler`. Dùng silhouette và số thành viên cụm để chọn k.
- **Applied:** thử `k = 2,3,4,5` với hai biến đổi `log1p + StandardScaler` và `StandardScaler` trực tiếp. Giải thích lựa chọn cấu hình/k dựa vào silhouette, phân bố cụm, khả năng diễn giải.

**Cùng chuẩn chấm:** có thực nghiệm đối chiếu và lựa chọn được bảo vệ bằng kết quả cụ thể. **Không yêu cầu** cấu hình Applied có silhouette cao hơn.

### D – Diễn giải và đặt tên cụm (20 điểm)

1. Chạy `03_customer_insights.ipynb`.
2. Dùng **giá trị RFM gốc** để mô tả các cụm (trung vị, số khách hàng).
3. Đặt tên có ý nghĩa cho ít nhất 3 nhóm nếu cấu hình chọn có ít nhất 3 cụm; nếu chọn k = 2, giải thích hai nhóm và sự phù hợp của k.
4. Không gán tên dựa vào số hiệu cluster 0/1/2; nhãn là ngẫu nhiên và có thể đổi thứ tự.

### E – Đề xuất và báo cáo (15 điểm)

1. Đưa ra **2 khuyến nghị** khác nhau cho các nhóm khách hàng.
2. Với mỗi khuyến nghị, chỉ ra số liệu RFM làm cơ sở.
3. Nêu **ít nhất 1 giới hạn**: dữ liệu giả lập, không có kết quả mua sau chiến dịch, thay đổi theo thời điểm đo RFM, hoặc silhouette không phản ánh trực tiếp hiệu quả kinh doanh.

## 3. Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| A. Tiền xử lý, xác định khách hàng và RFM đúng | 20 |
| B. Fit K-Means đúng và giải thích chuẩn hóa | 20 |
| C. Thử k/cấu hình và đánh giá có căn cứ | 25 |
| D. Profile và đặt tên cụm theo số liệu | 20 |
| E. Hai đề xuất kinh doanh, giới hạn và báo cáo | 15 |
| **Tổng** | **100** |

**Công bằng:** lộ trình Foundation và Applied đều đạt tối đa 100 điểm nếu đạt các yêu cầu của lộ trình đã chọn.

## 4. Nộp bài

- 3 file `.ipynb` với kết quả/biểu đồ và câu trả lời ngắn.
- `LAB03_REPORT.md` hoặc PDF theo [mẫu](REPORT_TEMPLATE.md), tối đa 2 trang.
- Có thể nộp repository GitHub cá nhân; **không commit** thư mục môi trường, cache hoặc dữ liệu khách hàng thật.

## 5. Liên kết Lab 1–2 và mở rộng (không bắt buộc)

Trong Notebook 03 có phần tự quan sát **3 sản phẩm phổ biến nhất theo số hóa đơn trong từng cụm**. Hãy so sánh hai cụm và giải thích vì sao sản phẩm phổ biến chưa chắc là đặc trưng riêng cho một nhóm.

Nếu muốn tìm hiểu thêm, chạy [Notebook 04 – Rule-based Clustering](../notebooks/04_rule_based_clustering_optional.ipynb). Bạn sẽ xây dựng các đặc trưng đồng mua sản phẩm từ luật Apriori và so sánh K-Means dựa trên RFM với K-Means dựa trên RFM + Rule Features. Không cần Papermill hoặc chạy lại Lab 1–2.

**Notebook 04 không tính là điều kiện để đạt tối đa 100 điểm.**
