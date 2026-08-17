# Roadmap

## 1. Rubric chấm điểm (5 tiêu chí)

| #   | Tiêu chí                      | Yêu cầu cụ thể                                                                                                                                                                                                                                 | Điểm trừ / lưu ý                                                                  |
| --- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 1   | Liệt kê & phân loại quy trình | Tối thiểu **10 quy trình**, chia đều 3 cấp (Quản lý / Cốt lõi / Hỗ trợ), mỗi cấp ≥3, một cấp sẽ có 4. Vẽ sơ đồ kiến trúc quy trình tổng thể.                                                                                                   | —                                                                                 |
| 2   | Mô tả quy trình               | Mô tả bằng lời cho **10 quy trình**: bước thực hiện, actor (ai kích hoạt / ai hưởng lợi), kịch bản thành công & thất bại.                                                                                                                      | —                                                                                 |
| 3   | Mô hình hóa BPMN              | Tối thiểu **6 quy trình** (2 Quản lý + 2 Cốt lõi + 2 Hỗ trợ), dùng **BPMN 2.0** (Lucidchart). Điểm theo số gateway: >7 cổng = 1đ, >5 = 0.75đ, 4–5 = 0.5đ, <3 = 0.25đ, 0 cổng = 0đ.                                                             | Sai ký hiệu/tên/quy tắc vẽ: **-0.25đ/lỗi**                                        |
| 4   | Phân tích quy trình           | Phân tích tối thiểu **2 quy trình** (tối đa cả 6). Định tính: VA/BVA/NVA + tối thiểu 4 loại lãng phí (Move, Hold, Over-processing, Defects), bảng 3 cột (mô tả – phân loại – khắc phục), đánh dấu trên sơ đồ. Định lượng: thời gian + chi phí. | —                                                                                 |
| 5   | Trình bày báo cáo             | Theo mẫu khóa luận của trường: mục lục nội dung/hình/bảng/từ viết tắt, font size 12, đen trắng nhất quán. Nhãn bảng ở trên, nhãn hình ở dưới.                                                                                                  | Lỗi chính tả: **-1đ/lỗi** (dễ mất trắng cả tiêu chí). Sai vị trí nhãn: -1 đến -2đ |

## 2. Mốc thời gian

| Tuần                | Khoảng ngày    | Việc cần làm theo giảng viên                                                                                                            | Trạng thái      |
| ------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| 1–2                 | 06/07 – 19/07  | Lập nhóm (≥4 người), chọn công ty và lĩnh vực, tạo repo GitHub, thêm email giảng viên, phân chia công việc ban đầu                      | ✅ Hoàn tất     |
| 3–5                 | 20/07 – 09/08  | Rải công việc từng tuần: liệt kê quy trình, mô tả, bắt đầu mô hình hóa                                                                  | ⏳ Đang bắt đầu |
| 6–7                 | 10/08 – 23/08  | Chuẩn bị **slide báo cáo cuối kỳ**: mỗi cấp (quản lý/cốt lõi/hỗ trợ) chọn 1 quy trình tiêu biểu để trình bày, nhận góp ý từ giảng viên  | ⏳ Sắp tới      |
| +1 tuần sau báo cáo | ~24/08 – 30/08 | Chỉnh sửa theo góp ý, hoàn thiện toàn bộ báo cáo Word (10 quy trình mô tả, 6 sơ đồ BPMN, phân tích, đề xuất), nộp file Word + PDF slide | ⏳ Sắp tới      |

## 3. Bài học rút ra từ báo cáo mẫu

|                          | CellphoneS                                 | FUTA Bus Lines                                                                       | Áp dụng cho nhóm                                                                                   |
| ------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Số quy trình mô hình hóa | 6                                          | 9 (vượt yêu cầu tối thiểu)                                                           | Làm đúng tối thiểu 6 trước, dư sức thì mở rộng                                                     |
| Cấu trúc chương          | Gộp mô hình hóa + phân tích chung 1 chương | Tách riêng: Chương 2 chỉ mô hình hóa, Chương 3 chỉ phân tích                         | **Nên theo FUTA** — tách bạch giúp rubric tiêu chí 3 và 4 dễ chấm riêng, dễ tự rà soát điểm        |
| Độ sâu phân tích         | Chỉ bảng VA/BVA/NVA + lãng phí cơ bản      | Có thêm Stakeholder Analysis, Issue Register (cột giải pháp cụ thể), Pareto, Why-Why | Làm tối thiểu 2 quy trình theo chuẩn FUTA (Issue Register có cột "khắc phục") để tối ưu tiêu chí 4 |
| Đề xuất cải tiến         | Gộp chung, chung chung ở phần Kết luận     | Cụ thể theo từng vấn đề, có người phụ trách/thời hạn                                 | Làm bảng đề xuất riêng cho từng lãng phí phát hiện                                                 |

## 4. Kế hoạch công việc chi tiết theo tuần (từ hiện tại)

### Tuần 3 (20–26/07) — Chốt danh sách quy trình
- [x] Rà lại quy trình → ánh xạ vào 3 cấp **Quản lý / Cốt lõi / Hỗ trợ** theo chuẩn APQC (`docs/03-kien-truc-quy-trinh-doanh-nghiep.md`).
- [x] Chốt tối thiểu **10 quy trình chính thức** (đầy đủ 4 thành phần: Tác nhân, Mô tả bước, Khách hàng, Kết quả).
- [x] Vẽ sơ đồ **Kiến trúc quy trình tổng thể** (`diagrams/kien-truc-quy-trinh.svg` và `.drawio`).
- [x] Phân công 4 thành viên phụ trách theo nhóm quy trình và học phần.

### Tuần 4 (27/07–02/08) — Mô tả quy trình
- [x] Mô tả bằng lời cả 10 quy trình: bước thực hiện, actor kích hoạt/hưởng lợi, kịch bản thành công/thất bại.
- [x] Soạn bộ câu hỏi khảo sát: 10 định tính (5 structured + 5 unstructured) + 10 định lượng (5 structured + 5 unstructured) cho các quy trình trọng tâm.

### Tuần 5 (03–09/08) — Mô hình hóa BPMN
- [x] Vẽ BPMN cho các quy trình trọng tâm (S2 Kiểm kê kho, S3 Đăng ký tài khoản, S1 Tuyển dụng, C1/C2 Vận hành kho), mỗi sơ đồ đạt **$\ge 8$ Gateways** (>7 cổng để đạt điểm tối đa 1.0đ/sơ đồ).
- [x] Rà soát ký hiệu, quy tắc đặt tên động từ + danh từ, Split-Join tương ứng, Message flow giữa các pool độc lập (`diagrams/*.svg` và `diagrams/*.drawio`).

### Tuần 6 (10–16/08) — Phân tích + chuẩn bị báo cáo
- [x] Phân tích định tính (Bảng VA/BVA/NVA có cột biện pháp khắc phục, Bảng 4 loại Lãng phí Move/Hold/Overdo/Defects có biện pháp khắc phục).
- [x] Vẽ Sơ đồ Xương cá Fishbone & Phân tích 5-Whys cho các vấn đề cốt lõi.
- [x] Phân tích định lượng (Thời gian chu kỳ, Thời gian chờ, PCE, Tỷ lệ lỗi và Chi phí thiệt hại).
- [x] Chuẩn bị đề xuất giải pháp cải tiến TO-BE (RFID, Cycle counting, Zalo ZNS OTP, ATS AI Screening, e-Offer).

### Tuần sau báo cáo (~24–30/08) — Hoàn thiện & nộp
- [x] Tổng hợp toàn bộ Báo cáo Đồ án chuẩn theo mẫu Khóa luận tốt nghiệp của Khoa HTTT – UIT (`docs/07-tong-hop-bao-cao-mon-hoc-chuan-uit.md`).
- [x] Kiểm tra nghiêm ngặt: Nhãn Bảng ở TRÊN, Nhãn Hình ở DƯỚI, Mục lục, Danh mục hình, Danh mục bảng, Danh mục viết tắt, 0 lỗi chính tả.

---

## 5. Danh mục Sản phẩm Bàn giao Đạt Chuẩn (Deliverables Index)

1. `docs/03-kien-truc-quy-trinh-doanh-nghiep.md`: Danh mục 10 quy trình chuẩn hóa (M1–M3, C1–C4, S1–S3).
2. `docs/04-quy-trinh-kho-nhap-xuat-kiem-ke.md`: Báo cáo chuyên sâu quy trình Kho, Nhập xuất, Kiểm kê (S2, C1, C2, M3).
3. `docs/workspaces/NguyenCongHung/Bao cao ca nhan - M3 S3 S4 S1 (ACFC).md`: Báo cáo cá nhân tổng hợp bốn quy trình M3/S3/S4/S1 (đã gộp phần chuyên sâu Đăng ký & Kích hoạt tài khoản Member S4 và Tuyển dụng & Onboarding S1 vào chung).
4. `docs/06-quy-trinh-tuyen-dung-nhan-su.md`: Báo cáo chuyên sâu quy trình Tuyển dụng & Onboarding nhân sự (S1).
5. `docs/07-tong-hop-bao-cao-mon-hoc-chuan-uit.md`: Báo cáo đồ án hoàn chỉnh theo mẫu chuẩn Khóa luận tốt nghiệp UIT.
6. Thư mục `diagrams/` (cấp gốc, dùng chung): Kiến trúc quy trình và các sơ đồ nhóm/thành viên khác (C1–C4, tổng hợp kho). Sơ đồ 4 quy trình của Nguyễn Công Hưng (M3, S3, S4, S1) đã chuyển vào `docs/workspaces/NguyenCongHung/diagrams/`. Đã bỏ toàn bộ sơ đồ Xương cá (Fishbone).

