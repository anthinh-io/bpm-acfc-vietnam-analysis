# Workspace Nguyễn Công Hưng – ACFC

**Sinh viên:** Nguyễn Công Hưng  
**MSSV:** 24730100

## Phạm vi sở hữu

**Cập nhật 17/08/2026:** phạm vi cá nhân của Hưng gồm **M3, S3, S4 và S1** (tuyển dụng). Sơ đồ BPMN của bốn quy trình này đã được chuyển từ thư mục `diagrams/` cấp gốc (dùng chung cho nhóm) vào thư mục con **`diagrams/` ngay trong workspace** để hồ sơ cá nhân tự chứa. Sơ đồ kiến trúc toàn nhóm (`kien-truc-quy-trinh`) và các sơ đồ của thành viên khác (C1–C4, tổng hợp kho) vẫn ở `diagrams/` cấp gốc.

| Mã | Cấp | Quy trình | Sơ đồ BPMN (trong `diagrams/` của workspace) | Trạng thái |
|---|---|---|---|---|
| M3 | Quản lý | Lập kế hoạch mua hàng và phân bổ hàng hóa theo mùa | `bpmn-hoach-dinh-phan-bo-hang-hoa-m3.svg` | Xong bản nháp — AS-IS + BPMN + phân tích định lượng |
| S3 | Hỗ trợ | Kiểm kê và xử lý chênh lệch tồn kho | `bpmn-kiem-ke-ton-kho-s2.svg` | Xong bản nháp — AS-IS + BPMN + phân tích định lượng |
| S4 | Hỗ trợ | Đăng ký, xác thực OTP & kích hoạt tài khoản thành viên | `bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg` | Xong bản nháp — AS-IS + BPMN (8 cổng XOR, có Split & Join) + phân tích định lượng |
| S1 | Hỗ trợ | Tuyển dụng & tiếp nhận (onboarding) nhân sự | `bpmn-tuyen-dung-nhan-su-s1.svg` | Xong bản nháp — AS-IS + BPMN (8 cổng XOR) + phân tích định lượng |

> Lưu ý mã: file BPMN dùng hậu tố khác với mã workspace. Ánh xạ: S3 (kiểm kê) ↔ `...-s2`, S4 (kích hoạt tài khoản) ↔ `...-s3`, S1 (tuyển dụng) ↔ `...-s1`. Cần thống nhất lại bảng ánh xạ khi gộp vào báo cáo chung.

README này chỉ xác nhận phạm vi cá nhân của Hưng (M3, S3, S4, S1), không thay mặt xác nhận danh mục quy trình chung của cả nhóm.

## Cấu trúc hồ sơ

Workspace gồm **một báo cáo tổng, tự chứa** bao trùm cả bốn quy trình M3/S3/S4/S1 và thư mục sơ đồ tự chứa (hai báo cáo chuyên sâu S4 và S1 trước đây đã được gộp hẳn vào báo cáo tổng cho gọn):

- `Bao cao ca nhan - M3 S3 S4 S1 (ACFC).md`: **báo cáo tổng, tự chứa** — mục tiêu/phạm vi, đối chiếu rubric, danh mục quy trình, mô tả AS-IS (bảng bước + kịch bản) cho cả M3/S3/S4/S1, phương pháp + nhật ký bằng chứng, bộ câu hỏi 10 định tính + 10 định lượng mỗi quy trình, phân tích VA/BVA/NVA + 4 loại lãng phí + nguyên nhân gốc, phân tích định lượng ba nhóm Thời gian/Chất lượng/Chi phí (công thức + ví dụ minh họa) và đề xuất khắc phục + TO-BE cho cả bốn quy trình. Riêng S4 có mô tả sâu chương trình thành viên (5 hạng thẻ, đủ 8 cổng, PDPA) và S1 có phần tuyển dụng & onboarding chuỗi bán lẻ/kho vận, đều đã nằm trong báo cáo tổng.
- `diagrams/`: sơ đồ BPMN (`.drawio` nguồn + `.svg` xuất, kèm PNG) của **bốn** quy trình M3/S3/S4/S1 thuộc phạm vi cá nhân.
- `hinh-anh/`: ảnh PNG xuất từ SVG (bằng skill `export_png.py`) để nhúng Word/PowerPoint.
- `scripts/`: script Python sinh sơ đồ BPMN 2.0 (thư mục này được `.gitignore` bỏ theo dõi, chỉ giữ trên đĩa).

Mỗi quy trình có cặp `.drawio` (nguồn diagrams.net) và `.svg` (bản xuất) trong `diagrams/`. Sơ đồ không dùng Mermaid/PlantUML và không dàn mọi khối thành một chuỗi trái–phải: luồng chính, nhánh điều kiện, đường quay lại và chuyển lane có tọa độ riêng theo từng quy trình. Bộ sinh kiểm tra trước khi xuất: không cho phép khối/nhãn đè nhau; sequence flow, message flow và data association phải cách khối không liên quan tối thiểu **24 px**, còn nhãn gateway/event có vùng an toàn **12 px**.

Các bước chưa có bằng chứng nội bộ được đánh dấu `C – cần xác thực`; số liệu minh họa không được gọi là số liệu ACFC thực tế.
