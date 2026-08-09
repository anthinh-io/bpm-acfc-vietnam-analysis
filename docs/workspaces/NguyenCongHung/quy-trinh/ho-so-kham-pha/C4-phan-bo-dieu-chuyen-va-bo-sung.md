# C4 – PHÂN BỔ, ĐIỀU CHUYỂN VÀ BỔ SUNG HÀNG HÓA CHO CHUỖI CỬA HÀNG

| Trường | Nội dung |
|---|---|
| Cấp | Cốt lõi |
| Khách hàng | Cửa hàng nhận đúng hàng, đúng thời điểm và đúng số lượng |
| Chủ quy trình dự kiến | Hàng hóa/Phân bổ phối hợp Vận hành/Kho trung tâm; cần xác thực |
| Kích hoạt | Nhu cầu bổ sung theo số tháng tồn kho, điều chuyển cân bằng tồn hoặc kế hoạch lô hàng |
| Đầu vào | Danh sách phân bổ/điều chuyển, tồn nguồn–đích, sức chứa, lịch giao |
| Đầu ra | Danh sách soạn hàng, phiếu điều chuyển, phiếu giao hàng, xác nhận cửa hàng, hồ sơ chênh lệch |
| Outcome dương | Hàng đến cửa hàng, nhận đủ và tồn được cập nhật |
| Outcome âm | Thiếu nguồn, giao trễ, sai/mất/hư hoặc cửa hàng từ chối nhận |
| Bằng chứng | EV02–EV05 trong `research.md` |

## Cổng điều kiện dự kiến cần xác thực

1. Nhu cầu là bổ sung hay điều chuyển? 2. Nguồn hàng đủ? 3. Cửa hàng đích còn sức chứa? 4. Danh sách điều chuyển đã duyệt? 5. Danh sách đóng gói khớp? 6. Đã đặt lịch phương tiện? 7. Giao đúng lịch? 8. Cửa hàng nhận đủ/đúng? 9. Chênh lệch đã đóng?

## Vai trò/làn đề xuất

ACFC: Hàng hóa/Phân bổ, Vận hành, Kho trung tâm, Cửa hàng. Pool ngoài: Đơn vị logistics thuê ngoài/vận chuyển.

## Dữ liệu và ngoại lệ

Danh sách điều chuyển/bổ sung, danh sách soạn hàng, phiếu điều chuyển, danh sách đóng gói, phiếu giao hàng, xác nhận cửa hàng, hồ sơ chênh lệch/sự cố. Ngoại lệ gồm thiếu nguồn, sai mã/kích cỡ/màu, giao trễ, mất/hư, cửa hàng không nhận và phải lập lại điều chuyển.

## Ưu tiên triển khai

C4 là quy trình đầu tiên phải hoàn thành đầy đủ BPMN, VA/BVA/NVA, bốn loại lãng phí và khung định lượng để rà soát trước 09/08.
