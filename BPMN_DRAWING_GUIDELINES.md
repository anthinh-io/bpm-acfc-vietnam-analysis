# Quy tắc vẽ và rà soát sơ đồ BPMN

## 1. Chuẩn và thứ tự thực hiện

- [ ] Dùng đúng chuẩn **BPMN 2.0**, không dùng flowchart hoặc UML thay thế.
- [ ] Mô tả bằng lời trước khi vẽ: tác nhân, khách hàng, trigger, các bước theo thứ tự và outcome tích cực/tiêu cực.
- [ ] Mỗi hình thể hiện khoảng một quy trình. Quy trình lớn cần chia thành subprocess hoặc sơ đồ con.
- [ ] Sơ đồ phải khớp với mô tả quy trình, dữ liệu khảo sát và workshop.
- [ ] Có thể dùng Lucidchart hoặc công cụ BPMN tương đương.
- [ ] Sơ đồ có đủ độ phức tạp theo rubric: 0 gateway = 0 điểm; dưới 3 = 0,25 điểm; 4-5 = 0,5 điểm; trên 5 = 0,75 điểm; trên 7 = 1 điểm.

## 2. Pool và lane

- [ ] Pool đại diện cho tổ chức hoặc đối tác; lane đại diện cho vai trò, bộ phận hoặc hệ thống như ERP, CRM.
- [ ] Phân biệt rõ pool nội bộ và pool bên ngoài, ví dụ khách hàng hoặc đối tác.
- [ ] Có thể dùng mỗi tổ chức một pool với nhiều lane. Nếu gộp nhiều bộ phận, pool phải thể hiện rõ tổ chức bao trùm.
- [ ] Mọi tác nhân trong mô tả quy trình đều có pool hoặc lane tương ứng.
- [ ] Mỗi activity nằm trong lane của người, bộ phận hoặc hệ thống thực hiện, không để activity nằm ngoài lane.
- [ ] Thuật ngữ về vai trò phải nhất quán giữa các sơ đồ, ví dụ chỉ dùng một tên là "Nhân viên kho".

![Quy tắc về pool, lane và message flow](diagrams/images/bpmn-pool-lane.png)

*Nguồn: slide/chap03.pdf, trang 54.*

## 3. Activity và subprocess

- [ ] Activity dùng hình chữ nhật bo góc.
- [ ] Tên activity theo cấu trúc **Động từ + Danh từ/Tân ngữ**, ví dụ "Kiểm tra tồn kho".
- [ ] Tránh tên mơ hồ như "Xử lý", "Ghi lại" hoặc "Thực hiện".
- [ ] Không tách nhiều sequence flow trực tiếp từ activity khi các luồng biểu diễn kết quả khác nhau; phải dùng gateway.
- [ ] Activity phức tạp được mô hình hóa thành subprocess và có dấu **+**.
- [ ] Với subprocess đóng, luồng chỉ nối vào khung subprocess.
- [ ] Với subprocess mở rộng, activity bên trong không nối trực tiếp ra process cha.

![Ví dụ thiết kế BPMN và cách đặt tên activity](diagrams/images/bpmn-vi-du.png)

*Nguồn: slide/chap03.pdf, trang 30.*

## 4. Event

![Ký hiệu start, intermediate và end event](diagrams/images/bpmn-event-types.png)

*Nguồn: hình người dùng cung cấp.*

- [ ] Start event là hình tròn nét đơn; sơ đồ đơn giản chỉ dùng một start event.
- [ ] Intermediate event là hình tròn nét đôi; dùng timer event khi có bước chờ hoặc lặp theo thời hạn.
- [ ] End event là hình tròn nét đậm và phải thể hiện outcome thật, ví dụ "Đơn hàng đã hoàn tất" hoặc "Đơn hàng đã từ chối".
- [ ] Có thể dùng nhiều end event cho các nhánh tích cực và tiêu cực.
- [ ] Tên event mô tả trạng thái đã xảy ra, ví dụ "Đơn hàng đã nhận", không đặt như tên activity.
- [ ] Message event dùng đúng ký hiệu phong bì: rỗng là nhận, tô đen là gửi.
- [ ] Không đặt end event giữa quy trình nếu luồng nghiệp vụ thực tế vẫn tiếp tục.

![Các dạng event BPMN](diagrams/images/bpmn-event.png)

*Nguồn: slide/chap03.pdf, trang 59.*

## 5. Gateway

![Các loại gateway BPMN](diagrams/images/bpmn-gateway-types.png)

*Nguồn: hình người dùng cung cấp.*

- [ ] Dùng **XOR** khi chỉ đúng một nhánh được chọn.
- [ ] Dùng **AND** khi tất cả nhánh chạy song song và chỉ tiếp tục sau khi mọi nhánh hoàn tất.
- [ ] Dùng **OR** khi một hoặc nhiều nhánh có thể được chọn.
- [ ] Dùng **event-based gateway** khi nhánh tiếp theo phụ thuộc vào sự kiện xảy ra, không dùng để kiểm tra điều kiện dữ liệu.
- [ ] Dùng **parallel event-based gateway** khi phải chờ các sự kiện quy định cùng xảy ra trước khi tiếp tục.
- [ ] Chỉ dùng **complex gateway** cho điều kiện đồng bộ đặc biệt không biểu diễn được bằng XOR, AND hoặc OR; phải ghi rõ quy tắc kích hoạt.
- [ ] Mỗi nhánh ra từ XOR hoặc OR đều có nhãn điều kiện.
- [ ] Split phải có join tương ứng cùng loại, trừ nhánh kết thúc ngay sau split.
- [ ] Không split bằng OR rồi join bằng AND hoặc ghép sai loại gateway.
- [ ] Có nhánh tích cực và tiêu cực khi quy trình có cả hai outcome.

![So sánh gateway XOR, AND và OR](diagrams/images/bpmn-gateway.png)

*Nguồn: slide/chap03.pdf, trang 44.*

## 6. Luồng kết nối

- [ ] Sequence flow là nét liền có mũi tên và chỉ dùng trong cùng một pool.
- [ ] Không dùng sequence flow xuyên ranh giới giữa hai pool.
- [ ] Message flow là nét đứt và chỉ dùng để trao đổi giữa các pool, ví dụ gửi đơn hàng, hóa đơn hoặc thông báo.
- [ ] Không dùng message flow để nối các activity trong cùng một pool.
- [ ] Không nối trực tiếp từ bên ngoài vào activity ẩn bên trong subprocess.
- [ ] Đường nối rõ ràng, hạn chế giao cắt và không gây hiểu sai thứ tự thực hiện.

## 7. Dữ liệu

- [ ] Data object biểu diễn file hoặc hồ sơ; collection có ba gạch; data store dùng hình trụ.
- [ ] Mỗi đối tượng dữ liệu có data association nối với ít nhất một activity.
- [ ] Association được dùng để nối dữ liệu hoặc annotation, không thay cho sequence flow.
- [ ] Hướng dữ liệu nhất quán: mũi tên rỗng là input, mũi tên đặc là output.

![Ví dụ data object và data store](diagrams/images/bpmn-du-lieu.png)

*Nguồn: slide/chap03.pdf, trang 56.*

## 8. Rà soát trước khi nộp

- [ ] Đối chiếu với rubric, đặc biệt là số gateway, cách đặt tên và chuẩn ký hiệu.
- [ ] Kiểm tra mọi split và join, vì thiếu join là lỗi logic nghiêm trọng.
- [ ] Kiểm tra tên tác nhân, activity, event và dữ liệu khớp với phần mô tả bằng lời.
- [ ] Kiểm tra pool, lane, sequence flow và message flow đúng phạm vi.
- [ ] Kiểm tra không có dữ liệu mồ côi hoặc ký hiệu sai hình dạng.
- [ ] So khớp cách đặt tên pool và lane giữa các thành viên trong nhóm.
- [ ] Đảm bảo sơ đồ đủ rõ, dễ đọc và không để AI tạo tự do rồi nộp nguyên.
