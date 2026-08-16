# S4 – ĐĂNG KÝ VÀ KÍCH HOẠT TÀI KHOẢN THÀNH VIÊN

| Trường | Nội dung |
|---|---|
| Cấp | Hỗ trợ |
| Mục tiêu quy trình | Đảm bảo khách hàng tự đăng ký, xác thực và kích hoạt tài khoản thành viên (hoặc đăng nhập/khôi phục mật khẩu) nhanh chóng, giảm tỷ lệ bỏ dở và giảm tải cho CSKH |
| Khách hàng | Khách hàng mua sắm trên website/app ACFC (đăng ký mới hoặc đăng nhập lại) |
| Giá trị mang lại | Khách hàng truy cập được quyền lợi thành viên (điểm thưởng, ưu đãi, lịch sử đơn hàng); ACFC thu thập dữ liệu khách hàng cho kênh bán hàng trực tuyến và giảm khối lượng yêu cầu hỗ trợ tài khoản |
| Chủ quy trình dự kiến | CSKH/Digital-Ecommerce hoặc IT vận hành website/app; cần xác thực |
| Kích hoạt | Khách hàng bấm "Đăng ký ngay" (tài khoản mới) hoặc đăng nhập/quên mật khẩu (tài khoản đã có) trên website hoặc app ACFC |
| Đầu vào | Số điện thoại/email, mã OTP, thông tin cá nhân, yêu cầu đặt lại mật khẩu |
| Đầu ra | Tài khoản được tạo và kích hoạt, hoặc phiên đăng nhập hợp lệ; mật khẩu tạm thời khi quên mật khẩu |
| Outcome dương | Tài khoản được tạo/kích hoạt thành công, khách hàng đăng nhập được và sử dụng quyền lợi thành viên (điểm thưởng, lịch sử đơn hàng, đổi hàng trực tuyến) |
| Outcome âm | OTP sai/hết hạn/không nhận được, số điện thoại đã tồn tại, thông tin không hợp lệ, hoặc quên mật khẩu không xử lý được → chuyển CSKH |
| Bằng chứng | EV09, EV10 trong `research.md` |

## Cổng điều kiện dự kiến cần xác thực

1. Khách hàng đã có tài khoản hay đăng ký mới? 2. Số điện thoại đăng ký đã tồn tại trong hệ thống? 3. Mã OTP nhận được đúng hạn? 4. Mã OTP nhập đúng? 5. Thông tin cá nhân điền đầy đủ/hợp lệ? 6. Khách hàng nhớ mật khẩu hay quên? 7. Yêu cầu đặt lại mật khẩu được gửi thành công? 8. Mật khẩu tạm thời/mới được nhập đúng? 9. Đăng nhập thành công? 10. Cần chuyển CSKH khi lỗi lặp lại hoặc kéo dài?

## Vai trò/làn đề xuất

ACFC: Khách hàng, Hệ thống website/app ACFC (tự động: gửi OTP, xác thực, cấp mật khẩu tạm), CSKH/Tổng đài (hỗ trợ khi có vướng mắc).

## Dữ liệu và ngoại lệ

Số điện thoại/email, mã OTP, mật khẩu, thông tin cá nhân (họ tên, ngày sinh...), lịch sử đăng nhập. Ngoại lệ gồm OTP hết hạn hoặc nhập sai nhiều lần, số điện thoại/email đã đăng ký trước đó, tài khoản bị khóa, quên mật khẩu lặp lại, không nhận được SMS/email.
