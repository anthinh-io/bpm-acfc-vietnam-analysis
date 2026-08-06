# C3 – PHÂN TÍCH QUY TRÌNH

## VA/BVA/NVA

| Hoạt động | Phân loại | Lý do/khắc phục |
|---|---|---|
| Kiểm tra bộ chứng từ và thông báo lô hàng | BVA | Kiểm soát tính hợp lệ; dùng danh sách kiểm tra điện tử. |
| Nhận và đếm hàng | VA | Đưa hàng vào trạng thái có thể bán/phân bổ. |
| Kiểm tra mã hàng/số lượng/tình trạng | BVA | Ngăn lỗi tồn kho; quét mã và lưu ảnh bằng chứng. |
| Cất hàng vào vị trí và cập nhật phiếu nhập kho | VA | Đưa hàng vào trạng thái sẵn sàng trong kho. |
| Chờ xe hoặc chứng từ | NVA | Chờ (Hold); đặt thời hạn xử lý. |
| Đếm lại do chênh lệch | NVA | Lỗi (Defects); chuẩn hóa danh sách đóng gói và quét mã. |

## Bốn loại lãng phí

| Loại | Biểu hiện cần kiểm chứng | Cải tiến |
|---|---|---|
| Di chuyển (Move) | Bàn giao chứng từ/hàng qua nhiều điểm | Một mã lô và luồng bàn giao rõ. |
| Chờ (Hold) | Chờ lịch nhận, phản hồi hoặc xử lý chênh lệch | Bảng theo dõi lô quá hạn. |
| Xử lý dư (Over-processing) | Đối chiếu/nhập lại hóa đơn, danh sách đóng gói, mã hàng | Tích hợp dữ liệu gốc và mã vạch. |
| Lỗi (Defects) | Thiếu, thừa, sai mã hàng, hỏng bao bì | Quét khi nhận, lưu ảnh và lập yêu cầu xử lý sớm. |

## Vấn đề, nguyên nhân và khắc phục

| Vấn đề cần kiểm chứng | Nguyên nhân giả định | Khắc phục đề xuất |
|---|---|---|
| Thời gian từ bến nhận đến nhập kho kéo dài | Chờ lịch nhận, chứng từ hoặc cất hàng | Đặt thời hạn từng chặng, đặt lịch trước và theo dõi lô quá hạn. |
| Chênh lệch khi nhận hàng | Danh sách đóng gói, hóa đơn và hàng thực tế không khớp | Quét theo mã hàng, lưu ảnh và dùng một mã hồ sơ chênh lệch. |
| Phiếu nhập kho bị treo | Thiếu người duyệt hoặc chứng từ bổ sung | Quy định người thay thế, nhắc hạn và khóa trạng thái sẵn sàng. |

## KPI định lượng

Khung ghi nhận: sau phỏng vấn điền ba mốc **thấp nhất – thường gặp – cao nhất** cho từng KPI; hiện chưa có số ACFC.

| KPI | Công thức/dữ liệu cần lấy | Trạng thái |
|---|---|---|
| Thời gian bến nhận–nhập kho | Thời điểm hàng sẵn sàng - thời điểm đến | Chưa có số ACFC |
| Độ chính xác chứng từ | Lô không phải bổ sung chứng từ / tổng lô | Chưa có số ACFC |
| Tỷ lệ chênh lệch khi nhận | Lô có chênh lệch / tổng lô | Chưa có số ACFC |
| Tỷ lệ cất hàng đúng hạn | Lô cất đúng hạn / tổng lô | Chưa có số ACFC |
| Chi phí mỗi lô | Chi phí nhận/nhập kho / số lô | Chưa có số ACFC |

## Đề xuất tương lai (TO-BE) sơ bộ

Dùng một mã lô xuyên suốt, kiểm tra chứng từ trước khi xe đến, quét mã vạch khi nhận, tách trạng thái `đã nhận`, `tạm giữ`, `sẵn sàng`, và tự mở hồ sơ chênh lệch khi lệch.
