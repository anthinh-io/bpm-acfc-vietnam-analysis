# Workspace Nguyễn Công Hưng – ACFC

**Sinh viên:** Nguyễn Công Hưng  
**MSSV:** 24730100

## Phạm vi sở hữu

| Mã | Cấp | Quy trình |
|---|---|---|
| M3 | Quản lý | Lập kế hoạch mua hàng và phân bổ hàng hóa theo mùa |
| C3 | Cốt lõi | Tiếp nhận lô hàng mới và nhập kho trung tâm |
| C4 | Cốt lõi | Phân bổ, điều chuyển và bổ sung hàng hóa cho chuỗi cửa hàng |
| S3 | Hỗ trợ | Kiểm kê và xử lý chênh lệch tồn kho |

## Kết quả rà soát workspace nhóm

Đối chiếu bộ ACFC của Triệu Khang (Part 2/3) và hồ sơ ACFC của Gia Bảo trên các nhánh nhóm hiện có:

- Triệu Khang đã chốt **M1–M2, C1–C2, S1–S2**: vận hành cửa hàng, doanh số/kế hoạch kinh doanh, bán hàng tại cửa hàng, đơn online, đổi/bảo hành/khiếu nại và quyền dữ liệu.
- Gia Bảo có thêm một Core: **Tổ chức sự kiện truyền thông sản phẩm**.
- Hưng phụ trách **M3, C3, C4, S3**; cụm này không trùng sáu mã trên nếu giữ đúng ranh giới trong hồ sơ mục tiêu.

Điểm cần nhóm chốt trước khi ghi danh mục cuối: quy trình sự kiện của Gia Bảo **thay cho C1 bán hàng tại cửa hàng** hay là quy trình thứ 11. Vì vậy README này chỉ xác nhận phạm vi của Hưng, chưa gọi tổng nhóm là “10 quy trình”. Luồng cụm Hưng là **M3 → C3 → C4**, còn **S3** phản hồi dữ liệu chênh lệch về M3/C4.

## Mốc tiến độ

**06–09/08:** khóa phạm vi/bằng chứng và rà soát C4. **10–13/08:** hoàn thiện M3/C3/S3. **14–16/08:** xác thực, cập nhật gateway và TO-BE.

## Cấu trúc hồ sơ

- `01. Tom tat va muc tieu.md`: bối cảnh, ranh giới và mục tiêu.
- `02. Thu thap du lieu quy trinh - Hang hoa & ton kho ACFC.md`: bằng chứng, vai trò và bộ câu hỏi.
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
