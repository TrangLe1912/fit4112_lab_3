# FIT4112 – Gợi ý tổ chức Lab 3 cho giảng viên

## Đối tượng

- **HTTT:** K-Means lần đầu → dạy theo *Foundation* có hướng dẫn từng bước.
- **PTPM:** đã học K-Means → dạy theo *Applied* hướng phân tích so sánh và ra quyết định.
- Không khóa cứng lộ trình theo lớp. Tránh để kiến thức đầu vào quyết định điểm tối đa.

## Gợi ý tiến độ 200 phút

| Hoạt động | Phút |
|---|---:|
| Giới thiệu bài toán và trực quan ôn K-Means | 25 |
| Notebook 01 – Tạo đặc trưng RFM | 40 |
| Notebook 02 – K-Means và thử k | 65 |
| Notebook 03 – Diễn giải và khuyến nghị | 50 |
| Chia sẻ kết quả, hoàn thiện báo cáo | 20 |
| **Tổng** | **200** |

Trong 25 phút đầu, người học PTPM có thể khảo sát dữ liệu và đặt giả thuyết; HTTT xem trực quan mô hình từng bước. Không tạo áp lực làm thêm thuật toán cho PTPM.

## Nghi thức kiểm thử trước khi phát cho sinh viên

1. `python -m pip install -r requirements.txt`
2. `python tests/smoke_test.py`
3. `python tests/run_notebooks.py`
4. Mở từng notebook kiểm tra biểu đồ, đường dẫn và câu hỏi tiếng Việt.
5. Thử đổi `TRACK = "APPLIED"` trong Notebook 02, xác nhận có bảng hai cấu hình và xuất được customer_segments.csv.
6. Kiểm tra Notebook 03 ghi `top_products_by_segment.csv` và Notebook 04 chạy được khi dùng đúng `selected_model.json`.

## Giảng viên cần quan sát

- RFM theo **CustomerID**; Frequency là số **hóa đơn duy nhất**, không phải số dòng sản phẩm.
- Recency tính từ **mốc ngày tham chiếu thống nhất**, không dùng `datetime.now()` vì kết quả sẽ thay đổi mỗi năm.
- Mô hình dùng **đặc trưng đã biến đổi và chuẩn hóa**, nhưng diễn giải trên **RFM ban đầu**.
- Random state cố định để sinh viên dễ đối chiếu; cluster label 0/1/2 không phải xếp hạng khách hàng.
- Silhouette có thể ưu ái những cụm hình học, không đồng nghĩa một chiến lược marketing tốt.
- Dữ liệu demo được tạo tổng hợp, có nhiều kiểu hành vi, không đại diện cho một doanh nghiệp thật.

## Phân công theo lộ trình (chung rubric 100)

| Năng lực | Foundation | Applied |
|---|---|---|
| Xử lý RFM | Làm theo mã mẫu, giải thích | Xác minh định nghĩa và giới hạn |
| K-Means | Dùng log+scaler, k=2/3/4 | Thêm scaler trực tiếp, k=2..5 |
| Đánh giá | Silhouette + kích thước cụm | Thêm thay đổi cấu hình và tính diễn giải |
| Phân tích | Tên cụm + 2 hành động | Cùng đầu ra, nêu lý do lựa chọn phương pháp |

Không cộng điểm đặc quyền cho Applied; không trừ điểm Foundation vì không thử thêm cấu hình.

## Cập nhật từ shop_cluster (Lab 3 cũ)

- Notebook 03 phân tích **top 3 sản phẩm theo số hóa đơn trong từng cụm**. Đây là cầu nối trực tiếp sang ý tưởng mua cùng nhau ở Lab 1–2.
- Notebook 04 tự chọn rút gọn từ [shop_cluster](https://github.com/TrangLe1912/shop_cluster), chỉ khai phá một số **cặp sản phẩm không trùng**, không dùng 200 luật và không nhân trọng số lift tùy tiện.
- Đặc trưng pair chỉ bật khi **cả hai sản phẩm xuất hiện cùng một hóa đơn** của khách, tránh nhầm hành vi mua khác lần với đồng mua.
- So sánh nhãn phân cụm bằng ARI và profile. Không đối chiếu silhouette từ các không gian đặc trưng khác nhau để kết luận mô hình nâng cấp tốt hơn.
- Dữ liệu demo cập nhật tên/SKU theo nhóm sở thích mà **không thay Quantity, UnitPrice, InvoiceDate, CustomerID hoặc InvoiceNo**, giữ RFM tái lập.

## Tiếp nối Lab 1–2

Thử ghép đặc trưng xu hướng mua sản phẩm hay luật kết hợp vào RFM chỉ là **mở rộng** sau khi học xong Lab 3 cốt lõi. Với người mới, làm Feature Engineering từ luật ngay trong bài đầu tiên về K-Means là quá tải.
