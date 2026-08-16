# S4 – PHÂN TÍCH QUY TRÌNH

## VA/BVA/NVA

| Hoạt động | Phân loại | Lý do/khắc phục |
|---|---|---|
| Nhập số điện thoại/thông tin cá nhân | BVA | Cần để tạo hồ sơ khách hàng và định danh tài khoản. |
| Nhận và xác nhận mã OTP | BVA | Xác thực bảo mật trước khi tạo tài khoản. |
| Tạo và kích hoạt tài khoản | VA | Giá trị trực tiếp — khách hàng mua sắm và hưởng ưu đãi thành viên. |
| Đăng nhập bằng mật khẩu đã lưu | VA | Truy cập ngay quyền lợi thành viên. |
| Chờ nhận OTP/mật khẩu tạm | NVA | Chờ (Hold); rút ngắn thời gian gửi và có kênh dự phòng. |
| Nhập lại OTP do sai/hết hạn | NVA | Lỗi (Defects); cho phép gửi lại OTP không cần nhập lại toàn bộ thông tin. |
| Đăng ký lại từ đầu khi OTP hết hạn (không lưu tạm thông tin đã nhập) | NVA | Xử lý dư (Over-processing); lưu tạm dữ liệu đã nhập trong phiên đăng ký. |
| Liên hệ CSKH qua nhiều kênh không đầu mối rõ ràng | NVA | Di chuyển (Move); hợp nhất kênh hỗ trợ tài khoản ngay trên trang đăng ký/đăng nhập. |

## Bốn loại lãng phí

| Loại | Biểu hiện cần kiểm chứng | Cải tiến |
|---|---|---|
| Di chuyển (Move) | Khách hàng phải tự tìm và chuyển qua hotline/fanpage/Zalo/email khi gặp lỗi tài khoản | Đặt nút hỗ trợ/chatbot ngay trên trang đăng ký/đăng nhập. |
| Chờ (Hold) | Chờ nhận OTP hoặc email/SMS mật khẩu tạm thời | Rút ngắn thời gian gửi, thêm kênh gửi dự phòng, hiển thị đếm ngược hiệu lực. |
| Xử lý dư (Over-processing) | Phải nhập lại toàn bộ thông tin cá nhân khi OTP hết hạn hoặc đăng ký thất bại | Lưu tạm dữ liệu đã nhập trong phiên, chỉ yêu cầu gửi lại OTP. |
| Lỗi (Defects) | OTP sai/hết hạn, số điện thoại đã tồn tại nhưng không có thông báo hướng dẫn rõ, quên mật khẩu lặp lại | Thông báo lỗi cụ thể kèm hướng dẫn bước tiếp theo (vd. gợi ý đăng nhập nếu số điện thoại đã tồn tại). |

## Vấn đề, nguyên nhân và khắc phục

| Vấn đề cần kiểm chứng | Nguyên nhân giả định | Khắc phục đề xuất |
|---|---|---|
| Tỷ lệ bỏ dở đăng ký cao | OTP đến chậm/hết hạn, phải nhập lại toàn bộ thông tin | Lưu tạm dữ liệu phiên, gia hạn hoặc rút ngắn hợp lý thời gian hiệu lực OTP theo dữ liệu thực tế. |
| Khách hàng không tự xử lý được lỗi đăng nhập | Thông báo lỗi chung chung, thiếu hướng dẫn bước kế tiếp | Chuẩn hóa thông báo lỗi theo từng nguyên nhân cụ thể (OTP sai, số điện thoại đã tồn tại, tài khoản khóa). |
| Khối lượng yêu cầu CSKH liên quan tài khoản tăng | Không có kênh tự phục vụ đủ rõ ràng trên trang đăng ký/đăng nhập | Tích hợp chatbot/hướng dẫn tự khắc phục ngay tại bước phát sinh lỗi trước khi chuyển CSKH. |

## Phân tích định lượng (Thời gian – Chất lượng – Chi phí)

Rubric yêu cầu **tính toán** trên ba nhóm chỉ số: Thời gian, Chất lượng, Chi phí. Do chưa tiếp cận được số nội bộ ACFC, phần dưới trình bày **công thức + một ví dụ tính toán minh họa** để thể hiện phương pháp.

> ⚠️ **Lưu ý liêm chính học thuật:** mọi con số ở cột "Dữ liệu giả định" và "Kết quả tính" bên dưới là **số nhóm tự đặt để minh họa cách tính — KHÔNG phải số liệu thực của ACFC**. Sau phỏng vấn/workshop sẽ thay bằng ba mốc *thấp nhất – thường gặp – cao nhất* từ dữ liệu thật rồi áp lại đúng công thức ở cột 2.

### a) Nhóm Thời gian (Time)

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Thời gian hoàn tất đăng ký (Cycle time) | Thời điểm kích hoạt − thời điểm bắt đầu | Bắt đầu 0s → kích hoạt 90s | **90 giây** |
| Thời gian chờ nhận OTP (Waiting/NVA) | Thời điểm nhận OTP − thời điểm gửi | ≈ 20 giây | **20 giây** |
| Hiệu suất chu kỳ (PCE) | (Cycle − Waiting) / Cycle | (90 − 20) / 90 | **≈ 78%** |
| Thời gian xử lý yêu cầu CSKH | Thời điểm đóng − thời điểm khách liên hệ | Liên hệ 09:00 → đóng 11:00 | **2 giờ** |

### b) Nhóm Chất lượng (Quality)

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Tỷ lệ đăng ký thành công | Tài khoản tạo thành công / tổng lượt bắt đầu | 820 / 1.000 | **82%** |
| Tỷ lệ bỏ dở đăng ký | 1 − tỷ lệ đăng ký thành công | 1 − 0,82 | **18%** |
| Tỷ lệ OTP xác nhận đúng lần đầu | Lượt đúng lần đầu / tổng lượt gửi OTP | 880 / 1.000 | **88%** |
| Tỷ lệ cần CSKH hỗ trợ | Lượt chuyển CSKH / tổng lượt đăng ký-đăng nhập | 60 / 1.000 | **6%** |

### c) Nhóm Chi phí (Cost)

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Chi phí gửi OTP | Tổng lượt gửi OTP × đơn giá SMS | 1.000 × 300đ | **300.000đ / 1.000 lượt** |
| Chi phí xử lý CSKH (Defects/Move) | Số lượt CSKH × thời gian × đơn giá giờ | 60 × 0,25 giờ × 100.000đ | **1.500.000đ** |
| Chi phí doanh thu mất do bỏ dở (cơ hội) | Số lượt bỏ dở × giá trị đơn bình quân × tỷ lệ chuyển đổi | 180 × 500.000đ × 10% | **9.000.000đ** |

*Đơn giá SMS 300đ và đơn giá giờ CSKH 100.000đ là giả định minh họa; thay bằng đơn giá thật khi có dữ liệu ACFC.*

## Đề xuất tương lai (TO-BE) sơ bộ

Lưu tạm dữ liệu đã nhập trong phiên đăng ký để chỉ cần gửi lại OTP khi hết hạn, chuẩn hóa thông báo lỗi theo từng nguyên nhân cụ thể kèm hướng dẫn bước kế tiếp, hợp nhất đầu mối hỗ trợ tài khoản (chatbot/CSKH) ngay trên trang đăng ký/đăng nhập, và theo dõi tỷ lệ hết hạn OTP để điều chỉnh thời gian hiệu lực hợp lý.

## Bảng đề xuất khắc phục theo lãng phí

| Loại lãng phí | Vấn đề | Đề xuất khắc phục | Người phụ trách đề xuất | Thời hạn đề xuất |
|---|---|---|---|---|
| Di chuyển (Move) | Khách hàng phải tự tìm kênh hỗ trợ (hotline/fanpage/Zalo/email) khi gặp lỗi tài khoản | Đặt nút hỗ trợ/chatbot ngay trên trang đăng ký/đăng nhập | CSKH phối hợp Digital-Ecommerce/IT | Ngắn hạn — bổ sung trong lần cập nhật giao diện gần nhất |
| Chờ (Hold) | Chờ nhận OTP hoặc mật khẩu tạm không có kênh dự phòng | Thêm kênh gửi dự phòng, hiển thị đếm ngược hiệu lực OTP | IT vận hành website/app | Ngắn hạn — 1 quý |
| Xử lý dư (Over-processing) | Phải nhập lại toàn bộ thông tin khi OTP hết hạn hoặc đăng ký thất bại | Lưu tạm dữ liệu phiên đăng ký, chỉ yêu cầu gửi lại OTP | IT vận hành website/app | Trung hạn — 1–2 quý |
| Lỗi (Defects) | Thông báo lỗi chung chung khi OTP sai/hết hạn hoặc số điện thoại đã tồn tại | Chuẩn hóa thông báo lỗi cụ thể theo từng nguyên nhân, kèm hướng dẫn bước kế tiếp | CSKH phối hợp Digital-Ecommerce/IT | Trung hạn — 1–2 quý |

Ghi chú: người phụ trách và thời hạn ở trên là đề xuất của nhóm dựa trên phân tích lãng phí, chưa phải cam kết chính thức của ACFC; cần xác nhận lại nếu có phỏng vấn/workshop với chủ quy trình.
