# BÁO CÁO CHUYÊN SÂU: QUY TRÌNH ĐĂNG KÝ, XÁC THỰC OTP & KÍCH HOẠT TÀI KHOẢN THÀNH VIÊN ACFC

**Học phần:** IE203.F31.CN1.CNTT – Hệ thống quản trị qui trình nghiệp vụ  
**Giảng viên hướng dẫn:** ThS. Hà Lê Hoài Trung  
**Đơn vị thực hiện:** Nhóm nghiên cứu Đề tài BPM ACFC Việt Nam  

---

## 1. Bối cảnh Nghiên cứu & Mục tiêu Quy trình

Trong chiến lược phát triển bán lẻ đa kênh (*Omnichannel Retail*) của **ACFC**, chương trình khách hàng thân thiết (**ACFC Member**) là đòn bẩy trung tâm giúp tăng tỷ lệ giữ chân khách hàng. Hệ thống phân hạng khách hàng được chia làm 5 bậc chi tiết:
- **Member**: 0 VNĐ
- **Silver**: Định mức chi tiêu lên đến hạng (Discount 5%)
- **Gold**: Định mức chi tiêu đạt ngưỡng (Discount 10%)
- **Platinum**: Định mức chi tiêu đạt ngưỡng (Discount 10%)
- **Diamond**: Định mức chi tiêu cao nhất (Discount 10%)

Việc tích lũy điểm được hệ thống tính toán theo từng hạng:
- 100.000 VNĐ = 1 điểm (áp dụng Member/Silver)
- 100.000 VNĐ = 3 điểm (áp dụng Gold)
- 100.000 VNĐ = 5 điểm (áp dụng Platinum)
- 100.000 VNĐ = 10 điểm (áp dụng Diamond)

Quy đổi: 1 điểm = 1.000 VNĐ khi đổi thưởng (áp dụng cho hạng Gold trở lên, giảm tối đa 50% giá trị hóa đơn).
Đồng thời, khách hàng được ưu đãi tháng sinh nhật giảm 20-30%. Hệ thống được quản trị tập trung thông qua nền tảng **Salesforce CRM** kết hợp với phần mềm POS **Retail Pro Prism** và **Adobe Magento Commerce**.

---

## 2. Phương pháp Thực hiện & Bằng chứng Thu thập (Evidence-based)

*Bảng 5.1: Nhật ký bằng chứng nghiệp vụ Đăng ký & Kích hoạt Tài khoản ACFC.*

| Mã bằng chứng | Nguồn trích dẫn chính thức | Nội dung nghiệp vụ trích xuất | Mức độ tin cậy |
| :---: | :--- | :--- | :---: |
| **EV09** | [Hướng dẫn tạo tài khoản – ACFC](https://www.acfc.com.vn/huong-dan-tao-tai-khoan) | Xác thực OTP qua Zalo ZNS và SMS (fallback) | Mức A |
| **EV10** | Chính sách thành viên ACFC | 5 bậc hạng thẻ, tỷ lệ tích điểm và quy đổi | Mức A |

---

## 3. Khám phá & Mô tả Quy trình AS-IS: Đăng ký & Kích hoạt Tài khoản

### 3.1. Hồ sơ Quy trình (Process Profile)
* **Mã quy trình:** S3
* **Tên quy trình:** Đăng ký, xác thực OTP & kích hoạt tài khoản thành viên.
* **Cấp độ:** Quy trình Hỗ trợ (*Support Process*).
* **Mục tiêu quy trình:** Kích hoạt tài khoản nhanh chóng, đồng bộ profile đa kênh, cấp ưu đãi sinh nhật và đặc quyền hạng thẻ.
* **Đối tượng khách hàng (Customer):** Khách hàng mới hoặc tài khoản Legacy cần dịch chuyển dữ liệu.
* **Tác nhân kích hoạt (Trigger):** Khách hàng đăng ký trên App/Web hoặc tại Store POS.
* **Đầu vào (Inputs):** Số điện thoại, OTP, Thông tin định danh.
* **Đầu ra (Outputs):** Hồ sơ khách hàng tạo thành công trên Salesforce CRM, liên kết Retail Pro Prism, Magento.
* **Kết quả tích cực:** Khách hàng nhận OTP qua Zalo ZNS ngay lập tức, tài khoản kích hoạt, tự động nâng cấp hạng (Auto tier upgrade) khi doanh số đạt.
* **Kết quả tiêu cực:** Lỗi xác thực OTP, bỏ dở do quá nhiều thông tin.

### 3.2. Bảng Trình tự các Bước Thực hiện (Step-by-Step AS-IS Table)

*Bảng 5.2: Bảng các bước thực hiện quy trình Đăng ký & Kích hoạt tài khoản thành viên ACFC.*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Khách hàng | *Truy cập* App/Web, *Đồng ý* PDPA & *Nhập* SĐT | Checkbox, SĐT | Trạng thái đồng ý, SĐT | **G1: Đồng ý PDPA?** (Không → End *Hủy đăng ký*) |
| 2 | Salesforce CRM | *Kiểm tra* trùng lặp SĐT (Duplicate profile check) | SĐT | Kết quả tra cứu | **G2: SĐT đã tồn tại?** (Có → End *Điều hướng Đăng nhập*) |
| 3 | Cổng ĐK (Frontend) | *Khởi tạo* hồ sơ tạm trên CRM (gộp dữ liệu Legacy nếu có) | SĐT, Lịch sử cũ | Bản ghi CRM tạm | (Nếu G2: Chưa) |
| 4 | OTP Gateway | *Gửi* OTP — Zalo ZNS (chính) **hoặc** SMS (fallback) | SĐT, Mã OTP | Tin nhắn OTP | **G3: Kênh Zalo ZNS?** — *Split XOR* → *Join (gộp kênh, XOR merge)* |
| 5 | Hệ thống | *Kiểm tra* trạng thái cổng gửi OTP | Trạng thái kết nối | Cảnh báo hệ thống | **G4: Cổng OTP lỗi?** |
| 6 | Call Center | *Xác minh* thủ công qua CSKH 1900 3038 | SĐT | Trạng thái xác minh | (Nếu G4: Có) |
| 7 | Sự kiện Timer | *Chờ* khách nhập OTP ≤ 120s | — | Sự kiện hẹn giờ | (Nếu G4: Không) — Timer intermediate event |
| 8 | Khách hàng | *Nhập* mã xác thực OTP | Mã OTP | Trạng thái OTP | **G5: OTP hợp lệ?** |
| 9 | Hệ thống | *Kiểm tra* số lần nhập sai OTP (Retry limit) | Số lần nhập | Lỗi xác thực | **G6: Sai ≥ 3 lần?** (Có → End *Khóa 24h → CSKH*; Chưa → nhập lại) |
| 10 | Khách hàng | *Điền* thông tin cá nhân & *Tạo* mật khẩu | Thông tin form, mật khẩu | Hồ sơ cập nhật | (Nếu G5: Có) — **G7: MK chuẩn & đồng ý ĐK?** (Không → nhập lại) |
| 11 | Salesforce CRM | *Tạo* User & *cấp* Member ID | Hồ sơ đầy đủ | Member ID | (Nếu G7: Có) |
| 12 | Hệ thống tích hợp | *Đồng bộ* hồ sơ sang Magento (Web/App) & Retail Pro Prism (POS) | API Data | Dữ liệu App/Web/POS | **G8: Đồng bộ Magento + Retail Pro?** (Không → Hàng đợi retry & cảnh báo DevOps) |
| 13 | Hệ thống | *Kích hoạt* tài khoản: Auto-login + Voucher 100k + Auto tier upgrade | Member ID | Tài khoản active | (Nếu G8: Có) → End *Kích hoạt xong* |

---

## 4. Mô hình hóa Quy trình BPMN 2.0 (Đúng 8 Gateways)

Sơ đồ được mô hình hóa theo chuẩn **BPMN 2.0**: 1 Pool "Hệ sinh thái ACFC Member" – 5 Lane (Khách hàng, Cổng ĐK Frontend, Salesforce CRM, OTP Gateway ZNS/SMS, CSKH & Đồng bộ), đủ **8 cổng điều kiện XOR** (có **Split & Join** tại cổng chọn kênh OTP), **1 sự kiện trung gian Timer** (chờ OTP ≤120s) và **4 sự kiện Kết thúc (End event)**.

Danh sách 8 Cổng điều kiện (Gateways) – đồng bộ tuyệt đối với Hình 5.2:

1. **XOR G1 – Đồng ý PDPA?** Khách hàng có đồng ý chính sách bảo mật dữ liệu PDPA (Nghị định 13/2023/NĐ-CP) không? *(Không → End: Hủy đăng ký).*
2. **XOR G2 – SĐT đã tồn tại?** Số điện thoại đăng ký đã tồn tại trên Salesforce CRM chưa (Duplicate profile check)? *(Có → End: Điều hướng Đăng nhập).*
3. **XOR G3 – Kênh gửi OTP (Zalo ZNS ↔ SMS)?** Gửi OTP qua Zalo ZNS (chính) hay SMS (fallback)? Đây là **cổng Split (XOR)**: hệ thống chọn **một** kênh, hai nhánh sau đó **hợp lại tại cổng Join – gộp kênh (XOR merge)** trước khi kiểm tra cổng OTP. *(Split và Join cùng loại XOR để tránh deadlock.)*
4. **XOR G4 – Cổng OTP lỗi?** Cổng gửi OTP (ZNS/SMS) có bị lỗi không (→ chuyển CSKH 1900 3038 xác minh thủ công); nếu không → sự kiện Timer *Chờ OTP ≤120s*.
5. **XOR G5 – OTP hợp lệ?** Mã OTP khách nhập có hợp lệ và còn hiệu lực (trong 120s) không?
6. **XOR G6 – Sai ≥ 3 lần?** Số lần nhập sai OTP có vượt quá giới hạn (≥3 lần) không? *(Có → End: Khóa 24h → CSKH; Chưa → quay lại nhập OTP).*
7. **XOR G7 – MK chuẩn & đồng ý ĐK?** Mật khẩu có đạt chuẩn an toàn và khách hàng có đồng ý điều khoản đăng ký không? *(Không → quay lại điền thông tin).*
8. **XOR G8 – Đồng bộ Magento + Retail Pro?** Tiến trình đồng bộ hồ sơ sang Adobe Magento và Retail Pro Prism có thành công không? *(Không → Hàng đợi retry & cảnh báo DevOps; Có → End: Kích hoạt xong + Auto tier upgrade).*
