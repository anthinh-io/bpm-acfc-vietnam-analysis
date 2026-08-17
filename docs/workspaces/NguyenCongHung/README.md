# Workspace Nguyễn Công Hưng – ACFC

**Sinh viên:** Nguyễn Công Hưng  
**MSSV:** 24730100

## Phạm vi sở hữu

**Cập nhật 11/08/2026:** yêu cầu chung của nhóm rút gọn còn **1 Quản lý + 1 Hỗ trợ** bắt buộc mỗi thành viên (nhóm đã đủ tối thiểu 6 quy trình BPMN + phân tích). Hưng hoàn thiện **M3 và S3** theo yêu cầu bắt buộc, đồng thời bổ sung thêm **S4** (quy trình Hỗ trợ thứ hai, không trùng mã/nội dung với quy trình của thành viên khác) từ nội dung công khai trên trang chủ ACFC. C3/C4 không còn trong phạm vi bài làm tuần này nên đã gỡ khỏi workspace.

| Mã | Cấp | Quy trình | Sơ đồ BPMN (trong `diagrams/`) | Trạng thái |
|---|---|---|---|---|
| M3 | Quản lý | Lập kế hoạch mua hàng và phân bổ hàng hóa theo mùa | `bpmn-hoach-dinh-phan-bo-hang-hoa-m3.svg` | **Xong bản nháp** — AS-IS + BPMN + phân tích định lượng |
| S3 | Hỗ trợ | Kiểm kê và xử lý chênh lệch tồn kho | `bpmn-kiem-ke-ton-kho-s2.svg` + `fishbone-kiem-ke-kho.svg` | **Xong bản nháp** — AS-IS + BPMN + xương cá + phân tích định lượng |
| S4 | Hỗ trợ | Đăng ký, xác thực OTP & kích hoạt tài khoản thành viên | `bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg` + `fishbone-kich-hoat-tai-khoan.svg` | **Xong bản nháp** — AS-IS + BPMN (8 cổng XOR, có Split & Join, đã xử lý hết đè line/deadlock) + xương cá + phân tích định lượng; **đã gộp vào báo cáo `03`** |

> Lưu ý mã: file trong `diagrams/` dùng hậu tố nhóm (`m3`, `s2`, `s3`) khác với mã workspace (M3, S3, S4). Ánh xạ: S3 (kiểm kê) ↔ `...-s2`, S4 (kích hoạt tài khoản) ↔ `...-s3`. Cần thống nhất lại bảng ánh xạ khi gộp vào báo cáo chung.

README này chỉ xác nhận phạm vi cá nhân của Hưng (M3, S3, S4), không thay mặt xác nhận danh mục quy trình chung của cả nhóm.

## Mốc tiến độ

**06–09/08:** khóa phạm vi/bằng chứng. **10–13/08:** hoàn thiện M3/S3 (phạm vi bắt buộc mới) + hoàn thành bản nháp báo cáo Word cá nhân. **14–16/08:** xác thực, cập nhật gateway và TO-BE; hoàn thiện sơ đồ BPMN S4 (8 cổng XOR, Split & Join, xử lý hết đè line/deadlock) và **đã gộp S4 vào bản nháp báo cáo `03`** (phạm vi cá nhân 3 quy trình M3/S3/S4).

**Mục tiêu tuần này (10–16/08):** hoàn thành bản nháp báo cáo Word cho M3/S3/S4 — xem `03. Du thao bao cao ca nhan - M3 va S3.md`. File này hiện **đã gộp đủ cả M3, S3 và S4** (discovery + AS-IS + VA/BVA/NVA + 4 lãng phí + phân tích định lượng + TO-BE cho từng quy trình). Đây vẫn là bản nháp cấp cá nhân, chưa gộp vào `docs/Phan_2...docx`/Phần 3/Phần 4 dùng chung của nhóm; việc chắt lọc nội dung đưa vào báo cáo chung sẽ thực hiện sau khi nhóm rà soát.

## Cấu trúc hồ sơ

- `01. Tom tat va muc tieu.md`: bối cảnh, ranh giới và mục tiêu.
- `02. Thu thap du lieu quy trinh - Hang hoa & ton kho ACFC.md`: bằng chứng, vai trò và bộ câu hỏi (phạm vi M3/S3/S4).
- `03. Du thao bao cao ca nhan - M3 va S3.md`: bản nháp gộp discovery + AS-IS + phân tích của **M3, S3 và S4**, chuẩn bị nội dung cho báo cáo Word cá nhân. (Tên file giữ nguyên để không phá liên kết; nội dung đã mở rộng gồm cả S4.)
- `quy-trinh/ho-so-kham-pha/`: research log và hồ sơ từng quy trình.
- `quy-trinh/mo-ta-as-is/`: mô tả hiện trạng bằng lời.
- `quy-trinh/phan-tich/`: VA/BVA/NVA, lãng phí, phân tích định lượng (công thức + ví dụ minh họa) và TO-BE sơ bộ.
- `../../../diagrams/`: sơ đồ BPMN (`.drawio` nguồn + `.svg` xuất) và sơ đồ xương cá của M3/S3/S4 (đặt ở thư mục `diagrams/` cấp gốc dùng chung cho cả nhóm — xem bảng phạm vi phía trên để biết tên file).

Mỗi quy trình có cặp `.drawio` (nguồn diagrams.net) và `.svg` (bản xuất) trong `diagrams/`. Sơ đồ không dùng Mermaid/PlantUML và không dàn mọi khối thành một chuỗi trái–phải: luồng chính, nhánh điều kiện, đường quay lại và chuyển lane có tọa độ riêng theo từng quy trình.

Bộ sinh kiểm tra trước khi xuất: không cho phép khối/nhãn đè nhau; sequence flow, message flow và data association phải cách khối không liên quan tối thiểu **24 px**, còn nhãn gateway/event có vùng an toàn **12 px**.

Các bước chưa có bằng chứng nội bộ được đánh dấu `C – cần xác thực`; số liệu minh họa không được gọi là số liệu ACFC thực tế.
