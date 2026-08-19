# S1 – Đổi hàng, bảo hành và xử lý khiếu nại – Phân tích định lượng

## 1. Mục tiêu phân tích

Phân tích định lượng S1 tập trung vào ba nhóm chỉ số chính theo rubric:

- **Thời gian**
- **Chất lượng**
- **Chi phí**

Hiện chưa có dữ liệu vận hành nội bộ thực tế của ACFC để tính ra giá trị cuối cùng. Vì vậy, phần này xác định **chỉ số cần đo, cách tính và dữ liệu cần thu thập**, không tự tạo số liệu giả.

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

| Case ID | Loại yêu cầu | Hồ sơ đủ lần đầu? | Số lần bổ sung | Thời gian kiểm tra | Chuyển cấp? | Kết quả | Cycle Time | Rework? |
|---|---|---|---:|---:|---|---|---:|---|
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

Nên thu thập dữ liệu trong nhiều case trước khi đưa ra kết luận.

---

## 8. Nguyên tắc sử dụng số liệu

- Không tự tạo số liệu nếu chưa có dữ liệu thực tế.
- Nếu dùng số giả định để minh họa công thức, phải ghi rõ **“Ví dụ minh họa”**.
- Khi có dữ liệu thật, nên tính:
  - trung bình;
  - trung vị nếu cần;
  - lớn nhất;
  - nhỏ nhất;
  - tỷ lệ phần trăm;
  - số lượng case.
- Nên phân tách dữ liệu theo loại yêu cầu:
  - đổi hàng;
  - bảo hành;
  - khiếu nại.
- Nếu có nhiều kênh tiếp nhận, nên so sánh theo từng kênh để xác định kênh nào có cycle time hoặc tỷ lệ rework cao hơn.
