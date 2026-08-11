# Workspace Nguyễn Công Hưng – ACFC

**Sinh viên:** Nguyễn Công Hưng  
**MSSV:** 24730100

## Phạm vi sở hữu

**Cập nhật 11/08/2026:** yêu cầu chung của nhóm rút gọn còn **1 Quản lý + 1 Hỗ trợ** bắt buộc mỗi thành viên (nhóm đã đủ tối thiểu 6 quy trình BPMN + phân tích). Hưng tập trung hoàn thiện **M3 và S3**; C3/C4 không còn trong phạm vi bài làm tuần này nên đã gỡ khỏi workspace.

| Mã | Cấp | Quy trình | Trạng thái |
|---|---|---|---|
| M3 | Quản lý | Lập kế hoạch mua hàng và phân bổ hàng hóa theo mùa | **Đang hoàn thiện** |
| S3 | Hỗ trợ | Kiểm kê và xử lý chênh lệch tồn kho | **Đang hoàn thiện** |

README này chỉ xác nhận phạm vi cá nhân của Hưng (M3, S3), không thay mặt xác nhận danh mục quy trình chung của cả nhóm.

## Mốc tiến độ

**06–09/08:** khóa phạm vi/bằng chứng. **10–13/08:** hoàn thiện M3/S3 (phạm vi bắt buộc mới) + hoàn thành bản nháp báo cáo Word cá nhân. **14–16/08:** xác thực, cập nhật gateway và TO-BE.

**Mục tiêu tuần này (10–16/08):** hoàn thành bản nháp báo cáo Word cho M3/S3 — xem `03. Du thao bao cao ca nhan - M3 va S3.md`. Đây vẫn là bản nháp cấp cá nhân, chưa gộp vào `docs/Phan_2...docx`/Phần 3/Phần 4 dùng chung của nhóm; việc chắt lọc nội dung đưa vào báo cáo chung sẽ thực hiện sau khi nhóm rà soát.

## Cấu trúc hồ sơ

- `01. Tom tat va muc tieu.md`: bối cảnh, ranh giới và mục tiêu.
- `02. Thu thap du lieu quy trinh - Hang hoa & ton kho ACFC.md`: bằng chứng, vai trò và bộ câu hỏi.
- `03. Du thao bao cao ca nhan - M3 va S3.md`: bản nháp gộp discovery + AS-IS + phân tích của M3/S3, chuẩn bị nội dung cho báo cáo Word cá nhân.
- `quy-trinh/ho-so-kham-pha/`: research log và hồ sơ từng quy trình.
- `quy-trinh/mo-ta-as-is/`: mô tả hiện trạng bằng lời.
- `quy-trinh/bpmn/`: mô hình BPMN 2.0 mở và chỉnh sửa được bằng bpmn.io.
- `quy-trinh/drawio/`: nguồn diagrams.net native, mỗi khối có tọa độ riêng để giữ bố cục pool/lane và các nhánh ngoại lệ.
- `quy-trinh/blueprint/`: blueprint pool/lane, event, task, dữ liệu, gateway và luồng thực thi theo prompt BPMN 2.0.
- `quy-trinh/images/`: bản SVG dùng trong báo cáo/slide.
- `quy-trinh/phan-tich/`: VA/BVA/NVA, lãng phí, KPI và TO-BE sơ bộ.

Bốn bộ `.drawio`, `.bpmn` và `.svg` được đồng bộ từ `generate_native_bpmn_diagrams.py`. Bộ sinh không dùng Mermaid/PlantUML và không dàn mọi khối thành một chuỗi trái–phải: luồng chính, nhánh điều kiện, đường quay lại và chuyển lane có tọa độ riêng theo từng quy trình.

Bộ sinh kiểm tra trước khi xuất: không cho phép khối/nhãn đè nhau; sequence flow, message flow và data association phải cách khối không liên quan tối thiểu **24 px**, còn nhãn gateway/event có vùng an toàn **12 px**.

Các bước chưa có bằng chứng nội bộ được đánh dấu `C – cần xác thực`; số liệu minh họa không được gọi là số liệu ACFC thực tế.
