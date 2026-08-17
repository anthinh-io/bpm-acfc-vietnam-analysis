# BÁO CÁO CÁ NHÂN – QUY TRÌNH M3, S3, S4 & S1 (ACFC)

**Sinh viên:** Nguyễn Công Hưng<br>
**MSSV:** 24730100<br>
**Môn:** IE203.F31.CN1.CNTT – Hệ thống quản trị qui trình nghiệp vụ<br>
**GVHD:** ThS. Hà Lê Hoài Trung<br>
**Doanh nghiệp phân tích:** Công ty Cổ phần Thời trang và Mỹ phẩm Âu Châu (ACFC)<br>
**Ngày cập nhật:** 17/08/2026

> **Mục đích tài liệu:** đây là **báo cáo tổng hợp cấp cá nhân** cho bốn quy trình Hưng phụ trách — **M3 (Quản lý)**, **S3 (Hỗ trợ)**, **S4 (Hỗ trợ)** và **S1 (Hỗ trợ)** — gộp liền mạch discovery, mô tả hiện trạng (AS-IS), bộ câu hỏi thu thập dữ liệu, phân tích định tính/định lượng và đề xuất TO-BE. Tài liệu tự chứa (self-contained): mọi bảng bước, kịch bản, câu hỏi phỏng vấn và bảng KPI đều nằm trong file này để có thể copy/paste và định dạng lại thành báo cáo Word khi nhóm chắt lọc. Số liệu định lượng còn thiếu tuân thủ nguyên tắc **không tự bịa số ACFC** — xem mục 9 và 11.

---

## Mục lục

1. [Mục tiêu, phạm vi và nguyên tắc](#1-mục-tiêu-phạm-vi-và-nguyên-tắc)
2. [Đối chiếu rubric](#2-đối-chiếu-rubric)
3. [Danh mục quy trình phụ trách](#3-danh-mục-quy-trình-phụ-trách)
4. [Mô tả quy trình hiện tại (AS-IS)](#4-mô-tả-quy-trình-hiện-tại-as-is)
5. [Phương pháp thu thập và xác thực](#5-phương-pháp-thu-thập-và-xác-thực)
6. [Bộ câu hỏi thu thập dữ liệu (10 định tính + 10 định lượng mỗi quy trình)](#6-bộ-câu-hỏi-thu-thập-dữ-liệu)
7. [Kế hoạch làm việc (mốc cá nhân)](#7-kế-hoạch-làm-việc-mốc-cá-nhân)
8. [Phân tích định tính](#8-phân-tích-định-tính)
9. [Phân tích định lượng (Thời gian – Chất lượng – Chi phí)](#9-phân-tích-định-lượng-thời-gian--chất-lượng--chi-phí)
10. [Đề xuất khắc phục theo lãng phí và TO-BE](#10-đề-xuất-khắc-phục-theo-lãng-phí-và-to-be)
11. [Kết luận và nội dung cần xác thực](#11-kết-luận-và-nội-dung-cần-xác-thực)

---

## 1. Mục tiêu, phạm vi và nguyên tắc

### 1.1. Bối cảnh và phạm vi cá nhân

Phạm vi cá nhân của Hưng thuộc mảng **hàng hóa, kho, tồn kho, tài khoản thành viên và tuyển dụng nhân sự ACFC**. Theo yêu cầu rút gọn của nhóm (cập nhật 11/08/2026), mỗi thành viên bắt buộc hoàn thiện **1 quy trình Quản lý + 1 quy trình Hỗ trợ** (nhóm đã đạt tối thiểu 6 quy trình BPMN + phân tích ở cấp chung). Hưng dồn toàn lực hoàn thiện **M3 (Quản lý)** và **S3 (Hỗ trợ)** theo yêu cầu bắt buộc, đồng thời bổ sung hai quy trình Hỗ trợ: **S4** — đăng ký/kích hoạt tài khoản thành viên và **S1** — tuyển dụng & tiếp nhận nhân sự chuỗi bán lẻ/kho vận, cả hai khai thác từ nội dung công khai trên trang chủ và trang tuyển dụng ACFC, đã kiểm tra không trùng mã hoặc nội dung với quy trình của thành viên khác. C3/C4 (2 quy trình Cốt lõi) không còn trong phạm vi bài làm tuần này nên đã gỡ khỏi workspace cá nhân.

| Mã | Cấp | Quy trình | Ranh giới | Trạng thái |
|---|---|---|---|---|
| M3 | Quản lý | Lập kế hoạch mua hàng và phân bổ theo mùa | Dữ liệu bán hàng/tồn → kế hoạch được duyệt | Xong bản nháp |
| S3 | Hỗ trợ | Kiểm kê và xử lý chênh lệch tồn kho | Kiểm kê/cảnh báo → điều chỉnh hoặc chuyển cấp | Xong bản nháp |
| S4 | Hỗ trợ | Đăng ký, xác thực OTP & kích hoạt tài khoản thành viên | Truy cập App/Web → tài khoản được tạo/kích hoạt hoặc chuyển CSKH | Xong bản nháp |
| S1 | Hỗ trợ | Tuyển dụng & tiếp nhận (onboarding) nhân sự chuỗi bán lẻ/kho vận | Yêu cầu tuyển dụng → ký hợp đồng sau probation hoặc thanh lý | Xong bản nháp |

### 1.2. Ranh giới với các workspace khác

- Phạm vi tuần này gồm M3, S3, S4 và S1; không mô tả các quy trình Quản lý/Cốt lõi/Hỗ trợ khác đã thuộc phạm vi phụ trách của thành viên khác trong nhóm.
- M3 nhận doanh số/KPI/kế hoạch thương mại từ M2 nhưng **chỉ sở hữu bước mua hàng và phân bổ**; M3 phát hành kế hoạch mua/yêu cầu điều chuyển làm đầu ra bàn giao, không mô tả sâu các bước nhận hàng/điều chuyển nội bộ.
- M1 thực hiện vận hành/đếm thường lệ; **S3 xử lý kiểm soát, đếm lại, điều chỉnh và chuyển cấp chênh lệch**. Kết quả S3 được phản hồi cho M3 để điều chỉnh kế hoạch, hạn mức tồn và nguyên nhân thất thoát.
- **S4** (đăng ký/kích hoạt tài khoản thành viên) khác với quy trình xử lý yêu cầu quyền dữ liệu cá nhân đã thuộc phạm vi thành viên khác: S4 chỉ dừng ở tạo/kích hoạt tài khoản, không xử lý yêu cầu truy cập/xóa/chỉnh sửa dữ liệu cá nhân theo quyền của chủ thể dữ liệu.
- **S1** (tuyển dụng & tiếp nhận nhân sự) chỉ mô tả luồng từ yêu cầu tuyển dụng đến ký hợp đồng sau thử việc; **không** bao gồm quản trị lương thưởng, đào tạo dài hạn hay đánh giá hiệu suất định kỳ sau khi đã ký hợp đồng chính thức — các mảng này (nếu có) thuộc quy trình nhân sự khác.

### 1.3. Nguyên tắc học thuật xuyên suốt

Hoạt động có nguồn công khai hỗ trợ được đánh dấu mức **A/B**; bước nối, ngưỡng, thời hạn hoặc số liệu nội bộ chưa có bằng chứng được đánh dấu **`C – cần xác thực`** và không trình bày như số liệu/quy trình chính thức đã được ACFC xác nhận.

- **A** – Chính sách, hướng dẫn hoặc trang chính thức ACFC → dùng để xác định quy tắc công khai và kết quả đầu ra cho khách hàng.
- **B** – Mô tả công việc/tin tuyển dụng chính thức của ACFC → dùng để nhận diện vai trò và hoạt động; luồng nối vẫn cần xác thực.
- **C** – Suy luận ngành hoặc giả định của nhóm → chỉ dùng làm câu hỏi/nhánh dự kiến, **không** gọi là quy trình chính thức.

Mỗi hoạt động, gateway và KPI đều ghi mã nguồn hoặc nhãn `C – cần xác thực`; **không điền số ACFC nếu chưa có nguồn hoặc người có thẩm quyền xác nhận**.

## 2. Đối chiếu rubric

| Tiêu chí rubric | Yêu cầu | Đóng góp của M3/S3/S4/S1 trong báo cáo này |
|---|---|---|
| 1. Liệt kê & phân loại quy trình | Tối thiểu 10 quy trình, ≥3 mỗi cấp | M3 (Quản lý), S3, S4, S1 (Hỗ trợ) — góp 4/10 trong phạm vi cá nhân (danh mục 10 quy trình đầy đủ ở cấp nhóm) |
| 2. Mô tả quy trình | Mô tả bằng lời: bước (Động từ + Danh từ), actor, input/output, gateway, kịch bản thành/bại | Đầy đủ ở mục 4 — bảng bước + actor + ghi chú hệ thống + kịch bản thành công/thất bại cho cả M3, S3, S4, S1 |
| 3. Mô hình hóa BPMN | Mô hình hóa quy trình bằng BPMN 2.0 (pool/lane, gateway, nhiều End, Split & Join cùng loại) | **Đã vẽ** — M3 & S3 (sơ đồ **collaboration** 2 pool trên 1 canvas, nối bằng message flow): `diagrams/bpmn-kho-van-hanh-m3-s3.svg`; S4: `diagrams/bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg`; S1: `diagrams/bpmn-tuyen-dung-nhan-su-s1.svg`. Cả bốn quy trình đều đạt **8 cổng điều kiện** (M3: 2 cặp XOR split–merge + 1 cặp AND split–join + 2 XOR quyết định; S3: 6 XOR + 1 cặp AND; S4: 8 XOR có Split & Join chọn kênh OTP; S1: 8 XOR theo luồng tuyển dụng), đầy đủ **Split & Join cùng loại**, có `.drawio` nguồn đi kèm — xem mục 3–4 |
| 4. Phân tích quy trình | ≥20 câu phỏng vấn (10 định tính + 10 định lượng); VA/BVA/NVA; 4 loại lãng phí; phân tích nguyên nhân gốc; định lượng Thời gian/Chất lượng/Chi phí có công thức + tính toán | M3/S3/S4/S1 đều có bộ câu hỏi 10+10 (mục 6), VA/BVA/NVA + 4 lãng phí + bảng vấn đề–nguyên nhân–khắc phục (mục 8) và **phân tích định lượng đầy đủ 3 nhóm chỉ số có công thức + ví dụ tính toán** (mục 9) |
| 5. Trình bày báo cáo | Theo mẫu khóa luận UIT: mục lục, danh mục hình/bảng, viết tắt, tài liệu tham khảo; không lỗi chính tả | Báo cáo có mục lục và nguồn tham chiếu; danh mục hình/bảng và mục lục tự động sẽ hoàn thiện khi chuyển sang bản Word chính thức |

## 3. Danh mục quy trình phụ trách

| Mã | Cấp | Quy trình | Kích hoạt | Đầu vào chính | Đầu ra chính |
|---|---|---|---|---|---|
| M3 | Quản lý | Lập kế hoạch mua hàng và phân bổ hàng hóa theo mùa | Kỳ kế hoạch mùa hoặc cảnh báo lệch tỷ lệ bán qua/số tháng tồn kho | Báo cáo bán hàng, tồn kho, dự báo, biên lợi nhuận, kế hoạch thương mại | Kế hoạch phân bổ được duyệt, yêu cầu mua/điều chuyển |
| S3 | Hỗ trợ | Kiểm kê và xử lý chênh lệch tồn kho | Lịch kiểm kê hoặc cảnh báo tồn thực tế lệch sổ | Kế hoạch kiểm kê, sổ tồn, danh sách mã hàng/vị trí | Phiếu kiểm kê, đề nghị điều chỉnh, báo cáo hao hụt/chuyển cấp |
| S4 | Hỗ trợ | Đăng ký, xác thực OTP & kích hoạt tài khoản thành viên | Khách hàng đăng ký/đăng nhập trên App/Web hoặc tại Store POS | Số điện thoại, OTP, thông tin định danh | Tài khoản kích hoạt, hồ sơ đồng bộ Salesforce CRM ↔ Magento ↔ Retail Pro Prism |
| S1 | Hỗ trợ | Tuyển dụng & tiếp nhận nhân sự chuỗi bán lẻ/kho vận | Yêu cầu tuyển dụng, CV ứng viên nộp qua ATS đa kênh | Yêu cầu nhân sự, CV, hồ sơ ứng viên | Hợp đồng lao động (sau probation) hoặc thanh lý, gói onboarding (uniform + tài khoản POS/Retail Pro Prism) |

**Luồng liên hệ giữa các quy trình:** kết quả S3 (chênh lệch, hao hụt, nguyên nhân) được phản hồi trực tiếp cho M3 để hiệu chỉnh kế hoạch mùa và hạn mức tồn ở chu kỳ tiếp theo. S4 vận hành ở tuyến khách hàng/tài khoản thành viên: hồ sơ và hạng thẻ do S4 tạo ra là dữ liệu đầu vào cho các quy trình bán hàng đa kênh, gián tiếp cấp nguồn nhu cầu mà M3 lập kế hoạch phân bổ. S1 cấp nguồn lực con người cho toàn chuỗi: nhân sự cửa hàng/kho do S1 tuyển và onboard chính là actor vận hành các bước đếm tồn (S3), bán hàng và hỗ trợ tài khoản (S4); chất lượng và tỷ lệ nghỉ việc (turnover) của S1 tác động trực tiếp tới năng lực thực thi của M3/S3/S4.

## 4. Mô tả quy trình hiện tại (AS-IS)

### 4.1. M3 – Lập kế hoạch mua hàng và phân bổ theo mùa

**Actor kích hoạt:** Hàng hóa/Phân bổ (theo lịch mùa) hoặc hệ thống cảnh báo lệch tỷ lệ bán qua/số tháng tồn kho.
**Actor hưởng lợi:** Vận hành/cửa hàng (nhận đúng cơ cấu hàng) và Tài chính thương mại (kiểm soát ngân sách) trực tiếp; khách hàng cuối (hàng đúng nhu cầu tại cửa hàng) gián tiếp.
**Ranh giới:** từ khi bước vào kỳ kế hoạch/phát hiện lệch mục tiêu → đến khi phát hành kế hoạch mua hàng/yêu cầu điều chuyển. Các bước nhận hàng và điều chuyển nội bộ nằm ngoài phạm vi mô tả của M3 trong bản này.

| # | Actor | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Hàng hóa/Phân bổ | Thu thập dữ liệu bán hàng, tồn kho và dự báo | Hệ thống ERP/báo cáo bán hàng — `C` |
| 2 | Hàng hóa/Phân bổ | Chốt dự báo nhu cầu theo mùa | — |
| 3 | Hàng hóa/Phân bổ | Phân tích tỷ lệ bán qua và số tháng tồn kho | So với mục tiêu theo nhãn hàng/mã hàng |
| 4 | Hàng hóa/Phân bổ | Lập kế hoạch mua hàng và phân bổ theo cửa hàng/nhãn hàng | Đầu ra: bản nháp kế hoạch |
| 5 | Tài chính thương mại | Kiểm tra biên lợi nhuận và ngân sách | Cổng điều kiện |
| 6 | Vận hành | Kiểm tra sức chứa cửa hàng | Cổng điều kiện (chạy song song với Bước 7 qua cặp AND) |
| 7 | Hàng hóa/Phân bổ | Xác nhận nguồn hàng khả dụng | Có thể cần Message Flow tới Pool Chủ thương hiệu — `C` |
| 8 | Hàng hóa/Phân bổ | Trình kế hoạch phân bổ để phê duyệt | Cấp duyệt cụ thể — `C – cần xác thực` |
| 9 | Cấp phê duyệt (`C`) | Phê duyệt kế hoạch phân bổ | Cổng điều kiện |
| 10 | Hàng hóa/Phân bổ | Phát hành kế hoạch mua hàng/yêu cầu điều chuyển | Kèm cổng XOR kiểm tra đồng bộ WMS — kết thúc phạm vi mô tả |
| 11 | Hàng hóa/Phân bổ | Theo dõi kết quả thực hiện và tiếp nhận dữ liệu chênh lệch từ S3 | Đầu vào cho chu kỳ lập kế hoạch tiếp theo |

**Kịch bản thành công:** dữ liệu đầy đủ → dự báo được chốt → tỷ lệ bán qua/số tháng tồn kho xác nhận lệch mục tiêu → kế hoạch nằm trong biên lợi nhuận/ngân sách → (song song) cửa hàng đủ sức chứa **và** hàng nguồn khả dụng → kế hoạch được duyệt ngay lần trình đầu tiên → phát hành lệnh mua và đồng bộ WMS thành công. Trên sơ đồ BPMN, hai bước kiểm tra sức chứa (Bước 6) và xác nhận nguồn hàng (Bước 7) chạy song song qua **cặp cổng AND (split–join)**. **Kết quả:** "Kế hoạch mua hàng và phân bổ đã được duyệt và phát hành."

**Kịch bản thất bại/ngoại lệ:**
- Dữ liệu bán hàng/tồn kho thiếu hoặc chưa khớp nguồn → trả lại Bước 1 để bổ sung trước khi phân tích.
- Nhu cầu vượt biên lợi nhuận/ngân sách (Bước 5) → Tài chính thương mại yêu cầu điều chỉnh kế hoạch (quay lại Bước 4) hoặc từ chối nếu vượt quá nhiều.
- Cửa hàng không đủ sức chứa (Bước 6) → điều chỉnh số lượng phân bổ hoặc giãn lịch giao.
- Hàng nguồn không khả dụng (Bước 7) → ghi nhận thiếu hàng, tìm nguồn thay thế hoặc lùi kế hoạch; có thể phải chuyển cấp nếu ảnh hưởng mùa vụ.
- Kế hoạch không được duyệt (Bước 9) → trả về Bước 4 để chỉnh sửa; nếu lặp lại nhiều lần, chuyển cấp phê duyệt cao hơn — ngưỡng số lần/thời hạn `C – cần xác thực`.
- Sau theo dõi (Bước 11), nếu S3 phát hiện chênh lệch vượt ngưỡng hoặc bộ phận vận hành báo thiếu/dư hàng kéo dài → kích hoạt lập lại kế hoạch ở chu kỳ tiếp theo (không chờ hết mùa).

**Nguồn/trạng thái:** EV02, EV04, EV07; các ngưỡng dự báo, biên lợi nhuận, số tháng tồn kho, cấp/thẩm quyền duyệt cụ thể và số lần lặp trước khi chuyển cấp là `C – cần xác thực`.

### 4.2. S3 – Kiểm kê và xử lý chênh lệch tồn kho

**Actor kích hoạt:** Quản lý/Kiểm soát tồn kho (theo lịch định kỳ) hoặc hệ thống cảnh báo tồn thực tế lệch sổ.
**Actor hưởng lợi:** Hàng hóa/Vận hành (M3) và Kế toán doanh thu/Tài chính (cần dữ liệu tồn chính xác) trực tiếp; cửa hàng (giảm thất thoát) và khách hàng (đúng hàng sẵn có) gián tiếp.
**Ranh giới:** từ lịch kiểm kê/cảnh báo chênh lệch → đến khi đóng hồ sơ và phản hồi cho M3. Các bước điều chuyển/bổ sung tiếp theo nằm ngoài phạm vi mô tả của S3 trong bản này.

| # | Actor | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Quản lý/Kiểm soát tồn kho | Lập lịch kiểm kê | Timer event (định kỳ) hoặc Message event (cảnh báo hệ thống) |
| 2 | Kiểm soát tồn kho/Vận hành | Xác định phạm vi và mẫu đếm | — |
| 3 | Quản lý | Duyệt phạm vi kiểm kê | Cổng điều kiện |
| 4 | Cửa hàng/Kho | Chuẩn bị phiếu kiểm kê | — |
| 5 | Cửa hàng/Kho | Đếm tồn thực tế | — |
| 6 | Kiểm soát tồn kho/Vận hành | Đối chiếu tồn thực tế với sổ tồn | Hệ thống ERP/quản lý kho — `C` |
| 7 | Kiểm soát tồn kho/Vận hành | Xác định điều kiện đếm lại | Cổng điều kiện — nếu có, quay lại Bước 5 |
| 8 | Cửa hàng/Kho | Kiểm tra giao dịch nhập, xuất, điều chuyển, bán hàng, hủy hoặc hàng lỗi | Đối chiếu chứng từ liên quan |
| 9 | Kiểm soát tồn kho/Vận hành | Phân loại nguyên nhân chênh lệch | Cổng điều kiện |
| 10 | Kiểm soát tồn kho/Vận hành | Lập đề nghị điều chỉnh tồn (nếu trong ngưỡng) | Ngưỡng cụ thể — `C` |
| 11 | Kiểm soát tồn kho/Vận hành | Lập báo cáo hao hụt/sự cố và chuyển cấp (nếu vượt ngưỡng/lặp lại) | Nhánh song song với Bước 10 |
| 12 | Quản lý/Kế toán doanh thu | Phê duyệt điều chỉnh hoặc bút toán hao hụt | Cổng điều kiện |
| 13 | Kiểm soát tồn kho/Vận hành | Cập nhật hệ thống tồn kho | — |
| 14 | Kiểm soát tồn kho/Vận hành | Đóng hồ sơ kiểm kê | Cổng điều kiện: đúng hạn? |
| 15 | Kiểm soát tồn kho/Vận hành | Gửi kết quả phản hồi cho M3 | Đầu vào chu kỳ lập kế hoạch tiếp theo |

**Kịch bản thành công:** đến kỳ kiểm kê → phạm vi được duyệt → đếm tồn thực tế khớp sổ ngay lần đầu → hồ sơ được ghi nhận và đóng đúng hạn, không phát sinh điều chỉnh. **Kết quả:** "Kiểm kê khớp sổ, hồ sơ đã đóng đúng hạn." Nếu có chênh lệch nhưng trong ngưỡng: xác định đúng nguyên nhân ở lần đếm lại đầu tiên → đề nghị điều chỉnh được phê duyệt → hệ thống cập nhật → hồ sơ đóng đúng hạn → kết quả phản hồi cho M3.

**Kịch bản thất bại/ngoại lệ:**
- Đếm tồn thực tế không khớp sổ (Bước 6) và điều kiện đếm lại được kích hoạt (Bước 7) → quay lại đếm lại; nếu đếm lại vẫn lệch, chuyển sang xác định nguyên nhân sâu hơn.
- Không xác định được nguyên nhân trong thời hạn quy định (Bước 9) → vẫn phải lập báo cáo tạm với nhãn "nguyên nhân chưa xác định", có thể phải chuyển cấp sớm hơn quy trình thông thường.
- Chênh lệch vượt ngưỡng điều chỉnh, lặp lại nhiều kỳ hoặc có dấu hiệu hao hụt/mất mát (Bước 11) → lập báo cáo sự cố/hao hụt riêng, chuyển cấp cho Quản lý/Kế toán xác minh trách nhiệm bồi hoàn — ngưỡng, cấp chuyển và trách nhiệm cụ thể là `C – cần xác thực`.
- Điều chỉnh hoặc bút toán không được phê duyệt (Bước 12) → yêu cầu bổ sung bằng chứng/giải trình, quay lại Bước 9.
- Hồ sơ không đóng đúng hạn (Bước 14) → gắn cờ quá hạn, báo cáo cho Quản lý; hồ sơ vẫn phải đóng sau khi bổ sung đủ bằng chứng.

**Nguồn/trạng thái:** EV03, EV05, EV08; lịch kiểm kê, ngưỡng điều chỉnh, thời hạn xác định nguyên nhân, trách nhiệm bồi hoàn và cấp chuyển là `C – cần xác thực`.

### 4.3. S4 – Đăng ký, xác thực OTP & kích hoạt tài khoản thành viên

**Actor kích hoạt:** Khách hàng truy cập App/Web ACFC (hoặc Store POS) để đăng ký/đăng nhập.
**Actor hưởng lợi:** Khách hàng (mua sắm, tích điểm, ưu đãi hạng thẻ) trực tiếp; ACFC (dữ liệu khách hàng, kênh bán trực tuyến) và CSKH (giảm tải hỗ trợ nếu tự phục vụ trơn tru) gián tiếp.
**Ranh giới:** từ khi khách truy cập App/Web → đến khi tài khoản được tạo/kích hoạt hoặc chuyển CSKH. Không xử lý yêu cầu quyền dữ liệu cá nhân của chủ thể dữ liệu.

**Bối cảnh chương trình thành viên (ACFC Member):** tài khoản kích hoạt bởi S4 là cửa ngõ vào chương trình khách hàng thân thiết 5 bậc — **Member → Silver → Gold → Platinum → Diamond** (ưu đãi 5–10% theo hạng, ưu đãi sinh nhật 20–30%), tích điểm lũy tiến theo hạng (100.000đ = 1 điểm với Member/Silver, tăng dần tới 10 điểm với Diamond; 1 điểm = 1.000đ khi đổi thưởng, áp dụng từ hạng Gold, giảm tối đa 50% giá trị hóa đơn). Hệ thống được quản trị tập trung qua **Salesforce CRM** kết hợp POS **Retail Pro Prism** và **Adobe Magento Commerce**. *(Chi tiết bậc hạng/tỷ lệ điểm theo chính sách công khai — mức A; các định mức chi tiêu cụ thể lên hạng là `C – cần xác thực`.)*

| # | Actor | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Khách hàng | Truy cập App/Web, đồng ý PDPA và nhập số điện thoại | Cổng điều kiện G1: đồng ý PDPA? |
| 2 | Salesforce CRM | Kiểm tra trùng lặp số điện thoại (duplicate profile check) | Cổng điều kiện G2: số điện thoại đã tồn tại? |
| 3 | Cổng ĐK (Frontend) | Khởi tạo hồ sơ tạm trên CRM, gộp dữ liệu Legacy nếu có | — |
| 4 | OTP Gateway | Gửi OTP qua Zalo ZNS (chính) hoặc SMS (fallback) | Thời hạn hiệu lực OTP — `C` |
| 5 | Hệ thống | Kiểm tra trạng thái cổng gửi OTP | Cổng điều kiện G4 |
| 6 | Call Center | Xác minh thủ công qua CSKH 1900 3038 (khi cổng OTP lỗi) | Nhánh ngoại lệ |
| 7 | Sự kiện Timer | Chờ khách nhập OTP ≤ 120s | Timer event |
| 8 | Khách hàng | Nhập mã xác thực OTP | — |
| 9 | Hệ thống | Kiểm tra số lần nhập sai OTP (retry limit) | Cổng điều kiện G6: sai ≥ 3 lần? |
| 10 | Khách hàng | Điền thông tin cá nhân và tạo mật khẩu | Cổng điều kiện G7: mật khẩu đạt chuẩn + đồng ý điều khoản? |
| 11 | Salesforce CRM | Tạo User và cấp Member ID | — |
| 12 | Hệ thống tích hợp | Đồng bộ hồ sơ sang Magento (Web/App) và Retail Pro Prism (POS) | Cổng điều kiện G8: đồng bộ thành công? |
| 13 | Hệ thống | Kích hoạt tài khoản: Auto-login + Voucher 100k + Auto tier upgrade | Kết thúc thành công |

**Kịch bản thành công:** đồng ý PDPA → số điện thoại chưa tồn tại → OTP gửi qua Zalo ZNS thành công → khách nhập đúng OTP trong 120s → mật khẩu đạt chuẩn + đồng ý điều khoản → tạo Member ID → đồng bộ Magento + Retail Pro thành công → kích hoạt tài khoản kèm ưu đãi. **Kết quả:** "Tài khoản được tạo và kích hoạt thành công."

**Kịch bản thất bại/ngoại lệ:**
- Không đồng ý PDPA (G1) → hủy đăng ký.
- Số điện thoại đã tồn tại (G2) → điều hướng sang đăng nhập/lấy lại mật khẩu.
- Cổng OTP lỗi (G4) → CSKH xác minh thủ công qua hotline 1900 3038.
- Nhập sai OTP ≥ 3 lần (G6) → khóa 24h, chuyển CSKH; ngưỡng số lần thử `C – cần xác thực`.
- Mật khẩu chưa đạt chuẩn/chưa đồng ý điều khoản (G7) → quay lại điền thông tin.
- Đồng bộ Magento/Retail Pro thất bại (G8) → đưa vào hàng đợi retry và cảnh báo DevOps.

**Cấu trúc BPMN (Hình S4):** 1 Pool "Hệ sinh thái ACFC Member" – 5 Lane (Khách hàng, Cổng ĐK Frontend, Salesforce CRM, OTP Gateway ZNS/SMS, CSKH & Đồng bộ), **8 cổng điều kiện XOR**, **1 sự kiện trung gian Timer** (chờ OTP ≤ 120s) và **4 sự kiện Kết thúc** (Hủy đăng ký / Điều hướng đăng nhập / Khóa 24h→CSKH / Kích hoạt xong).

**Danh sách 8 cổng điều kiện (Gateways) – đồng bộ với Hình S4:**

1. **XOR G1 – Đồng ý PDPA?** Khách có đồng ý chính sách bảo mật dữ liệu PDPA (Nghị định 13/2023/NĐ-CP) không? *(Không → End: Hủy đăng ký.)*
2. **XOR G2 – SĐT đã tồn tại?** Số điện thoại đã có hồ sơ trên Salesforce CRM chưa (duplicate profile check)? *(Có → End: Điều hướng đăng nhập.)*
3. **XOR G3 – Kênh gửi OTP (Zalo ZNS ↔ SMS)?** Đây là **cổng Split (XOR)** chọn **một** kênh; hai nhánh **hợp lại tại cổng Join – gộp kênh (XOR merge)** trước khi kiểm tra cổng OTP (Split và Join **cùng loại XOR** để tránh deadlock).
4. **XOR G4 – Cổng OTP lỗi?** Cổng gửi OTP có lỗi không (→ CSKH 1900 3038 xác minh thủ công); nếu không → sự kiện Timer *Chờ OTP ≤ 120s*.
5. **XOR G5 – OTP hợp lệ?** Mã OTP khách nhập có hợp lệ và còn hiệu lực (trong 120s) không?
6. **XOR G6 – Sai ≥ 3 lần?** Số lần nhập sai OTP có vượt giới hạn không? *(Có → End: Khóa 24h → CSKH; Chưa → nhập lại.)*
7. **XOR G7 – MK chuẩn & đồng ý ĐK?** Mật khẩu đạt chuẩn an toàn và khách đồng ý điều khoản không? *(Không → quay lại điền thông tin.)*
8. **XOR G8 – Đồng bộ Magento + Retail Pro?** Đồng bộ hồ sơ sang Magento và Retail Pro Prism có thành công không? *(Không → hàng đợi retry & cảnh báo DevOps; Có → End: Kích hoạt xong + Auto tier upgrade.)*

**Nguồn/trạng thái:** EV09, EV10; thời hạn hiệu lực OTP, kênh gửi mật khẩu tạm, ngưỡng khóa tài khoản, chủ quy trình nội bộ và thời gian xử lý CSKH là `C – cần xác thực`.

### 4.4. S1 – Tuyển dụng & tiếp nhận nhân sự chuỗi bán lẻ/kho vận

**Actor kích hoạt:** Phòng Nhân sự (HR Dept) khi có yêu cầu tuyển dụng từ cửa hàng/kho/khối văn phòng.
**Actor hưởng lợi:** Cửa hàng/Kho/Khối HQ (được bổ sung nhân sự đúng chuẩn) trực tiếp; toàn chuỗi vận hành (M3/S3/S4 có người thực thi) và ứng viên (có việc làm, được onboard) gián tiếp.
**Ranh giới:** từ khi phát sinh yêu cầu tuyển dụng và đăng tin → đến khi ký hợp đồng lao động sau thử việc (hoặc thanh lý nếu không đạt). Không bao gồm quản trị lương thưởng, đào tạo dài hạn hay đánh giá hiệu suất sau khi đã ký hợp đồng chính thức.

**Phân nhóm đối tượng:** **Store staff** (nhân viên cửa hàng — tuyển số lượng lớn/volume hiring, đặc thù bán lẻ, turnover ~25% `C`) và **HQ/Warehouse staff** (nhân viên văn phòng/kho vận — yêu cầu chuyên môn cao/specialized). Kênh thu hút ứng viên: `tuyendung.acfc.com.vn`, TopCV, LinkedIn, VietnamWorks và các hội nhóm Facebook.

| # | Actor | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | HR Dept | Đăng tải tin tuyển dụng | Cổng G1: vị trí thuộc Store staff (volume) hay HQ/Warehouse (specialized)? |
| 2 | ATS System | Sàng lọc hồ sơ qua ATS (ATS screening) | Đầu vào CV đa kênh — Cổng G2: ứng viên có fashion retail experience (→ Fast-track)? |
| 3 | HR Recruiter | Kiểm tra lý lịch (background check) | NDA/Non-compete cho HQ-Warehouse, Criminal record cho Store — Cổng G3: đạt chuẩn? |
| 4 | Line Manager | Phỏng vấn vòng 1 (V1) | Cổng G4: đạt V1? |
| 5 | HR Director/Ban GĐ | Phỏng vấn chuyên sâu vòng 2 & 3 (Senior) | Cổng G5: đạt V2/V3? |
| 6 | HR Dept | Đàm phán và chốt thư mời (Offer Letter) | Cổng G6: ứng viên chấp nhận offer? (Yes/Negotiate/Decline) |
| 7 | HR/Y tế | Khám sức khỏe trước tuyển dụng (health check) | Cổng G7: đạt khám sức khỏe theo luật định? |
| 8 | HR & IT Dept | Triển khai onboarding | Cấp Brand uniform, đào tạo product knowledge, tạo tài khoản POS/Retail Pro Prism |
| 9 | Line Manager | Đánh giá thử việc 2 tháng (probation review) | KPI: Sales target + Customer satisfaction |
| 10 | HR Dept | Xem xét và ký hợp đồng lao động | Cổng G8: đạt KPI probation? (Đạt → ký HĐ; Không → thanh lý) |

**Kịch bản thành công:** yêu cầu tuyển dụng rõ ràng → ATS lọc được hồ sơ phù hợp (ứng viên có kinh nghiệm bán lẻ → Fast-track) → background check đạt → vượt phỏng vấn V1 và V2/V3 → chấp nhận offer → đạt khám sức khỏe → onboarding đầy đủ → đạt KPI probation 2 tháng → ký hợp đồng chính thức. **Kết quả:** "Tuyển được nhân sự phù hợp và ký hợp đồng sau thử việc."

**Kịch bản thất bại/ngoại lệ:**
- Không có hồ sơ đạt qua ATS (G2) → đăng lại tin/mở rộng kênh tuyển.
- Background check không đạt (G3) → loại ứng viên, tránh rủi ro pháp lý/an ninh.
- Trượt phỏng vấn V1 hoặc V2/V3 (G4/G5) → loại hoặc lưu hồ sơ cho vị trí khác.
- Ứng viên từ chối/không chốt được offer (G6) → đàm phán lại hoặc chuyển ứng viên dự phòng.
- Không đạt khám sức khỏe theo luật định (G7) → dừng tiếp nhận.
- Không đạt KPI probation (G8) → thanh lý hợp đồng thử việc, Exit interview; nếu turnover cao kéo dài → phản hồi lại khâu tuyển chọn/onboarding. Ngưỡng KPI, thời hạn từng vòng và cấp duyệt cụ thể là `C – cần xác thực`.

**Nguồn/trạng thái:** EV13, EV14; turnover ~25%, ngưỡng KPI probation, số vòng phỏng vấn theo cấp bậc, thời hạn từng bước và tiêu chí background check cụ thể là `C – cần xác thực`.

## 5. Phương pháp thu thập và xác thực

Nguyên tắc bằng chứng theo 3 mức A/B/C như mục 1.3. Mỗi hoạt động, gateway và KPI đều ghi mã nguồn hoặc nhãn `C – cần xác thực`; không điền số ACFC nếu chưa có nguồn hoặc người có thẩm quyền xác nhận.

**Nhật ký bằng chứng (EV01–EV10):**

| Mã | Nguồn | Nội dung hỗ trợ | Mức | Áp dụng |
|---|---|---|---|---|
| EV01 | [ACFC Home](https://www.acfc.com.vn/home) | ACFC là nhà phân phối chính hãng nhiều thương hiệu, vận hành hệ thống cửa hàng/kênh mua sắm | A | Nền |
| EV02 | [Senior Product Executive](https://tuyendung.acfc.com.vn/job/detail?id=648) | Lập kế hoạch phân bổ hàng; nhận thông tin lô; theo dõi lịch đến; lập danh sách điều chuyển/bổ sung; xử lý giao trễ/mất/lỗi | B | M3 |
| EV03 | [Operations Executive](https://tuyendung.acfc.com.vn/job/detail?id=341) | Quản lý hàng trong kho; theo dõi kế hoạch điều chuyển; kiểm soát tồn; phối hợp nhận/giao sản phẩm | B | S3 |
| EV04 | [District Supervisor](https://tuyendung.acfc.com.vn/job/detail?id=318) | Theo dõi tồn, đề xuất bổ sung hoặc hợp nhất kho theo kế hoạch và hiệu suất | B | M3 |
| EV05 | [Store Manager – Nike](https://tuyendung.acfc.com.vn/job/detail?id=631) | Kiểm đếm hàng ngày/tuần/tháng; nhập/xuất hàng trong chuỗi; báo cáo bán chậm/bán chạy | B | S3 |
| EV06 | [Khai trương kho ACFC](https://tuyendung.acfc.com.vn/news/acfc-warehouse-opening-post73) | Bối cảnh vận hành kho và dòng nhận hàng | B | Nền |
| EV07 | [Product Manager](https://tuyendung.acfc.com.vn/job/detail?id=333) | Lập kế hoạch mua, dự báo, theo dõi bán hàng/tồn kho và kế hoạch tồn | B | M3 |
| EV08 | [Revenue Accountant](https://tuyendung.acfc.com.vn/job/detail?id=267) | Theo dõi tồn kho trực tuyến, đối soát doanh thu/hóa đơn và báo cáo | B | S3 |
| EV09 | [Hướng dẫn tạo tài khoản – ACFC](https://www.acfc.com.vn/huong-dan-tao-tai-khoan) | Các bước đăng ký: nhập số điện thoại, nhận/xác nhận OTP, điền thông tin cá nhân, hoàn tất đăng ký | A | S4 |
| EV10 | [Hướng dẫn kích hoạt tài khoản thành viên – ACFC](https://www.acfc.com.vn/huong-dan-kich-hoat-tai-khoan-thanh-vien) | Các bước đăng nhập/kích hoạt tài khoản đã đăng ký, xử lý quên mật khẩu, truy cập thông tin thành viên | A | S4 |
| EV13 | [Trang tuyển dụng ACFC](https://tuyendung.acfc.com.vn) | Danh sách vị trí tuyển dụng Store và HQ/Warehouse, mô tả công việc và yêu cầu | A | S1 |
| EV14 | TopCV, LinkedIn, VietnamWorks | Các kênh đăng tuyển đa nền tảng và bước sàng lọc hồ sơ (ATS screening) | B | S1 |

**Đối tượng ưu tiên phỏng vấn và mục tiêu xác thực:**

| Quy trình | Đối tượng ưu tiên | Mục tiêu xác thực |
|---|---|---|
| M3 | Hàng hóa/Phân bổ, Quản lý nhãn hàng, Tài chính thương mại, Vận hành | Dự báo, số tháng tồn kho, tỷ lệ bán qua, biên lợi nhuận, cấp duyệt và kế hoạch phân bổ |
| S3 | Quản lý cửa hàng, Kiểm soát tồn kho/Vận hành, Kế toán doanh thu/Tài chính | Chu kỳ kiểm kê, đếm lại, ngưỡng điều chỉnh, hao hụt, phê duyệt và tuổi chênh lệch |
| S4 | Digital/E-commerce, CSKH, IT vận hành website/app, Marketing khách hàng thành viên | Luồng đăng ký/kích hoạt, OTP, tỷ lệ bỏ dở, xử lý lỗi đăng nhập, khối lượng và chi phí hỗ trợ CSKH |
| S1 | HR tuyển dụng, Line Manager cửa hàng/kho, HR Director, IT onboarding | Kênh tuyển, bước ATS, số vòng phỏng vấn, tỷ lệ đạt/loại mỗi vòng, time-to-hire, cost-per-hire, turnover và tỷ lệ đạt probation |

**Quy tắc tổng hợp:** ghi nguyên ý câu trả lời, nguồn và thời điểm phỏng vấn; phân loại `Đã xác nhận` / `Xác nhận một phần` / `Giả định` / `Bác bỏ`; cập nhật lại AS-IS, phân tích và BPMN; gửi lại chủ quy trình xác nhận trước khi đưa vào báo cáo chung. Nếu không tiếp cận được nhân sự ACFC, giữ trạng thái `C – giả định cần xác thực` và **không dùng số minh họa như số thật**.

## 6. Bộ câu hỏi thu thập dữ liệu

Mỗi quy trình có **10 câu định tính + 10 câu định lượng** (đủ ≥20 câu theo rubric tiêu chí 4). Câu định lượng ánh xạ trực tiếp tới các KPI ở mục 9 để thay số minh họa bằng số thật sau phỏng vấn.

### 6.1. M3 – Lập kế hoạch mua hàng và phân bổ theo mùa

**Định tính:** (1) Dữ liệu tỷ lệ bán qua/số tháng tồn kho được chốt ở thời điểm nào? (2) Dự báo do ai lập và ai kiểm tra? (3) Mã hàng/cửa hàng được xếp hạng theo tiêu chí nào? (4) Biên lợi nhuận và ngân sách được kiểm tra ở bước nào? (5) Thiếu hoặc dư hàng được xử lý thế nào? (6) Ai duyệt phân bổ và điều kiện duyệt là gì? (7) Khi nào phải lập lại kế hoạch? (8) Kết quả S3 được phản hồi vào kế hoạch ra sao? (9) Kế hoạch được lưu trên hệ thống nào? (10) Điểm nghẽn lớn nhất là gì?

**Định lượng:** (1) Độ chính xác dự báo là bao nhiêu phần trăm? (2) Tỷ lệ bán qua được tính theo công thức và kỳ nào? (3) Số tháng tồn kho bình quân là bao nhiêu? (4) Mỗi kỳ có bao nhiêu mã hàng/cửa hàng? (5) Thời gian lập kế hoạch là bao lâu? (6) Thời gian phê duyệt là bao lâu? (7) Tỷ lệ phân bổ thay đổi là bao nhiêu phần trăm? (8) Tỷ lệ giảm giá xả hàng là bao nhiêu phần trăm? (9) Tỷ lệ hết hàng/dư hàng là bao nhiêu phần trăm? (10) Chi phí lập lại kế hoạch là bao nhiêu?

### 6.2. S3 – Kiểm kê và xử lý chênh lệch tồn kho

**Định tính:** (1) Kích hoạt kiểm kê là lịch hay cảnh báo? (2) Phạm vi và mẫu đếm được xác định thế nào? (3) Tồn thực tế/sổ được so sánh trên hệ thống nào? (4) Điều kiện nào bắt buộc đếm lại? (5) Ngưỡng điều chỉnh là bao nhiêu và ai đặt ngưỡng? (6) Nguyên nhân chênh lệch được xác định bằng cách nào? (7) Hồ sơ bồi hoàn/thất thoát gồm những gì? (8) Cấp nào phê duyệt điều chỉnh? (9) Vụ việc được đóng theo điều kiện nào? (10) Kết quả được dùng cho M3 ra sao?

**Định lượng:** (1) Có bao nhiêu đợt kiểm kê mỗi tháng? (2) Độ chính xác tồn kho là bao nhiêu phần trăm? (3) Hao hụt là bao nhiêu phần trăm hoặc giá trị? (4) Thời gian kiểm kê trung bình là bao lâu? (5) Tỷ lệ đếm lại là bao nhiêu phần trăm? (6) Tỷ lệ điều chỉnh là bao nhiêu phần trăm? (7) Có bao nhiêu vụ quá hạn? (8) Tuổi chênh lệch trung bình là bao nhiêu ngày? (9) Chi phí mỗi đợt kiểm kê là bao nhiêu? (10) Tỷ lệ đóng đúng hạn là bao nhiêu phần trăm?

### 6.3. S4 – Đăng ký và kích hoạt tài khoản thành viên

**Định tính:** (1) Khách hàng bắt đầu đăng ký từ những kênh nào (website, app, tại quầy)? (2) Những thông tin bắt buộc để tạo tài khoản gồm những gì? (3) OTP được gửi qua kênh nào và hiệu lực bao lâu? (4) Khi OTP sai/hết hạn thì luồng xử lý ra sao (nhập lại hay đăng ký lại từ đầu)? (5) Số điện thoại đã tồn tại được xử lý và thông báo thế nào? (6) Khách quên mật khẩu được cấp lại theo cách nào? (7) Khi nào một yêu cầu được chuyển sang CSKH? (8) CSKH hỗ trợ qua những kênh nào và có đầu mối tập trung không? (9) Quyền lợi thành viên được kích hoạt ngay khi tạo tài khoản hay sau bước nào? (10) Điểm nghẽn lớn nhất khiến khách bỏ dở đăng ký là gì?

**Định lượng:** (1) Tỷ lệ đăng ký thành công là bao nhiêu phần trăm? (2) Tỷ lệ bỏ dở đăng ký là bao nhiêu phần trăm? (3) Thời gian hoàn tất đăng ký trung bình là bao lâu? (4) Thời gian chờ nhận OTP trung bình là bao lâu? (5) Tỷ lệ OTP xác nhận đúng lần đầu là bao nhiêu phần trăm? (6) Tỷ lệ quên mật khẩu trên tổng lượt đăng nhập là bao nhiêu? (7) Tỷ lệ khách cần CSKH hỗ trợ hoàn tất đăng ký/kích hoạt là bao nhiêu? (8) Mỗi ngày/tháng có bao nhiêu lượt đăng ký mới? (9) Chi phí gửi OTP (đơn giá SMS × số lượt) là bao nhiêu? (10) Chi phí xử lý mỗi yêu cầu CSKH liên quan tài khoản là bao nhiêu?

### 6.4. S1 – Tuyển dụng & tiếp nhận nhân sự

**Định tính:** (1) Yêu cầu tuyển dụng phát sinh và được phê duyệt như thế nào? (2) Store staff và HQ/Warehouse staff khác nhau ra sao về kênh tuyển và tiêu chí? (3) ATS sàng lọc hồ sơ theo tiêu chí nào và ai cấu hình? (4) Điều kiện nào để một ứng viên vào luồng Fast-track? (5) Background check gồm những kiểm tra gì cho từng nhóm vị trí? (6) Có bao nhiêu vòng phỏng vấn và ai tham gia mỗi vòng theo cấp bậc? (7) Offer được đàm phán và chốt theo quy tắc nào? (8) Onboarding gồm những hạng mục gì (uniform, đào tạo, cấp tài khoản POS)? (9) KPI probation 2 tháng được đo bằng gì và ai đánh giá? (10) Nguyên nhân turnover cao nhất ở nhóm nào và được xử lý ra sao?

**Định lượng:** (1) Time-to-hire trung bình (từ đăng tin đến ký offer) là bao nhiêu ngày? (2) Mỗi vị trí nhận trung bình bao nhiêu hồ sơ? (3) Tỷ lệ hồ sơ vượt qua sàng lọc ATS là bao nhiêu phần trăm? (4) Tỷ lệ đạt ở mỗi vòng phỏng vấn (V1, V2/V3) là bao nhiêu? (5) Tỷ lệ ứng viên chấp nhận offer (offer acceptance rate) là bao nhiêu? (6) Tỷ lệ đạt khám sức khỏe là bao nhiêu phần trăm? (7) Tỷ lệ vượt qua probation 2 tháng là bao nhiêu? (8) Turnover rate của Store staff và HQ/Warehouse là bao nhiêu phần trăm/năm? (9) Cost-per-hire trung bình (chi phí tuyển trên mỗi nhân sự) là bao nhiêu? (10) Mỗi tháng tuyển được bao nhiêu nhân sự mới trên tổng nhu cầu (fill rate)?

## 7. Kế hoạch làm việc (mốc cá nhân)

| Giai đoạn | Thời gian | Nội dung |
|---|---|---|
| Khóa phạm vi/bằng chứng | 06–09/08 | Rà soát bằng chứng, chốt phạm vi M3/S3/S4 |
| Hoàn thiện AS-IS + phân tích | 10–13/08 | Hoàn thiện discovery, AS-IS, phân tích M3/S3/S4; hoàn thành bản nháp báo cáo cá nhân |
| Xác thực + BPMN | 14–17/08 | Đã vẽ BPMN M3/S3/S4/S1 (`diagrams/`); gộp toàn bộ discovery + AS-IS + phân tích của cả bốn quy trình vào một báo cáo tổng; còn lại: phỏng vấn xác thực (nếu tiếp cận được nhân sự ACFC), cập nhật gateway/số liệu thật và TO-BE |

## 8. Phân tích định tính

### 8.1. VA/BVA/NVA – M3

| Hoạt động | Phân loại | Lý do/khắc phục |
|---|---|---|
| Thu thập dữ liệu bán hàng, tồn kho và dự báo | BVA | Cần cho quyết định; dùng một bộ dữ liệu chuẩn |
| Phân tích tỷ lệ bán và số tháng tồn kho | BVA | Hỗ trợ lập kế hoạch; tự động hóa bảng theo dõi |
| Lập kế hoạch phân bổ | VA | Tạo cơ cấu hàng phù hợp nhu cầu cửa hàng |
| Kiểm tra biên lợi nhuận/ngân sách | BVA | Kiểm soát tài chính; đặt quy tắc tự động |
| Chờ dữ liệu hoặc phê duyệt | NVA | Chờ (Hold); đặt thời hạn và cảnh báo quá hạn |
| Nhập lại cùng một báo cáo | NVA | Xử lý dư (Over-processing); dùng một nguồn dữ liệu gốc |
| Lập lại kế hoạch do dữ liệu sai | NVA | Lỗi (Defects); kiểm tra bắt buộc trước khi gửi |

### 8.2. VA/BVA/NVA – S3

| Hoạt động | Phân loại | Lý do/khắc phục |
|---|---|---|
| Lập kế hoạch kiểm kê | BVA | Kiểm soát tài sản và độ chính xác dữ liệu |
| Đếm tồn thực tế | BVA | Bằng chứng tồn thực tế |
| So sánh với sổ tồn | BVA | Phát hiện sai lệch |
| Đếm lại khi có chênh lệch | BVA | Cần xác minh trước điều chỉnh |
| Điều chỉnh tồn được phê duyệt | BVA | Cần cho sổ sách và quản trị rủi ro |
| Chờ phê duyệt hoặc bằng chứng | NVA | Chờ (Hold); đặt thời hạn và chuyển cấp |
| Đếm lại do bàn giao không đủ | NVA | Lỗi (Defects); chuẩn hóa biên bản và quét mã |
| Nhập cùng điều chỉnh ở nhiều nơi | NVA | Xử lý dư (Over-processing); dùng một hồ sơ điều chỉnh |

### 8.3. VA/BVA/NVA – S4

| Hoạt động | Phân loại | Lý do/khắc phục |
|---|---|---|
| Nhập số điện thoại/thông tin cá nhân | BVA | Cần để tạo hồ sơ khách hàng và định danh tài khoản |
| Nhận và xác nhận mã OTP | BVA | Xác thực bảo mật trước khi tạo tài khoản |
| Tạo và kích hoạt tài khoản | VA | Giá trị trực tiếp — khách hàng mua sắm và hưởng ưu đãi thành viên |
| Đăng nhập bằng mật khẩu đã lưu | VA | Truy cập ngay quyền lợi thành viên |
| Chờ nhận OTP/mật khẩu tạm | NVA | Chờ (Hold); rút ngắn thời gian gửi và có kênh dự phòng |
| Nhập lại OTP do sai/hết hạn | NVA | Lỗi (Defects); cho gửi lại OTP không cần nhập lại toàn bộ thông tin |
| Đăng ký lại từ đầu khi OTP hết hạn | NVA | Xử lý dư (Over-processing); lưu tạm dữ liệu đã nhập trong phiên |
| Liên hệ CSKH qua nhiều kênh không đầu mối rõ | NVA | Di chuyển (Move); hợp nhất kênh hỗ trợ ngay trên trang đăng ký/đăng nhập |

### 8.4. VA/BVA/NVA – S1

| Hoạt động | Phân loại | Lý do/khắc phục |
|---|---|---|
| Đăng tin và sàng lọc ATS | BVA | Cần để lọc hồ sơ đạt chuẩn; tối ưu tiêu chí lọc để giảm sót ứng viên tốt |
| Phỏng vấn V1 và V2/V3 | VA | Trực tiếp chọn đúng người phù hợp vị trí |
| Background check/khám sức khỏe | BVA | Tuân thủ pháp lý và kiểm soát rủi ro |
| Onboarding (uniform, đào tạo, cấp tài khoản) | VA | Biến ứng viên thành nhân sự vận hành được ngay |
| Chờ phản hồi giữa các vòng phỏng vấn | NVA | Chờ (Hold); đặt SLA phản hồi cho từng vòng |
| Ứng viên/HR trao đổi offer qua nhiều kênh rời rạc | NVA | Di chuyển (Move); tập trung liên lạc trên một hệ ATS/email chuẩn |
| Nhập lại thông tin ứng viên ở nhiều biểu mẫu | NVA | Xử lý dư (Over-processing); dùng một hồ sơ ứng viên xuyên suốt ATS |
| Tuyển lại do nghỉ việc sớm (turnover cao) | NVA | Lỗi (Defects); cải thiện chọn lọc và onboarding để giảm nghỉ việc |

### 8.5. Bốn loại lãng phí (Move – Hold – Over-processing – Defects)

| Loại | M3 | S3 | S4 | S1 |
|---|---|---|---|---|
| Di chuyển (Move) | Chuyển tệp qua nhiều kênh → một nơi lưu trữ, một mã kế hoạch | Chuyển phiếu/biên bản qua nhiều đầu mối → hồ sơ điện tử, một mã vụ việc | Khách tự tìm hotline/fanpage/Zalo/email khi lỗi → nút hỗ trợ/chatbot ngay trên trang đăng ký/đăng nhập | Trao đổi offer/hồ sơ qua nhiều kênh rời rạc → tập trung trên một hệ ATS |
| Chờ (Hold) | Chờ báo cáo/ngân sách/phê duyệt → thời hạn, người phụ trách, cảnh báo | Chờ đếm lại/giải trình/duyệt → thời hạn, hàng đợi quá hạn, người phụ trách | Chờ nhận OTP/mật khẩu tạm → rút ngắn thời gian gửi, thêm kênh dự phòng, đếm ngược hiệu lực | Chờ phản hồi giữa các vòng phỏng vấn → SLA phản hồi từng vòng, cảnh báo quá hạn |
| Xử lý dư (Over-processing) | Nhập/đối chiếu trùng dữ liệu → bảng theo dõi, quy tắc tự động | Đếm/nhập/đối chiếu trùng → kiểm kê theo rủi ro, dùng dữ liệu gốc | Nhập lại toàn bộ thông tin khi OTP hết hạn → lưu tạm dữ liệu phiên, chỉ gửi lại OTP | Nhập lại thông tin ứng viên ở nhiều biểu mẫu → một hồ sơ ứng viên xuyên suốt |
| Lỗi (Defects) | Dự báo/mã hàng sai → kiểm tra dữ liệu gốc, khóa phiên bản | Chênh lệch lặp lại, thiếu bằng chứng, sai giao dịch → mã vạch, nhật ký kiểm tra, mã nguyên nhân | OTP sai/hết hạn, SĐT đã tồn tại không có thông báo rõ → thông báo lỗi cụ thể kèm hướng dẫn bước tiếp theo | Tuyển lại do nghỉ việc sớm/turnover cao → cải thiện chọn lọc và onboarding |

### 8.6. Phân tích nguyên nhân gốc (Vấn đề – Nguyên nhân – Khắc phục)

| Quy trình | Vấn đề cần kiểm chứng | Nguyên nhân giả định | Khắc phục đề xuất |
|---|---|---|---|
| M3 | Kế hoạch phải lập lại | Dữ liệu dự báo/tồn/gốc chưa đồng nhất | Khóa phiên bản, kiểm tra trước khi gửi, ghi rõ người phụ trách |
| M3 | Phê duyệt chậm | Thiếu thời hạn và tiêu chí duyệt thống nhất | Thiết lập hạn duyệt, hàng đợi quá hạn, chuyển cấp |
| M3 | Phân bổ lệch nhu cầu | Số tháng tồn, tỷ lệ bán, sức chứa chưa đồng bộ | Bảng theo dõi chung, quy tắc phân bổ cần xác thực |
| S3 | Độ chính xác tồn kho giảm | Giao dịch chưa cập nhật hoặc đếm sai | Khóa thời điểm kiểm kê, quét mã, đối chiếu sổ trước điều chỉnh |
| S3 | Chênh lệch quá hạn | Đếm lại/giải trình/phê duyệt bị chờ | Đặt thời hạn, hàng đợi quá hạn, chuyển cấp theo rủi ro |
| S3 | Điều chỉnh lặp lại | Chưa phân loại nguyên nhân gốc | Mã nguyên nhân, nhật ký kiểm tra, phản hồi về M3 |
| S4 | Tỷ lệ bỏ dở đăng ký cao | OTP đến chậm/hết hạn, phải nhập lại toàn bộ thông tin | Lưu tạm dữ liệu phiên, điều chỉnh hợp lý thời gian hiệu lực OTP theo dữ liệu thực |
| S4 | Khách không tự xử lý được lỗi đăng nhập | Thông báo lỗi chung chung, thiếu hướng dẫn bước kế tiếp | Chuẩn hóa thông báo lỗi theo từng nguyên nhân (OTP sai, SĐT đã tồn tại, tài khoản khóa) |
| S4 | Khối lượng yêu cầu CSKH về tài khoản tăng | Thiếu kênh tự phục vụ rõ ràng trên trang đăng ký/đăng nhập | Tích hợp chatbot/hướng dẫn tự khắc phục tại bước phát sinh lỗi trước khi chuyển CSKH |
| S1 | Thời gian tuyển (time-to-hire) kéo dài | Chờ phản hồi giữa các vòng phỏng vấn, thiếu SLA từng vòng | Đặt SLA phản hồi cho mỗi vòng, hàng đợi ứng viên quá hạn, nhắc tự động |
| S1 | Ứng viên từ chối offer / nhận việc rồi bỏ | Quy trình phỏng vấn dài, trao đổi offer rời rạc, chậm ra quyết định | Rút gọn vòng cho vị trí cửa hàng (fast-track), tập trung trao đổi offer trên một hệ ATS |
| S1 | Nghỉ việc sớm (turnover cao ở nhân sự cửa hàng) | Chọn lọc chưa sát yêu cầu vị trí, onboarding chưa đủ | Chuẩn hóa tiêu chí sàng lọc theo vị trí, hoàn thiện onboarding (uniform, đào tạo, cấp tài khoản POS) |

## 9. Phân tích định lượng (Thời gian – Chất lượng – Chi phí)

Rubric yêu cầu **tính toán** trên ba nhóm chỉ số: Thời gian, Chất lượng, Chi phí. Do chưa tiếp cận được số nội bộ ACFC, phần dưới trình bày **công thức + một ví dụ tính toán minh họa** để thể hiện phương pháp.

> ⚠️ **Lưu ý liêm chính học thuật:** mọi con số ở cột "Dữ liệu giả định" và "Kết quả tính" bên dưới là **số nhóm tự đặt để minh họa cách tính — KHÔNG phải số liệu thực của ACFC**. Sau phỏng vấn/workshop sẽ thay bằng ba mốc *thấp nhất – thường gặp – cao nhất* từ dữ liệu thật rồi áp lại đúng công thức ở cột "Công thức". Các đơn giá giờ công (120k–150k), đơn giá SMS (300đ) và đơn giá giờ CSKH (100k) đều là giả định minh họa.

### 9.1. M3 – Lập kế hoạch mua hàng và phân bổ

**a) Nhóm Thời gian (Time)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Thời gian chu kỳ lập kế hoạch (Cycle time) | Thời điểm phát hành − thời điểm bắt đầu | Bắt đầu 09:00 ngày 1 → phát hành 17:00 ngày 5 | **40 giờ** |
| Thời gian xử lý thực (Processing/VA+BVA) | Σ thời gian các bước tạo/kiểm/duyệt (B1–B10) | ≈ 14 giờ | **14 giờ** |
| Thời gian chờ (Waiting/NVA) | Cycle − Processing | 40 − 14 | **26 giờ** |
| Hiệu suất chu kỳ (PCE) | Processing / Cycle time | 14 / 40 | **35%** |
| Thời gian phê duyệt | Thời điểm duyệt − thời điểm trình | Trình 14:00 ngày 3 → duyệt 10:00 ngày 5 | **≈ 44 giờ** |

*Nhận xét: PCE 35% nghĩa là gần 2/3 thời gian là chờ (NVA) — khớp với lãng phí "Chờ (Hold)" ở mục 8.5.*

**b) Nhóm Chất lượng (Quality)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Độ chính xác dự báo | 1 − abs(dự báo − thực tế) / thực tế | Dự báo 1.000, thực tế 1.200 | **83,3%** |
| Tỷ lệ bán qua (Sell-through) | Số bán / số khả dụng | 750 / 1.000 | **75%** |
| Số tháng tồn kho (WoS) | Tồn cuối kỳ / tốc độ bán bình quân tháng | 600 / 250 | **2,4 tháng** |
| Tỷ lệ thay đổi phân bổ | Kế hoạch sửa / kế hoạch phát hành | 15 / 100 | **15%** |

**c) Nhóm Chi phí (Cost)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Chi phí lập lại kế hoạch (Defects) | Số lần lập lại × giờ công × đơn giá giờ | 2 lần × 8 giờ × 150.000đ | **2.400.000đ / mùa** |
| Chi phí đọng vốn tồn dư (Over-stock) | Giá trị tồn dư × chi phí giữ hàng/tháng | 200 sp × 300.000đ × 2% | **1.200.000đ / tháng** |
| Chi phí chờ phê duyệt (Hold) | Số kế hoạch × giờ chờ × đơn giá giờ | 4 × 26 giờ × 150.000đ | **15.600.000đ / mùa** |

### 9.2. S3 – Kiểm kê và xử lý chênh lệch tồn kho

**a) Nhóm Thời gian (Time)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Thời gian chu kỳ kiểm kê (Cycle time) | Thời điểm đóng hồ sơ − thời điểm bắt đầu (freeze) | Freeze 20:00 → đóng hồ sơ 08:00 hôm sau | **12 giờ** |
| Thời gian đếm thực tế (Processing/VA+BVA) | Σ thời gian đếm + đối chiếu (B5–B6) | ≈ 4 giờ | **4 giờ** |
| Thời gian chờ (Waiting/NVA) | Chờ duyệt phạm vi + chờ phê duyệt điều chỉnh (B3, B12) | ≈ 6 giờ | **6 giờ** |
| Hiệu suất chu kỳ (PCE) | Processing / Cycle time | 4 / 12 | **33%** |
| Tuổi chênh lệch chưa đóng | Ngày hiện tại − ngày mở hồ sơ | Mở 01/08 → xét 06/08 | **5 ngày** |

**b) Nhóm Chất lượng (Quality)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Độ chính xác tồn kho (IRA) | 1 − Σ abs(chênh lệch) / tổng tồn kho | 1 − 30 / 10.000 | **99,7%** |
| Tỷ lệ hao hụt (Shrinkage) | Giá trị thiếu không giải thích / giá trị tồn | 3.000.000đ / 2.000.000.000đ | **0,15%** |
| Tỷ lệ đếm lại | Số mã phải đếm lại / tổng mã đếm | 40 / 500 | **8%** |
| Tỷ lệ điều chỉnh | Kiểm kê có điều chỉnh / tổng kiểm kê | 3 / 20 | **15%** |
| Tỷ lệ đóng đúng hạn | Hồ sơ đóng đúng hạn / tổng hồ sơ | 18 / 20 | **90%** |

**c) Nhóm Chi phí (Cost)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Chi phí mỗi đợt kiểm kê | Số người × số giờ × đơn giá giờ | 5 người × 4 giờ × 120.000đ | **2.400.000đ / đợt** |
| Chi phí đếm lại (Defects) | Số giờ đếm lại × đơn giá giờ | 6 giờ × 120.000đ | **720.000đ / đợt** |
| Chi phí hao hụt phải bồi thường/xóa sổ | Giá trị thiếu không thu hồi được | Theo ví dụ trên | **3.000.000đ / đợt** |

### 9.3. S4 – Đăng ký và kích hoạt tài khoản thành viên

**a) Nhóm Thời gian (Time)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Thời gian hoàn tất đăng ký (Cycle time) | Thời điểm kích hoạt − thời điểm bắt đầu | Bắt đầu 0s → kích hoạt 90s | **90 giây** |
| Thời gian chờ nhận OTP (Waiting/NVA) | Thời điểm nhận OTP − thời điểm gửi | ≈ 20 giây | **20 giây** |
| Hiệu suất chu kỳ (PCE) | (Cycle − Waiting) / Cycle | (90 − 20) / 90 | **≈ 78%** |
| Thời gian xử lý yêu cầu CSKH | Thời điểm đóng − thời điểm khách liên hệ | Liên hệ 09:00 → đóng 11:00 | **2 giờ** |

**b) Nhóm Chất lượng (Quality)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Tỷ lệ đăng ký thành công | Tài khoản tạo thành công / tổng lượt bắt đầu | 820 / 1.000 | **82%** |
| Tỷ lệ bỏ dở đăng ký | 1 − tỷ lệ đăng ký thành công | 1 − 0,82 | **18%** |
| Tỷ lệ OTP xác nhận đúng lần đầu | Lượt đúng lần đầu / tổng lượt gửi OTP | 880 / 1.000 | **88%** |
| Tỷ lệ cần CSKH hỗ trợ | Lượt chuyển CSKH / tổng lượt đăng ký-đăng nhập | 60 / 1.000 | **6%** |

**c) Nhóm Chi phí (Cost)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Chi phí gửi OTP | Tổng lượt gửi OTP × đơn giá SMS | 1.000 × 300đ | **300.000đ / 1.000 lượt** |
| Chi phí xử lý CSKH (Defects/Move) | Số lượt CSKH × thời gian × đơn giá giờ | 60 × 0,25 giờ × 100.000đ | **1.500.000đ** |
| Chi phí doanh thu mất do bỏ dở (cơ hội) | Số lượt bỏ dở × giá trị đơn bình quân × tỷ lệ chuyển đổi | 180 × 500.000đ × 10% | **9.000.000đ** |

### 9.4. S1 – Tuyển dụng & tiếp nhận nhân sự

**a) Nhóm Thời gian (Time)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Thời gian tuyển (Time-to-hire) | Ngày ứng viên nhận offer − ngày mở tin tuyển | Mở tin 01/08 → nhận offer 21/08 | **20 ngày** |
| Thời gian lấp đầy vị trí (Time-to-fill) | Ngày nhân sự đi làm − ngày phát sinh nhu cầu | Nhu cầu 28/07 → đi làm 04/09 | **38 ngày** |
| Thời gian chờ giữa các vòng (Waiting/NVA) | Σ thời gian chờ phản hồi các vòng phỏng vấn | ≈ 9 ngày | **9 ngày** |
| Hiệu suất chu kỳ (PCE) | (Time-to-hire − Waiting) / Time-to-hire | (20 − 9) / 20 | **55%** |

**b) Nhóm Chất lượng (Quality)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Tỷ lệ hồ sơ qua sàng lọc ATS | Hồ sơ đạt / tổng hồ sơ nhận | 120 / 500 | **24%** |
| Tỷ lệ chấp nhận offer (Offer acceptance) | Số nhận offer / số offer gửi | 18 / 25 | **72%** |
| Tỷ lệ lấp đầy đúng hạn (Fill rate) | Vị trí lấp đầy đúng hạn / tổng vị trí cần | 8 / 10 | **80%** |
| Tỷ lệ nghỉ việc sớm (Early turnover ≤ 3 tháng) | Số nghỉ trong 3 tháng / số tuyển | 5 / 20 | **25%** |

**c) Nhóm Chi phí (Cost)**

| KPI | Công thức | Dữ liệu giả định (minh họa) | Kết quả tính |
|---|---|---|---|
| Chi phí trên mỗi tuyển dụng (Cost-per-hire) | Tổng chi phí tuyển / số nhân sự tuyển được | 40.000.000đ / 20 | **2.000.000đ / người** |
| Chi phí đăng tin & nền tảng tuyển | Σ phí đăng tin các kênh / kỳ | Theo hợp đồng kênh | **cần xác thực** |
| Chi phí tuyển lại do nghỉ sớm (Defects) | Số nghỉ sớm × chi phí trên mỗi tuyển dụng | 5 × 2.000.000đ | **10.000.000đ** |

*Nhận xét: PCE 55% và tỷ lệ nghỉ sớm 25% (số minh họa) cùng chỉ ra hai điểm nghẽn — chờ giữa các vòng (Hold) và chất lượng chọn lọc/onboarding (Defects) — khớp với mục 8.4 và 8.6.*

## 10. Đề xuất khắc phục theo lãng phí và TO-BE

### 10.1. Bảng đề xuất khắc phục theo lãng phí

| Quy trình | Loại lãng phí | Vấn đề | Đề xuất khắc phục | Người phụ trách đề xuất | Thời hạn đề xuất |
|---|---|---|---|---|---|
| M3 | Di chuyển | Bản kế hoạch/báo cáo bị chuyển qua nhiều kênh (email, chat, bảng tính rời) | Gộp về một nơi lưu trữ dùng chung và một mã kế hoạch duy nhất theo mùa | Hàng hóa/Phân bổ | Ngắn hạn |
| M3 | Chờ | Chờ báo cáo, ngân sách hoặc phê duyệt không có hạn xử lý rõ ràng | Đặt SLA cho từng bước duyệt, gắn người phụ trách và cảnh báo tự động khi quá hạn | Quản lý Hàng hóa/Phân bổ | Ngắn hạn |
| M3 | Xử lý dư | Nhập/đối chiếu trùng dữ liệu bán hàng – tồn kho từ nhiều nguồn | Chuẩn hóa một nguồn dữ liệu gốc, tự động hóa bảng theo dõi tỷ lệ bán qua/số tháng tồn | Hàng hóa/Phân bổ + IT | Trung hạn |
| M3 | Lỗi | Dự báo hoặc mã hàng sai khiến phải lập lại kế hoạch | Bắt buộc kiểm tra dữ liệu gốc và khóa phiên bản trước khi trình duyệt | Hàng hóa/Phân bổ | Ngắn hạn |
| S3 | Di chuyển | Phiếu kiểm kê/biên bản chuyển qua nhiều đầu mối giấy tờ | Chuyển sang hồ sơ điện tử và một mã vụ việc duy nhất cho mỗi đợt kiểm kê | Kiểm soát tồn kho/Vận hành | Ngắn hạn |
| S3 | Chờ | Chờ đếm lại, giải trình hoặc duyệt điều chỉnh không có hạn rõ ràng | Đặt thời hạn xử lý, hàng đợi quá hạn và người phụ trách theo từng bước | Quản lý cửa hàng/Kiểm soát tồn kho | Ngắn hạn |
| S3 | Xử lý dư | Đếm/nhập/đối chiếu trùng dữ liệu tồn ở nhiều nơi | Kiểm kê theo mức rủi ro (không đếm dàn đều), dùng một hồ sơ điều chỉnh gốc | Kiểm soát tồn kho/Vận hành + IT | Trung hạn |
| S3 | Lỗi | Chênh lệch lặp lại, thiếu bằng chứng bàn giao, sai giao dịch | Quét mã vạch khi đếm, nhật ký kiểm tra và mã nguyên nhân chuẩn hóa | Kiểm soát tồn kho/Vận hành | Trung hạn |
| S4 | Di chuyển | Khách phải tự tìm kênh hỗ trợ (hotline/fanpage/Zalo/email) khi gặp lỗi tài khoản | Đặt nút hỗ trợ/chatbot ngay trên trang đăng ký/đăng nhập | CSKH + Digital-Ecommerce/IT | Ngắn hạn |
| S4 | Chờ | Chờ nhận OTP hoặc mật khẩu tạm không có kênh dự phòng | Thêm kênh gửi dự phòng, hiển thị đếm ngược hiệu lực OTP | IT vận hành website/app | Ngắn hạn |
| S4 | Xử lý dư | Phải nhập lại toàn bộ thông tin khi OTP hết hạn hoặc đăng ký thất bại | Lưu tạm dữ liệu phiên đăng ký, chỉ yêu cầu gửi lại OTP | IT vận hành website/app | Trung hạn |
| S4 | Lỗi | Thông báo lỗi chung chung khi OTP sai/hết hạn hoặc số điện thoại đã tồn tại | Chuẩn hóa thông báo lỗi cụ thể theo từng nguyên nhân, kèm hướng dẫn bước kế tiếp | CSKH + Digital-Ecommerce/IT | Trung hạn |
| S1 | Di chuyển | Trao đổi offer/hồ sơ ứng viên qua nhiều kênh rời rạc (email, điện thoại, tin nhắn) | Tập trung liên lạc và trạng thái ứng viên trên một hệ ATS | HR Tuyển dụng + IT | Trung hạn |
| S1 | Chờ | Chờ phản hồi giữa các vòng phỏng vấn kéo dài time-to-hire | Đặt SLA phản hồi từng vòng, hàng đợi ứng viên quá hạn, nhắc tự động | HR Tuyển dụng + Trưởng bộ phận tuyển | Ngắn hạn |
| S1 | Xử lý dư | Nhập lại thông tin ứng viên ở nhiều biểu mẫu qua các vòng | Dùng một hồ sơ ứng viên xuyên suốt ATS, kế thừa dữ liệu giữa các vòng | HR Tuyển dụng + IT | Trung hạn |
| S1 | Lỗi | Nghỉ việc sớm/turnover cao ở nhân sự cửa hàng khiến phải tuyển lại | Chuẩn hóa tiêu chí sàng lọc theo vị trí, hoàn thiện onboarding (uniform, đào tạo, cấp tài khoản POS) | HR Tuyển dụng + Quản lý cửa hàng | Trung hạn |

*Ghi chú: người phụ trách và thời hạn ở trên là đề xuất của nhóm dựa trên phân tích lãng phí, chưa phải cam kết chính thức của ACFC; cần xác nhận lại nếu có phỏng vấn/workshop với chủ quy trình.*

### 10.2. TO-BE sơ bộ

- **M3:** chuẩn hóa một bộ dữ liệu bán hàng–tồn kho–dự báo, tự động kiểm tra biên lợi nhuận/số tháng tồn, gắn người phụ trách và thời hạn, lưu một phiên bản kế hoạch và cảnh báo khi cần lập lại.
- **S3:** đặt lịch kiểm kê và phạm vi trên một hệ thống, quét mã khi đếm, tự động tạo đếm lại theo ngưỡng, dùng mã nguyên nhân chuẩn, phê duyệt điều chỉnh theo hạn mức và theo dõi hồ sơ quá hạn.
- **S4:** lưu tạm dữ liệu đã nhập trong phiên đăng ký để chỉ cần gửi lại OTP khi hết hạn, chuẩn hóa thông báo lỗi theo từng nguyên nhân kèm hướng dẫn bước kế tiếp, hợp nhất đầu mối hỗ trợ tài khoản (chatbot/CSKH) ngay trên trang đăng ký/đăng nhập, và theo dõi tỷ lệ hết hạn OTP để điều chỉnh thời gian hiệu lực hợp lý.
- **S1:** quản lý ứng viên và trạng thái tuyển trên một hệ ATS duy nhất (một hồ sơ ứng viên xuyên suốt các vòng), đặt SLA phản hồi cho từng vòng phỏng vấn kèm cảnh báo quá hạn, áp fast-track cho các vị trí cửa hàng phổ thông để rút ngắn time-to-hire, chuẩn hóa tiêu chí sàng lọc theo vị trí và hoàn thiện onboarding (uniform, đào tạo, cấp tài khoản POS/Retail Pro Prism) nhằm giảm tỷ lệ nghỉ việc sớm.

## 11. Kết luận và nội dung cần xác thực

M3, S3, S4 và S1 đã có đủ mô tả bước–actor–kịch bản thành/bại (rubric tiêu chí 2), sơ đồ BPMN (rubric tiêu chí 3 — cả bốn quy trình đều đạt 8 cổng điều kiện gồm XOR và AND, có đầy đủ Split & Join cùng loại), bộ câu hỏi 10+10 mỗi quy trình và phân tích VA/BVA/NVA + 4 loại lãng phí + phân tích nguyên nhân gốc + phân tích định lượng ba nhóm chỉ số có ví dụ tính toán + đề xuất khắc phục (rubric tiêu chí 4), dựa trên bằng chứng công khai (mức A/B) và giả định cần xác thực (mức C). Khoảng trống còn lại:

1. **Số liệu định lượng thật:** các con số ở mục 9 hiện là **ví dụ minh họa** để trình bày cách tính, chưa phải số ACFC; cần phỏng vấn theo bộ câu hỏi ở mục 6 để thay bằng số thật (ba mốc thấp nhất – thường gặp – cao nhất).
2. **Xác nhận cấp duyệt/ngưỡng/tham số:** thẩm quyền duyệt kế hoạch M3, ngưỡng điều chỉnh S3, thời hạn xử lý và trách nhiệm bồi hoàn; với S4 là thời hạn hiệu lực OTP, kênh gửi mật khẩu tạm, ngưỡng số lần sai trước khi khóa tài khoản; và với S1 là số vòng phỏng vấn theo vị trí, thẩm quyền duyệt offer, ngưỡng thời gian thử việc và tiêu chí đánh giá KPI thử việc — tất cả vẫn ở mức `C – cần xác thực`.
3. **Đối chiếu mã sơ đồ nhóm:** file BPMN trong `diagrams/` dùng hậu tố nhóm khác với mã workspace (M3, S3, S4) — cần thống nhất bảng ánh xạ mã khi gộp vào báo cáo chung để tránh nhầm S3 (kiểm kê) với S4 (kích hoạt tài khoản). Ánh xạ hiện tại: M3 & S3 (kiểm kê) đã gộp vào sơ đồ collaboration `bpmn-kho-van-hanh-m3-s3.svg`, S4 (kích hoạt tài khoản) ↔ `...-s3`, S1 (tuyển dụng) ↔ `...-s1`.
4. **Chắt lọc vào báo cáo chung:** sau khi xác thực, nhóm quyết định phần nội dung M3/S3/S4 nào được đưa vào các file báo cáo Word dùng chung; đây vẫn là báo cáo cấp cá nhân, không tự ý chỉnh sửa file docx chung khi chưa thống nhất.
