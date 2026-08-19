# Vòng đời BPM: Phân tích Quy trình

## 1. Mục tiêu phân tích quy trình

- Sau khi mô hình hóa xong, câu hỏi đặt ra là: quy trình vừa vẽ ra liệu đã đạt được **performance** mà người quản lý mong muốn hay chưa? Nếu chưa, phải quay lại đánh giá và mô hình hóa lại.
- Phân tích quy trình chính là bước trả lời câu hỏi đó — tìm xem hoạt động nào đang gây vấn đề, nguyên nhân vì sao, và có cách nào hỗ trợ để giảm sai sót, giảm thời gian, giảm chi phí cho bước đó.
- Đầu ra của giai đoạn này là một danh sách các vấn đề đã được ghi nhận, kèm nguyên nhân gốc rễ — làm cơ sở để bước Thiết kế lại biết nên sửa gì.
- Hai hướng tiếp cận song song:
  - **Phân tích định tính:** một dạng nghiên cứu dựa trên quan sát, phỏng vấn, bảng câu hỏi — để tìm hiểu ý kiến, quan điểm, và bản chất thật sự của vấn đề từ chính người đang vận hành quy trình.
  - **Phân tích định lượng:** dựa trên số liệu — thời gian, chi phí, chất lượng — để đánh giá hiệu suất quy trình một cách khách quan hơn.

## 2. Phân tích định tính

- **Phân tích giá trị gia tăng (Value-Added Analysis):**
  - Bước đầu tiên là chia nhỏ quy trình thành các hoạt động, rồi chia mỗi hoạt động thành các bước — có thể là bước chuẩn bị, bước thực thi, hoặc bước tạm dừng.
  - Sau đó phân loại từng bước vào một trong ba nhóm:
    - **VA — Gia tăng giá trị (Value-Adding):** bước trực tiếp tạo ra giá trị hoặc sự hài lòng cho khách hàng. Để xác định, tự hỏi ba câu: khách hàng có sẵn lòng trả tiền cho bước này không? Khách hàng có đồng ý đây là bước cần thiết để đạt mục tiêu của họ không? Nếu bỏ bước này, khách hàng có thấy sản phẩm/dịch vụ kém giá trị hơn không?
    - **BVA/PVA — Gia tăng giá trị nghiệp vụ (Business Value-Adding):** bước không trực tiếp phục vụ khách hàng nhưng cần thiết để doanh nghiệp vận hành trơn tru, tạo doanh thu, hoặc đáp ứng yêu cầu pháp lý. Câu hỏi nhận diện: bước này có cần thiết để tạo doanh thu hay cải thiện doanh nghiệp không? Nếu bỏ đi, công ty có nguy cơ thua lỗ hay vi phạm quy định không? Ví dụ: kiểm tra tính đầy đủ hồ sơ tuyển sinh, xác minh tính hợp lệ của bằng cấp — bỏ qua bước này, cơ quan quản lý có thể xử phạt nếu phát hiện hồ sơ giả mạo.
    - **NVA — Không gia tăng giá trị (Non-Value-Adding):** những bước còn lại — thường là bàn giao, chuyển tiếp thông tin nội bộ, chờ đợi phê duyệt, hoặc làm lại vì lỗi. Ví dụ: kỹ sư công trường gửi yêu cầu thiết bị cho thư ký, thư ký tìm kiếm rồi chờ kỹ sư văn phòng duyệt — cả chuỗi bàn giao và chờ đợi này không tạo ra giá trị nào cho khách hàng.
- **Phân tích sự lãng phí (Waste Analysis):**
  - Nếu phân tích giá trị gia tăng nhìn quy trình theo hướng tích cực (tìm bước nào tạo giá trị), thì phân tích lãng phí nhìn theo hướng ngược lại — cố tìm ra những hao phí ẩn trong quy trình.
  - Kỹ thuật này bắt nguồn từ Taiichi Ohno, người xây dựng hệ thống sản xuất của Toyota những năm 1970, sau này được tích hợp vào nhiều mô hình quản lý khác như Lean Management. Ý tưởng cốt lõi: nhìn suốt dòng thời gian từ lúc nhận yêu cầu khách hàng đến lúc thu được tiền, rồi cố gắng cắt bỏ mọi hao phí không tạo ra giá trị trên dòng thời gian đó.
  - Ba nhóm lãng phí chính:
    - **Vận chuyển (Move):** di chuyển không cần thiết — *Transportation* (vật liệu, tài liệu vật lý di chuyển giữa phòng ban, giữa công ty và bên ngoài) và *Motion* (chuyển động thừa của người thực hiện). Cách giảm phổ biến là chuyển sang tài liệu điện tử thay vì bản giấy.
    - **Lưu kho/Chờ đợi (Hold):** *Inventory* — công việc tồn đọng, ví dụ hàng trăm phương tiện đang chờ xử lý tại một trạm kiểm tra; và *Waiting* — chờ tài nguyên, chờ phê duyệt từ nhiều phòng ban.
    - **Làm quá mức (Over-do):** *Defects* — lỗi dẫn đến vòng lặp làm lại; *Over-processing* — làm kỹ hơn mức cần thiết, ví dụ đo khí thải xe chính xác hơn tiêu chuẩn yêu cầu gây hao mòn xe không cần thiết; *Over-production* — tạo ra kết quả không ai dùng đến, ví dụ báo giá gửi đi nhưng phần lớn không chuyển thành đơn hàng, hay phần lớn hồ sơ tuyển sinh nộp vào không đủ điều kiện nhưng vẫn phải tốn công xử lý.
- **Phân tích bên liên quan & Đăng ký vấn đề:**
  - Cùng một quy trình, mỗi người sẽ nhìn thấy một con số khác nhau — người này thấy vấn đề nghiêm trọng, người kia lại không. Vì vậy cần thu thập ý kiến từ nhiều phía để trung hòa các quan điểm thiên vị.
  - Năm nhóm đối tượng thường được phỏng vấn: khách hàng, người trực tiếp vận hành quy trình, đối tác/nhà cung cấp bên ngoài, chủ sở hữu quy trình, và nhà tài trợ. Mỗi nhóm quan tâm đến khía cạnh khác nhau — khách hàng lo về thời gian và tính minh bạch, người vận hành than phiền về áp lực và lỗi trong khâu bàn giao.
  - Các vấn đề thu thập được ghi vào một bảng đăng ký vấn đề: định danh vấn đề, mô tả, mức độ ảnh hưởng, và đề xuất khắc phục.
- **Truy nguyên nhân gốc rễ:**
  - **Biểu đồ Pareto:** so sánh mức độ tác động của từng vấn đề bằng biểu đồ cột, giúp thấy ngay vấn đề nào đáng ưu tiên xử lý nhất.
  - **Mô hình 5 Whys:** hỏi liên tiếp "tại sao" — tối đa khoảng năm cấp — để đi từ triệu chứng bề mặt đến nguyên nhân sâu xa.
  - **Sơ đồ xương cá (Fishbone):** phân nhóm nguyên nhân theo các yếu tố khác nhau, dựng thành hai cấp — nguyên nhân chính và nguyên nhân thứ cấp.

## 3. Phân tích định lượng

- Nếu phân tích định tính trả lời câu hỏi "vấn đề là gì, do đâu", thì phân tích định lượng trả lời bằng con số: quy trình đang tốn bao nhiêu thời gian, chi phí, và chất lượng ra sao.
- **Ba loại thời gian:**
  - **Thời gian xử lý (Processing time):** thời gian thực tế thực hiện công việc.
  - **Thời gian chờ (Waiting time):** thời gian nằm chờ — chờ tài nguyên, chờ phê duyệt.
  - **Thời gian chu kỳ (Cycle time):** tổng thời gian từ lúc bắt đầu đến lúc hoàn thành cả quy trình.
  - **Hiệu suất chu kỳ** = thời gian xử lý chia cho thời gian chu kỳ — tỷ lệ càng thấp, quy trình càng mất nhiều thời gian vào việc chờ hơn là làm việc thật sự.
- **Công thức tính thời gian chu kỳ theo cấu trúc luồng:**
  - **Tuần tự:** cộng dồn thời gian từng hoạt động — t1 + t2 + ... + tn.
  - **Rẽ nhánh lựa chọn (XOR):** không biết chắc đi nhánh nào, nên lấy trung bình có trọng số theo xác suất từng nhánh — ví dụ nhánh xảy ra 90% mất 20 đơn vị thời gian, nhánh còn lại xảy ra 10% mất 10 đơn vị, thì thời gian trung bình là 0,9×20 + 0,1×10 = 19 đơn vị.
  - **Song song (AND):** các nhánh chạy đồng thời, nên chỉ cần tính theo nhánh mất thời gian lâu nhất — lấy max trong các nhánh.
  - **Vòng lặp làm lại:** có xác suất phải quay lại làm lại, công thức là t chia cho (1 trừ r), với r là tỷ lệ phải làm lại — tỷ lệ làm lại càng cao, thời gian chu kỳ trung bình càng kéo dài.
- **Mô phỏng quy trình:**
  - Trong thực tế, số liệu thời gian không phải lúc nào cũng có sẵn hoặc đo được chính xác — nhiều khi phải ước lượng dựa trên quan sát hoặc kinh nghiệm.
  - Mô phỏng là cách chạy thử quy trình nhiều lần với các con số giả định có gắn xác suất, để ước lượng ra phân phối thời gian, chi phí, và mức độ sử dụng tài nguyên trước khi bắt tay vào cải tiến thật sự.

## 4. Ví dụ minh họa

- **Quy trình mượn thiết bị của công ty PIT:** dùng xuyên suốt buổi học để minh họa cả hai nhánh phân tích — từ phân loại VA/BVA/NVA cho từng bước (điền form, gửi thư ký, kiểm tra tồn kho, phê duyệt của kỹ sư văn phòng...), đến tính lãng phí vận chuyển tài liệu vật lý và vòng lặp xử lý lỗi, rồi dùng biểu đồ Pareto để tìm ra "chấp thuận trễ" là nguyên nhân chiếm phần lớn chi phí phát sinh.
- **Quy trình tuyển sinh của Đại học Newton:** ví dụ để lớp thực hành phân loại VA/BVA/NVA, như xác minh hồ sơ đầy đủ, kiểm tra tính hợp lệ bằng cấp và chứng chỉ ngoại ngữ; đồng thời minh họa lãng phí over-production khi phần lớn đơn đăng ký nộp vào không đủ điều kiện nhưng vẫn tốn công xử lý.
- **Tính thời gian chu kỳ:** áp dụng công thức cho từng loại cấu trúc luồng — tuần tự cộng dồn, rẽ nhánh nhân xác suất, song song lấy max.
