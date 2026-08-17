# Hồ sơ khám phá: Xử lý đơn hàng trực tuyến và giao hàng


## 1. Tổng quan

### 1.1. Tên, mục tiêu, phạm vi

**Tên quy trình:** Xử lý đơn hàng trực tuyến và giao hàng.

**Mục tiêu:** Tiếp nhận thông tin đơn hàng trực tuyến do khách hàng gửi, xác nhận thông tin đơn qua điện thoại, kiểm tra khả năng đáp ứng, xử lý thiếu hàng theo phương án khách hàng lựa chọn, đóng gói, bàn giao vận chuyển và xử lý kết quả đến khi đơn được đóng, bị hủy, hoặc được chuyển sang xử lý khiếu nại.

**Phạm vi:**

- Bắt đầu khi khách hàng gửi thông tin đơn hàng trực tuyến và Bộ phận xử lý đơn hàng tiếp nhận thông tin đơn.
- Bao gồm khách hàng gửi và xác nhận thông tin đơn, Bộ phận xử lý đơn hàng gọi xác thực, hủy đơn khi không liên hệ được, kiểm tra tồn kho hoặc khả năng đáp ứng bằng hệ thống nội bộ, xử lý phương án chờ hàng, thay thế sản phẩm, mua số lượng hiện có hoặc hủy khi thiếu hàng, đóng gói, lập hoặc cập nhật vận đơn, cập nhật trạng thái, bàn giao vận chuyển, xử lý giao thành công, giao thất bại, hoàn hàng và chuyển khiếu nại.
- Không bao gồm xử lý lỗi hoặc quá thời hạn thanh toán trực tuyến; đây là ngoại lệ của khâu thanh toán khi đặt hàng, không được mô hình hóa trong quy trình này.
- Không bao gồm tên cụ thể của đơn vị vận chuyển và cách theo dõi, đóng đơn nhiều kiện.

### 1.2. Điểm bắt đầu, đầu vào, đầu ra

**Điểm bắt đầu:** Khách hàng gửi thông tin đơn hàng trực tuyến; Bộ phận xử lý đơn hàng tiếp nhận thông tin đơn.

**Đầu vào:**

- Thông tin khách hàng và liên hệ.
- Sản phẩm, số lượng và giá trị đơn.
- Địa chỉ giao hàng.
- Phương thức giao hàng.
- Phương thức thanh toán.

**Đầu ra tích cực:** Đơn được giao thành công, trạng thái được cập nhật, thanh toán được đối soát và đơn được đóng.

**Đầu ra tiêu cực hoặc ngoại lệ:**

- Không liên hệ được khách hàng qua số điện thoại đã cung cấp: bộ phận xử lý đơn hàng hủy đơn.
- Không đủ hàng: khách hàng chọn chờ hàng, thay thế sản phẩm, mua số lượng hiện có, hủy phần hàng thiếu hoặc hủy toàn bộ đơn; bộ phận xử lý đơn hàng thực hiện phương án, cập nhật đơn và gửi xác nhận.
- Giao thất bại: Đơn vị vận chuyển xác định nguyên nhân và đánh giá khả năng giao lại. Nếu còn khả năng giao lại, Bộ phận xử lý đơn hàng liên hệ khách hàng và gửi yêu cầu giao lại. Nếu không thể tiếp tục giao, Đơn vị vận chuyển tự chuyển hoàn.
- Hàng hoàn bị hư hỏng hoặc thất lạc: chuyển sang xử lý khiếu nại.

### 1.3. Khách hàng, tác nhân, bộ phận liên quan

| Nhóm | Thành phần | Vai trò đã xác nhận |
|---|---|---|
| Khách hàng | Khách mua hàng trực tuyến | Đặt hàng, cung cấp số điện thoại và thông tin đơn, xác nhận thông tin, lựa chọn phương án khi thiếu hàng, nhận thông báo xác nhận và nhận hàng |
| Nội bộ | Bộ phận xử lý đơn hàng | Tiếp nhận và xác thực đơn, kiểm tra khả năng đáp ứng, thực hiện phương án khách hàng chọn khi thiếu hàng, cập nhật đơn, đóng gói, cập nhật vận đơn và trạng thái, xử lý kết quả giao |
| Hệ thống | Hệ thống nội bộ | Được bộ phận xử lý đơn hàng sử dụng để kiểm tra tồn kho hoặc khả năng đáp ứng; tên hệ thống: **Không rõ** |
| Bên ngoài | Đơn vị vận chuyển | Nhận bàn giao, giao hàng, xác định nguyên nhân giao thất bại, đánh giá khả năng giao lại, giao lại hoặc tự chuyển hoàn; tên đơn vị: không thuộc phạm vi hỏi |
| Nội bộ | Bộ phận xử lý khiếu nại | Tiếp nhận trường hợp hàng hoàn hư hỏng hoặc thất lạc từ Bộ phận xử lý đơn hàng |

### 1.4. Kết quả và điều kiện

**Điều kiện thuận lợi:** Liên hệ được khách hàng và xác thực thông tin đơn, hàng sẵn có theo đơn ban đầu hoặc phương án xử lý thiếu hàng, đóng gói hoàn tất, bàn giao được cho đơn vị vận chuyển và giao thành công.

**Điều kiện rẽ nhánh:** Liên hệ được hoặc không liên hệ được khách hàng; đủ hoặc thiếu hàng; khách hàng chọn chờ hàng, thay thế sản phẩm, mua số lượng hiện có, hủy phần hàng thiếu hoặc hủy toàn bộ đơn; giao thành công hoặc giao thất bại; Đơn vị vận chuyển đánh giá còn khả năng giao lại hoặc không thể tiếp tục giao; hàng hoàn bình thường hoặc hư hỏng hay thất lạc.

## 3. Mô tả quy trình hiện tại

### 3.1. Các bước theo thứ tự

| Bước | Người thực hiện | Hoạt động | Đầu vào | Đầu ra | Điều kiện | Thời gian |
|---|---|---|---|---|---|---|
| 1. Tiếp nhận và liên hệ xác thực | Bộ phận xử lý đơn hàng | Tiếp nhận đơn, gọi vào số điện thoại khách hàng cung cấp và xác thực thông tin khách hàng, sản phẩm, số lượng, giá trị đơn, địa chỉ, phương thức giao và thanh toán | Thông tin đơn trực tuyến do khách hàng gửi | Kết quả liên hệ và xác thực | Liên hệ được thì thông tin đơn được xác thực và chuyển sang kiểm tra khả năng đáp ứng; không liên hệ được thì hủy đơn và kết thúc quy trình | Với đơn có hàng sẵn, từ tiếp nhận đơn hợp lệ đến đóng gói trong cùng ngày làm việc; nếu quá ngày làm việc thì chuyển sang hôm sau. Thời gian chờ bổ sung hàng không thuộc khoảng này |
| 2. Kiểm tra khả năng đáp ứng | Bộ phận xử lý đơn hàng | Kiểm tra tồn kho hoặc khả năng đáp ứng bằng hệ thống nội bộ | Đơn đã được xác thực qua điện thoại | Kết quả đủ hoặc không đủ hàng | Đủ hàng thì chuyển đóng gói; không đủ hàng thì trao đổi với khách | Nằm trong mục tiêu thời gian của chuỗi bước từ tiếp nhận đến đóng gói; thời gian riêng: **Không rõ** |
| 3. Xử lý phương án thiếu hàng | Bộ phận xử lý đơn hàng; khách hàng | Thông báo thiếu hàng, ghi nhận ý kiến, xác định và thực hiện phương án khách hàng chọn, cập nhật đơn trên hệ thống và gửi xác nhận | Kết quả kiểm tra không đủ hàng | Đơn được cập nhật theo phương án đã chọn hoặc bị hủy | Chờ hàng thì ghi nhận đơn chờ và theo dõi bổ sung hàng; thay thế thì kiểm tra hàng thay thế và điều chỉnh đơn; mua số lượng hiện có thì điều chỉnh số lượng và giá trị thanh toán; không đồng ý thì hủy toàn bộ hoặc phần hàng thiếu và hoàn tiền cho phần bị hủy nếu đã thanh toán | Thời gian xử lý riêng: **Không rõ**; thời gian chờ bổ sung hàng: **Không rõ** |
| 4. Đóng gói hàng hóa | Bộ phận xử lý đơn hàng | Đóng gói hàng hóa | Hàng sẵn theo đơn ban đầu hoặc phương án khách hàng lựa chọn | Hàng đã đóng gói | Thực hiện khi hàng đã sẵn sàng; không thực hiện nếu khách hàng hủy toàn bộ đơn | Với đơn có hàng sẵn, hoàn thành trong cùng ngày làm việc từ khi tiếp nhận đơn hợp lệ; nếu quá ngày làm việc thì chuyển sang hôm sau. Đơn chờ được đóng gói sau khi có hàng bổ sung |
| 5. Lập vận đơn, cập nhật trạng thái và bàn giao | Bộ phận xử lý đơn hàng; đơn vị vận chuyển | Tạo hoặc cập nhật thông tin vận đơn, cập nhật trạng thái đơn hàng và bàn giao cho đơn vị vận chuyển | Hàng đã đóng gói | Kiện hàng được bàn giao và trạng thái được cập nhật | Tên đơn vị vận chuyển, thứ tự chi tiết giữa ba hoạt động và bằng chứng bàn giao: **Không rõ** | Từ đóng gói xong đến bàn giao: trong cùng ngày làm việc; nếu quá ngày làm việc thì chuyển sang hôm sau |
| 6. Nhận kết quả giao và cập nhật trạng thái | Bộ phận xử lý đơn hàng | Nhận kết quả giao, xác định kết quả và cập nhật trạng thái | Kết quả giao từ đơn vị vận chuyển | Nhánh giao thành công hoặc giao thất bại | Quy tắc trạng thái cụ thể: **Không rõ** | Thời gian giao công khai dự kiến từ 1 đến 7 ngày làm việc tùy vùng; thời gian xử lý nội bộ riêng: **Không rõ** |
| 7. Kết thúc khi giao thành công | Bộ phận xử lý đơn hàng | Cập nhật trạng thái, đối soát thanh toán và đóng đơn | Kết quả giao thành công | Đơn đã đóng | Điều kiện đối soát và bằng chứng đóng đơn: **Không rõ** | **Không rõ** |
| 8. Phân tích giao thất bại | Đơn vị vận chuyển; Bộ phận xử lý đơn hàng | Đơn vị vận chuyển xác định nguyên nhân, đánh giá khả năng giao lại và gửi kết quả; Bộ phận xử lý đơn hàng tiếp nhận kết quả và cập nhật trạng thái | Kết quả giao thất bại | Nguyên nhân, khả năng giao lại và trạng thái được cập nhật | Đơn vị vận chuyển đánh giá còn khả năng giao lại hoặc không thể tiếp tục giao | **Không rõ** |
| 9. Giao lại hoặc chuyển hoàn | Bộ phận xử lý đơn hàng; Đơn vị vận chuyển | Nếu còn khả năng giao lại, Bộ phận xử lý đơn hàng liên hệ khách hàng và gửi yêu cầu để Đơn vị vận chuyển giao lại; nếu không thể tiếp tục giao, Đơn vị vận chuyển tự chuyển hàng về | Kết quả đánh giá khả năng giao lại | Kết quả giao lại hoặc hàng hoàn | Điều kiện đánh giá chi tiết của Đơn vị vận chuyển: **Không rõ** | **Không rõ** |
| 10. Xử lý hàng hoàn | Bộ phận xử lý đơn hàng | Kiểm tra hàng hoàn, cập nhật tồn kho, thanh toán và trạng thái đóng đơn | Hàng được chuyển hoàn | Hàng hoàn được ghi nhận và đơn được đóng | Hàng hư hỏng hoặc thất lạc thì chuyển xử lý khiếu nại | **Không rõ** |
| 11. Chuyển khiếu nại | Bộ phận xử lý đơn hàng; Bộ phận xử lý khiếu nại | Bộ phận xử lý đơn hàng chuyển trường hợp hư hỏng hoặc thất lạc; Bộ phận xử lý khiếu nại tiếp nhận | Kết quả kiểm tra hàng hoàn cho thấy hư hỏng hoặc thất lạc | Trường hợp đã được chuyển xử lý khiếu nại | Quy trình khiếu nại tiếp theo: **Không rõ** | **Không rõ** |

### 3.2. Chi tiết xử lý khi thiếu hàng

Khi kết quả kiểm tra cho thấy không đủ hàng, Bộ phận xử lý đơn hàng thông báo tình trạng thiếu hàng, ghi nhận ý kiến và xác định phương án khách hàng lựa chọn.

- **Chờ hàng:** Ghi nhận đơn chờ, cập nhật trạng thái trên hệ thống và gửi xác nhận cho khách hàng. Theo dõi bổ sung hàng, thông báo khi có hàng rồi chuyển sang đóng gói.
- **Thay thế sản phẩm:** Kiểm tra hàng thay thế, điều chỉnh và cập nhật đơn theo sản phẩm khách hàng chọn, gửi xác nhận rồi chuyển sang đóng gói.
- **Mua số lượng hiện có:** Điều chỉnh số lượng, cập nhật giá trị thanh toán và đơn trên hệ thống, gửi xác nhận rồi chuyển sang đóng gói.
- **Không tiếp tục mua:** Hủy toàn bộ đơn hoặc phần hàng thiếu theo lựa chọn của khách hàng, cập nhật nội dung hủy trên hệ thống, hoàn tiền cho phần bị hủy nếu đã thanh toán và gửi xác nhận hủy. Hủy toàn bộ thì kết thúc quy trình; hủy phần hàng thiếu thì chuyển phần còn lại sang đóng gói.

Các phương án không làm kết thúc toàn bộ đơn cùng nhập lại luồng đóng gói khi hàng của đơn đã sẵn sàng.

### 3.3. Ngoại lệ thanh toán không thuộc phạm vi

Khi phương thức thanh toán trực tuyến lỗi hoặc quá thời hạn, hệ thống tự động hủy giao dịch. Ngoại lệ này thuộc khâu thanh toán khi đặt hàng và không được mô hình hóa trong quy trình hiện tại.

Nguồn công khai xác nhận các nhánh tự hủy đối với thanh toán Visa, Master, JCB, ATM và Momo khi giao dịch không tiếp tục, hết thời gian hoặc phát sinh lỗi: [Phương thức thanh toán](https://www.acfc.com.vn/phuong-thuc-thanh-toan).

### 3.4. Thời gian giao hàng công khai

Chính sách ACFC công bố thời gian giao dự kiến theo vùng: nội tỉnh hoặc nội thành từ 1 đến 3 ngày làm việc, nội vùng từ 2 đến 4 ngày, liên vùng giữa Thành phố Hồ Chí Minh, Hà Nội và Đà Nẵng từ 3 đến 5 ngày, và từ ba thành phố lớn đến thành phố khác thuộc vùng khác từ 5 đến 7 ngày. Đây là thời gian giao dự kiến cho khách hàng, không phải SLA xử lý nội bộ. Ngày lễ, Tết và tình huống phát sinh có thể làm thay đổi thời gian: [Chính sách giao hàng](https://www.acfc.com.vn/chinh-sach-giao-hang).


## 4. Nguồn  đã dùng

- [Hướng dẫn đặt hàng](https://www.acfc.com.vn/huong-dan-dat-hang): hành trình đặt hàng, thông báo đặt hàng thành công, theo dõi đơn và khả năng phát sinh nhiều kiện.
- [Phương thức thanh toán](https://www.acfc.com.vn/phuong-thuc-thanh-toan): phương thức thanh toán và nhánh tự động hủy khi thanh toán trực tuyến lỗi, quá hạn hoặc không tiếp tục.
- [Chính sách giao hàng](https://www.acfc.com.vn/chinh-sach-giao-hang): phạm vi giao, điều kiện địa chỉ và thời gian giao dự kiến theo vùng.
- [Điều khoản dịch vụ](https://www.acfc.com.vn/dieu-khoan-dich-vu): các trường hợp ACFC có thể từ chối hoặc hủy đơn do lỗi hệ thống, thông tin sai, giá hiển thị sai hoặc mục đích mua không phù hợp.
- **Nhân sự ACFC:** các bước nội bộ, tác nhân, cách liên hệ khách hàng để xác thực đơn, nhánh hủy khi không liên hệ được, các phương án xử lý thiếu hàng, giao thất bại, hoàn hàng, đối soát và thời gian xử lý nội bộ được ghi trong hồ sơ này.
