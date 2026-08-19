# S1 – Đổi hàng, bảo hành và xử lý khiếu nại - hiện trạng

Quy trình bắt đầu khi Khách hàng phát sinh nhu cầu đổi hàng, bảo hành hoặc khiếu nại liên quan đến một giao dịch đã thực hiện và gửi yêu cầu đến ACFC qua kênh tiếp nhận phù hợp.

CSKH hoặc Nhân viên cửa hàng tiếp nhận yêu cầu và ghi nhận các thông tin ban đầu như mã đơn hàng, hóa đơn, sản phẩm liên quan và lý do yêu cầu.

Nếu chưa xác định được giao dịch hoặc thông tin ban đầu chưa đầy đủ, Khách hàng được hướng dẫn bổ sung thông tin trước khi yêu cầu được tiếp tục xử lý.

Khi đã xác định được giao dịch, CSKH hoặc Nhân viên cửa hàng kiểm tra các điều kiện áp dụng của yêu cầu, bao gồm thời hạn, chứng từ mua hàng, nhóm sản phẩm và các điều kiện liên quan theo chính sách đổi hàng/bảo hành.

Nếu hồ sơ hoặc bằng chứng chưa đầy đủ, Khách hàng được yêu cầu bổ sung. Tùy trường hợp, bằng chứng có thể gồm ảnh hoặc video về tình trạng sản phẩm.

Sau khi hồ sơ đầy đủ, sản phẩm và các bằng chứng liên quan được kiểm tra để xác định yêu cầu có đáp ứng điều kiện hỗ trợ hay không.

Nếu yêu cầu không đáp ứng điều kiện, CSKH hoặc Nhân viên cửa hàng thông báo từ chối và nêu lý do cho Khách hàng.

Nếu yêu cầu đáp ứng điều kiện, đơn vị xử lý xác định phương án phù hợp. Phương án có thể là đổi sản phẩm, bảo hành hoặc hình thức xử lý khác tùy theo trường hợp và chính sách áp dụng.

Trong trường hợp đổi hàng, đơn vị liên quan kiểm tra khả năng có sản phẩm thay thế phù hợp.

Nếu có sản phẩm thay thế, việc đổi được thực hiện. Trường hợp sản phẩm thay thế có giá trị cao hơn, phần chênh lệch được xử lý theo chính sách áp dụng.

Nếu không có sản phẩm thay thế hoặc trường hợp không thể xử lý theo quy tắc thông thường, yêu cầu được chuyển sang phương án khác hoặc chuyển cho Quản lý/đơn vị có thẩm quyền xem xét.

Sau khi phương án xử lý được thực hiện, CSKH hoặc Nhân viên cửa hàng cập nhật trạng thái và thông báo kết quả cuối cùng cho Khách hàng.

Quy trình kết thúc khi Khách hàng nhận được kết quả xử lý như đổi hàng, bảo hành, phương án xử lý khác hoặc thông báo từ chối có lý do.

## Luồng chính

1. Khách hàng gửi yêu cầu đổi hàng, bảo hành hoặc khiếu nại.
2. CSKH/Nhân viên cửa hàng tiếp nhận yêu cầu.
3. Xác định giao dịch liên quan.
4. Nếu chưa đủ thông tin, yêu cầu Khách hàng bổ sung.
5. Kiểm tra các điều kiện áp dụng:
   - Thời hạn.
   - Chứng từ mua hàng.
   - Nhóm sản phẩm.
   - Điều kiện theo chính sách.
6. Nếu thiếu hồ sơ hoặc bằng chứng, yêu cầu bổ sung.
7. Kiểm tra sản phẩm và bằng chứng liên quan.
8. Xác định yêu cầu có đủ điều kiện hỗ trợ hay không.
9. Nếu không đủ điều kiện, thông báo từ chối và lý do.
10. Nếu đủ điều kiện, xác định phương án xử lý.
11. Nếu đổi hàng, kiểm tra sản phẩm thay thế.
12. Nếu có sản phẩm thay thế, thực hiện đổi hàng.
13. Nếu sản phẩm thay thế có giá trị cao hơn, xử lý phần chênh lệch theo chính sách.
14. Nếu không có sản phẩm thay thế hoặc không thể xử lý theo quy tắc thông thường, chuyển phương án khác hoặc chuyển cấp.
15. Cập nhật trạng thái và thông báo kết quả cho Khách hàng.
16. Kết thúc quy trình.

## Điểm quyết định chính

- Có xác định được giao dịch liên quan không?
- Hồ sơ/thông tin đã đầy đủ chưa?
- Yêu cầu có nằm trong thời hạn và điều kiện áp dụng không?
- Sản phẩm có đáp ứng điều kiện hỗ trợ không?
- Có sản phẩm thay thế phù hợp không?
- Sản phẩm thay thế có giá trị cao hơn không?
- Trường hợp có thể xử lý theo quy tắc thông thường hay cần chuyển cấp?

## Điểm cần xác nhận trước khi chốt BPMN

- Kênh tiếp nhận chính thức của yêu cầu là CSKH, cửa hàng hay cả hai.
- Ai là người trực tiếp kiểm tra tình trạng sản phẩm.
- Có bộ phận kiểm tra sản phẩm riêng hay do cửa hàng/kho thực hiện.
- Trường hợp nào bắt buộc cần ảnh/video.
- Khi không có sản phẩm thay thế, phương án ưu tiên là bảo hành, phương án khác hay chuyển cấp.
- Trường hợp nào bắt buộc phải có Quản lý/đơn vị có thẩm quyền phê duyệt.
- Có bước hoàn tiền trong S1 hay không; nếu có thì nằm ở nhánh nào và do đơn vị nào thực hiện.
- Hệ thống/biểu mẫu dùng để ghi nhận và theo dõi yêu cầu.
