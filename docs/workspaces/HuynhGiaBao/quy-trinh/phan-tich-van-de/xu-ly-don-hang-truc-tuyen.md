# Chọn vấn đề và phân tích nguyên nhân
## Phân tích các bên liên quan

| Bên liên quan | Mối quan tâm | Vấn đề tác động | Vai trò trong cải tiến |
|---|---|---|---|
| Khách hàng | Thông tin đơn chính xác, biết tình trạng hàng, nhận hàng đúng dự kiến và được thông báo rõ khi có ngoại lệ | Thiếu hàng, đơn chuyển sang ngày sau, giao lại, chuyển hoàn | Xác nhận thông tin liên hệ, địa chỉ, phương án thiếu hàng và khả năng nhận hàng |
| Bộ phận xử lý đơn hàng | Kiểm soát hàng đợi, tồn kho, tiến độ đóng gói, bàn giao và trạng thái đơn | Tất cả vấn đề trong quy trình | Theo dõi vấn đề, điều phối xử lý, áp dụng quy tắc ưu tiên và phối hợp các bên |
| Đơn vị vận chuyển | Thông tin người nhận đầy đủ, kiện hàng sẵn sàng bàn giao, kết quả giao được chuyển chính xác | Chậm hoặc lệch trạng thái, giao lại, chuyển hoàn | Ghi nhận nguyên nhân giao thất bại, kết quả giao và tình trạng kiện hoàn; phối hợp đồng bộ trạng thái |
| Bộ phận xử lý khiếu nại | Hồ sơ chuyển giao đầy đủ, có bằng chứng về tình trạng kiện và trách nhiệm của các bên | Hàng hoàn hư hỏng hoặc thất lạc | Tiếp nhận, phân loại và theo dõi trường hợp khiếu nại sau khi được chuyển giao |
| Quản lý quy trình | Cycle time, chi phí ngoại lệ, tỷ lệ hoàn tất trong ngày và chất lượng dịch vụ | Các vấn đề ưu tiên trong issue register | Phê duyệt quy tắc điều phối, ngưỡng cảnh báo, chỉ số theo dõi và nguồn lực cải tiến |

Kết quả phân tích cho thấy Bộ phận xử lý đơn hàng là đầu mối trung tâm vì tiếp nhận, điều phối và cập nhật hầu hết ngoại lệ. Khách hàng và Đơn vị vận chuyển quyết định trực tiếp khả năng giao thành công; Bộ phận xử lý khiếu nại tham gia khi hàng hoàn bất thường; Quản lý quy trình cung cấp quy tắc, chỉ số và nguồn lực. Vì vậy, cải tiến cần tập trung vào phối hợp giữa các bên và khả năng theo dõi trạng thái xuyên suốt.


## Issue register


| Vấn đề | Bước | Cơ sở ghi nhận | Nguyên nhân giả định | Tác động định tính | Tác động định lượng | Ưu tiên | Cải tiến | Owner |
|---|---|---|---|---|---|---|---|---|
| Không liên hệ được khách hàng, phải hủy đơn | 5-6 |  quy trình hủy đơn khi không liên hệ được khách hàng. | Số điện thoại sai, khách hàng không nghe máy hoặc thời điểm gọi chưa phù hợp. | Mất cơ hội hoàn tất đơn và phát sinh công việc xác thực, hủy đơn. | **Giả định:** 5% đơn. **Ước tính:** 2,5 trường hợp/50 đơn; chi phí tăng thêm 26.600 đồng/đơn hủy. Chưa quy đổi thành CT tăng thêm. | Chưa xếp hạng theo thời gian | Kiểm tra định dạng số điện thoại, ghi nhận kết quả liên hệ và chọn lại thời điểm liên hệ phù hợp. | Bộ phận xử lý đơn hàng |
| Thiếu hàng | 7-10 |  khách hàng phải chọn chờ hàng, thay thế, mua số lượng hiện có hoặc hủy khi không đủ hàng. | Tồn kho khả dụng chưa phản ánh kịp thời nhu cầu của đơn hoặc hàng chưa được giữ cho đơn. | Đơn chờ, thay đổi nội dung hoặc bị hủy một phần/toàn bộ; tăng trao đổi với khách hàng. | **Giả định:** 10% đơn. **Ước tính:** 5 trường hợp/50 đơn; 5,6355 giờ/trường hợp; 28,1775 giờ/50 đơn; 34.080 đồng/đơn thiếu hàng. | Trung bình | Kiểm tra khả năng đáp ứng sớm, thông báo thời điểm bổ sung dự kiến và theo dõi riêng đơn chờ hàng. | Bộ phận xử lý đơn hàng |
| Công việc cuối ca chuyển sang ngày làm việc tiếp theo | 9, 12 |  phần việc chưa hoàn tất khi hết giờ được chuyển sang ngày làm việc tiếp theo. | Quy tắc ưu tiên cuối ca, năng lực xử lý và thông tin hàng đợi chưa hỗ trợ phát hiện sớm đơn có nguy cơ trễ. | Đơn dở dang phải chờ, kéo dài thời điểm hoàn tất đóng gói và bàn giao. | **Giả định:** 10% đơn, tăng 8 giờ/trường hợp. **Ước tính:** 5 trường hợp và 40,0000 giờ/50 đơn. | Cao | Thiết lập quy tắc ưu tiên cuối ca, theo dõi tuổi đơn và điều phối tải trước khi hết ca. | Bộ phận xử lý đơn hàng |
| Kết quả giao phải chuyển qua nhiều bước | 13, 26, 29 |  kết quả giao được gửi từ Đơn vị vận chuyển, tiếp nhận rồi cập nhật tại Bộ phận xử lý đơn hàng. | Trạng thái giữa các bên chưa được đồng bộ tự động hoặc cảnh báo khi cập nhật chậm. | Tăng bước bàn giao, kéo dài thời gian cập nhật và tạo nguy cơ trạng thái không đồng bộ. | **Giả định:** 10% đơn bị chậm hoặc lệch trạng thái. Chưa đo số giờ tăng thêm. | Chưa xếp hạng theo thời gian | Chuẩn hóa trạng thái và thời điểm cập nhật; trung hạn đồng bộ trạng thái kèm nhật ký. | Bộ phận xử lý đơn hàng |
| Yêu cầu giao lại hoặc khiếu nại được chuyển thủ công | 17, 21-22 |  các bước chuyển thông tin không bổ sung hoạt động kiểm tra hoặc xử lý nghiệp vụ. | Hồ sơ, người nhận việc và trạng thái xử lý chưa được chuyển trên một luồng thông tin thống nhất. | Tăng số lần bàn giao và thời gian chờ bên tiếp nhận. | **Giả định:** phát sinh trên nhánh giao lần đầu thất bại, tương đương 10% tổng đơn. Chưa đo thời gian chờ tăng thêm. | Chưa xếp hạng theo thời gian | Chuẩn hóa hồ sơ chuyển giao; trung hạn tự động phân công và cập nhật trạng thái. | Bộ phận xử lý đơn hàng |
| Giao lần đầu thất bại, phải giao lại | 27-30 |  giao lại phát sinh sau lần giao đầu thất bại khi vẫn còn khả năng giao. | Không liên lạc được người nhận, người nhận vắng mặt hoặc từ chối nhận; số điện thoại, địa chỉ hoặc thời điểm giao chưa phù hợp. | Phát sinh thêm liên hệ, yêu cầu giao và một hoặc nhiều lượt vận chuyển. | **Giả định:** 10% đơn giao lần đầu thất bại; 70% trong nhóm này có thể giao lại, tương đương 7% tổng đơn. **Ước tính:** 3,5 trường hợp/50 đơn; 11,1050 giờ/trường hợp; 38,8675 giờ/50 đơn; 97.000 đồng/đơn giao lại. | Cao | Xác nhận lại số điện thoại, địa chỉ, khả năng nhận và thời điểm giao; phối hợp Đơn vị vận chuyển ghi mã nguyên nhân thất bại. | Bộ phận xử lý đơn hàng |
| Không thể tiếp tục giao, phải chuyển hoàn | 18-20, 31 |  kiện hàng được chuyển về khi không thể tiếp tục giao. | Thông tin người nhận chưa được xác nhận đủ hoặc nguyên nhân thất bại chưa được xử lý trước lượt giao tiếp theo. | Phát sinh vận chuyển ngược, tiếp nhận, kiểm tra và cập nhật lại đơn, tồn kho hoặc thanh toán. | **Giả định:** 4,4% tổng đơn. **Ước tính:** 2,2 trường hợp/50 đơn; 17,25 giờ/trường hợp; 37,9500 giờ/50 đơn; 111.400 đồng/đơn chuyển hoàn. | Cao | Ghi mã nguyên nhân chuyển hoàn, phân nhóm nguyên nhân có thể phòng ngừa và phối hợp Đơn vị vận chuyển kiểm soát bàn giao. | Bộ phận xử lý đơn hàng |
| Hàng hoàn hư hỏng hoặc thất lạc | 19-22 |  hàng hoàn có thể hư hỏng hoặc thất lạc; diễn giải thất lạc là thiếu hàng trong kiện hoàn là giả định. | Bằng chứng bàn giao hoặc tình trạng kiện chưa đủ để xác định thời điểm và trách nhiệm phát sinh. | Phát sinh kiểm tra, khiếu nại, điều chỉnh tồn kho hoặc thanh toán; có nguy cơ mất hàng. | **Giả định:** 10% số đơn hoàn, tương đương 0,44% tổng đơn và 0,22 trường hợp/50 đơn. **Ước tính:** 14.400 đồng/trường hợp chuyển khiếu nại, chưa gồm chi phí xử lý tiếp theo; chưa quy đổi thành CT tăng thêm. | Chưa xếp hạng theo thời gian | Lưu bằng chứng bàn giao, tình trạng kiện và mã nguyên nhân trước khi chuyển hồ sơ khiếu nại. | Bộ phận xử lý khiếu nại |

Issue register cho thấy ba nhóm vấn đề: khả năng đáp ứng và xử lý trong ngày; chuyển giao thông tin; ngoại lệ sau giao thất bại. Theo tác động thời gian đã ước tính, chuyển việc sang ngày sau, giao lại và chuyển hoàn là nhóm ưu tiên cao; thiếu hàng xếp trung bình. Các vấn đề còn lại vẫn cần theo dõi nhưng chưa xếp hạng do chưa có CT tăng thêm cùng đơn vị.

## Ưu tiên vấn đề bằng Pareto

Pareto dùng số giờ tăng thêm kỳ vọng trên 50 đơn để so sánh bốn vấn đề có cùng đơn vị. Công thức chung là:

`Tác động trên 50 đơn = Tần suất giả định × CT tăng thêm mỗi trường hợp × 50`.

Đầu vào cơ sở gồm: 10% đơn chuyển việc sang ngày sau và tăng 8 giờ; 10% đơn thiếu hàng và tăng 5,6355 giờ; 7% đơn giao lại, tính bằng `10% × 70%`, và tăng 11,1050 giờ; 4,4% đơn chuyển hoàn, tính bằng `10% × (30% + 70% × 20%)`, và tăng 17,25 giờ.

Các vấn đề liên quan doanh thu, chất lượng hoặc thời gian chưa đo vẫn được quản lý trong issue register nhưng không được ép quy đổi thành giờ.

| Thứ tự | Vấn đề | Tác động cơ sở | Tỷ trọng | Tỷ lệ tích lũy |
|---:|---|---:|---:|---:|
| 1 | Công việc cuối ca chuyển sang ngày làm việc tiếp theo | 40,0000 giờ/50 đơn | 27,6% | 27,6% |
| 2 | Giao lần đầu thất bại, phải giao lại | 38,8675 giờ/50 đơn | 26,8% | 54,4% |
| 3 | Không thể tiếp tục giao, phải chuyển hoàn | 37,9500 giờ/50 đơn | 26,2% | 80,6% |
| 4 | Thiếu hàng | 28,1775 giờ/50 đơn | 19,4% | 100,0% |
|  | **Tổng** | **144,9950 giờ/50 đơn** | **100,0%** |  |

<p align="center">
  <img src="../../images/pareto-van-de-xu-ly-don-hang-truc-tuyen.svg" alt="Pareto số giờ tăng thêm kỳ vọng trên 50 đơn của quy trình xử lý đơn trực tuyến" width="100%">
</p>

<p align="center"><em>Hình 4.1. Pareto số giờ tăng thêm kỳ vọng trên 50 đơn theo kịch bản cơ sở</em></p>

Ba vấn đề đầu tạo ra 80,6% tổng giờ tăng thêm của bốn vấn đề được định lượng. Công việc cuối ca chuyển sang ngày làm việc tiếp theo đứng đầu với 40,0000 giờ/50 đơn và được chọn để phân tích nguyên nhân.

### Phân tích kịch bản

Kịch bản thấp và cao được tính bằng cách nhân trực tiếp tổng tác động cơ sở với 50% và 150%. Cách tính này không nhân đồng thời tần suất và CT nên tránh khuếch đại bất định hai lần.

| Vấn đề | Thấp, 50% | Cơ sở, 100% | Cao, 150% |
|---|---:|---:|---:|
| Công việc cuối ca chuyển sang ngày làm việc tiếp theo | 20,00000 giờ | 40,00000 giờ | 60,00000 giờ |
| Giao lần đầu thất bại, phải giao lại | 19,43375 giờ | 38,86750 giờ | 58,30125 giờ |
| Không thể tiếp tục giao, phải chuyển hoàn | 18,97500 giờ | 37,95000 giờ | 56,92500 giờ |
| Thiếu hàng | 14,08875 giờ | 28,17750 giờ | 42,26625 giờ |
| **Tổng** | **72,49750 giờ** | **144,99500 giờ** | **217,49250 giờ** |
## Phân tích Why-Why: giả định

Why-Why phân tích ba nhóm nguyên nhân có thể làm công việc cuối ca phải chuyển sang ngày làm việc tiếp theo. Mỗi nhánh đi từ nguyên nhân trực tiếp đến điều kiện sâu hơn có thể xử lý.

| Nhánh | Cấp 1 | Cấp 2 | Cấp 3 |
|---|---|---|---|
| Quy trình cuối ca | Đơn đến gần cuối ca khó hoàn tất. | Đơn chưa được phân loại theo thời gian còn lại và khối lượng cần xử lý. | Chưa có ngưỡng ưu tiên hoặc thời điểm chốt xử lý dựa trên năng lực còn lại. |
| Năng lực xử lý | Khối lượng cuối ca có thể vượt năng lực đóng gói và bàn giao. | Nhân sự chưa được điều phối theo lượng đơn đang chờ. | Chưa dự báo tải công việc theo khung giờ. |
| Thông tin theo dõi | Đơn có nguy cơ trễ được phát hiện muộn. | Chưa có cảnh báo theo tuổi đơn và tiến độ xử lý. | Thông tin hàng đợi chưa được tổng hợp để điều phối. |

Ba nhánh cùng hướng đến một thiếu hụt quản trị: quy trình chưa kết hợp ngưỡng ưu tiên, năng lực còn lại và cảnh báo hàng đợi để xử lý đơn cuối ca.

## Hướng cải tiến

Cải tiến được chia thành hai tầng để vừa kiểm soát vấn đề trước mắt, vừa giảm thao tác chuyển giao về sau.

### Kiểm soát vận hành ngắn hạn

1. Quy định cách phân loại đơn cuối ca theo tuổi đơn, thời gian xử lý còn lại và thời điểm bàn giao dự kiến.
2. Theo dõi giờ tiếp nhận, giờ bắt đầu đóng gói, giờ hoàn tất và lý do chuyển sang ngày sau.
3. Giao một vai trò theo dõi hàng đợi và điều phối tải trước khi hết ca.
4. Xác nhận lại số điện thoại, địa chỉ, khả năng nhận và thời điểm giao trước khi yêu cầu giao lại.
5. Dùng mã nguyên nhân thống nhất cho thiếu hàng, giao thất bại, chuyển hoàn và hàng hoàn bất thường.

### Tự động hóa trung hạn

1. Cảnh báo đơn sắp vượt ngưỡng tuổi hoặc có nguy cơ không hoàn tất trong ca.
2. Tổng hợp đơn mới, đang xử lý, đang chờ và thời điểm hoàn tất dự kiến trên cùng một hàng đợi.
3. Đồng bộ trạng thái giao giữa Bộ phận xử lý đơn hàng và Đơn vị vận chuyển, kèm lịch sử cập nhật.
4. Tự động chuyển hồ sơ giao lại hoặc khiếu nại, phân công người xử lý và cập nhật trạng thái trên cùng luồng thông tin.
