# C4 – PHÂN TÍCH QUY TRÌNH

## VA/BVA/NVA

| Hoạt động | Phân loại | Lý do/khắc phục |
|---|---|---|
| Xác định nhu cầu bổ sung/điều chuyển | BVA | Cân bằng tồn theo kế hoạch. |
| Lập danh sách điều chuyển | VA | Đưa đúng hàng đến đúng cửa hàng. |
| Kiểm tra tồn nguồn và sức chứa nơi nhận | BVA | Ngăn hủy/lập lại; dùng dữ liệu đồng bộ. |
| Soạn, đóng gói và bàn giao hàng | VA | Đưa hàng đến trạng thái sẵn sàng bán tại cửa hàng. |
| Cửa hàng nhận và cập nhật tồn | BVA | Cần cho kiểm soát tài sản và bán hàng. |
| Chờ đặt lịch/nhận hàng | NVA | Chờ (Hold); đặt lịch và theo dõi yêu cầu tồn. |
| Điều chuyển lại do sai/mất/hư | NVA | Lỗi (Defects); quét mã, lưu ảnh đóng gói và một mã hồ sơ. |
| Nhập lặp điều chuyển trên nhiều hệ thống | NVA | Xử lý dư (Over-processing); dùng một mã điều chuyển. |

## Bốn loại lãng phí

| Loại | Biểu hiện cần kiểm chứng | Cải tiến |
|---|---|---|
| Di chuyển (Move) | Hàng và dữ liệu đi qua nhiều điểm bàn giao | Tối ưu tuyến, một mã điều chuyển và theo dõi. |
| Chờ (Hold) | Chờ nguồn hàng, duyệt, nhận hàng hoặc xác nhận cửa hàng | Thời hạn từng chặng và cảnh báo. |
| Xử lý dư (Over-processing) | Nhập lại danh sách, kiểm tra cùng mã hàng nhiều lần | Dữ liệu gốc, mã vạch và danh sách kiểm tra theo rủi ro. |
| Lỗi (Defects) | Sai mã/kích cỡ/màu, thiếu, mất hoặc hư | Quét hai điểm, ảnh đóng gói và mẫu xử lý chuẩn. |

## Vấn đề, nguyên nhân và khắc phục

| Vấn đề cần kiểm chứng | Nguyên nhân giả định | Khắc phục đề xuất |
|---|---|---|
| Tỷ lệ cấp đủ thấp hoặc hết hàng lặp lại | Nguồn hàng, sức chứa và nhu cầu chưa đồng bộ | Đồng bộ tồn/sức chứa trước duyệt và ưu tiên theo quy tắc được xác thực. |
| Điều chuyển trễ | Đặt lịch, nhận hàng hoặc xác nhận cửa hàng không có thời hạn rõ | Theo dõi mã điều chuyển xuyên suốt và cảnh báo từng mốc. |
| Sai/mất/hư khi bàn giao | Kiểm đếm và bằng chứng đóng gói chưa nhất quán | Quét hai điểm, lưu ảnh, biên bản và một mã hồ sơ ngoại lệ. |

## KPI định lượng

Khung ghi nhận: sau phỏng vấn điền ba mốc **thấp nhất – thường gặp – cao nhất** cho từng KPI; hiện chưa có số ACFC.

| KPI | Công thức/dữ liệu cần lấy | Trạng thái |
|---|---|---|
| Tỷ lệ cấp đủ | Số lượng cấp đủ / số lượng yêu cầu | Chưa có số ACFC |
| Thời gian chu kỳ điều chuyển | Thời điểm nhận - thời điểm tạo điều chuyển | Chưa có số ACFC |
| Tỷ lệ giao đúng hạn | Điều chuyển đúng hạn / tổng điều chuyển | Chưa có số ACFC |
| Tỷ lệ hết hàng | Cửa hàng/mã hàng bị thiếu / tổng cơ hội bán | Chưa có số ACFC |
| Tỷ lệ sai/mất/hư | Điều chuyển có lỗi / tổng điều chuyển | Chưa có số ACFC |
| Chi phí mỗi điều chuyển | Tổng chi phí / số điều chuyển | Chưa có số ACFC |

## Đề xuất tương lai (TO-BE) sơ bộ

Tạo một mã điều chuyển, đồng bộ tồn và sức chứa trước khi duyệt, giữ tồn có thời hạn cho yêu cầu đủ điều kiện, quét lúc soạn và nhận, đặt thời hạn giao, và mở một hồ sơ ngoại lệ cho mỗi điều chuyển.
