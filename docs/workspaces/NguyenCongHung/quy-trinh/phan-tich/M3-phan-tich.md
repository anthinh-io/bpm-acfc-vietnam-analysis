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

## KPI định lượng

Khung ghi nhận: sau phỏng vấn điền ba mốc **thấp nhất – thường gặp – cao nhất** cho từng KPI; hiện chưa có số ACFC.

| KPI | Công thức/dữ liệu cần lấy | Trạng thái |
|---|---|---|
| Độ chính xác dự báo | 1 - abs(dự báo - thực tế) / thực tế | Chưa có số ACFC |
| Tỷ lệ bán qua | Số bán / số khả dụng | Chưa có số ACFC |
| Số tháng tồn kho | Tồn cuối kỳ / tốc độ bán bình quân | Chưa có số ACFC |
| Thời gian phê duyệt | Thời điểm duyệt - thời điểm gửi | Chưa có số ACFC |
| Tỷ lệ thay đổi phân bổ | Kế hoạch sửa / kế hoạch phát hành | Chưa có số ACFC |

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
