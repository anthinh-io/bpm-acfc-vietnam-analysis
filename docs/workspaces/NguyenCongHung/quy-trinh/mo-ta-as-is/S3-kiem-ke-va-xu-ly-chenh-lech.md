# S3 – HIỆN TRẠNG SƠ BỘ: KIỂM KÊ VÀ XỬ LÝ CHÊNH LỆCH TỒN

## 1. Tóm tắt

Quy trình bắt đầu theo lịch kiểm kê ngày/tuần/tháng hoặc khi hệ thống phát hiện chênh lệch. Cửa hàng/Kho lập phạm vi kiểm kê, chuẩn bị phiếu kiểm kê và đối chiếu tồn thực tế với sổ tồn. Nếu có chênh lệch, nhân viên đếm lại và kiểm tra giao dịch nhập, xuất, điều chuyển, bán hàng, hủy hoặc hàng lỗi; Kiểm soát tồn kho/Vận hành phân loại nguyên nhân. Chênh lệch trong ngưỡng được lập đề nghị điều chỉnh để phê duyệt; chênh lệch vượt ngưỡng, lặp lại hoặc có dấu hiệu hao hụt được lập báo cáo sự cố/hao hụt và chuyển cấp. Kết quả cuối cùng được phản hồi cho **M3** để điều chỉnh kế hoạch, hạn mức tồn và nguyên nhân thất thoát; các bước điều chuyển/bổ sung tiếp theo nằm ngoài phạm vi mô tả của S3 trong bản này.

## 2. Actor kích hoạt và hưởng lợi

- **Actor kích hoạt:** Quản lý/Kiểm soát tồn kho (theo lịch định kỳ) hoặc hệ thống cảnh báo tồn thực tế lệch sổ.
- **Actor hưởng lợi trực tiếp:** Hàng hóa/Vận hành (M3) và Kế toán doanh thu/Tài chính — cần dữ liệu tồn chính xác.
- **Actor hưởng lợi gián tiếp:** cửa hàng (giảm thất thoát), khách hàng (đúng hàng sẵn có).

## 3. Các bước thực hiện

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

## 4. Kịch bản thành công

Đến kỳ kiểm kê → phạm vi được duyệt → đếm tồn thực tế khớp sổ ngay lần đầu → hồ sơ được ghi nhận và đóng đúng hạn, không phát sinh điều chỉnh. **Kết quả:** "Kiểm kê khớp sổ, hồ sơ đã đóng đúng hạn." Nếu có chênh lệch nhưng trong ngưỡng: xác định đúng nguyên nhân ở lần đếm lại đầu tiên → đề nghị điều chỉnh được phê duyệt → hệ thống cập nhật → hồ sơ đóng đúng hạn → kết quả phản hồi cho M3.

## 5. Kịch bản thất bại/ngoại lệ

- Đếm tồn thực tế không khớp sổ (Bước 6) và điều kiện đếm lại được kích hoạt (Bước 7) → quay lại đếm lại; nếu đếm lại vẫn lệch, chuyển sang xác định nguyên nhân sâu hơn.
- Không xác định được nguyên nhân trong thời hạn quy định (Bước 9) → vẫn phải lập báo cáo tạm với nhãn "nguyên nhân chưa xác định", có thể phải chuyển cấp sớm hơn quy trình thông thường.
- Chênh lệch vượt ngưỡng điều chỉnh, lặp lại nhiều kỳ hoặc có dấu hiệu hao hụt/mất mát (Bước 11) → lập báo cáo sự cố/hao hụt riêng, chuyển cấp cho Quản lý/Kế toán xác minh trách nhiệm bồi hoàn — ngưỡng, cấp chuyển và trách nhiệm cụ thể là `C – cần xác thực`.
- Điều chỉnh hoặc bút toán không được phê duyệt (Bước 12) → yêu cầu bổ sung bằng chứng/giải trình, quay lại Bước 9.
- Hồ sơ không đóng đúng hạn (Bước 14) → gắn cờ quá hạn, báo cáo cho Quản lý; hồ sơ vẫn phải đóng sau khi bổ sung đủ bằng chứng.

**Nguồn/trạng thái:** EV03, EV05, EV08; lịch kiểm kê, ngưỡng điều chỉnh, thời hạn xác định nguyên nhân, trách nhiệm bồi hoàn và cấp chuyển là `C – cần xác thực` bằng phỏng vấn Quản lý cửa hàng, Kiểm soát tồn kho/Vận hành và Kế toán doanh thu/Tài chính.
