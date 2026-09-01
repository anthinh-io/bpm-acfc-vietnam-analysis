# Thoại thuyết trình — Đăng ký & Kích hoạt tài khoản (Slide 19–23)

> Quy trình S3 – Hệ sinh thái ACFC Member. Tổng thời lượng gợi ý: **~5–6 phút**.
> Nhớ: **bật webcam**, nói chậm, mỗi slide chỉ nhấn 2–3 keyword chính, để hình ảnh/bảng "nói" thay mình.

---

## Slide 19 — Tổng quan quy trình (1/5) · ~70 giây

**Mở đầu / dẫn dắt kiến trúc quy trình:**

"Trong sơ đồ kiến trúc quy trình tổng thể dạng **ngôi nhà** mà nhóm đã trình bày ở phần đầu, hệ sinh thái ACFC Member gồm 3 lớp: lớp **cốt lõi** (bán hàng, tích điểm, ưu đãi), lớp **quản lý** và lớp **hỗ trợ**. Nhóm đã khảo sát khoảng **10 quy trình**, chọn **6 quy trình** phân tích sâu trong báo cáo Word. Trong buổi báo cáo hôm nay, do giới hạn thời gian, em xin đi sâu vào **1 quy trình tiêu biểu thuộc lớp Hỗ trợ**: **Đăng ký & Kích hoạt tài khoản** — đây là cửa ngõ đưa khách hàng vào toàn bộ hệ sinh thái, nên chất lượng của nó ảnh hưởng trực tiếp tới mọi quy trình phía sau."

**Thông tin tổng quan & Actor (bám 6 ô trên slide):**

- **Mục tiêu:** Tạo và kích hoạt tài khoản một cách **an toàn** và **liền mạch**.
- **Phạm vi:** Từ App/Web/POS cho đến khi tài khoản được kích hoạt, hoặc chuyển sang CSKH khi có ngoại lệ.
- **Số lượng Actor: 5 tác nhân** — (1) **Khách hàng**, (2) Cổng đăng ký/Frontend, (3) Salesforce CRM, (4) OTP Gateway (ZNS/SMS), (5) CSKH 1900 & bộ phận Đồng bộ/DevOps.
  → "Trong đó **Khách hàng chính là actor khách hàng** của quy trình — vừa là người **kích hoạt** quy trình (start event) vừa là người **hưởng lợi** cuối cùng (nhận Member ID, voucher, quyền lợi thành viên)."
- **Đầu vào:** Số điện thoại, mã OTP, thông tin cá nhân, mật khẩu.
- **Đầu ra / các trường hợp Output có thể xảy ra:**
  - ✅ **Thành công:** Tài khoản được kích hoạt → có **Member ID**, hồ sơ đồng bộ, voucher/ưu đãi.
  - ⚠️ **Ngoại lệ/Thất bại:** (a) Khách từ chối PDPA → **hủy đăng ký**; (b) SĐT đã tồn tại → **điều hướng đăng nhập**; (c) Sai OTP ≥ 3 lần → **khóa 24h và chuyển CSKH**.

*Chốt slide:* "Như vậy quy trình có **1 kết quả thành công** và **3 nhánh ngoại lệ** được xử lý rõ ràng."

---

## Slide 20 — BPMN hiện trạng (2/5) · ~110 giây

*Đây là slide trọng tâm — chỉ tay lên sơ đồ theo luồng.*

**Giới thiệu cấu trúc sơ đồ (chuẩn cú pháp BPMN):**

"Đây là sơ đồ **BPMN 2.0** hiện trạng. Toàn bộ đặt trong **1 Pool** — Hệ sinh thái ACFC Member — chia thành **5 Lane** đúng bằng 5 actor vừa nêu. Các Lane trao đổi với nhau qua **Message Flow** (ví dụ Frontend gửi yêu cầu sang OTP Gateway, Gateway trả mã OTP về cho Khách hàng). Sơ đồ đảm bảo **mỗi Task chỉ có 1 đầu vào – 1 đầu ra**, mọi chỗ rẽ nhánh đều đi qua **Gateway XOR**, và **mở cổng nào thì có đóng cổng tương ứng** — điển hình là cổng split kênh OTP được **gộp lại (XOR merge)** trước khi gửi. Sơ đồ có **đủ 8 Gateway quyết định**, **1 Timer Event 120 giây**, và **4 End event**."

**Mô tả luồng chính (Textual Process Description — đọc theo bullet, không lan man):**

1. Khách hàng **Truy cập App/Web** → **Đồng ý PDPA & Nhập SĐT**.
2. `Gateway 1 – Đồng ý PDPA?` → **Không** thì hủy; **Có** thì đi tiếp.
3. `Gateway 2 – SĐT đã tồn tại?` → **Rồi** thì điều hướng đăng nhập; **Chưa** thì **Khởi tạo hồ sơ tạm** trên CRM.
4. `Gateway 3 (Split) – Kênh Zalo ZNS?` → **Gửi OTP** qua Zalo ZNS (chính) hoặc SMS (fallback) → `Gateway 4 – Gộp kênh (join)`.
5. `Gateway 5 – Cổng OTP lỗi?` → nếu lỗi chuyển **CSKH 1900 xác minh thủ công**; nếu không → **Timer: Chờ OTP ≤ 120s** → **Nhập mã OTP**.
6. `Gateway 6 – OTP hợp lệ?` → sai thì `Gateway 7 – Sai ≥ 3 lần?` (chưa → nhập lại; đủ 3 → **Khóa 24h, chuyển CSKH**).
7. OTP hợp lệ → **Điền thông tin & Tạo mật khẩu** → `Gateway 8 – Mật khẩu chuẩn & đồng ý điều khoản?`.
8. Đạt → **Tạo User & cấp Member ID** → `Gateway 9 – Đồng bộ Magento + Retail Pro?` → lỗi thì **đưa vào hàng đợi retry + cảnh báo DevOps**; thành công thì **Kích hoạt xong**.
9. **End (thành công):** Auto-login + Voucher 100k + Auto tier upgrade.

*Chốt:* "Điểm đáng chú ý về mặt vận hành là **Timer 120 giây chờ OTP** và **nhánh retry đồng bộ** — đây chính là hai nơi phát sinh nghẽn mà phần phân tích tiếp theo sẽ định lượng."

**Đặt tên chuẩn (nếu giám khảo hỏi):** Activity đặt theo *Động từ + Danh từ* ("Gửi OTP", "Tạo User"), Event/Gateway đặt theo *Danh từ + Trạng thái/Câu hỏi* ("OTP hợp lệ?", "Kích hoạt xong").

---

## Slide 21 — Phân tích định tính (3/5) · ~60 giây

"Nhóm phân loại từng hoạt động theo **VA / BVA / NVA**:

- **VA – Giá trị gia tăng:** *Tạo & kích hoạt tài khoản* — bước duy nhất trực tiếp mở quyền lợi thành viên cho khách.
- **BVA – Giá trị cho doanh nghiệp:** *Gửi & xác thực OTP* — không tạo giá trị cho khách nhưng bắt buộc để **bảo mật tài khoản**.
- **NVA – Không giá trị (lãng phí):** *Nhập lại khi OTP lỗi* — thao tác thừa, cần loại bỏ.

Về **lãng phí**, nổi cộm 3 loại: **Chờ** (chờ nhận OTP – ảnh hưởng **Cao**), **Sai lỗi** (OTP lỗi/hết hạn, lỗi đồng bộ – **Cao**), và **Xử lý dư** (nhập lại thông tin – **Vừa**). Ba loại này khớp đúng với các nhánh ngoại lệ trên sơ đồ BPMN."

---

## Slide 22 — Phân tích định lượng (4/5) · ~60 giây

"Về con số hiện trạng, đo trên 3 nhóm chỉ tiêu:

- **Thời gian:** Hoàn tất trung bình **90 giây**, trong đó **chờ OTP ~20 giây**; **PCE = 78%**. → **Điểm nghẽn là khâu chờ OTP.**
- **Chất lượng:** Đăng ký thành công **82%**, OTP đúng ngay lần đầu **88%**, khoảng **6%** phải cần đến CSKH. → Dư địa cải thiện nằm ở **OTP và lỗi đăng nhập**.
- **Chi phí:** OTP khoảng **300.000đ/1.000 lượt**, CSKH ~**1,5 triệu**, và **cơ hội mất ~9 triệu** do khách bỏ dở. → Ưu tiên **giảm bỏ dở và giảm hỗ trợ lặp**."

*Chốt:* "PCE 78% và tỷ lệ thành công 82% cho thấy quy trình vận hành ổn nhưng vẫn rò rỉ ở khâu OTP — đó là lý do cho các đề xuất ở slide cuối."

---

## Slide 23 — Vấn đề & Hướng cải tiến (5/5) · ~55 giây

"Tổng hợp lại thành 4 cặp **Vấn đề → Tác động → Hướng cải tiến**:

1. **OTP chậm/hết hạn** → gây bỏ dở đăng ký → thêm **kênh OTP dự phòng + đồng hồ đếm ngược** cho khách.
2. **Nhập lại thông tin** → tăng thao tác → **lưu tạm phiên (session)** để không mất dữ liệu đã nhập.
3. **Lỗi đồng bộ CRM/Magento/POS** → tài khoản chưa kích hoạt → cơ chế **retry tự động + cảnh báo** DevOps.
4. **Thông báo lỗi chưa rõ** → tăng yêu cầu CSKH → **thông báo cụ thể + chatbot** hỗ trợ.

Những cải tiến này nhắm thẳng vào 2 điểm nghẽn đã định lượng: **chờ OTP** và **lỗi đồng bộ**, kỳ vọng nâng PCE và tỷ lệ đăng ký thành công."

*Câu chuyển tiếp:* "Đó là phần trình bày quy trình Đăng ký & Kích hoạt tài khoản, em xin chuyển sang phần tiếp theo / mời thầy cô đặt câu hỏi."

---

## Phụ lục A — Phương pháp khám phá quy trình (nói khi được hỏi, ~30s)

"Nhóm khám phá quy trình bằng **workshop kết hợp phỏng vấn**:
- **Thành phần tham dự:** đại diện bộ phận CSKH, nhân sự vận hành Frontend/CRM, và 1 khách hàng mẫu.
- **Minh chứng:** kịch bản workshop, biên bản họp và bản ghi màn hình thao tác đăng ký thực tế (đính kèm phụ lục báo cáo Word).
- Từ dữ liệu thu thập, nhóm dựng sơ đồ BPMN hiện trạng rồi đối chiếu lại với người vận hành để hiệu chỉnh."

## Phụ lục B — Bộ 10 câu hỏi thu thập dữ liệu (5 định tính + 5 định lượng)

**Nhóm ĐỊNH TÍNH (5 câu):**

1. *(Trắc nghiệm)* Bước nào trong quy trình khiến khách hàng **bối rối/dễ bỏ dở** nhất?
   - A. Đồng ý PDPA & nhập SĐT · B. Chờ & nhập OTP · C. Điền thông tin & tạo mật khẩu · D. Khác
2. *(Trắc nghiệm)* Khi OTP lỗi/hết hạn, khách thường phản ứng thế nào?
   - A. Thử gửi lại · B. Chờ thêm · C. Bỏ cuộc · D. Gọi CSKH
3. *(Tự luận)* Anh/chị mô tả trải nghiệm khó chịu nhất khi đăng ký tài khoản Member?
4. *(Tự luận)* Theo anh/chị, thông báo lỗi hiện tại đã đủ rõ để khách tự xử lý chưa? Vì sao?
5. *(Tự luận)* Nếu được thay đổi **một** điểm trong quy trình, anh/chị muốn cải thiện điều gì?

**Nhóm ĐỊNH LƯỢNG (5 câu):**

6. *(Trắc nghiệm)* Trung bình khách chờ OTP bao lâu?
   - A. < 10s · B. 10–20s · C. 20–60s · D. > 60s
7. *(Trắc nghiệm)* Tỷ lệ nhập đúng OTP ngay lần đầu ước khoảng?
   - A. < 70% · B. 70–85% · C. 85–95% · D. > 95%
8. *(Điền số)* Mỗi ngày có bao nhiêu lượt đăng ký, và bao nhiêu % phải cần CSKH hỗ trợ?
9. *(Điền số)* Tỷ lệ lỗi đồng bộ CRM/Magento/Retail Pro trên tổng số tài khoản tạo mới là bao nhiêu %?
10. *(Điền số)* Chi phí OTP và chi phí CSKH trung bình cho mỗi 1.000 lượt đăng ký là bao nhiêu?

---

### Ghi chú trình bày
- Bật **webcam** suốt phần nói; giữ giao tiếp mắt với camera.
- Chỉ đọc **keyword** trên slide, phần diễn giải nói tự nhiên.
- Slide 20 (BPMN) là trọng tâm — dành nhiều thời gian nhất, chỉ tay theo luồng.
- Bám đúng thời lượng nhóm đã phân bổ; nếu thiếu giờ, rút gọn slide 21–22, giữ nguyên 19–20–23.
