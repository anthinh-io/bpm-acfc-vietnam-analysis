# Xử lý đơn hàng trực tuyến và giao hàng - hiện trạng


## Luồng xử lý hiện tại

### Tiếp nhận và kiểm tra đơn

Bộ phận xử lý đơn hàng tiếp nhận thông tin đơn do khách hàng gửi, sau đó gọi vào số điện thoại khách hàng cung cấp để xác thực thông tin khách hàng, sản phẩm, số lượng, giá trị đơn, địa chỉ giao hàng, phương thức giao hàng và phương thức thanh toán.

Nếu liên hệ được khách hàng, thông tin đơn được xác thực và Bộ phận xử lý đơn hàng dùng hệ thống nội bộ để kiểm tra tồn kho hoặc khả năng đáp ứng.

Nếu không liên hệ được khách hàng, Bộ phận xử lý đơn hàng hủy đơn. Quy trình kết thúc với kết quả `Đơn đã hủy do không liên hệ được khách hàng`.

Nếu đủ hàng, Bộ phận xử lý đơn hàng chuyển sang đóng gói. Nếu không đủ hàng, bộ phận thông báo tình trạng thiếu hàng, ghi nhận ý kiến và xác định phương án khách hàng lựa chọn.

### Xử lý khi thiếu hàng

Nếu khách hàng đồng ý chờ hàng, Bộ phận xử lý đơn hàng ghi nhận đơn chờ, cập nhật trạng thái trên hệ thống và gửi xác nhận cho khách hàng. Bộ phận theo dõi việc bổ sung hàng, thông báo cho khách hàng khi có hàng rồi chuyển đơn sang đóng gói.

Nếu khách hàng đồng ý nhận sản phẩm thay thế, Bộ phận xử lý đơn hàng kiểm tra hàng thay thế, điều chỉnh đơn theo sản phẩm khách hàng đã chọn, cập nhật đơn trên hệ thống và gửi xác nhận cho khách hàng. Đơn tiếp tục sang đóng gói.

Nếu khách hàng chỉ mua số lượng hiện có, Bộ phận xử lý đơn hàng điều chỉnh số lượng, cập nhật giá trị thanh toán và đơn trên hệ thống, sau đó gửi xác nhận cho khách hàng. Đơn tiếp tục sang đóng gói.

Nếu khách hàng không đồng ý với các phương án tiếp tục mua, khách hàng chọn hủy toàn bộ đơn hoặc hủy phần hàng thiếu. Bộ phận xử lý đơn hàng cập nhật nội dung hủy trên hệ thống, hoàn tiền cho phần bị hủy nếu khách hàng đã thanh toán và gửi xác nhận hủy. Nếu khách hàng hủy toàn bộ đơn, quy trình kết thúc với kết quả `Đơn đã hủy theo lựa chọn của khách hàng`. Nếu khách hàng chỉ hủy phần hàng thiếu, phần hàng còn lại tiếp tục sang đóng gói.

Các phương án chờ hàng, thay thế sản phẩm, mua số lượng hiện có và hủy phần hàng thiếu cùng nhập lại luồng đóng gói khi hàng của đơn đã sẵn sàng.

### Đóng gói và bàn giao vận chuyển

Bộ phận xử lý đơn hàng đóng gói sau khi xác nhận hàng sẵn sàng theo đơn ban đầu hoặc phương án khách hàng lựa chọn. Mục tiêu hoàn thành trong cùng ngày làm việc áp dụng cho đơn có hàng sẵn; phần việc chưa hoàn thành được chuyển sang ngày làm việc tiếp theo. Đơn chờ hàng chỉ được đóng gói sau khi có hàng bổ sung.

Sau khi đóng gói, Bộ phận xử lý đơn hàng tạo hoặc cập nhật vận đơn, cập nhật trạng thái đơn và bàn giao kiện hàng cho Đơn vị vận chuyển. Ba hoạt động thuộc cùng một giai đoạn; thứ tự chi tiết và bằng chứng bàn giao chưa được xác định. Việc bàn giao diễn ra trong ngày đóng gói xong; nếu quá ngày làm việc thì chuyển sang ngày làm việc tiếp theo.

Đơn vị vận chuyển nhận kiện hàng và thực hiện giao hàng. Thời gian giao dự kiến cho khách hàng từ 1 đến 7 ngày làm việc tùy vùng.

### Xử lý kết quả giao hàng

Sau mỗi lần giao, Đơn vị vận chuyển xác định kết quả. Nếu giao thất bại, Đơn vị vận chuyển xác định nguyên nhân và đánh giá khả năng giao lại. Đơn vị vận chuyển gửi kết quả giao và kết quả đánh giá khả năng giao lại cho Bộ phận xử lý đơn hàng. Bộ phận xử lý đơn hàng tiếp nhận kết quả và cập nhật trạng thái đơn.

Nếu giao thành công, Bộ phận xử lý đơn hàng đối soát thanh toán và đóng đơn. Quy trình kết thúc với kết quả `Đơn giao thành công đã đóng`.

Nếu Đơn vị vận chuyển đánh giá còn khả năng giao lại, Bộ phận xử lý đơn hàng liên hệ khách hàng và gửi yêu cầu giao lại cho Đơn vị vận chuyển. Đơn vị vận chuyển thực hiện giao lại rồi đánh giá và gửi kết quả giao mới. Luồng quay lại bước tiếp nhận và xử lý kết quả giao hàng.

Nếu Đơn vị vận chuyển đánh giá không thể tiếp tục giao, Đơn vị vận chuyển tự chuyển hàng về cho Bộ phận xử lý đơn hàng, không chờ yêu cầu chuyển hoàn.

### Xử lý hàng hoàn

Bộ phận xử lý đơn hàng tiếp nhận và kiểm tra hàng hoàn.

Nếu kết quả kiểm tra không ghi nhận hư hỏng hoặc thất lạc, bộ phận cập nhật tồn kho, thanh toán và trạng thái, sau đó đóng đơn. Quy trình kết thúc với kết quả `Đơn chuyển hoàn đã đóng`.

Nếu hàng hoàn hư hỏng hoặc thất lạc, Bộ phận xử lý đơn hàng chuyển trường hợp cho Bộ phận xử lý khiếu nại. Quy trình kết thúc với kết quả `Trường hợp đã chuyển xử lý khiếu nại`.
