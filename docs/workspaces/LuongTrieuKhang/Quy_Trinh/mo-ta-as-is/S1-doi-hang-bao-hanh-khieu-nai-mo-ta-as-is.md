# S1 – Đổi hàng, bảo hành và xử lý khiếu nại - hiện trạng

Quy trình bắt đầu khi Khách hàng phát sinh nhu cầu đổi hàng, bảo hành hoặc khiếu nại liên quan đến một giao dịch đã thực hiện và gửi yêu cầu đến ACFC qua kênh tiếp nhận phù hợp.

CSKH hoặc Nhân viên cửa hàng tiếp nhận yêu cầu và ghi nhận các thông tin ban đầu như mã đơn hàng, hóa đơn, sản phẩm liên quan và lý do yêu cầu.

Nếu chưa xác định được giao dịch hoặc thông tin ban đầu chưa đầy đủ, Khách hàng được hướng dẫn bổ sung thông tin. Sau khi thông tin được bổ sung đầy đủ và giao dịch đã được xác định, yêu cầu tiếp tục được xử lý.

CSKH hoặc Nhân viên cửa hàng kiểm tra hồ sơ và các điều kiện áp dụng của yêu cầu, bao gồm thời hạn, chứng từ mua hàng, nhóm sản phẩm và các điều kiện liên quan theo chính sách đổi hàng/bảo hành.

Nếu hồ sơ hoặc bằng chứng chưa đầy đủ, Khách hàng được yêu cầu bổ sung. Tùy từng trường hợp, bằng chứng có thể bao gồm ảnh hoặc video thể hiện tình trạng sản phẩm. Sau khi hồ sơ được bổ sung đầy đủ, quy trình tiếp tục sang bước kiểm tra sản phẩm.

Đơn vị kiểm tra/xử lý sản phẩm thực hiện kiểm tra sản phẩm và các bằng chứng liên quan để xác định yêu cầu có đáp ứng điều kiện hỗ trợ hay không. Tên đơn vị thực tế thực hiện bước kiểm tra này cần được xác nhận.

Nếu yêu cầu không đáp ứng điều kiện hỗ trợ, CSKH hoặc Nhân viên cửa hàng thông báo từ chối và nêu rõ lý do cho Khách hàng. Quy trình kết thúc với kết quả **Yêu cầu bị từ chối**.

Nếu yêu cầu đáp ứng điều kiện hỗ trợ, đơn vị xử lý xác định phương án phù hợp. Phương án có thể là đổi sản phẩm, bảo hành hoặc hình thức xử lý khác tùy theo trường hợp và chính sách áp dụng.

Nếu phương án là đổi hàng, đơn vị liên quan kiểm tra khả năng có sản phẩm thay thế phù hợp.

Nếu có sản phẩm thay thế, việc đổi hàng được thực hiện. Trường hợp sản phẩm thay thế có giá trị cao hơn, phần chênh lệch được xử lý theo chính sách áp dụng.

Nếu không có sản phẩm thay thế, yêu cầu được xem xét để áp dụng phương án hỗ trợ khác theo chính sách.

Nếu phương án không phải đổi hàng, yêu cầu được chuyển sang bảo hành hoặc phương án xử lý khác phù hợp.

Trong trường hợp yêu cầu không thể xử lý theo quy tắc thông thường hoặc cần phê duyệt ngoại lệ, yêu cầu được chuyển cho Quản lý hoặc đơn vị có thẩm quyền xem xét và quyết định phương án xử lý.

Sau khi phương án xử lý được thực hiện, CSKH hoặc Nhân viên cửa hàng cập nhật trạng thái yêu cầu và thông báo kết quả cuối cùng cho Khách hàng.

Quy trình có hai kết quả chính:

- **Yêu cầu được xử lý:** Khách hàng nhận được kết quả đổi hàng, bảo hành hoặc phương án hỗ trợ khác.
- **Yêu cầu bị từ chối:** Khách hàng được thông báo lý do yêu cầu không đáp ứng điều kiện hỗ trợ.

Quy trình kết thúc khi kết quả đã được thông báo cho Khách hàng và trạng thái yêu cầu đã được cập nhật.

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

## Nội dung cần xác nhận

- Process Owner chính thức của S1.
- Các kênh tiếp nhận yêu cầu thực tế.
- Đơn vị thực hiện kiểm tra sản phẩm/bằng chứng.
- SLA cho bước yêu cầu khách hàng bổ sung thông tin/hồ sơ.
- SLA cho bước kiểm tra sản phẩm.
- SLA cho trường hợp chuyển cấp hoặc phê duyệt ngoại lệ.
- Các điều kiện cụ thể để đổi hàng, bảo hành hoặc từ chối.
- Phương án xử lý khi không có sản phẩm thay thế.
- Cấp có thẩm quyền phê duyệt trường hợp ngoại lệ.
- Hệ thống hoặc biểu mẫu sử dụng để tạo và theo dõi case.
- Việc xử lý chênh lệch giá khi đổi sản phẩm.
- Có hay không trường hợp hoàn tiền trong phạm vi S1.