# M1 – Quản lý vận hành cửa hàng – Phân tích định lượng

## 1. Mục tiêu phân tích

Phân tích định lượng M1 tập trung vào ba nhóm chỉ số chính theo rubric:

- **Thời gian**
- **Chất lượng**
- **Chi phí**

Hiện nhóm chưa tiếp cận được dữ liệu vận hành nội bộ thực tế của ACFC. Vì vậy, phần phân tích định lượng gồm hai nội dung:

- Xác định các chỉ số, công thức và dữ liệu cần thu thập khi triển khai đo lường thực tế.
- Sử dụng một bộ dữ liệu giả lập để minh họa cách tính và cách phân tích các chỉ số.

**Lưu ý:** Các số liệu giả lập trong phần này chỉ phục vụ mục đích minh họa phương pháp, không phải số liệu vận hành thực tế của ACFC.

---

## 2. Phân tích thời gian

### 2.1. Thời gian chuẩn bị đầu ca

**Mục đích:** Đo thời gian từ khi bắt đầu chuẩn bị đến khi cửa hàng sẵn sàng vận hành.

**Công thức:**

`Thời gian chuẩn bị đầu ca = Thời điểm cửa hàng sẵn sàng - Thời điểm bắt đầu chuẩn bị`

**Dữ liệu cần thu thập:**
- Giờ bắt đầu chuẩn bị.
- Giờ hoàn tất phân công nhân sự.
- Giờ hoàn tất kiểm tra khu vực bán hàng/trưng bày.
- Giờ hoàn tất kiểm tra hàng hóa.
- Giờ cửa hàng chính thức sẵn sàng vận hành.

**Ý nghĩa:**
- Nếu thời gian chuẩn bị kéo dài, cần xác định bước nào chiếm nhiều thời gian nhất.
- Có thể so sánh giữa các ca hoặc cửa hàng để tìm nguyên nhân khác biệt.

---

### 2.2. Thời gian xử lý sự cố

**Mục đích:** Đo tốc độ phản ứng khi phát sinh vấn đề trong ca.

**Công thức:**

`Thời gian xử lý sự cố = Thời điểm xử lý xong/chuyển cấp - Thời điểm phát hiện sự cố`

Có thể tách thành:

`Thời gian xử lý tại cửa hàng`

và

`Thời gian chờ sau khi chuyển cấp`

**Dữ liệu cần thu thập:**
- Thời điểm phát hiện sự cố.
- Loại sự cố.
- Thời điểm bắt đầu xử lý.
- Thời điểm xử lý xong hoặc chuyển cấp.
- Thời điểm đơn vị khác phản hồi nếu có.

**Ý nghĩa:**
- Xác định loại sự cố gây mất thời gian nhất.
- Phân biệt thời gian xử lý thực tế và thời gian chờ.

---

### 2.3. Thời gian đối soát và đóng ca

**Mục đích:** Đo thời gian cần để hoàn tất các hoạt động cuối ca.

**Công thức:**

`Thời gian đóng ca = Thời điểm hoàn tất báo cáo - Thời điểm bắt đầu kiểm tra cuối ca`

Có thể tách thành:
- Thời gian đối soát tiền/hóa đơn.
- Thời gian kiểm tra hàng hóa.
- Thời gian tổng hợp kết quả bán hàng.
- Thời gian xử lý chênh lệch.

**Dữ liệu cần thu thập:**
- Giờ bắt đầu kiểm tra cuối ca.
- Giờ hoàn tất từng nhóm kiểm tra.
- Có/không có chênh lệch.
- Giờ hoàn tất xử lý chênh lệch.
- Giờ hoàn tất báo cáo.

---

### 2.4. Cycle Time của một ca vận hành

**Công thức:**

`Cycle Time = Thời điểm kết thúc quy trình - Thời điểm bắt đầu quy trình`

Trong M1, Cycle Time có thể gần bằng toàn bộ thời gian của một ca vận hành.

Tuy nhiên, khi phân tích cải tiến nên tách riêng:
- thời gian vận hành bình thường;
- thời gian chuẩn bị;
- thời gian chờ;
- thời gian rework;
- thời gian đóng ca.

---

## 3. Phân tích chất lượng

### 3.1. Tỷ lệ ca không phát sinh chênh lệch

**Công thức:**

`Tỷ lệ ca không chênh lệch = Số ca không phát sinh chênh lệch / Tổng số ca × 100%`

**Ý nghĩa:** Đánh giá mức độ ổn định của quá trình kiểm soát bán hàng, tiền/hóa đơn và hàng hóa.

---

### 3.2. Tỷ lệ ca phát sinh chênh lệch

**Công thức:**

`Tỷ lệ ca có chênh lệch = Số ca có chênh lệch / Tổng số ca × 100%`

Có thể phân loại chênh lệch theo:
- Tiền.
- Hóa đơn/chứng từ.
- Hàng hóa.
- Dữ liệu giao dịch.
- Khác.

---

### 3.3. Tỷ lệ sự cố xử lý được tại cửa hàng

**Công thức:**

`Tỷ lệ xử lý tại cửa hàng = Số sự cố xử lý được tại cửa hàng / Tổng số sự cố × 100%`

**Ý nghĩa:**
- Đánh giá khả năng tự xử lý của cửa hàng.
- Nếu tỷ lệ chuyển cấp cao, cần xem xét nguyên nhân và quyền xử lý hiện tại.

---

### 3.4. Tỷ lệ sự cố phải chuyển cấp

**Công thức:**

`Tỷ lệ chuyển cấp = Số sự cố phải chuyển cấp / Tổng số sự cố × 100%`

Có thể theo dõi thêm:
- Loại sự cố chuyển cấp nhiều nhất.
- Đơn vị nhận chuyển cấp.
- Thời gian phản hồi trung bình.

---

### 3.5. Tỷ lệ báo cáo hoàn tất đúng yêu cầu

**Công thức đề xuất:**

`Tỷ lệ báo cáo đạt yêu cầu = Số báo cáo đầy đủ/đúng yêu cầu / Tổng số báo cáo × 100%`

Cần xác nhận tiêu chí “đạt yêu cầu” với nhóm hoặc người phụ trách thực tế trước khi áp dụng.

---

### 3.6. Tỷ lệ rework cuối ca

**Công thức:**

`Tỷ lệ rework = Số ca phải kiểm tra/làm lại do chênh lệch / Tổng số ca × 100%`

**Ý nghĩa:** Phản ánh mức độ phát sinh hoạt động NVA trong giai đoạn đóng ca.

---

## 4. Phân tích chi phí

Hiện chưa có dữ liệu lương, chi phí nhân sự hoặc giá trị tổn thất thực tế của ACFC, vì vậy chỉ xác định cách tính.

### 4.1. Chi phí nhân công cho hoạt động chuẩn bị và đóng ca

**Công thức:**

`Chi phí nhân công = Tổng thời gian thực hiện × Chi phí nhân công theo giờ`

Có thể tính riêng cho:
- Chuẩn bị đầu ca.
- Đối soát cuối ca.
- Xử lý chênh lệch.
- Xử lý sự cố.

---

### 4.2. Chi phí rework

**Công thức:**

`Chi phí rework = Thời gian làm lại × Chi phí nhân công theo giờ`

Nếu nhiều người cùng tham gia:

`Chi phí rework = Σ (Thời gian của từng người × Chi phí nhân công/giờ của người đó)`

---

### 4.3. Chi phí do chênh lệch

Có thể theo dõi nếu ACFC có dữ liệu:

`Chi phí chênh lệch = Giá trị tiền thiếu/thừa + Giá trị hàng hóa thiếu/hư hỏng + Chi phí xử lý liên quan`

Không nên tự giả định rằng mọi chênh lệch đều tạo ra tổn thất tài chính; cần dùng dữ liệu thực tế.

---

### 4.4. Chi phí do thời gian chờ

Nếu muốn phân tích sâu:

`Chi phí thời gian chờ = Tổng thời gian nhân sự bị gián đoạn × Chi phí nhân công theo giờ`

Chỉ áp dụng khi chứng minh được thời gian chờ thực sự làm phát sinh chi phí hoặc mất năng suất.

---

## 5. Bộ chỉ số đề xuất

| Nhóm | Chỉ số | Công thức / cách đo |
|---|---|---|
| **Thời gian** | Thời gian chuẩn bị đầu ca | Giờ sẵn sàng - Giờ bắt đầu chuẩn bị |
| **Thời gian** | Thời gian xử lý sự cố | Giờ xử lý xong/chuyển cấp - Giờ phát hiện |
| **Thời gian** | Thời gian đóng ca | Giờ hoàn tất báo cáo - Giờ bắt đầu kiểm tra cuối ca |
| **Thời gian** | Thời gian xử lý chênh lệch | Giờ đóng chênh lệch - Giờ phát hiện chênh lệch |
| **Chất lượng** | Tỷ lệ ca không chênh lệch | Ca không chênh lệch / Tổng ca × 100% |
| **Chất lượng** | Tỷ lệ ca có chênh lệch | Ca có chênh lệch / Tổng ca × 100% |
| **Chất lượng** | Tỷ lệ xử lý sự cố tại cửa hàng | Sự cố tự xử lý / Tổng sự cố × 100% |
| **Chất lượng** | Tỷ lệ chuyển cấp | Sự cố chuyển cấp / Tổng sự cố × 100% |
| **Chất lượng** | Tỷ lệ rework | Ca phải làm lại / Tổng ca × 100% |
| **Chi phí** | Chi phí xử lý sự cố | Thời gian xử lý × chi phí nhân công/giờ |
| **Chi phí** | Chi phí rework | Thời gian làm lại × chi phí nhân công/giờ |
| **Chi phí** | Giá trị chênh lệch | Tổng giá trị chênh lệch tiền/hàng hóa nếu có |

---

## 6. Dữ liệu cần thu thập

Để có thể hoàn thiện phần định lượng bằng số thực tế, cần thu thập tối thiểu:

| Dữ liệu | Mục đích |
|---|---|
| Thời gian bắt đầu/kết thúc chuẩn bị đầu ca | Tính thời gian chuẩn bị |
| Thời gian bắt đầu/kết thúc đóng ca | Tính thời gian đóng ca |
| Danh sách sự cố theo ca | Tính số lượng và tỷ lệ sự cố |
| Thời gian phát hiện và xử lý sự cố | Tính thời gian xử lý |
| Số ca có/không có chênh lệch | Tính tỷ lệ chất lượng |
| Loại và giá trị chênh lệch | Phân tích chất lượng/chi phí |
| Số case phải làm lại | Tính tỷ lệ rework |
| Số case chuyển cấp | Tính tỷ lệ chuyển cấp |
| Thời gian phản hồi khi chuyển cấp | Phân tích Hold |
| Chi phí nhân công theo giờ hoặc mức quy đổi | Tính chi phí quy trình |

---

## 7. Mẫu bảng thu thập dữ liệu
**“giả lập minh họa”**
| Ca    | Thời gian chuẩn bị (phút) | Số sự cố | Sự cố chuyển cấp | Có chênh lệch? | Thời gian xử lý chênh lệch (phút) | Thời gian đóng ca (phút) | Rework? |
| ----- | ------------------------: | -------: | ---------------: | -------------- | --------------------------------: | -----------------------: | ------- |
| Ca 1  |                        22 |        1 |                0 | Không          |                                 0 |                       28 | Không   |
| Ca 2  |                        25 |        2 |                1 | Có             |                                18 |                       42 | Có      |
| Ca 3  |                        20 |        0 |                0 | Không          |                                 0 |                       26 | Không   |
| Ca 4  |                        27 |        1 |                0 | Có             |                                12 |                       36 | Có      |
| Ca 5  |                        24 |        1 |                1 | Không          |                                 0 |                       31 | Không   |
| Ca 6  |                        21 |        0 |                0 | Không          |                                 0 |                       25 | Không   |
| Ca 7  |                        29 |        3 |                1 | Có             |                                25 |                       49 | Có      |
| Ca 8  |                        23 |        1 |                0 | Không          |                                 0 |                       29 | Không   |
| Ca 9  |                        26 |        2 |                1 | Có             |                                15 |                       40 | Có      |
| Ca 10 |                        22 |        1 |                0 | Không          |                                 0 |                       27 | Không   |

### 7.1. Phân tích thời gian từ dữ liệu

Thời gian chuẩn bị đầu ca trung bình:

(22 + 25 + 20 + 27 + 24 + 21 + 29 + 23 + 26 + 22) / 10

= 239 / 10 = 23,9 phút/ca

Thời gian đóng ca trung bình:

(28 + 42 + 26 + 36 + 31 + 25 + 49 + 29 + 40 + 27) / 10

= 333 / 10 = 33,3 phút/ca

Đối với 4 ca có chênh lệch:

Thời gian xử lý chênh lệch trung bình

= (18 + 12 + 25 + 15) / 4

= 70 / 4 = 17,5 phút/case

Như vậy, trong dữ liệu giả lập, ca có chênh lệch thường cần nhiều thời gian đóng ca hơn.

### 7.2. Phân tích chất lượng

Tổng số ca:

10 ca

Số ca không có chênh lệch:

6 ca

Tỷ lệ ca không chênh lệch:

6 / 10 × 100% = 60%

Số ca có chênh lệch:

4 ca

Tỷ lệ ca có chênh lệch:

4 / 10 × 100% = 40%

Tổng số sự cố:

1 + 2 + 0 + 1 + 1 + 0 + 3 + 1 + 2 + 1 = 12 sự cố

Số sự cố phải chuyển cấp:

4 sự cố

Tỷ lệ sự cố chuyển cấp:

4 / 12 × 100% ≈ 33,3%

Số ca phát sinh rework:

4 ca

Tỷ lệ rework:

4 / 10 × 100% = 40%

### 7.3. Ví dụ giả lập chi phí rework

Giả sử để minh họa:

Chi phí nhân công trung bình: 60.000 đồng/giờ/người
Mỗi case chênh lệch tạm tính có 1 nhân sự trực tiếp xử lý.
Tổng thời gian xử lý chênh lệch: 70 phút.

Quy đổi:

70 phút = 70 / 60 = 1,17 giờ

Chi phí rework giả lập:

1,17 × 60.000 ≈ 70.000 đồng

Nếu thực tế có nhiều nhân sự cùng tham gia thì cần tính riêng thời gian và chi phí của từng người.

### 7.4. Kết quả tổng hợp giả lập
| Chỉ số                                |         Kết quả giả lập |
| ------------------------------------- | ----------------------: |
| Thời gian chuẩn bị trung bình         |        **23,9 phút/ca** |
| Thời gian đóng ca trung bình          |        **33,3 phút/ca** |
| Thời gian xử lý chênh lệch trung bình |      **17,5 phút/case** |
| Tổng số sự cố                         |                  **12** |
| Tỷ lệ sự cố chuyển cấp                |               **33,3%** |
| Tỷ lệ ca không chênh lệch             |                 **60%** |
| Tỷ lệ ca có chênh lệch                |                 **40%** |
| Tỷ lệ rework                          |                 **40%** |
| Chi phí rework minh họa               | **≈ 70.000 đồng/10 ca** |

## 8. Câu hỏi định lượng

1. Trung bình một ca mất bao nhiêu phút để hoàn tất công tác chuẩn bị đầu ca?
Trả lời : Khoảng 23,9 phút/ca.

2. Trung bình một ca mất bao nhiêu phút để hoàn tất đối soát và đóng ca?
Trả lời : Khoảng 33,3 phút/ca.

3. Trong một tuần hoặc một tháng, cửa hàng có tổng cộng bao nhiêu ca vận hành?
Trả lời : Trong bộ dữ liệu minh họa, nhóm sử dụng 10 ca vận hành để phân tích.

4. Trong khoảng thời gian đó, có bao nhiêu sự cố phát sinh trong quá trình vận hành?
Trả lời : Có 12 sự cố phát sinh trong 10 ca.

5. Trong số các sự cố phát sinh, có bao nhiêu sự cố cửa hàng tự xử lý được?
Trả lời : Có 8/12 sự cố được xử lý tại cửa hàng, tương đương khoảng 66,7%.

6. Có bao nhiêu sự cố phải chuyển cho Bộ phận Vận hành bán lẻ?
Trả lời : Có 4/12 sự cố, tương đương khoảng 33,3%.

7. Trong 10 ca gần nhất, có bao nhiêu ca phát sinh chênh lệch tiền, hóa đơn hoặc hàng hóa?
Trả lời : Có 4/10 ca phát sinh chênh lệch, tương đương 40%; 6 ca không phát sinh chênh lệch, tương đương 60%.

8. Một trường hợp chênh lệch cuối ca trung bình mất bao nhiêu phút để kiểm tra và xử lý?
Trả lời : Trung bình khoảng 17,5 phút/trường hợp.

9. Một trường hợp chuyển cấp trung bình mất bao nhiêu phút hoặc bao nhiêu giờ để nhận được phản hồi?
Trả lời : Chưa có dữ liệu cụ thể để tính chính xác chỉ số này. Khi thu thập thực tế cần ghi lại thời điểm chuyển cấp và thời điểm nhận phản hồi.

10. Trong các ca phát sinh chênh lệch, có bao nhiêu trường hợp phải kiểm tra hoặc thực hiện lại công việc?
Trả lời : Có 4/10 ca phát sinh rework, tương đương 40% tổng số ca trong bộ dữ liệu minh họa.
