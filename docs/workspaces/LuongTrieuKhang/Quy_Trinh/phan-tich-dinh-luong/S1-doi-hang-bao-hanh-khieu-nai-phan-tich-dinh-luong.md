# S1 – Đổi hàng, bảo hành và xử lý khiếu nại – Phân tích định lượng

## 1. Mục tiêu phân tích

Phân tích định lượng S1 tập trung vào ba nhóm chỉ số chính theo rubric:

- **Thời gian**
- **Chất lượng**
- **Chi phí**

Hiện nhóm chưa tiếp cận được dữ liệu vận hành nội bộ thực tế của ACFC. Vì vậy, phần phân tích định lượng gồm hai nội dung:

- Xác định các chỉ số, công thức và dữ liệu cần thu thập khi triển khai đo lường thực tế.
- Sử dụng một bộ dữ liệu giả lập để minh họa cách tính và cách phân tích các chỉ số.

**Lưu ý:** Các số liệu giả lập trong phần này chỉ phục vụ mục đích minh họa phương pháp, không phải số liệu vận hành thực tế của ACFC.

---

## 2. Phân tích thời gian

### 2.1. Thời gian xử lý yêu cầu từ lúc tiếp nhận đến khi hoàn tất

**Mục đích:** Đo tổng thời gian cần để xử lý một yêu cầu đổi hàng, bảo hành hoặc khiếu nại.

**Công thức:**

`Cycle Time = Thời điểm đóng yêu cầu - Thời điểm tiếp nhận yêu cầu`

**Dữ liệu cần thu thập:**
- Thời điểm khách gửi yêu cầu.
- Thời điểm CSKH/Cửa hàng tiếp nhận.
- Thời điểm hồ sơ đầy đủ.
- Thời điểm hoàn tất kiểm tra sản phẩm/bằng chứng.
- Thời điểm có quyết định xử lý.
- Thời điểm thông báo kết quả cuối cùng cho khách hàng.

**Ý nghĩa:**
- Cho biết tổng thời gian xử lý một case.
- Có thể so sánh giữa đổi hàng, bảo hành và khiếu nại.
- Giúp xác định loại yêu cầu nào có cycle time dài nhất.

---

### 2.2. Thời gian chờ khách hàng bổ sung hồ sơ

**Công thức:**

`Thời gian chờ bổ sung = Thời điểm khách bổ sung đầy đủ - Thời điểm yêu cầu bổ sung`

**Dữ liệu cần thu thập:**
- Loại thông tin còn thiếu.
- Thời điểm yêu cầu khách bổ sung.
- Thời điểm khách bổ sung đầy đủ.
- Số lần yêu cầu bổ sung.

**Ý nghĩa:**
- Xác định mức độ ảnh hưởng của hồ sơ chưa đầy đủ đến cycle time.
- Có thể đánh giá hiệu quả của checklist hồ sơ ban đầu.

---

### 2.3. Thời gian kiểm tra sản phẩm/bằng chứng

**Công thức:**

`Thời gian kiểm tra = Thời điểm hoàn tất kiểm tra - Thời điểm bắt đầu kiểm tra`

**Dữ liệu cần thu thập:**
- Thời điểm bắt đầu kiểm tra.
- Thời điểm hoàn tất kiểm tra.
- Đơn vị thực hiện.
- Có cần chuyển sản phẩm sang nơi khác hay không.

**Ý nghĩa:**
- Xác định bước kiểm tra có phải bottleneck hay không.
- So sánh thời gian giữa các nhóm sản phẩm/trường hợp khác nhau.

---

### 2.4. Thời gian xử lý trường hợp chuyển cấp

**Công thức:**

`Thời gian chuyển cấp = Thời điểm có kết quả xử lý ngoại lệ - Thời điểm chuyển cấp`

**Dữ liệu cần thu thập:**
- Thời điểm chuyển cấp.
- Đơn vị/người tiếp nhận.
- Thời điểm phản hồi.
- Thời điểm có quyết định cuối cùng.

**Ý nghĩa:**
- Đánh giá phần Hold trong quy trình.
- Xác định trường hợp ngoại lệ nào gây chậm xử lý nhiều nhất.

---

## 3. Phân tích chất lượng

### 3.1. Tỷ lệ hồ sơ đầy đủ ngay lần tiếp nhận đầu tiên

**Công thức:**

`Tỷ lệ First-Time-Complete = Số case đủ hồ sơ ngay lần đầu / Tổng số case × 100%`

**Ý nghĩa:**
- Đánh giá mức độ rõ ràng của hướng dẫn tiếp nhận.
- Nếu tỷ lệ thấp, cần xem lại checklist hoặc cách hướng dẫn khách hàng.

---

### 3.2. Tỷ lệ case phải bổ sung hồ sơ

**Công thức:**

`Tỷ lệ bổ sung hồ sơ = Số case phải bổ sung / Tổng số case × 100%`

Có thể theo dõi thêm:
- Số lần bổ sung trung bình/case.
- Loại thông tin thường thiếu nhất.

---

### 3.3. Tỷ lệ yêu cầu được xử lý

**Công thức:**

`Tỷ lệ yêu cầu được xử lý = Số case được chấp nhận xử lý / Tổng số case × 100%`

Có thể phân loại theo:
- Đổi hàng.
- Bảo hành.
- Phương án xử lý khác.

---

### 3.4. Tỷ lệ yêu cầu bị từ chối

**Công thức:**

`Tỷ lệ từ chối = Số case bị từ chối / Tổng số case × 100%`

Có thể phân nhóm nguyên nhân:
- Quá thời hạn.
- Thiếu chứng từ.
- Không thuộc nhóm sản phẩm hỗ trợ.
- Tình trạng sản phẩm không đáp ứng điều kiện.
- Lý do khác.

---

### 3.5. Tỷ lệ case phải chuyển cấp

**Công thức:**

`Tỷ lệ chuyển cấp = Số case phải chuyển cấp / Tổng số case × 100%`

**Ý nghĩa:**
- Đánh giá mức độ phụ thuộc vào cấp quản lý/đơn vị khác.
- Nếu tỷ lệ cao, cần xem xét lại thẩm quyền hoặc quy tắc xử lý tại tuyến đầu.

---

### 3.6. Tỷ lệ xử lý không cần rework

**Công thức:**

`Tỷ lệ xử lý không rework = Số case hoàn tất không phải kiểm tra/làm lại / Tổng số case × 100%`

Hoặc:

`Tỷ lệ rework = Số case phải kiểm tra/làm lại / Tổng số case × 100%`

**Ý nghĩa:**
- Đo mức độ ổn định của quy trình.
- Phản ánh mức độ phát sinh NVA.

---

## 4. Phân tích chi phí

Hiện chưa có dữ liệu chi phí nội bộ của ACFC, vì vậy chỉ xác định cách tính.

### 4.1. Chi phí nhân công xử lý một case

**Công thức:**

`Chi phí xử lý case = Σ (Thời gian của từng actor × Chi phí nhân công/giờ của actor đó)`

Có thể gồm:
- CSKH/Cửa hàng.
- Người kiểm tra sản phẩm.
- Quản lý/đơn vị xử lý ngoại lệ.
- Nhân sự liên quan khác.

---

### 4.2. Chi phí rework

**Công thức:**

`Chi phí rework = Tổng thời gian kiểm tra/làm lại × Chi phí nhân công theo giờ`

Ví dụ hoạt động có thể phát sinh rework:
- kiểm tra lại hồ sơ;
- yêu cầu lại thông tin;
- kiểm tra lại sản phẩm;
- cập nhật lại case.

---

### 4.3. Chi phí logistics/di chuyển sản phẩm

Nếu sản phẩm phải vận chuyển giữa cửa hàng, kho hoặc đơn vị xử lý:

`Chi phí logistics = Tổng chi phí vận chuyển/phát sinh liên quan đến case`

Chỉ áp dụng khi thực tế quy trình có hoạt động này.

---

### 4.4. Chi phí đổi sản phẩm hoặc xử lý sau bán hàng

Nếu có dữ liệu thực tế:

`Chi phí xử lý sau bán hàng = Chi phí sản phẩm thay thế + Chi phí vận chuyển + Chi phí nhân công + Chi phí khác`

Không nên mặc định mọi case đều tạo ra chi phí sản phẩm thay thế.

---

## 5. Bộ chỉ số đề xuất

| Nhóm | Chỉ số | Công thức / cách đo |
|---|---|---|
| **Thời gian** | Cycle Time | Thời điểm đóng case - Thời điểm tiếp nhận |
| **Thời gian** | Thời gian chờ bổ sung hồ sơ | Giờ bổ sung đầy đủ - Giờ yêu cầu bổ sung |
| **Thời gian** | Thời gian kiểm tra sản phẩm | Giờ hoàn tất - Giờ bắt đầu kiểm tra |
| **Thời gian** | Thời gian xử lý chuyển cấp | Giờ có kết quả - Giờ chuyển cấp |
| **Chất lượng** | First-Time-Complete | Case đủ hồ sơ lần đầu / Tổng case × 100% |
| **Chất lượng** | Tỷ lệ bổ sung hồ sơ | Case phải bổ sung / Tổng case × 100% |
| **Chất lượng** | Tỷ lệ được xử lý | Case được chấp nhận / Tổng case × 100% |
| **Chất lượng** | Tỷ lệ từ chối | Case bị từ chối / Tổng case × 100% |
| **Chất lượng** | Tỷ lệ chuyển cấp | Case chuyển cấp / Tổng case × 100% |
| **Chất lượng** | Tỷ lệ rework | Case phải làm lại / Tổng case × 100% |
| **Chi phí** | Chi phí xử lý/case | Tổng thời gian nhân sự × chi phí nhân công |
| **Chi phí** | Chi phí rework | Thời gian làm lại × chi phí nhân công |
| **Chi phí** | Chi phí logistics | Tổng chi phí vận chuyển/phát sinh |
| **Chi phí** | Chi phí xử lý sau bán hàng | Sản phẩm + logistics + nhân công + chi phí khác |

---

## 6. Dữ liệu cần thu thập

| Dữ liệu | Mục đích |
|---|---|
| Thời điểm tiếp nhận và đóng case | Tính Cycle Time |
| Loại yêu cầu | So sánh đổi hàng/bảo hành/khiếu nại |
| Hồ sơ đầy đủ ngay lần đầu hay không | Tính First-Time-Complete |
| Số lần bổ sung hồ sơ | Đo rework và Hold |
| Thời gian chờ khách bổ sung | Phân tích thời gian |
| Thời gian kiểm tra sản phẩm | Phân tích bottleneck |
| Kết quả xử lý | Tính tỷ lệ được xử lý/từ chối |
| Lý do từ chối | Phân tích chất lượng |
| Có chuyển cấp hay không | Tính tỷ lệ chuyển cấp |
| Thời gian xử lý chuyển cấp | Phân tích Hold |
| Có rework hay không | Tính tỷ lệ rework |
| Chi phí nhân công/giờ | Tính chi phí xử lý |
| Chi phí vận chuyển nếu có | Tính chi phí logistics |

---

## 7. Mẫu bảng thu thập dữ liệu
**“giả lập minh họa”**
| Case  | Loại yêu cầu | Hồ sơ đủ lần đầu? | Số lần bổ sung | Thời gian chờ bổ sung (phút) | Thời gian kiểm tra SP (phút) | Chuyển cấp? | Kết quả    | Cycle Time (phút) | Rework? |
| ----- | ------------ | ----------------- | -------------: | ---------------------------: | ---------------------------: | ----------- | ---------- | ----------------: | ------- |
| S1-01 | Đổi hàng     | Có                |              0 |                            0 |                           18 | Không       | Được xử lý |                55 | Không   |
| S1-02 | Bảo hành     | Không             |              1 |                           25 |                           30 | Không       | Được xử lý |                95 | Có      |
| S1-03 | Khiếu nại    | Có                |              0 |                            0 |                           25 | Có          | Được xử lý |               120 | Không   |
| S1-04 | Đổi hàng     | Không             |              1 |                           20 |                           20 | Không       | Được xử lý |                80 | Có      |
| S1-05 | Bảo hành     | Có                |              0 |                            0 |                           35 | Có          | Được xử lý |               135 | Không   |
| S1-06 | Khiếu nại    | Không             |              2 |                           45 |                           28 | Có          | Được xử lý |               160 | Có      |
| S1-07 | Đổi hàng     | Có                |              0 |                            0 |                           15 | Không       | Được xử lý |                50 | Không   |
| S1-08 | Bảo hành     | Không             |              1 |                           30 |                           32 | Không       | Từ chối    |               100 | Có      |
| S1-09 | Khiếu nại    | Có                |              0 |                            0 |                           22 | Không       | Được xử lý |                70 | Không   |
| S1-10 | Đổi hàng     | Không             |              1 |                           25 |                           24 | Không       | Từ chối    |                85 | Có      |

### 7.1. Phân tích thời gian
Cycle Time trung bình

Tổng Cycle Time:

55 + 95 + 120 + 80 + 135 + 160 + 50 + 100 + 70 + 85 = 950 phút

Cycle Time trung bình:

950 / 10 = 95 phút/case

Thời gian kiểm tra sản phẩm trung bình

(18 + 30 + 25 + 20 + 35 + 28 + 15 + 32 + 22 + 24) / 10

= 249 / 10

= 24,9 phút/case

Thời gian chờ bổ sung hồ sơ

Có 5 case phải bổ sung hồ sơ:

25 + 20 + 45 + 30 + 25 = 145 phút

Thời gian chờ bổ sung trung bình:

145 / 5 = 29 phút/case cần bổ sung

Điều này minh họa rằng việc hồ sơ không đầy đủ ngay từ đầu có thể làm tăng đáng kể Cycle Time.

### 7.2. So sánh Cycle Time theo loại yêu cầu
Đổi hàng

Các case S1-01, S1-04, S1-07, S1-10:

(55 + 80 + 50 + 85) / 4

= 270 / 4

= 67,5 phút/case

Bảo hành

(95 + 135 + 100) / 3

= 110 phút/case

Khiếu nại

(120 + 160 + 70) / 3

≈ 116,7 phút/case

Loại yêu cầu	Cycle Time trung bình giả lập
Đổi hàng	67,5 phút
Bảo hành	110 phút
Khiếu nại	116,7 phút

Trong dữ liệu giả lập, khiếu nại có Cycle Time cao nhất, tiếp theo là bảo hành và cuối cùng là đổi hàng.

### 7.3. Phân tích chất lượng
First-Time-Complete

Có 5/10 case có hồ sơ đầy đủ ngay từ lần đầu.

First-Time-Complete = 5 / 10 × 100% = 50%

Tỷ lệ phải bổ sung hồ sơ

Có 5 case phải bổ sung.

5 / 10 × 100% = 50%

Tỷ lệ yêu cầu được xử lý

Có 8 case được xử lý.

8 / 10 × 100% = 80%

Tỷ lệ từ chối

Có 2 case bị từ chối.

2 / 10 × 100% = 20%

Tỷ lệ chuyển cấp

Có 3 case phải chuyển cấp.

3 / 10 × 100% = 30%

Tỷ lệ rework

Có 5 case phát sinh rework.

5 / 10 × 100% = 50%

### 7.4. Ví dụ giả lập chi phí rework

Giả sử để minh họa:

Chi phí nhân công trung bình: 60.000 đồng/giờ
Có 5 case rework
Mỗi case phát sinh trung bình 15 phút thao tác làm lại

Tổng thời gian rework:

5 × 15 = 75 phút

Quy đổi:

75 / 60 = 1,25 giờ

Chi phí rework giả lập:

1,25 × 60.000 = 75.000 đồng

Đây chỉ là ví dụ minh họa. Khi có dữ liệu thật cần tính thời gian thực tế của từng actor tham gia xử lý.

### 7.5. Tổng hợp kết quả giả lập
| Chỉ số                           |                      Kết quả |
| -------------------------------- | ---------------------------: |
| Cycle Time trung bình            |             **95 phút/case** |
| Thời gian kiểm tra SP trung bình |           **24,9 phút/case** |
| Thời gian chờ bổ sung trung bình | **29 phút/case cần bổ sung** |
| First-Time-Complete              |                      **50%** |
| Tỷ lệ phải bổ sung hồ sơ         |                      **50%** |
| Tỷ lệ được xử lý                 |                      **80%** |
| Tỷ lệ từ chối                    |                      **20%** |
| Tỷ lệ chuyển cấp                 |                      **30%** |
| Tỷ lệ rework                     |                      **50%** |
| Chi phí rework minh họa          |      **75.000 đồng/10 case** |


## 8. Câu hỏi
1. Trung bình một yêu cầu đổi hàng, bảo hành hoặc khiếu nại mất bao lâu từ lúc tiếp nhận đến khi hoàn tất?
Trả lời: Cycle Time trung bình là 95 phút/case.

2. Trung bình mất bao nhiêu phút để kiểm tra sản phẩm và bằng chứng của một case?
Trả lời: Trung bình khoảng 24,9 phút/case.

3. Trong 10 case gần nhất, có bao nhiêu case có hồ sơ đầy đủ ngay từ lần tiếp nhận đầu tiên?
Trả lời: Có 5/10 case, tương đương 50% First-Time-Complete.

4. Có bao nhiêu case phải yêu cầu khách hàng bổ sung hồ sơ hoặc bằng chứng?
Trả lời: Có 5/10 case, tương đương 50%.

5. Với những case phải bổ sung hồ sơ, thời gian chờ bổ sung trung bình là bao lâu?
Trả lời: Tổng thời gian chờ là 145 phút cho 5 case, trung bình 29 phút/case cần bổ sung.

6. Có bao nhiêu yêu cầu được xử lý và bao nhiêu yêu cầu bị từ chối?
Trả lời: Có 8/10 case được xử lý, tương đương 80%; và 2/10 case bị từ chối, tương đương 20%.

7. Có bao nhiêu case phải chuyển cấp cho Quản lý hoặc đơn vị khác?
Trả lời: Có 3/10 case phải chuyển cấp, tương đương 30%.

8. Có bao nhiêu case phát sinh rework?
Trả lời: Có 5/10 case phát sinh rework, tương đương 50%.

9. Loại yêu cầu nào có Cycle Time trung bình cao nhất?
Trả lời:

Đổi hàng: 67,5 phút/case
Bảo hành: 110 phút/case
Khiếu nại: 116,7 phút/case

Trong bộ dữ liệu minh họa, khiếu nại có Cycle Time cao nhất.

10. Chi phí rework ước tính trong 10 case là bao nhiêu?
Trả lời: Giả sử có 5 case rework, mỗi case mất trung bình 15 phút và chi phí nhân công là 60.000 đồng/giờ:

5 × 15 = 75 phút = 1,25 giờ

1,25 × 60.000 = 75.000 đồng

→ Chi phí rework giả lập khoảng 75.000 đồng/10 case.