# Workspace Nguyễn Thanh Thịnh – ACFC

## Cấu trúc hồ sơ

| Hạng mục | Tương ứng phần báo cáo | File | Trạng thái |
|---|---|---|---|
| Giới thiệu & Tóm tắt (kèm giới thiệu ACFC) | Phần mở đầu báo cáo (trước Chương 1) | [`00-gioi-thieu-va-tom-tat.md`](00-gioi-thieu-va-tom-tat.md) | Bản nháp — bối cảnh, giới thiệu công ty ACFC (lịch sử, ranh giới ACFC/DAFC, đối thủ, quy mô, thành tựu, cơ cấu tổ chức, hoạt động kinh doanh — có trích dẫn), thách thức vận hành, mục tiêu/phạm vi, cấu trúc báo cáo |
| Chương 1 — Liệt kê quy trình nghiệp vụ | Chương 1 (README.md gốc) | [`01-chuong-1-kien-truc-quy-trinh.md`](01-chuong-1-kien-truc-quy-trinh.md) | Bản nháp — phân loại 3 cấp, sơ đồ kiến trúc quy trình (`so_do_quy_trinh.drawio`/`.svg`), danh mục 10 quy trình chính thức, phần mở rộng, checklist việc cần nhóm xử lý |
| Chương 2 — Mô hình hóa quy trình nghiệp vụ | Chương 2 (README.md gốc) | [`02-chuong-2-mo-hinh-hoa.md`](02-chuong-2-mo-hinh-hoa.md) | Bản nháp — đủ cả 6 quy trình (M1, Kho vận hành, C2, S1, C3, S4); sơ đồ BPMN của Kho vận hành và S4 đang chờ Hưng sửa lỗi |
| Chương 3 — Phân tích quy trình | Chương 3 (README.md gốc) | [`03-chuong-3-phan-tich-quy-trinh.md`](03-chuong-3-phan-tich-quy-trinh.md) | Bản nháp — đủ cả 6 quy trình, nhiều mục còn gắn nhãn `[giả định]` cần thành viên xác nhận — xem mục "Thông báo tiến độ" bên dưới |

## Thông báo tiến độ



| Thành viên | Quy trình phụ trách | Vị trí Ch.2 | Vị trí Ch.3 | Việc cần làm |
|---|---|---|---|---|
| Lương Triệu Khang | M1, S1 | 2.1, 2.4 | 3.3, 3.4 | Cả 2 quy trình lãng phí mới có 3/4 loại (thiếu bằng chứng Defects), chưa có Pareto/5-Whys, chưa có phân tích các bên liên quan — Chương 3 đang để trống các mục này, cần Khang xác nhận hoặc bổ sung. Phần định lượng cũng mới chỉ có công thức, chưa có số liệu thật. |
| Huỳnh Gia Bảo | C2, C3 | 2.3, 2.5 | 3.1, 3.2 | Dữ liệu đầy đủ nhất (có Pareto, C3 có thêm 5 Whys + xương cá, số liệu phần lớn đã xác nhận qua phỏng vấn) — chủ yếu cần rà lại xem mình trích dẫn/tính lại có đúng không, không cần bổ sung dữ liệu mới. |
| Nguyễn Công Hưng | S4, Kho vận hành | 2.2, 2.6 | 3.5, 3.6 | 2 việc khẩn: **(1)** sơ đồ BPMN của S4 và Kho vận hành (mục 2.2.2) vẫn còn lỗi cổng XOR join mất cân bằng nhánh và còn sót nhãn ID kiểu "G1:/G2:..." chưa xóa — cần sửa rồi export đè lên đúng tên file cũ. **(2)** Mục 3.6 (Kho vận hành) — vì quy trình này chưa có phân tích VA/BVA/NVA/lãng phí nào từ Hưng, gắn nhãn `[giả định]` từng dòng — cần Hưng xác nhận, sửa hoặc bác bỏ, không phải dữ liệu Hưng đã cung cấp. Mục 9.3 (số liệu S4) trong báo cáo gốc của Hưng cũng tự ghi là "minh họa, không phải số thật" — Chương 3 đã tránh dùng làm số liệu thật, nhưng cần Hưng cung cấp số thật để thay vào. |

Cách rà soát nhanh: mỗi quy trình ở cả Chương 2 và Chương 3 đều có sẵn mục "Phỏng vấn"/"Phỏng vấn bổ sung" liệt kê câu hỏi còn thiếu — dùng chính danh sách đó làm checklist khi đối chiếu với hiểu biết thực tế, không cần đọc lại toàn bộ mục.

Sau khi mọi người rà xong, còn 2 việc lớn: viết Chương 4 (Đánh giá & Kết luận) và chuyển toàn bộ sang bản Word — cả hai đều chưa bắt đầu.
