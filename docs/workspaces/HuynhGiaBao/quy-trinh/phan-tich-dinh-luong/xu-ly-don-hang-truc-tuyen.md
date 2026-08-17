# Phân tích định lượng quy trình xử lý đơn hàng trực tuyến



## Cơ sở tính toán



Quy tắc quy đổi dùng cho phép tính:

- `1 ngày làm việc = 8 giờ làm việc`.
- CT gồm thời gian xử lý và thời gian chờ.
- PT chỉ gồm thời gian trực tiếp thực hiện hoạt động.
- Các đại lượng trong cùng một phép tính được quy về giờ làm việc.

### Thời gian theo hoạt động

| STT | Hoạt động | CT | PT | Trạng thái số liệu |
|---:|---|---:|---:|---|
| 1 | Gửi thông tin đơn | 0,08 giờ | 0,08 giờ | Giả định |
| 2 | Xác nhận thông tin đơn | 0,08 giờ | 0,08 giờ | Giả định |
| 3 | Chọn phương án xử lý thiếu hàng | 0,25 giờ | 0,10 giờ | Giả định |
| 4 | Nhận hàng | 0 giờ | 0 giờ | Kết quả của hoạt động giao hàng, không cộng lần hai |
| 5 | Gọi xác thực thông tin đơn | 0,25 giờ | 0,17 giờ | Giả định |
| 6 | Hủy đơn | 0,17 giờ | 0,10 giờ | Giả định |
| 7 | Kiểm tra tồn kho trên hệ thống | 0,10 giờ | 0,08 giờ | Giả định |
| 8 | Thông báo tình trạng thiếu hàng | 0,17 giờ | 0,08 giờ | Giả định |
| 9 | Đóng gói đơn hàng | 4,00 giờ | 0,50 giờ | CT giả định trong giới hạn cùng ngày làm việc; PT giả định |
| 10 | Thực hiện phương án khách hàng chọn | Theo phương án | Theo phương án | Giả định; xem bảng nhánh thiếu hàng |
| 11 | Gửi xác nhận hủy | 0,08 giờ | 0,05 giờ | Giả định |
| 12 | Hoàn tất và bàn giao kiện hàng | 4,00 giờ | 0,25 giờ | CT giả định trong giới hạn cùng ngày làm việc; PT giả định |
| 13 | Tiếp nhận kết quả giao | 0,08 giờ | 0,05 giờ | Giả định |
| 14 | Cập nhật, đối soát và đóng đơn | 0,33 giờ | 0,25 giờ | Giả định |
| 15 | Cập nhật trạng thái giao thất bại | 0,08 giờ | 0,05 giờ | Giả định |
| 16 | Liên hệ khách hàng | 0,25 giờ | 0,17 giờ | Giả định |
| 17 | Gửi yêu cầu giao lại | 0,08 giờ | 0,05 giờ | Giả định |
| 18 | Tiếp nhận hàng hoàn | 0,25 giờ | 0,17 giờ | Giả định |
| 19 | Kiểm tra hàng hoàn | 0,50 giờ | 0,33 giờ | Giả định |
| 20 | Cập nhật tồn kho, thanh toán, trạng thái và đóng đơn | 0,50 giờ | 0,33 giờ | Giả định |
| 21 | Chuyển trường hợp khiếu nại | 0,17 giờ | 0,08 giờ | Giả định |
| 22 | Tiếp nhận trường hợp khiếu nại | 0,17 giờ | 0,08 giờ | Giả định |
| 23 | Nhận kiện hàng | 0,25 giờ | 0,17 giờ | Giả định |
| 24 | Giao hàng | 1-7 ngày làm việc | 0,50 giờ | CT theo chính sách công khai, tùy vùng; PT giả định phân bổ cho một đơn |
| 25 | Xác định kết quả giao | 0,08 giờ | 0,05 giờ | Giả định |
| 26 | Gửi kết quả giao thành công | 0,08 giờ | 0,03 giờ | Giả định |
| 27 | Xác định nguyên nhân giao thất bại | 0,17 giờ | 0,10 giờ | Giả định |
| 28 | Đánh giá khả năng giao lại | 0,08 giờ | 0,05 giờ | Giả định |
| 29 | Gửi kết quả giao và đánh giá | 0,08 giờ | 0,03 giờ | Giả định |
| 30 | Giao lại | 1 ngày làm việc | 0,50 giờ | Giả định |
| 31 | Chuyển hàng về | 2 ngày làm việc | 0,50 giờ | Giả định |

### Xác suất và tỷ lệ lặp

| Biến | Giá trị | Ý nghĩa | Trạng thái số liệu |
|---|---:|---|---|
| `p_lien_he_duoc` | 95% | Liên hệ và xác thực được khách hàng | Giả định |
| `p_khong_lien_he_duoc` | 5% | Không liên hệ được và hủy đơn | Giả định |
| `p_du_hang` | 90% | Đơn có đủ hàng | Giả định |
| `p_thieu_hang` | 10% | Đơn thiếu ít nhất một sản phẩm | Giả định |
| `p_cho_hang` | 20% | Khách hàng chọn chờ bổ sung hàng trong nhóm đơn thiếu hàng | Giả định |
| `p_thay_the` | 30% | Khách hàng chọn sản phẩm thay thế trong nhóm đơn thiếu hàng | Giả định |
| `p_mua_hien_co` | 25% | Khách hàng mua số lượng hiện có trong nhóm đơn thiếu hàng | Giả định |
| `p_huy_phan_thieu` | 15% | Khách hàng hủy phần hàng thiếu trong nhóm đơn thiếu hàng | Giả định |
| `p_huy_toan_bo` | 10% | Khách hàng hủy toàn bộ đơn trong nhóm đơn thiếu hàng | Giả định |
| `p_giao_thanh_cong_lan_dau` | 90% | Giao thành công ngay lần đầu | Giả định |
| `p_giao_that_bai` | 10% | Lần giao đầu thất bại | Giả định |
| `p_co_the_giao_lai` | 70% | Đơn giao thất bại còn khả năng giao lại | Giả định |
| `p_chuyen_hoan` | 30% | Đơn giao thất bại không thể giao lại | Giả định |
| `r_giao_lai` | 20% | Một lượt giao lại tiếp tục thất bại và phải lặp | Giả định |

Tổng xác suất của các nhánh loại trừ bằng 100%:

- `95% + 5% = 100%`.
- `90% + 10% = 100%`.
- `20% + 30% + 25% + 15% + 10% = 100%`.
- `90% + 10% = 100%`.
- `70% + 30% = 100%`.

### Chi phí đầu vào

| Khoản chi | Giá trị | Đơn vị | Trạng thái số liệu |
|---|---:|---|---|
| Nhân sự xử lý đơn hàng | 80.000 | đồng/giờ | Giả định |
| Nhân sự xử lý khiếu nại | 100.000 | đồng/giờ | Giả định |
| Phí giao hàng lần đầu | 40.000 | đồng/đơn | Giả định |
| Phí giao lại | 40.000 | đồng/lượt | Giả định |
| Phí chuyển hoàn | 40.000 | đồng/đơn | Giả định |
| Bao bì | 10.000 | đồng/đơn | Giả định |
| Hệ thống và công cụ hỗ trợ | 5.000 | đồng/đơn | Giả định |

## Tính cycle time

### Cấu trúc tuần tự

Với các hoạt động tuần tự:

`CT = ΣTi`.

Đường cơ sở gồm các hoạt động `1 → 5 → 2 → 7 → 9 → 12 → 23 → 24 → 25 → 26 → 13 → 14`. Hoạt động 4 là kết quả khách hàng nhận hàng nên không được cộng thêm vào CT.

CT trước và sau giai đoạn giao hàng:

`CT_ngoài_giao_hàng = 0,08 + 0,25 + 0,08 + 0,10 + 4,00 + 4,00 + 0,25 + 0,08 + 0,08 + 0,08 + 0,33 = 9,33 giờ làm việc/đơn`.

Thời gian giao được giữ theo bốn vùng. Khi cần tính CT toàn đường cơ sở, thời gian giao được quy đổi theo giả định `1 ngày làm việc = 8 giờ làm việc`.

| Vùng giao | Thời gian giao công khai | CT giao quy đổi | CT đường cơ sở |
|---|---:|---:|---:|
| Nội tỉnh hoặc nội thành | 1-3 ngày làm việc | 8-24 giờ | 17,33-33,33 giờ, tương đương 2,17-4,17 ngày làm việc |
| Nội vùng | 2-4 ngày làm việc | 16-32 giờ | 25,33-41,33 giờ, tương đương 3,17-5,17 ngày làm việc |
| Liên vùng giữa Thành phố Hồ Chí Minh, Hà Nội và Đà Nẵng | 3-5 ngày làm việc | 24-40 giờ | 33,33-49,33 giờ, tương đương 4,17-6,17 ngày làm việc |
| Từ ba thành phố lớn đến tỉnh khác vùng | 5-7 ngày làm việc | 40-56 giờ | 49,33-65,33 giờ, tương đương 6,17-8,17 ngày làm việc |

CT trên là kết quả phân tích từ thời gian giao công khai và thời gian giả định.
### Cấu trúc XOR

Với các nhánh loại trừ:

`CT_XOR = Σ(pi × Ti)`.

#### Kết quả xác thực

Hoạt động gọi xác thực diễn ra trước gateway XOR. Sau đó, 95% đơn đi qua bước xác nhận và 5% đơn đi qua bước hủy:

`CT_xác_thực = 0,25 + 95% × 0,08 + 5% × 0,17 = 0,3345 giờ/đơn`.

#### Phương án thiếu hàng

| Phương án | Xác suất trong nhóm thiếu hàng | CT | PT |
|---|---:|---:|---:|
| Chờ bổ sung hàng | 20% | 3 ngày làm việc, quy đổi 24 giờ | 0,25 giờ |
| Thay thế sản phẩm | 30% | 0,75 giờ | 0,33 giờ |
| Mua số lượng hiện có | 25% | 0,33 giờ | 0,17 giờ |
| Hủy phần hàng thiếu | 15% | 0,50 giờ | 0,25 giờ |
| Hủy toàn bộ đơn | 10% | 0,33 giờ | 0,17 giờ |

CT kỳ vọng của hoạt động thực hiện phương án:

`CT_phương_án = 20% × 24 + 30% × 0,75 + 25% × 0,33 + 15% × 0,50 + 10% × 0,33 = 5,2155 giờ/đơn thiếu hàng`.

Cộng thời gian thông báo thiếu hàng và thời gian khách hàng chọn phương án:

`CT_cụm_thiếu_hàng = 0,17 + 0,25 + 5,2155 = 5,6355 giờ/đơn thiếu hàng`.

Với tỷ lệ thiếu hàng giả định là 10%, phần CT kỳ vọng tăng thêm trên toàn bộ đơn là:

`CT_tăng_thêm_do_thiếu_hàng = 10% × 5,6355 = 0,5636 giờ/đơn`.

#### Kết quả giao lần đầu

Kết quả giao lần đầu có hai nhánh loại trừ:

`CT_kết_quả_giao = 90% × CT_thành_công + 10% × CT_thất_bại`.

Sau lần giao đầu, nhánh thành công cần `0,57 giờ` để xác định và gửi kết quả, tiếp nhận kết quả, đối soát và đóng đơn. Nhánh thất bại cần `0,41 giờ` để xác định nguyên nhân, đánh giá khả năng giao lại, gửi kết quả và cập nhật trạng thái.

CT của nhánh giao lại được tính ở phần vòng lặp là `11,1050 giờ`. CT của nhánh chuyển hoàn bình thường là:

`CT_chuyển_hoàn = 16,00 + 0,25 + 0,50 + 0,50 = 17,25 giờ/đơn chuyển hoàn`.

CT kỳ vọng sau một lần giao thất bại:

`CT_thất_bại = 0,41 + 70% × 11,1050 + 30% × 17,25 = 13,3585 giờ/đơn giao thất bại`.

CT kỳ vọng của gateway kết quả giao lần đầu:

`CT_kết_quả_giao = 90% × 0,57 + 10% × 13,3585 = 1,8489 giờ/đơn`.

### Cấu trúc AND

Với các nhánh chạy song song:

`CT_AND = max(T1, T2, ..., Tn)`.



### Vòng lặp giao lại

Với một cụm hoạt động lặp có thời gian `T` và xác suất lặp `r`:

`CT_vòng_lặp = T/(1-r)`.

Một lượt giao lại gồm liên hệ khách hàng, gửi yêu cầu, giao hàng và xử lý kết quả. CT xử lý kết quả là `0,57 giờ` nếu giao thành công và `0,49 giờ` nếu tiếp tục thất bại. Với xác suất lặp `20%`, CT kỳ vọng của phần xử lý kết quả trong một lượt là:

`CT_kết_quả_một_lượt = 80% × 0,57 + 20% × 0,49 = 0,554 giờ/lượt`.

Thời gian kỳ vọng của một lượt giao lại:

`T_một_lượt = 0,25 + 0,08 + 8,00 + 0,554 = 8,884 giờ làm việc/lượt`.

Với tỷ lệ tiếp tục lặp giả định `r = 20%`:

`CT_vòng_lặp_giao = 8,884/(1-20%) = 11,1050 giờ làm việc/đơn phát sinh giao lại`.

## Processing time và hiệu suất thời gian

PT của đường cơ sở là tổng thời gian trực tiếp của các hoạt động `1, 5, 2, 7, 9, 12, 23, 24, 25, 26, 13, 14`:

`PT = 0,08 + 0,17 + 0,08 + 0,08 + 0,50 + 0,25 + 0,17 + 0,50 + 0,05 + 0,03 + 0,05 + 0,25 = 2,21 giờ/đơn`.

Hiệu suất thời gian được tính theo công thức:

`Hiệu suất thời gian = PT/CT × 100%`.

| Vùng giao | CT đường cơ sở | Hiệu suất theo biên dưới CT | Hiệu suất theo biên trên CT |
|---|---:|---:|---:|
| Nội tỉnh hoặc nội thành | 17,33-33,33 giờ | `2,21/17,33 × 100% = 12,75%` | `2,21/33,33 × 100% = 6,63%` |
| Nội vùng | 25,33-41,33 giờ | `2,21/25,33 × 100% = 8,72%` | `2,21/41,33 × 100% = 5,35%` |
| Liên vùng giữa ba thành phố lớn | 33,33-49,33 giờ | `2,21/33,33 × 100% = 6,63%` | `2,21/49,33 × 100% = 4,48%` |
| Từ ba thành phố lớn đến tỉnh khác vùng | 49,33-65,33 giờ | `2,21/49,33 × 100% = 4,48%` | `2,21/65,33 × 100% = 3,38%` |

## Chi phí quy trình

Chi phí được tính theo công thức:

`Chi phí = Σ(thời gian nguồn lực × đơn giá) + chi phí vật tư/hệ thống`.

Thời gian của nhân sự ACFC trên đường cơ sở gồm gọi xác thực, kiểm tra tồn kho, đóng gói, hoàn tất bàn giao, tiếp nhận kết quả giao, đối soát và đóng đơn:

`PT_ACFC = 0,17 + 0,08 + 0,50 + 0,25 + 0,05 + 0,25 = 1,30 giờ/đơn`.

Chi phí đường cơ sở:

`Chi phí_nhân_sự = 1,30 × 80.000 = 104.000 đồng/đơn`.

`Chi phí_đường_cơ_sở = 104.000 + 40.000 + 10.000 + 5.000 = 159.000 đồng/đơn`.

### Chi phí tăng thêm của ngoại lệ

| Ngoại lệ | Công thức | Chi phí tăng thêm |
|---|---|---:|
| Không liên hệ được và hủy đơn | `(0,17 + 0,10) × 80.000 + 5.000 chi phí hệ thống` | 26.600 đồng/đơn hủy |
| Xử lý thiếu hàng | `(0,08 + 0,10 + 0,246) × 80.000` | 34.080 đồng/đơn thiếu hàng |
| Giao lại | `[(0,17 + 0,05 + 80% × 0,30 + 20% × 0,05) × 80.000 + 40.000]/(1-20%)` | 97.000 đồng/đơn phát sinh giao lại |
| Chuyển hoàn và đóng đơn | `(0,17 + 0,33 + 0,33) × 80.000 + 40.000 + 5.000` | 111.400 đồng/đơn chuyển hoàn |
| Chuyển trường hợp khiếu nại | `0,08 × 80.000 + 0,08 × 100.000` | 14.400 đồng/trường hợp, chưa gồm chi phí xử lý khiếu nại tiếp theo |

Trong phép tính thiếu hàng, PT kỳ vọng của hoạt động thực hiện phương án là:

`PT_phương_án = 20% × 0,25 + 30% × 0,33 + 25% × 0,17 + 15% × 0,25 + 10% × 0,17 = 0,246 giờ/đơn thiếu hàng`.

## Kết luận

Đường cơ sở có CT từ 17,33 đến 65,33 giờ làm việc tùy vùng giao, PT là 2,21 giờ và chi phí là 159.000 đồng/đơn. Hiệu suất thời gian nằm trong khoảng 3,38%-12,75%; nhánh thiếu hàng và vòng lặp giao lại làm tăng thêm CT.
