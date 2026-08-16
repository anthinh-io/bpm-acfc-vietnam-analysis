# S4 – HIỆN TRẠNG SƠ BỘ: ĐĂNG KÝ VÀ KÍCH HOẠT TÀI KHOẢN THÀNH VIÊN

## 1. Tóm tắt

Quy trình bắt đầu khi khách hàng truy cập website hoặc app ACFC để mua sắm. Nếu chưa có tài khoản, khách hàng chọn "Đăng ký ngay", nhập số điện thoại, nhận và xác nhận mã OTP, điền thông tin cá nhân rồi hoàn tất đăng ký để hệ thống tạo và kích hoạt tài khoản mới. Nếu đã có tài khoản, khách hàng đăng nhập bằng email/số điện thoại và mật khẩu đã đăng ký; nếu quên mật khẩu, khách hàng yêu cầu cấp mật khẩu kích hoạt tạm thời rồi đổi mật khẩu mới. Sau khi đăng nhập thành công, khách hàng truy cập giao diện tài khoản thành viên để xem/đổi thông tin cá nhân, điểm thưởng, lịch sử đơn hàng và đổi hàng trực tuyến. Khi phát sinh vướng mắc (không nhận được OTP, tài khoản bị khóa, quên mật khẩu lặp lại), khách hàng được hướng dẫn liên hệ CSKH qua hotline, fanpage, Zalo hoặc email.

## 2. Actor kích hoạt và hưởng lợi

- **Actor kích hoạt:** Khách hàng truy cập website/app ACFC để đăng ký tài khoản mới hoặc đăng nhập/kích hoạt tài khoản đã có.
- **Actor hưởng lợi trực tiếp:** Khách hàng — được mua sắm, tích điểm và hưởng ưu đãi dành riêng cho thành viên.
- **Actor hưởng lợi gián tiếp:** ACFC (dữ liệu khách hàng, kênh bán hàng trực tuyến); CSKH (giảm khối lượng hỗ trợ nếu quy trình tự phục vụ vận hành trơn tru).

## 3. Các bước thực hiện

| # | Actor | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Khách hàng | Truy cập website hoặc app ACFC | Cổng điều kiện: đã có tài khoản? |
| 2a | Khách hàng | Bấm "Đăng ký ngay" (chưa có tài khoản) | Nhánh đăng ký mới |
| 3a | Khách hàng | Nhập số điện thoại đăng ký | — |
| 4a | Hệ thống website/app | Gửi mã OTP xác nhận số điện thoại | Thời hạn hiệu lực OTP — `C` |
| 5a | Khách hàng | Nhập mã OTP xác nhận | Cổng điều kiện: mã đúng và còn hạn? |
| 6a | Khách hàng | Điền đầy đủ thông tin cá nhân còn lại | — |
| 7a | Khách hàng | Bấm "Đăng ký" | — |
| 8a | Hệ thống website/app | Tạo và kích hoạt tài khoản mới | Cổng điều kiện: số điện thoại chưa tồn tại, thông tin hợp lệ |
| 2b | Khách hàng | Nhập email/số điện thoại và mật khẩu đã đăng ký (đã có tài khoản) | Nhánh đăng nhập |
| 3b | Khách hàng | Chọn "Đăng nhập" | Cổng điều kiện: nhớ mật khẩu? |
| 4b | Khách hàng | Bấm "Quên mật khẩu? Nhấn vào đây" (nếu quên) | — |
| 5b | Hệ thống website/app | Gửi mật khẩu kích hoạt tạm thời | Kênh gửi (SMS/email) — `C` |
| 6b | Khách hàng | Đăng nhập bằng mật khẩu tạm và đổi mật khẩu mới | Cổng điều kiện: đổi mật khẩu thành công? |
| 7 | Hệ thống website/app | Xác thực đăng nhập thành công | Cổng điều kiện |
| 8 | Hệ thống website/app | Hiển thị giao diện tài khoản thành viên | Thông tin cá nhân, điểm thưởng, lịch sử đơn hàng, đổi hàng trực tuyến |
| 9 | CSKH/Tổng đài | Hỗ trợ xử lý khi có vướng mắc | Hotline 1900 3038, fanpage, Zalo, email — nhánh ngoại lệ |

## 4. Kịch bản thành công

Khách hàng mới truy cập website/app → bấm "Đăng ký ngay" → nhập số điện thoại → nhận và nhập đúng OTP trong hạn → điền đủ thông tin cá nhân → bấm "Đăng ký" → hệ thống tạo và kích hoạt tài khoản ngay. **Kết quả:** "Tài khoản được tạo và kích hoạt thành công." Với khách hàng đã có tài khoản: nhập đúng email/số điện thoại và mật khẩu → đăng nhập thành công ngay lần đầu → truy cập được giao diện tài khoản thành viên.

## 5. Kịch bản thất bại/ngoại lệ

- Không nhận được mã OTP hoặc mã hết hạn (Bước 4a–5a) → khách hàng phải yêu cầu gửi lại OTP hoặc liên hệ CSKH nếu lặp lại nhiều lần.
- Số điện thoại đăng ký đã tồn tại trong hệ thống (Bước 8a) → đăng ký bị từ chối; khách hàng cần chuyển sang đăng nhập hoặc lấy lại mật khẩu — thông báo lỗi cụ thể và bước xử lý tiếp theo chưa được nguồn công khai xác nhận, `C – cần xác thực`.
- Khách hàng quên mật khẩu (Bước 3b–4b) → yêu cầu cấp mật khẩu tạm; nếu không nhận được hoặc mật khẩu tạm hết hạn, phải yêu cầu lại hoặc liên hệ CSKH.
- Đăng nhập thất bại nhiều lần hoặc tài khoản bị khóa (Bước 7) → chuyển CSKH qua hotline 1900 3038, fanpage, Zalo hoặc email `cskh@acfc.com.vn`; ngưỡng số lần thử trước khi khóa tài khoản chưa được nguồn công khai xác nhận, `C – cần xác thực`.

**Nguồn/trạng thái:** EV09, EV10; thời hạn hiệu lực OTP, kênh gửi mật khẩu tạm, ngưỡng khóa tài khoản, chủ quy trình nội bộ và thời gian xử lý CSKH là `C – cần xác thực` bằng phỏng vấn CSKH/Digital-Ecommerce hoặc IT vận hành website/app.
