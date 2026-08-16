# M1 – Quản lý vận hành cửa hàng

## Thông tin chung

| Trường | Nội dung |
|---|---|
| **Cấp** | Management – Quy trình quản lý |
| **Mục tiêu** | Đảm bảo cửa hàng được chuẩn bị, tổ chức và kiểm soát trong suốt ca vận hành; các vấn đề phát sinh được xử lý hoặc chuyển cấp và kết quả vận hành được ghi nhận. |
| **Customer** | Người mua sắm tại cửa hàng |
| **Process Owner dự kiến** | Quản lý cửa hàng – cần xác nhận |
| **Kích hoạt** | Bắt đầu ca/kỳ vận hành và cửa hàng tiếp nhận thông tin cần thiết để tổ chức hoạt động |
| **Điểm kết thúc** | Ca vận hành kết thúc, thông tin vận hành được tổng hợp và các vấn đề phát sinh đã được xử lý hoặc chuyển cho đơn vị chịu trách nhiệm |
| **Đầu vào** | Kế hoạch/mục tiêu vận hành, lịch làm việc, thông tin nhân sự, tình trạng cửa hàng và hàng hóa |
| **Đầu ra** | Kết quả vận hành của ca, thông tin bán hàng/tiền/hàng hóa được tổng hợp, vấn đề hoặc chênh lệch được ghi nhận |
| **Outcome dương** | `Ca vận hành hoàn thành` |
| **Outcome ngoại lệ** | `Vấn đề cần chuyển cấp` |

## Actors

| Actor | Vai trò trong quy trình |
|---|---|
| **Quản lý cửa hàng** | Tổ chức hoạt động cửa hàng, phân công công việc, theo dõi vận hành, xử lý hoặc chuyển cấp các vấn đề phát sinh |
| **Nhân viên bán hàng** | Thực hiện các nhiệm vụ vận hành và phục vụ khách hàng trong ca |
| **Thu ngân** | Thực hiện nghiệp vụ thanh toán, hóa đơn và cung cấp thông tin phục vụ kiểm tra/đối soát |
| **Nhân sự phụ trách hàng hóa/kho** | Theo dõi tình trạng hàng hóa, tồn kho và hỗ trợ kiểm tra các chênh lệch liên quan |
| **Retail Operations / đơn vị liên quan** | Tiếp nhận các vấn đề vượt khả năng xử lý tại cửa hàng; vai trò và tên đơn vị chính xác cần xác nhận |

## Customer

Customer cuối cùng của quy trình là **người mua sắm tại cửa hàng ACFC**.

Retail Operations, quản lý và các phòng ban nội bộ là **stakeholder**, không phải Customer cuối cùng.

## Giá trị mang lại

### Đối với khách hàng

- Cửa hàng sẵn sàng phục vụ.
- Nhân sự và khu vực bán hàng được tổ chức.
- Hàng hóa và hoạt động bán hàng được theo dõi.
- Sự cố vận hành được phát hiện và xử lý để hạn chế ảnh hưởng đến trải nghiệm mua sắm.

### Đối với ACFC

- Duy trì kiểm soát hoạt động cửa hàng.
- Có thông tin để theo dõi tình hình vận hành.
- Phát hiện chênh lệch hoặc vấn đề cần xử lý.
- Xác định rõ vấn đề nào đã xử lý và vấn đề nào cần chuyển cấp.

## Khả năng xảy ra sau quy trình

### 1. Ca vận hành hoàn thành bình thường

Hoạt động cửa hàng kết thúc theo kế hoạch, thông tin cần thiết được tổng hợp và không còn vấn đề cần xử lý thêm.

### 2. Có sự cố nhưng cửa hàng xử lý được

Trong quá trình vận hành phát sinh vấn đề nhưng được xử lý trong phạm vi cửa hàng; quy trình vẫn tiếp tục và đóng ca bình thường.

### 3. Có chênh lệch nhưng xác định và xử lý được

Khi tổng hợp/kiểm tra cuối ca phát hiện chênh lệch, cửa hàng xác định được nguyên nhân và hoàn tất việc xử lý hoặc ghi nhận.

### 4. Vấn đề cần chuyển cấp

Sự cố hoặc chênh lệch vượt khả năng xử lý của cửa hàng nên phải chuyển cho Retail Operations hoặc đơn vị chịu trách nhiệm tiếp tục xử lý.

## Phạm vi quy trình

M1 tập trung vào **quản lý hoạt động của cửa hàng trong một ca/kỳ vận hành**.

M1 không đi sâu vào:

- Quy trình bán hàng cho từng khách.
- Quy trình xử lý đơn hàng online.
- Quy trình mua hàng.
- Quy trình phân bổ/điều chuyển hàng giữa các điểm.
- Quy trình đổi hàng, bảo hành và khiếu nại.

Các nội dung trên được xem là quy trình khác hoặc dữ liệu đầu vào/đầu ra liên quan đến M1.

## Dữ liệu và thông tin liên quan

Các nhóm dữ liệu có khả năng được sử dụng trong M1 gồm:

- Kế hoạch/mục tiêu vận hành.
- Lịch làm việc và phân công nhân sự.
- Thông tin tình trạng cửa hàng.
- Thông tin hàng hóa/tồn kho.
- Dữ liệu bán hàng.
- Thông tin thanh toán và hóa đơn.
- Thông tin chênh lệch hoặc sự cố.
- Thông tin/báo cáo cuối ca.

## Các điểm cần xác nhận

1. Process Owner chính thức có phải Quản lý cửa hàng không?
2. Quản lý cửa hàng nhận kế hoạch/mục tiêu từ Retail Operations hay một đơn vị khác?
3. Những hoạt động nào bắt buộc phải thực hiện đầu ca?
4. Việc kiểm tra cuối ca gồm chính xác những nội dung nào?
5. Ai là người nhận báo cáo/kết quả cuối ca?
6. Loại sự cố nào cửa hàng được tự xử lý?
7. Loại sự cố nào bắt buộc phải chuyển cấp?
8. Khi có chênh lệch tiền/hàng hóa, đơn vị nào chịu trách nhiệm xử lý tiếp?
9. ACFC đang dùng hệ thống hoặc biểu mẫu nào để ghi nhận các thông tin này?
10. Các bước chuẩn bị và kiểm tra có thực hiện song song hay theo trình tự?
