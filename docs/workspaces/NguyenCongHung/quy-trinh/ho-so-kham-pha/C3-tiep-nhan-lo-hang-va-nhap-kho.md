# C3 – TIẾP NHẬN LÔ HÀNG MỚI VÀ NHẬP KHO TRUNG TÂM

| Trường | Nội dung |
|---|---|
| Cấp | Cốt lõi |
| Khách hàng | Hàng hóa/Vận hành cần hàng sẵn sàng để phân bổ cho cửa hàng |
| Chủ quy trình dự kiến | Hậu cần/Kho trung tâm; cần xác thực |
| Kích hoạt | Nhận thông báo lô hàng và bộ chứng từ |
| Đầu vào | Thông báo lô hàng, hóa đơn, danh sách đóng gói, danh mục mã hàng, lịch nhận |
| Đầu ra | Phiếu nhập kho, phiếu cất hàng, hồ sơ chênh lệch |
| Outcome dương | Hàng được đối chiếu, ghi nhận và sẵn sàng phân bổ |
| Outcome âm | Thiếu/thừa/sai/hỏng hoặc chứng từ không hợp lệ; mở hồ sơ xử lý |
| Bằng chứng | EV02, EV03, EV06 trong `research.md` |

## Cổng điều kiện dự kiến cần xác thực

1. Đã nhận thông báo lô hàng? 2. Chứng từ đầy đủ? 3. Lịch/điểm nhận phù hợp? 4. Số lượng khớp danh sách đóng gói? 5. Mã hàng/dữ liệu gốc hợp lệ? 6. Chất lượng/bao bì đạt? 7. Chênh lệch xử lý được tại kho? 8. Phiếu nhập kho được duyệt? 9. Cất hàng hoàn tất đúng hạn?

## Vai trò/làn đề xuất

ACFC: Hậu cần, Kho trung tâm, Hàng hóa/Vận hành, Tài chính. Pool ngoài: Chủ thương hiệu và đơn vị logistics thuê ngoài/vận chuyển.

## Dữ liệu và ngoại lệ

Thông báo lô hàng, hóa đơn/danh sách đóng gói, danh sách kiểm tra nhận hàng, phiếu nhập kho, hồ sơ chênh lệch, phiếu cất hàng. Ngoại lệ gồm giao trễ, thiếu/thừa mã hàng, hư hỏng, chứng từ sai và không đủ năng lực tiếp nhận.
