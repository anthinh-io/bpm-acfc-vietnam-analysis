# BÁO CÁO CHUYÊN SÂU: QUY TRÌNH TUYỂN DỤNG & TIẾP NHẬN NHÂN SỰ CHUỖI BÁN LẺ VÀ KHO VẬN ACFC

**Học phần:** IE203.F31.CN1.CNTT – Hệ thống quản trị qui trình nghiệp vụ  
**Giảng viên hướng dẫn:** ThS. Hà Lê Hoài Trung  
**Đơn vị thực hiện:** Nhóm nghiên cứu Đề tài BPM ACFC Việt Nam  

---

## 1. Bối cảnh Nghiên cứu & Mục tiêu Quy trình

Quy trình tuyển dụng và tiếp nhận nhân sự (S1) đóng vai trò sống còn trong chuỗi bán lẻ ACFC. Quy trình yêu cầu sự phân biệt rõ ràng:
- **Store staff**: Nhân viên cửa hàng, tuyển dụng số lượng lớn (volume hiring), có tính đặc thù cao do đặc tính ngành bán lẻ với turnover rate lên tới ~25%.
- **HQ/Warehouse staff**: Nhân viên văn phòng, kho vận có yêu cầu chuyên môn cao (specialized).

Ứng viên được thu hút thông qua các kênh thực tế như: `tuyendung.acfc.com.vn`, TopCV, LinkedIn, VietnamWorks và các hội nhóm Facebook Groups.

---

## 2. Phương pháp Thực hiện & Bằng chứng Thu thập

*Bảng 6.1: Nhật ký bằng chứng nghiệp vụ Tuyển dụng ACFC.*

| Mã bằng chứng | Nguồn trích dẫn chính thức | Nội dung nghiệp vụ trích xuất | Mức độ tin cậy |
| :---: | :--- | :--- | :---: |
| **EV13** | tuyendung.acfc.com.vn | Danh sách các vị trí tuyển dụng Store và HQ | Mức A |
| **EV14** | TopCV, LinkedIn, VietnamWorks | Các kênh đăng tuyển, quy trình ATS screening | Mức B |

---

## 3. Khám phá & Mô tả Quy trình AS-IS: Tuyển dụng & Tiếp nhận Nhân sự

### 3.1. Hồ sơ Quy trình (Process Profile)
* **Mã quy trình:** S1
* **Tên quy trình:** Tuyển dụng & tiếp nhận nhân sự chuỗi bán lẻ và kho vận.
* **Mục tiêu quy trình:** Cung cấp nguồn nhân sự đúng tiêu chuẩn, onboard ứng viên bằng các bước cấp phát Brand uniform và mở Account POS/Retail Pro Prism.
* **Đối tượng:** Store staff và HQ/Warehouse staff.
* **Đầu vào (Inputs):** Yêu cầu tuyển dụng, CV ứng viên nộp qua ATS.
* **Đầu ra (Outputs):** Hợp đồng lao động, Báo cáo probation review sau 2 tháng.
* **Kết quả tích cực:** Tuyển được nhân sự phù hợp (Fast-track nếu có fashion retail experience), vượt qua probation với các chỉ số KPI tốt.
* **Kết quả tiêu cực:** Turnover cao, phải Exit interview.

### 3.2. Bảng Trình tự các Bước Thực hiện (Step-by-Step AS-IS Table)

*Bảng 6.2: Bảng các bước thực hiện quy trình Tuyển dụng & Tiếp nhận nhân sự (S1).*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | HR Dept | *Đăng tải* Tin tuyển dụng | Yêu cầu nhân sự | Tin đăng tuyển | **Gateway 1: Vị trí thuộc nhóm Store staff (volume) hay HQ/Warehouse (specialized)?** |
| 2 | ATS System | *Thực hiện* Sàng lọc ATS (ATS screening process) | CV đa kênh | CV rút gọn | **Gateway 2: Ứng viên có fashion retail experience (chuyển sang Fast-track)?** |
| 3 | HR Recruiter | *Kiểm tra* Background check (Non-compete NDA cho HQ/Warehouse, Criminal record cho Store staff) | CV, Người tham chiếu | Báo cáo kiểm tra | **Gateway 3: Background check của ứng viên có đạt tiêu chuẩn không?** |
| 4 | Line Manager | *Phỏng vấn* Vòng 1 (V1) | Báo cáo CV | Kết quả V1 | **Gateway 4: Ứng viên có đạt V1 (Line Manager)?** |
| 5 | HR Dir / Ban GĐ | *Phỏng vấn* Vòng 2 & V3 (đối với Senior) | Đánh giá V1 | Kết quả cuối cùng | **Gateway 5: Ứng viên có đạt phỏng vấn chuyên sâu (V2/V3) không?** |
| 6 | HR Dept | *Đàm phán* Offer Letter (Thương lượng & Chốt) | Kết quả PV | Thỏa thuận Offer | **Gateway 6: Candidate accepts Offer? (Yes/Negotiate/Decline)** |
| 7 | HR / Medical | *Thực hiện* Khám sức khỏe trước tuyển dụng (Health Check) | Thỏa thuận Offer | Kết quả y tế | **Gateway 7: Pass statutory Health Check?** |
| 8 | HR & IT Dept | *Triển khai* Quá trình Onboarding | Hồ sơ y tế | Gói Onboarding | Cấp Brand uniform, đào tạo product knowledge, setup POS/Retail Pro Prism account |
| 9 | Line Manager | *Đánh giá* Thử việc 2 tháng (Probation review) | Báo cáo công việc | Phiếu đánh giá | KPI gồm Sales target và Customer satisfaction |
| 10 | HR Dept | *Xem xét* Ký hợp đồng lao động | Phiếu đánh giá | Hợp đồng / Thanh lý | **Gateway 8: Ứng viên có đạt KPI probation review 2 tháng không?** |

---

## 4. Mô hình hóa Quy trình BPMN 2.0 (Đáp ứng $\ge 8$ Gateways)

Danh sách 8 Cổng điều kiện (Gateways):
1. **XOR 1:** Vị trí tuyển dụng thuộc nhóm Store staff (volume hiring) hay HQ/Warehouse (specialized)?
2. **XOR 2:** Ứng viên có Fashion retail experience (Kích hoạt luồng Fast-track vs Standard track)?
3. **XOR 3:** Kết quả Background check (Non-compete NDA đối với HQ/Warehouse, Criminal record đối với Store staff) có hợp lệ không?
4. **XOR 4:** Kết quả Phỏng vấn V1 (Line Manager) có đạt không?
5. **XOR 5:** Kết quả Phỏng vấn chuyên sâu V2/V3 (HR Director / Ban Giám đốc) có đạt không?
6. **XOR 6:** Candidate accepts Offer? (Yes/Negotiate/Decline)
7. **XOR 7:** Pass statutory Health Check? (Khám sức khỏe theo luật định)
8. **XOR 8:** Ứng viên có đạt các KPI (Sales target, Customer satisfaction) trong 2-month probation review không?
