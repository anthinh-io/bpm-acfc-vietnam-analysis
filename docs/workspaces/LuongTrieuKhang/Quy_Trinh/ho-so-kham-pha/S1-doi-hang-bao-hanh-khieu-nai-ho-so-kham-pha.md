# S1 – Đổi hàng, bảo hành và xử lý khiếu nại

## Thông tin chung

| Trường | Nội dung |
|---|---|
| **Cấp** | Support – Quy trình hỗ trợ |
| **Mục tiêu** | Tiếp nhận và xử lý yêu cầu sau bán hàng của khách hàng theo chính sách áp dụng; xác định yêu cầu có đủ điều kiện hay không và thực hiện phương án phù hợp như đổi hàng, bảo hành hoặc xử lý khiếu nại. |
| **Customer** | Khách hàng đã thực hiện giao dịch mua hàng và phát sinh nhu cầu sau bán hàng |
| **Process Owner dự kiến** | Bộ phận CSKH / đơn vị tiếp nhận yêu cầu – cần xác nhận |
| **Kích hoạt** | Khách hàng gửi yêu cầu đổi hàng, bảo hành hoặc khiếu nại liên quan đến giao dịch đã thực hiện |
| **Điểm kết thúc** | Khách hàng nhận được kết quả xử lý cuối cùng hoặc thông báo từ chối có lý do |
| **Đầu vào** | Thông tin giao dịch, hóa đơn/mã đơn, sản phẩm, tem nhãn/phụ kiện, ảnh/video hoặc bằng chứng khi cần, chính sách áp dụng |
| **Đầu ra** | Kết quả đổi hàng/bảo hành/xử lý khiếu nại, yêu cầu bổ sung thông tin hoặc thông báo từ chối |
| **Outcome dương** | `Yêu cầu được xử lý` |
| **Outcome ngoại lệ** | `Yêu cầu bị từ chối hoặc cần chuyển cấp` |

## Actors

| Actor | Vai trò trong quy trình |
|---|---|
| **Khách hàng** | Khởi tạo yêu cầu; cung cấp thông tin giao dịch, sản phẩm và các bằng chứng cần thiết; nhận kết quả xử lý |
| **CSKH / Nhân viên cửa hàng** | Tiếp nhận yêu cầu, kiểm tra thông tin ban đầu, hướng dẫn khách bổ sung hồ sơ và theo dõi trạng thái xử lý |
| **Đơn vị kiểm tra / xử lý sản phẩm** | Kiểm tra tình trạng sản phẩm, tem nhãn, phụ kiện và các điều kiện liên quan; tên đơn vị chính xác cần xác nhận |
| **Quản lý / đơn vị có thẩm quyền** | Xem xét các trường hợp ngoại lệ hoặc trường hợp không thể xử lý theo quy tắc thông thường |
| **Đơn vị liên quan khác** | Có thể phối hợp khi cần bảo hành, xử lý hàng thay thế hoặc các trường hợp đặc thù; cần xác nhận theo thực tế |

## Customer

Customer của quy trình là **khách hàng đã mua sản phẩm và phát sinh nhu cầu đổi hàng, bảo hành hoặc khiếu nại sau bán hàng**.

Khách hàng mong muốn:

- Yêu cầu được tiếp nhận rõ ràng.
- Điều kiện xử lý được giải thích nhất quán.
- Không phải cung cấp lại thông tin nhiều lần.
- Nhận được kết quả cuối cùng hoặc lý do từ chối cụ thể.

## Giá trị mang lại

### Đối với khách hàng

- Có kênh xử lý khi sản phẩm hoặc giao dịch phát sinh vấn đề.
- Được hướng dẫn rõ về điều kiện, chứng từ và bằng chứng cần thiết.
- Nhận được phương án xử lý phù hợp khi yêu cầu đủ điều kiện.
- Nhận được phản hồi rõ ràng khi yêu cầu không đủ điều kiện.

### Đối với ACFC

- Chuẩn hóa việc tiếp nhận và xử lý yêu cầu sau bán hàng.
- Giảm rủi ro xử lý không nhất quán giữa các trường hợp.
- Kiểm soát việc đổi hàng/bảo hành theo chính sách.
- Theo dõi được trạng thái và kết quả của từng yêu cầu.
- Hạn chế việc xử lý sai điều kiện hoặc lạm dụng chính sách.

## Khả năng xảy ra sau quy trình

### 1. Yêu cầu được xử lý thành công

Khách hàng đáp ứng điều kiện áp dụng và nhận được phương án phù hợp như đổi hàng, bảo hành hoặc hình thức xử lý khác.

### 2. Yêu cầu cần bổ sung thông tin

Thông tin giao dịch, chứng từ hoặc bằng chứng chưa đủ để đánh giá yêu cầu nên khách hàng phải bổ sung trước khi tiếp tục.

### 3. Yêu cầu không đủ điều kiện

Yêu cầu không đáp ứng điều kiện về thời hạn, chứng từ, nhóm sản phẩm, tình trạng sản phẩm hoặc điều kiện khác theo chính sách; khách hàng được thông báo lý do từ chối.

### 4. Yêu cầu cần chuyển cấp

Trường hợp không thể xử lý theo quy tắc thông thường hoặc có ngoại lệ cần được chuyển cho quản lý/đơn vị có thẩm quyền xem xét.

## Phạm vi quy trình

S1 tập trung vào **xử lý yêu cầu sau bán hàng** của khách hàng.

S1 không bao gồm:

- Quy trình bán hàng ban đầu.
- Quy trình đặt hàng trực tuyến.
- Quy trình quản lý tồn kho tổng thể.
- Quy trình mua hàng.
- Quy trình thanh toán bán hàng thông thường.
- Toàn bộ quy trình tài chính/kế toán liên quan đến doanh nghiệp.

Thông tin giao dịch bán hàng được sử dụng như dữ liệu đầu vào để xác minh yêu cầu.

## Dữ liệu và thông tin liên quan

Các nhóm dữ liệu có khả năng được sử dụng trong S1 gồm:

- Mã đơn hàng hoặc hóa đơn.
- Kênh mua hàng.
- Ngày mua hàng.
- Thông tin sản phẩm.
- Nhóm sản phẩm/thương hiệu.
- Tình trạng sản phẩm.
- Tem nhãn và phụ kiện đi kèm.
- Ảnh/video hoặc bằng chứng khi cần.
- Lý do đổi hàng/bảo hành/khiếu nại.
- Kết quả kiểm tra điều kiện.
- Phương án xử lý.
- Trạng thái yêu cầu.
- Kết quả cuối cùng gửi cho khách hàng.

## Các điểm cần xác nhận

1. Process Owner chính thức của S1 là CSKH, cửa hàng hay đơn vị nào khác?
2. Yêu cầu sau bán hàng được tiếp nhận qua những kênh nào?
3. Ai là người trực tiếp kiểm tra tình trạng sản phẩm?
4. Có bộ phận kiểm tra sản phẩm riêng hay việc kiểm tra do cửa hàng/kho thực hiện?
5. Các điều kiện bắt buộc để chấp nhận đổi hàng/bảo hành gồm chính xác những gì?
6. Trường hợp nào bắt buộc phải có ảnh hoặc video?
7. Khi không có sản phẩm thay thế, phương án ưu tiên là gì?
8. Trường hợp nào cần quản lý hoặc đơn vị khác phê duyệt ngoại lệ?
9. Có bước hoàn tiền trong quy trình S1 không; nếu có thì đơn vị nào thực hiện?
10. Hệ thống hoặc biểu mẫu nào đang được dùng để ghi nhận và theo dõi yêu cầu?
