# Phân tích định tính quy trình xử lý đơn hàng trực tuyến và giao hàng
## Phân loại hoạt động theo VA/BVA/NVA

Bảng phân loại 31 hoạt động từ góc nhìn người mua hàng trực tuyến, dựa trên giá trị khách hàng nhận được và yêu cầu vận hành, kiểm soát của ACFC.

| Hoạt động | Người thực hiện | VA/BVA/NVA | Giải thích |
|---|---|---|---|
| 1. Gửi thông tin đơn | Khách hàng | VA | Hình thành yêu cầu mua hàng theo nhu cầu của khách hàng. |
| 2. Xác nhận thông tin đơn | Khách hàng | VA | Bảo đảm đơn phản ánh đúng sản phẩm, số lượng, giao hàng và thanh toán khách hàng chọn. |
| 3. Chọn phương án xử lý thiếu hàng | Khách hàng | VA | Cho phép khách hàng quyết định kết quả phù hợp khi ACFC không đủ hàng. |
| 4. Nhận hàng | Khách hàng | VA | Là kết quả trực tiếp khách hàng cần đạt từ quy trình. |
| 5. Gọi xác thực thông tin đơn | Bộ phận xử lý đơn hàng | BVA | Không trực tiếp tạo giá trị cho khách hàng nhưng là kiểm soát bắt buộc trước khi xử lý đơn. |
| 6. Hủy đơn | Bộ phận xử lý đơn hàng | BVA | Ngăn ACFC tiếp tục xử lý đơn không xác thực được, tránh phát sinh chi phí và rủi ro giao hàng. |
| 7. Kiểm tra tồn kho trên hệ thống | Bộ phận xử lý đơn hàng | BVA | Cần để kiểm soát khả năng đáp ứng và quyết định luồng đủ hàng hoặc thiếu hàng. |
| 8. Thông báo tình trạng thiếu hàng | Bộ phận xử lý đơn hàng | VA | Cung cấp thông tin để khách hàng chọn phương án phù hợp với nhu cầu. |
| 9. Đóng gói đơn hàng | Bộ phận xử lý đơn hàng | VA | Chuẩn bị hàng đủ điều kiện bàn giao và bảo vệ hàng trong quá trình giao. |
| 10. Thực hiện phương án khách hàng chọn | Bộ phận xử lý đơn hàng | VA | Điều chỉnh đơn theo lựa chọn cụ thể của khách hàng khi thiếu hàng. |
| 11. Gửi xác nhận hủy | Bộ phận xử lý đơn hàng | VA | Xác nhận kết quả hủy mà khách hàng đã lựa chọn. |
| 12. Hoàn tất và bàn giao kiện hàng | Bộ phận xử lý đơn hàng | VA | Đưa kiện hàng vào luồng vận chuyển để khách hàng có thể nhận hàng. |
| 13. Tiếp nhận kết quả giao | Bộ phận xử lý đơn hàng | NVA | Chỉ tiếp nhận thông tin từ Đơn vị vận chuyển, không làm thay đổi kết quả khách hàng nhận; có thể tự động hóa. |
| 14. Cập nhật, đối soát và đóng đơn | Bộ phận xử lý đơn hàng | BVA | Cần để kiểm soát trạng thái, thanh toán và hoàn tất quản lý đơn. |
| 15. Cập nhật trạng thái giao thất bại | Bộ phận xử lý đơn hàng | BVA | Ghi nhận tình trạng cần thiết để kiểm soát và tiếp tục xử lý đơn. |
| 16. Liên hệ khách hàng | Bộ phận xử lý đơn hàng | VA | Làm rõ thông tin giao lại để khách hàng có thể nhận hàng. |
| 17. Gửi yêu cầu giao lại | Bộ phận xử lý đơn hàng | NVA | Chỉ chuyển yêu cầu giữa ACFC và Đơn vị vận chuyển sau lần giao không thành công. |
| 18. Tiếp nhận hàng hoàn | Bộ phận xử lý đơn hàng | NVA | Là công việc phục hồi phát sinh vì đơn không được giao thành công. |
| 19. Kiểm tra hàng hoàn | Bộ phận xử lý đơn hàng | BVA | Cần để kiểm soát tình trạng hàng và quyết định cập nhật tồn kho hoặc chuyển khiếu nại. |
| 20. Cập nhật tồn kho, thanh toán, trạng thái và đóng đơn | Bộ phận xử lý đơn hàng | BVA | Cần để kiểm soát hàng hoàn, nghĩa vụ tài chính, trạng thái và kết thúc đơn. |
| 21. Chuyển trường hợp khiếu nại | Bộ phận xử lý đơn hàng | NVA | Chỉ bàn giao thông tin sang bộ phận khác, không thực hiện xử lý nghiệp vụ bổ sung. |
| 22. Tiếp nhận trường hợp khiếu nại | Bộ phận xử lý khiếu nại | NVA | Chỉ tiếp nhận thông tin bàn giao, có thể giảm bằng chuyển hồ sơ và trạng thái tự động. |
| 23. Nhận kiện hàng | Đơn vị vận chuyển | BVA | Là điều kiện vận hành bắt buộc để Đơn vị vận chuyển thực hiện giao hàng. |
| 24. Giao hàng | Đơn vị vận chuyển | VA | Trực tiếp đưa sản phẩm đến khách hàng và tạo kết quả chính của dịch vụ. |
| 25. Xác định kết quả giao | Đơn vị vận chuyển | BVA | Cần để xác định đơn giao thành công hay phải chuyển sang xử lý thất bại. |
| 26. Gửi kết quả giao thành công | Đơn vị vận chuyển | NVA | Chỉ truyền kết quả giao cho ACFC, không tạo thêm giá trị cho khách hàng. |
| 27. Xác định nguyên nhân giao thất bại | Đơn vị vận chuyển | BVA | Cung cấp căn cứ để quyết định cách xử lý tiếp theo và theo dõi nguyên nhân thất bại. |
| 28. Đánh giá khả năng giao lại | Đơn vị vận chuyển | BVA | Tránh tổ chức giao lại khi không còn khả thi và hỗ trợ quyết định chuyển hoàn. |
| 29. Gửi kết quả giao và đánh giá | Đơn vị vận chuyển | NVA | Chỉ truyền thông tin xử lý giữa Đơn vị vận chuyển và ACFC. |
| 30. Giao lại | Đơn vị vận chuyển | NVA | Làm lại hoạt động giao hàng vì lần giao trước không đạt kết quả. |
| 31. Chuyển hàng về | Đơn vị vận chuyển | NVA | Là vận chuyển ngược phát sinh vì không thể hoàn tất giao hàng. |

Kết quả gồm 11 hoạt động VA, 11 hoạt động BVA và 9 hoạt động NVA. VA tập trung vào xác lập nhu cầu, chuẩn bị và giao hàng; BVA tập trung vào kiểm soát tồn kho, trạng thái, thanh toán và ngoại lệ; NVA tập trung ở chuyển tiếp thông tin và xử lý sau giao thất bại. Vì vậy, ACFC cần giữ ổn định VA, tinh gọn BVA và ưu tiên giảm NVA, trước hết ở các bước chuyển tiếp thông tin.

## Phân tích lãng phí

Bảng phân tích lãng phí xem xét quy trình hiện trạng từ góc độ công việc không tạo giá trị và chỉ ghi nhận các loại có bằng chứng từ mô hình hoặc phỏng vấn.

| Bước | Loại lãng phí | Bằng chứng | Tác động | Hướng xử lý |
|---|---|---|---|---|
| Nhánh chờ bổ sung hàng sau bước 10 | Waiting/Hold | Khách hàng có thể chọn chờ hàng; đơn chỉ được đóng gói sau khi có hàng bổ sung. | Kéo dài thời gian hoàn tất và giữ đơn ở trạng thái chờ. | Kiểm tra khả năng đáp ứng sớm, thông báo thời gian dự kiến và theo dõi riêng đơn chờ hàng. |
| 9 và 12. Đóng gói, hoàn tất và bàn giao kiện hàng | Waiting/Hold | Dữ liệu phỏng vấn xác nhận phần việc chưa hoàn thành phải chuyển sang ngày làm việc tiếp theo khi đã hết giờ làm việc. | Đơn dở dang phải chờ sang ngày sau, kéo dài thời gian bàn giao. | Theo dõi giờ tiếp nhận, giờ đóng gói xong và giờ bàn giao; nhận diện đơn gần cuối ca để điều phối hoặc thông báo mốc xử lý tiếp theo. |
| 13, 26 và 29. Gửi, tiếp nhận kết quả giao | Move | Kết quả giao được chuyển từ Đơn vị vận chuyển sang Bộ phận xử lý đơn hàng rồi mới được cập nhật. | Tăng bước bàn giao, thời gian cập nhật và nguy cơ trạng thái không đồng bộ. | Đồng bộ trạng thái giao tự động giữa hai bên, kèm nhật ký cập nhật. |
| 17, 21 và 22. Chuyển yêu cầu giao lại hoặc trường hợp khiếu nại | Move | Các bước chỉ chuyển thông tin giữa các vai trò, không có kiểm tra hoặc lập hồ sơ bổ sung. | Tăng số lần bàn giao và thời gian chờ bên tiếp nhận xử lý. | Tự động chuyển hồ sơ, phân công người xử lý và cập nhật trạng thái trên cùng luồng thông tin. |
| 30. Giao lại | Defect | Giao lại phát sinh sau lần giao thất bại. Các nguyên nhân thường gặp từ phía người nhận gồm không liên lạc được, không có mặt, từ chối nhận, sai số điện thoại hoặc sai địa chỉ. | Phát sinh thêm một lần xử lý và vận chuyển; kéo dài thời gian hoàn tất đơn. | Xác nhận lại số điện thoại, địa chỉ, khả năng nhận hàng và thời điểm giao dựa trên nguyên nhân thực tế trước khi giao lại. |
| 31. Chuyển hàng về | Move | Đơn vị vận chuyển phải vận chuyển ngược kiện hàng khi không thể tiếp tục giao. | Phát sinh quãng vận chuyển, tiếp nhận hàng hoàn và kéo dài thời gian đóng đơn. | Ghi nhận nguyên nhân chuyển hoàn; giảm các nguyên nhân có thể phòng ngừa bằng xác nhận thông tin người nhận trước khi giao. |
| 19-22. Kiểm tra hàng hoàn và chuyển khiếu nại | Defect | Hàng hoàn có thể hư hỏng hoặc thất lạc. Giả định: thất lạc là thiếu hàng trong kiện hoàn đã được tiếp nhận. | Phát sinh kiểm tra, xử lý khiếu nại và điều chỉnh tồn kho hoặc thanh toán; có nguy cơ mất hàng. | Lưu bằng chứng bàn giao và tình trạng kiện hoàn; phân nhóm nguyên nhân trước khi quy trách nhiệm hoặc chọn biện pháp khắc phục. |

Lãng phí tập trung ở thời gian chờ bổ sung hàng hoặc sang ngày làm việc tiếp theo, các lượt chuyển thông tin và công việc phát sinh sau giao thất bại. Ưu tiên cải tiến là theo dõi mốc xử lý, đồng bộ trạng thái giao, xác nhận lại thông tin người nhận và kiểm soát bàn giao hàng hoàn. Chưa đưa Over-processing, Inventory và Overproduction vì chưa có bằng chứng.
