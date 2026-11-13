# Hai lộ trình trong cùng Lab 3

Lab 3 áp dụng **dạy học phân hóa**. Người học có thể tự chọn lộ trình, không bắt buộc theo tên lớp.

## Lộ trình A – Foundation (gợi ý HTTT)

**Mục tiêu:** Hiểu thuật toán K-Means qua thực hành; code đã có các bước thiết yếu để không bị quá tải Python.

1. Notebook 01: xem bảng giao dịch, hiểu các khái niệm **Recency, Frequency, Monetary**. Chạy mã mẫu tạo RFM.
2. Notebook 02: chọn `TRACK = "FOUNDATION"`, dùng `log1p` + `StandardScaler`, thử **k = 2, 3, 4**.
3. Dựa trên bảng Silhouette Score cùng kích thước từng cụm, chọn k hợp lý; giải thích vì sao không chỉ chọn k lớn nhất.
4. Notebook 03: dựa vào RFM gốc, đặt tên từng cụm, viết 2 đề xuất bán hàng/chăm sóc khách hàng.

**Câu hỏi chính:** K-Means làm gì? Vì sao cần chuẩn hóa? Số k ảnh hưởng đến kết quả thế nào? Cụm nào có khách hàng giá trị cao?

## Lộ trình B – Applied (gợi ý PTPM)

**Mục tiêu:** Không lặp lại việc gọi `KMeans.fit_predict()`; tập trung vào năng lực **thiết kế thử nghiệm và bảo vệ quyết định kỹ thuật**.

1. Notebook 01: thực hiện RFM, giải thích các lựa chọn định nghĩa Frequency (số hóa đơn) và Monetary (số tiền).
2. Notebook 02: chọn `TRACK = "APPLIED"`; so sánh hai cách xử lý đặc trưng:
   - `log1p(RFM) -> StandardScaler` (giảm độ lệch của Frequency/Monetary);
   - `RFM trực tiếp -> StandardScaler`.
3. Thử **k = 2, 3, 4, 5**. So sánh Silhouette, độ cân bằng kích thước cụm và mức độ dễ diễn giải. Chọn một cấu hình rồi giải thích bằng số liệu.
4. Notebook 03: đối chiếu profile cụm với giả thuyết ban đầu và bàn về cách kiểm chứng tính hữu ích trong doanh nghiệp.

**Câu hỏi chính:** Khi thay biến đổi đặc trưng, cấu trúc phân cụm thay đổi ra sao? Silhouette cao nhất có luôn dẫn tới phân khúc hữu ích nhất không?

## Thống nhất đánh giá

- **Hai lộ trình cùng rubric 100 điểm**, không dùng điểm cộng chỉ vì làm lộ trình Applied.
- Foundation đạt điểm tối đa khi thực hành đúng, phân tích đầy đủ và ra khuyến nghị có căn cứ.
- Applied đạt điểm tối đa bằng việc tự lựa chọn cấu hình và lý giải thuyết phục, nhưng không bắt buộc thử thêm thuật toán.
- Bạn học giỏi thuộc HTTT có thể chọn Applied, và PTPM muốn củng cố có thể chọn Foundation.
- **Không chấm theo silhouette cao nhất một cách máy móc.** Giá trị kinh doanh và khả năng diễn giải cũng quan trọng.

## Liên kết dữ liệu sản phẩm (gợi ý chung cho cả hai lộ trình)

Trong Notebook 03, học viên có thể xem **3 sản phẩm xuất hiện ở nhiều hóa đơn nhất** trong mỗi cụm. Khuyến khích đặt câu hỏi: top sản phẩm có khác nhau giữa các cụm không, và có căn cứ nào để đề xuất combo không? Phần này **không làm phát sinh điểm bắt buộc mới**.

## Nâng cao tự chọn

Mở [Notebook 04 – Rule-based Customer Clustering](../notebooks/04_rule_based_clustering_optional.ipynb): khai phá luật Apriori cấp hóa đơn, chọn tối đa 8 cặp sản phẩm không trùng, xây dựng Customer × Pair theo việc có mua **cùng một hóa đơn**, rồi thử RFM + Rule Features. So sánh nhãn với RFM baseline bằng **Adjusted Rand Index (ARI)** và profile, không kết luận “tốt hơn” chỉ dựa vào silhouette từ hai không gian đặc trưng khác nhau. Đây **không phải** yêu cầu để đạt điểm tối đa.
