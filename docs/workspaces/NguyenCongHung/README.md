# Workspace Nguyễn Công Hưng – ACFC

**Sinh viên:** Nguyễn Công Hưng  
**MSSV:** 24730100

## Phạm vi sở hữu

**Cập nhật 11/08/2026:** yêu cầu chung của nhóm rút gọn còn **1 Quản lý + 1 Hỗ trợ** bắt buộc mỗi thành viên (nhóm đã đủ tối thiểu 6 quy trình BPMN + phân tích). Hưng hoàn thiện **M3 và S3** theo yêu cầu bắt buộc, đồng thời bổ sung thêm **S4** (quy trình Hỗ trợ thứ hai, không trùng mã/nội dung với quy trình của thành viên khác) từ nội dung công khai trên trang chủ ACFC. C3/C4 không còn trong phạm vi bài làm tuần này nên đã gỡ khỏi workspace.

| Mã | Cấp | Quy trình | Sơ đồ BPMN (trong `diagrams/`) | Trạng thái |
|---|---|---|---|---|
| M3 | Quản lý | Lập kế hoạch mua hàng và phân bổ hàng hóa theo mùa | `bpmn-hoach-dinh-phan-bo-hang-hoa-m3.svg` | Xong bản nháp — AS-IS + BPMN + phân tích định lượng |
| S3 | Hỗ trợ | Kiểm kê và xử lý chênh lệch tồn kho | `bpmn-kiem-ke-ton-kho-s2.svg` | Xong bản nháp — AS-IS + BPMN + phân tích định lượng |
| S4 | Hỗ trợ | Đăng ký, xác thực OTP & kích hoạt tài khoản thành viên | `bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg` | Xong bản nháp — AS-IS + BPMN (8 cổng XOR, có Split & Join) + phân tích định lượng |

> Lưu ý mã: file trong `diagrams/` dùng hậu tố nhóm (`m3`, `s2`, `s3`) khác với mã workspace (M3, S3, S4). Ánh xạ: S3 (kiểm kê) ↔ `...-s2`, S4 (kích hoạt tài khoản) ↔ `...-s3`. Cần thống nhất lại bảng ánh xạ khi gộp vào báo cáo chung.

README này chỉ xác nhận phạm vi cá nhân của Hưng (M3, S3, S4), không thay mặt xác nhận danh mục quy trình chung của cả nhóm.

## Cấu trúc hồ sơ

Workspace đã **tinh gọn về một báo cáo tổng duy nhất** (gộp discovery + AS-IS + bộ câu hỏi + phân tích + TO-BE), tránh trùng lặp giữa nhiều bản nháp:

- `Bao cao ca nhan - M3 S3 S4 (ACFC).md`: **báo cáo tổng, tự chứa** — mục tiêu/phạm vi, đối chiếu rubric, danh mục quy trình, mô tả AS-IS (bảng bước + kịch bản), phương pháp + nhật ký bằng chứng, bộ câu hỏi 10 định tính + 10 định lượng mỗi quy trình, phân tích VA/BVA/NVA + 4 loại lãng phí + nguyên nhân gốc, phân tích định lượng ba nhóm Thời gian/Chất lượng/Chi phí (công thức + ví dụ minh họa) và đề xuất khắc phục + TO-BE cho M3/S3/S4.
- `hinh-anh/`: ảnh PNG xuất từ SVG trong `diagrams/` để nhúng Word/PowerPoint.
- `scripts/`: hai script Python sinh sơ đồ BPMN 2.0 (ghi kết quả vào `diagrams/` ở repo root).
- `../../../diagrams/`: sơ đồ BPMN (`.drawio` nguồn + `.svg` xuất) của M3/S3/S4 (đặt ở thư mục `diagrams/` cấp gốc dùng chung cho cả nhóm — xem bảng phạm vi phía trên để biết tên file).

Mỗi quy trình có cặp `.drawio` (nguồn diagrams.net) và `.svg` (bản xuất) trong `diagrams/`. Sơ đồ không dùng Mermaid/PlantUML và không dàn mọi khối thành một chuỗi trái–phải: luồng chính, nhánh điều kiện, đường quay lại và chuyển lane có tọa độ riêng theo từng quy trình. Bộ sinh kiểm tra trước khi xuất: không cho phép khối/nhãn đè nhau; sequence flow, message flow và data association phải cách khối không liên quan tối thiểu **24 px**, còn nhãn gateway/event có vùng an toàn **12 px**.

Các bước chưa có bằng chứng nội bộ được đánh dấu `C – cần xác thực`; số liệu minh họa không được gọi là số liệu ACFC thực tế.
