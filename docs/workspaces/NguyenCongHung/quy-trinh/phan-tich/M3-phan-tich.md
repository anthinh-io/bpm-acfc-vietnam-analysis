# M3 – PHÂN TÍCH QUY TRÌNH

## VA/BVA/NVA

| Hoạt động | Phân loại | Lý do/khắc phục |
|---|---|---|
| Thu thập dữ liệu bán hàng, tồn kho và dự báo | BVA | Cần cho quyết định; dùng một bộ dữ liệu chuẩn. |
| Phân tích tỷ lệ bán và số tháng tồn kho | BVA | Hỗ trợ lập kế hoạch; tự động hóa bảng theo dõi. |
| Lập kế hoạch phân bổ | VA | Tạo cơ cấu hàng phù hợp nhu cầu cửa hàng. |
| Kiểm tra biên lợi nhuận/ngân sách | BVA | Kiểm soát tài chính; đặt quy tắc tự động. |
| Chờ dữ liệu hoặc phê duyệt | NVA | Chờ (Hold); đặt thời hạn và cảnh báo quá hạn. |
| Nhập lại cùng một báo cáo | NVA | Xử lý dư (Over-processing); dùng một nguồn dữ liệu gốc. |
| Lập lại kế hoạch do dữ liệu sai | NVA | Lỗi (Defects); kiểm tra bắt buộc trước khi gửi. |

## Bốn loại lãng phí

| Loại | Biểu hiện cần kiểm chứng | Cải tiến |
|---|---|---|
| Di chuyển (Move) | Chuyển tệp qua nhiều kênh | Một nơi lưu trữ và một mã kế hoạch. |
| Chờ (Hold) | Chờ báo cáo, ngân sách hoặc phê duyệt | Thời hạn, người phụ trách và cảnh báo. |
| Xử lý dư (Over-processing) | Nhập/đối chiếu trùng dữ liệu | Bảng theo dõi và quy tắc tự động. |
| Lỗi (Defects) | Dự báo/mã hàng sai làm lập lại kế hoạch | Kiểm tra dữ liệu gốc và phiên bản. |

## Vấn đề, nguyên nhân và khắc phục

| Vấn đề cần kiểm chứng | Nguyên nhân giả định | Khắc phục đề xuất |
|---|---|---|
| Kế hoạch phải lập lại | Dữ liệu dự báo, tồn hoặc dữ liệu gốc chưa đồng nhất | Khóa phiên bản, kiểm tra trước khi gửi và ghi rõ người phụ trách. |
| Phê duyệt chậm | Thiếu thời hạn và tiêu chí duyệt thống nhất | Thiết lập hạn duyệt, hàng đợi quá hạn và chuyển cấp. |
| Phân bổ lệch nhu cầu | Số tháng tồn, tỷ lệ bán hoặc sức chứa chưa đồng bộ | Dùng bảng theo dõi chung và quy tắc phân bổ cần xác thực. |

## Phân tích định lượng (Thời gian – Chất lượng – Chi phí)

Rubric yêu cầu **tính toán** trên ba nhóm chỉ số: Thời gian, Chất lượng, Chi phí. Do chưa tiếp cận được số nội bộ ACFC, phần dưới trình bày **công thức + một ví dụ tính toán minh họa** để thể hiện phương pháp.

> ⚠️ **Lưu ý liêm chính học thuật:** mọi con số ở cột "Dữ liệu giả định" và "Kết quả tính" bên dưới là **số nhóm tự đặt để minh họa cách tính — KHÔNG phải số liệu thực của ACFC**. Sau phỏng vấn/workshop sẽ thay bằng ba mốc *thấp nhất – thường gặp – cao nhất* từ dữ liệu thật rồi áp lại đúng công thức ở cột 2.

### a) Nhóm Thời gian (Time)

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Thời gian chu kỳ lập kế hoạch (Cycle time) | Thời điểm phát hành − thời điểm bắt đầu | Bắt đầu 09:00 ngày 1 → phát hành 17:00 ngày 5 (5 ngày làm việc) | **40 giờ** |
| Thời gian xử lý thực (Processing/VA+BVA) | Σ thời gian các bước tạo/kiểm/duyệt (B1–B10) | ≈ 14 giờ | **14 giờ** |
| Thời gian chờ (Waiting/NVA) | Cycle − Processing | 40 − 14 | **26 giờ** |
| Hiệu suất chu kỳ (PCE) | Processing / Cycle time | 14 / 40 | **35%** |
| Thời gian phê duyệt | Thời điểm duyệt − thời điểm trình | Trình 14:00 ngày 3 → duyệt 10:00 ngày 5 | **≈ 44 giờ** |

*Nhận xét: PCE 35% nghĩa là gần 2/3 thời gian là chờ (NVA) — khớp với lãng phí "Chờ (Hold)" ở trên.*

### b) Nhóm Chất lượng (Quality)

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Độ chính xác dự báo | 1 − abs(dự báo − thực tế) / thực tế | Dự báo 1.000, thực tế 1.200 | **83,3%** |
| Tỷ lệ bán qua (Sell-through) | Số bán / số khả dụng | 750 / 1.000 | **75%** |
| Số tháng tồn kho (WoS) | Tồn cuối kỳ / tốc độ bán bình quân tháng | 600 / 250 | **2,4 tháng** |
| Tỷ lệ thay đổi phân bổ | Kế hoạch sửa / kế hoạch phát hành | 15 / 100 | **15%** |

### c) Nhóm Chi phí (Cost)

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Chi phí lập lại kế hoạch (Defects) | Số lần lập lại × giờ công × đơn giá giờ | 2 lần × 8 giờ × 150.000đ | **2.400.000đ / mùa** |
| Chi phí đọng vốn tồn dư (Over-stock) | Giá trị tồn dư × chi phí giữ hàng/tháng | 200 sp × 300.000đ × 2% | **1.200.000đ / tháng** |
| Chi phí chờ phê duyệt (Hold) | Số kế hoạch × giờ chờ × đơn giá giờ | 4 × 26 giờ × 150.000đ | **15.600.000đ / mùa** |

*Đơn giá giờ công 150.000đ là giả định minh họa; thay bằng đơn giá thật khi có dữ liệu nhân sự ACFC.*

## Đề xuất tương lai (TO-BE) sơ bộ

Chuẩn hóa một bộ dữ liệu bán hàng–tồn kho–dự báo, tự động kiểm tra biên lợi nhuận/số tháng tồn, gắn người phụ trách và thời hạn, lưu một phiên bản kế hoạch và cảnh báo khi cần lập lại.

## Bảng đề xuất khắc phục theo lãng phí

| Loại lãng phí | Vấn đề | Đề xuất khắc phục | Người phụ trách đề xuất | Thời hạn đề xuất |
|---|---|---|---|---|
| Di chuyển (Move) | Bản kế hoạch/báo cáo bị chuyển qua nhiều kênh (email, chat, bảng tính rời) | Gộp về một nơi lưu trữ dùng chung và một mã kế hoạch duy nhất theo mùa | Hàng hóa/Phân bổ | Ngắn hạn — áp dụng từ chu kỳ kế hoạch kế tiếp |
| Chờ (Hold) | Chờ báo cáo, ngân sách hoặc phê duyệt không có hạn xử lý rõ ràng | Đặt SLA cho từng bước duyệt, gắn người phụ trách và cảnh báo tự động khi quá hạn | Quản lý Hàng hóa/Phân bổ | Ngắn hạn — thiết lập SLA trong 1 chu kỳ |
| Xử lý dư (Over-processing) | Nhập/đối chiếu trùng dữ liệu bán hàng – tồn kho từ nhiều nguồn | Chuẩn hóa một nguồn dữ liệu gốc, tự động hóa bảng theo dõi tỷ lệ bán qua/số tháng tồn | Hàng hóa/Phân bổ phối hợp IT/hệ thống | Trung hạn — 2–3 chu kỳ kế hoạch |
| Lỗi (Defects) | Dự báo hoặc mã hàng sai khiến phải lập lại kế hoạch | Bắt buộc kiểm tra dữ liệu gốc và khóa phiên bản trước khi trình duyệt | Hàng hóa/Phân bổ | Ngắn hạn — áp dụng ngay từ lần trình kế hoạch tiếp theo |

Ghi chú: người phụ trách và thời hạn ở trên là đề xuất của nhóm dựa trên phân tích lãng phí, chưa phải cam kết chính thức của ACFC; cần xác nhận lại nếu có phỏng vấn/workshop với chủ quy trình.
