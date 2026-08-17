# Phân tích định lượng quy trình tổ chức sự kiện truyền thông sản phẩm

Phân tích định lượng cho thấy cycle time của quy trình chịu ảnh hưởng chủ yếu từ thời gian chờ kế hoạch, báo giá, thời gian chờ tại cụm phê duyệt nội bộ và lần điều chỉnh đầu tiên của hồ sơ. Do các nhánh phê duyệt chạy song song, thời gian của cụm được xác định theo nhánh hoàn thành chậm nhất, hiện là Tài chính với tối đa 336 giờ theo lịch. Mô hình chỉ dùng tỷ lệ 80% cho lần kiểm tra hợp đồng đầu tiên, không suy rộng tỷ lệ này cho các lượt sau. Thời gian xử lý trực tiếp chỉ chiếm một phần của tổng thời gian, cho thấy dư địa giảm thời gian chờ và làm lại.

<p align="center">
  <img src="../../images/to-chuc-su-kien-truyen-thong-san-pham-dinh-luong.svg" alt="BPMN định lượng quy trình tổ chức sự kiện truyền thông sản phẩm" width="100%">
</p>

<p align="center"><em>Hình: BPMN định lượng thời gian và chi phí quy trình tổ chức sự kiện truyền thông sản phẩm</em></p>

Trên sơ đồ, nhãn màu nâu thể hiện CT, PT và tỷ lệ; nhãn màu xanh thể hiện chi phí nguồn lực. Cụm phê duyệt nội bộ được tách thành ba nhánh xử lý song song gồm Pháp lý, Tài chính và Procurement. Gateway AND chỉ cho phép quy trình tiếp tục sau khi các nhánh áp dụng cho hồ sơ đã hoàn tất. Tỷ lệ 80% của nhánh Procurement thể hiện tỷ lệ tổng số sự kiện có hàng tặng theo dữ liệu phỏng vấn.

## Cơ sở số liệu

Dữ liệu phỏng vấn người tham gia quy trình là nguồn đầu vào chính của phân tích. Các giá trị này được trình bày theo đúng nội dung thu thập và không cần bổ sung tài liệu nội bộ, biểu mẫu, phiếu hoặc hợp đồng để xác nhận.

| Biến | Giá trị | Đơn vị | Nguồn | Ghi chú |
|---|---:|---|---|---|
| Lập đề xuất ý tưởng | 16 | giờ làm việc/sự kiện | Phỏng vấn nội bộ ACFC | Ước lượng của người tham gia |
| Lập kế hoạch và báo giá lần đầu | 80 | giờ trôi qua trong lịch làm việc/sự kiện | Phỏng vấn nội bộ ACFC và đơn vị tổ chức sự kiện | Dữ liệu phỏng vấn |
| Phản hồi pháp lý một lượt | 72 | giờ theo lịch/lượt | Phỏng vấn nội bộ ACFC | Dữ liệu phỏng vấn |
| Phản hồi tài chính | Tối đa 336 | giờ theo lịch/hồ sơ | Phỏng vấn nội bộ ACFC | Giá trị tối đa, không phải giá trị trung bình |
| Hợp đồng bị yêu cầu sửa lần đầu | 80 | phần trăm hồ sơ | Phỏng vấn nội bộ ACFC | Tỷ lệ ước lượng từ phỏng vấn |
| Sự kiện có xuất hàng làm quà và cần Procurement duyệt | 80 | phần trăm tổng số sự kiện | Phỏng vấn nội bộ ACFC | Tỷ lệ ước tính từ phỏng vấn |
| Lập báo cáo hậu sự kiện | 16 | giờ làm việc/sự kiện | Phỏng vấn nội bộ ACFC | Ước lượng của người tham gia |

## Giả định tính toán

| Cụm hoạt động | Cycle time | Processing time | Nguồn | Ghi chú |
|---|---:|---:|---|---|
| Gửi và tiếp nhận yêu cầu | 2 giờ theo lịch/sự kiện | 1 giờ làm việc/sự kiện | Giả định phân tích | Giả định |
| Tiếp nhận và lập đề xuất ý tưởng | 48 giờ theo lịch/sự kiện | 16 giờ làm việc/sự kiện | Giả định phân tích từ thời gian xử lý phỏng vấn | CT 48 giờ là giả định; PT 16 giờ là dữ liệu phỏng vấn |
| Xây dựng kế hoạch và báo giá | 336 giờ theo lịch/sự kiện | 24 giờ làm việc/sự kiện | Quy đổi và giả định phân tích từ dữ liệu phỏng vấn | CT 336 giờ và PT 24 giờ là giả định; dữ liệu gốc là 80 giờ trong lịch làm việc, tương đương 10 ngày làm việc |
| Xem xét kế hoạch và xác nhận điều kiện | 72 giờ theo lịch/sự kiện | 16 giờ làm việc/sự kiện | Giả định phân tích | Giả định |
| Hoàn thiện và trình hồ sơ | 17 giờ theo lịch/hồ sơ | 8,5 giờ làm việc/hồ sơ | Giả định phân tích | Giả định |
| Phản hồi Pháp lý một lượt | 72 giờ theo lịch/hồ sơ | 4 giờ làm việc/hồ sơ | CT từ phỏng vấn nội bộ ACFC; PT từ giả định phân tích | Chỉ PT 4 giờ là giả định |
| Phản hồi Tài chính điển hình | 120 giờ theo lịch/hồ sơ | 4 giờ làm việc/hồ sơ | Giả định phân tích | Giả định |
| Phản hồi Procurement khi có hàng tặng | 96 giờ theo lịch/hồ sơ | 2 giờ làm việc/hồ sơ | Giả định phân tích | Giả định |
| Một lượt điều chỉnh hồ sơ | 64 giờ theo lịch/lượt | 24 giờ làm việc/lượt | Giả định phân tích | Giả định |
| Ký hợp đồng | 48 giờ theo lịch/hợp đồng | 2 giờ làm việc/hợp đồng | Giả định phân tích | Giả định |
| Chuẩn bị, thực hiện và giám sát sự kiện | 336 giờ theo lịch/sự kiện | 96 giờ làm việc/sự kiện | Giả định phân tích | Giả định |
| Bàn giao và nghiệm thu | 137 giờ theo lịch/sự kiện | 18,5 giờ làm việc/sự kiện | Giả định phân tích | Giả định |
| Thanh toán | 120 giờ theo lịch/hồ sơ | 4 giờ làm việc/hồ sơ | Giả định phân tích | Giả định |
| Lập Báo cáo hậu sự kiện | 48 giờ theo lịch/báo cáo | 16 giờ làm việc/báo cáo | PT từ phỏng vấn nội bộ ACFC; CT từ giả định quy đổi | Chỉ CT 48 giờ là giả định |
| Phê duyệt báo cáo | 24 giờ theo lịch/báo cáo | 2 giờ làm việc/báo cáo | Giả định phân tích | Giả định |

Tỷ lệ 80% chỉ phản ánh số dự thảo hợp đồng bị yêu cầu sửa sau lần kiểm tra đầu tiên. Mô hình dùng tỷ lệ này để tính phần thời gian tăng thêm của lần trả đầu tiên. Sau khi điều chỉnh, hồ sơ được tính thêm một lượt phê duyệt; các lượt trả lại tiếp theo không được định lượng.

### Chuẩn hóa đơn vị thời gian

Cycle time được quy đổi về giờ theo lịch. Thời gian lập kế hoạch và báo giá lần đầu là 80 giờ trong lịch làm việc, tương đương 10 ngày làm việc theo dữ liệu phỏng vấn. Mô hình giả định 10 ngày làm việc tương đương 14 ngày theo lịch, tức 336 giờ.

## Tính cycle time

### Phần tuần tự trước phê duyệt

Thời gian trước phê duyệt được cộng theo công thức tuần tự:

`CT_trước = 2 + 48 + 336 + 72 + 17 = 475 giờ theo lịch/sự kiện`.

Trong đó, 48 giờ cho tiếp nhận và lập đề xuất, cùng 72 giờ cho xem xét kế hoạch và xác nhận điều kiện, là giả định phân tích.

### Cụm phê duyệt nội bộ

Pháp lý, Tài chính và Procurement xử lý song song, nên cycle time của cụm bằng thời gian của nhánh chậm nhất:

- Kịch bản điển hình: `CT_AND = max(72, 120, 96) = 120 giờ theo lịch/hồ sơ`.
- Kịch bản biên trên: `CT_AND = max(72, 336, 96) = 336 giờ theo lịch/hồ sơ`.

Một lượt điều chỉnh có cycle time 64 giờ. Trường hợp bị trả lại lần đầu cần thêm một lượt điều chỉnh và một lượt phê duyệt. Cycle time kỳ vọng của cụm được tính như sau:

- Kịch bản điển hình: `CT_phê_duyệt = 120 + 80% × (64 + 120) = 267,2 giờ theo lịch/hồ sơ`.
- Kịch bản biên trên: `CT_phê_duyệt = 336 + 80% × (64 + 336) = 656 giờ theo lịch/hồ sơ`.

### Phần tuần tự sau phê duyệt

Sau khi hồ sơ được duyệt, hai nhánh thanh toán và lập báo cáo chạy song song. Thời gian của phần còn lại là:

`CT_sau = 48 + 336 + 137 + max(120, 48) + 24 = 665 giờ theo lịch/sự kiện`.

### Cycle time toàn quy trình

Kết quả áp dụng cho trường hợp đi đến kết quả `Sự kiện hoàn thành`:

- Kịch bản điển hình: `CT = 475 + 267,2 + 665 = 1.407,2 giờ`, tương đương `58,6 ngày theo lịch/sự kiện`.
- Kịch bản biên trên: `CT = 475 + 656 + 665 = 1.796 giờ`, tương đương `74,8 ngày theo lịch/sự kiện`.

Khoảng cách giữa hai kịch bản phát sinh từ thời gian phản hồi Tài chính. Kết quả biên trên không phải thời gian trung bình thực tế; đây là phép tính sử dụng mức tối đa 336 giờ theo lịch từ dữ liệu phỏng vấn.

## Hiệu suất thời gian

Processing time được hiểu là tổng giờ làm việc trực tiếp của các nguồn lực. Đối với hoạt động song song, giờ công của các nhánh được cộng vì mỗi nhánh đều sử dụng nguồn lực; cycle time vẫn được xác định theo nhánh hoàn thành chậm nhất.

Trước phê duyệt, processing time là:

`PT_trước = 1 + 16 + 24 + 16 + 8,5 = 65,5 giờ làm việc/sự kiện`.

Processing time của lượt phê duyệt đầu tiên là:

`PT_phê_duyệt_đầu = 4 + 4 + 80% × 2 = 9,6 giờ làm việc/hồ sơ`.

Processing time tăng thêm do 80% hồ sơ bị trả lại lần đầu là:

`PT_điều_chỉnh_đầu = 80% × (24 + 9,6) = 26,88 giờ làm việc/hồ sơ`.

Tổng processing time của cụm phê duyệt là:

`PT_phê_duyệt = 9,6 + 26,88 = 36,48 giờ làm việc/hồ sơ`.

Sau phê duyệt, processing time là:

`PT_sau = 2 + 96 + 18,5 + 4 + 16 + 2 = 138,5 giờ làm việc/sự kiện`.

Tổng processing time của trường hợp hoàn thành là:

`PT = 65,5 + 36,48 + 138,5 = 240,48 giờ làm việc/sự kiện`.

Hiệu suất thời gian theo hai kịch bản:

- Kịch bản điển hình: `240,48 / 1.407,2 × 100% = 17,1%`.
- Kịch bản biên trên: `240,48 / 1.796 × 100% = 13,4%`.

Như vậy, thời gian xử lý trực tiếp chiếm dưới một phần năm cycle time trong cả hai kịch bản. Phần còn lại chủ yếu là thời gian chờ phản hồi, chờ bàn giao và thời gian phát sinh do hồ sơ quay lại điều chỉnh.

## Chi phí quy trình

Chi phí được tính theo tổng giờ làm việc của từng nguồn lực nhân với đơn giá, sau đó cộng chi phí vật tư và hệ thống. Do phỏng vấn chưa cung cấp đơn giá và các khoản chi này, toàn bộ số liệu chi phí được ghi là giả định phân tích.

| Nguồn lực | Thời gian | Đơn giá | Chi phí | Nguồn | Ghi chú |
|---|---:|---:|---:|---|---|
| Ban điều hành ACFC | 4,5 giờ làm việc/sự kiện | 500.000 đồng/giờ | 2.250.000 đồng/sự kiện | Giả định phân tích | Giả định |
| Phòng Marketing | 87,9 giờ làm việc/sự kiện | 200.000 đồng/giờ | 17.580.000 đồng/sự kiện | Giả định phân tích | Giả định |
| Đơn vị tổ chức sự kiện | 126,8 giờ làm việc/sự kiện | 300.000 đồng/giờ | 38.040.000 đồng/sự kiện | Giả định phân tích | Giả định |
| Phòng Pháp lý | 7,2 giờ làm việc/sự kiện | 300.000 đồng/giờ | 2.160.000 đồng/sự kiện | Giả định phân tích | Giả định |
| Phòng Tài chính | 11,2 giờ làm việc/sự kiện | 250.000 đồng/giờ | 2.800.000 đồng/sự kiện | Giả định phân tích | Giả định |
| Phòng Procurement | 2,88 giờ làm việc/sự kiện | 200.000 đồng/giờ | 576.000 đồng/sự kiện | Giả định phân tích | Giả định |

`Chi phí nhân lực = 2.250.000 + 17.580.000 + 38.040.000 + 2.160.000 + 2.800.000 + 576.000 = 63.406.000 đồng/sự kiện`.

| Khoản chi | Giá trị | Đơn vị | Nguồn | Ghi chú |
|---|---:|---|---|---|
| Sản xuất, địa điểm và vận hành sự kiện | 300.000.000 | đồng/sự kiện | Giả định phân tích | Giả định |
| Ngân sách hàng tặng khi có xuất hàng | 50.000.000 | đồng/sự kiện có hàng tặng | Giả định phân tích | Giả định |
| Hệ thống và công cụ hỗ trợ | 5.000.000 | đồng/sự kiện | Giả định phân tích | Giả định |

Với tỷ lệ có hàng tặng là 80% tổng số sự kiện theo phỏng vấn nội bộ ACFC, chi phí hàng tặng kỳ vọng là:

`Chi phí_hàng_tặng = 80% × 50.000.000 = 40.000.000 đồng/sự kiện`.

Tổng chi phí quy trình là:

`Chi phí = 63.406.000 + 300.000.000 + 40.000.000 + 5.000.000 = 408.406.000 đồng/sự kiện`.

## Kết luận định lượng

Kết quả cho thấy thời gian chờ kế hoạch và báo giá là tác động lớn nhất đến cycle time; lần điều chỉnh hợp đồng đầu tiên đứng thứ hai. Cụm phê duyệt đạt 267,2 giờ trong kịch bản điển hình và 656 giờ trong kịch bản biên trên. Hiệu suất thời gian đạt 17,1% và 13,4%. Vì vậy, hướng cải tiến nên ưu tiên rút ngắn thời gian lập kế hoạch, báo giá, giảm tỷ lệ dự thảo hợp đồng bị trả lại lần đầu và rút ngắn thời gian phản hồi Tài chính.
