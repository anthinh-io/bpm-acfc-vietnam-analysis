# Vòng đời BPM: Khám phá Quy trình

## 1. Thiết lập khám phá quy trình

- **4 hoạt động chính** khi thiết lập một dự án khám phá quy trình:
  1. **Xác định** — tập hợp một nhóm chịu trách nhiệm quản lý quy trình.
  2. **Thu thập thông tin** — xây dựng hiểu biết về quy trình bằng các phương pháp khám phá phù hợp.
  3. **Tiến hành mô hình hóa** — chuyển thông tin thu thập được thành mô hình (sơ đồ BPMN) thực tế.
  4. **Đảm bảo chất lượng mô hình** — kiểm tra mô hình đáp ứng các tiêu chí chất lượng.
- **Hai nhóm đối tượng tham gia:**
  - **Process Analyst (người phân tích quy trình):** kỹ năng cốt lõi là mô hình hóa — biết thu thập thông tin, xây dựng/kiểm tra giả thuyết, xác định mẫu (pattern), chú trọng chất lượng mô hình và thành thạo công cụ/ngôn ngữ mô hình hóa. Kỹ năng này độc lập với lĩnh vực chuyên môn cụ thể.
  - **Domain Expert (chuyên gia lĩnh vực/người vận hành):** nắm rõ quy trình vận hành thực tế tại tổ chức nhưng thường không có kỹ năng mô hình hóa.
- **Nguyên tắc chọn nhân sự:** khi thiết lập dự án BPM, nếu phải lựa chọn, ưu tiên người có kỹ năng phân tích/mô hình hóa quy trình hơn người chỉ có tri thức ngành — vì kỹ năng mô hình hóa khó đào tạo nhanh hơn kỹ năng tiếp nhận kiến thức nghiệp vụ.

## 2. Phương pháp khám phá quy trình

Có thể chọn một hoặc kết hợp nhiều phương pháp, tùy bối cảnh tổ chức, văn hóa và ngân sách dự án.

- **Dựa trên bằng chứng (Evidence-based):**
  - *Phân tích tài liệu:* thu thập sơ đồ tổ chức, chính sách nội bộ, sổ tay thuật ngữ, biểu mẫu, báo cáo, hướng dẫn làm việc. Ưu điểm: khách quan, có cấu trúc, không phụ thuộc sự sẵn sàng của nhân sự. Nhược điểm: tài liệu có thể lỗi thời hoặc sai mức độ trừu tượng so với thực tế.
  - *Quan sát:* theo dõi trực tiếp việc thực hiện quy trình.
    - Chủ động: đóng vai trò cụ thể (VD: đóng vai khách hàng trải nghiệm mua sắm) — nhược điểm là thiếu góc nhìn bao quát.
    - Bị động: quan sát người vận hành từ bên ngoài — nhược điểm là dễ gặp hiệu ứng thiên vị (người bị quan sát thay đổi hành vi).
  - *Khám phá tự động (Automatic Discovery):* trích xuất dữ liệu từ event log/database của hệ thống đang vận hành (thời gian, tên hoạt động, tài nguyên, chi phí) để tái dựng quy trình thực tế.
- **Dựa trên phỏng vấn (Interview-based):**
  - Hướng truy vết: *tiến* (forward — từ sự kiện bắt đầu đến kết thúc) hoặc *lùi* (backward — từ kết thúc ngược về bắt đầu).
  - Dạng câu hỏi: *có cấu trúc* (đóng/trắc nghiệm — dùng để xác thực giả thuyết mô hình hóa ban đầu) và *không có cấu trúc* (mở — dùng để tìm hiểu sâu cách xử lý tình huống).
  - Nội dung câu hỏi cần bao gồm cả *định lượng* (đo đếm được: số bước, thời gian) và *định tính* (cảm nhận khó/dễ của người vận hành).
- **Dựa trên hội thảo (Workshop-based):** tập hợp các bên liên quan chính (nhà phân tích, chuyên gia, chủ sở hữu quy trình) để cùng thảo luận và mô hình hóa trực tiếp, thường 3–5 phiên (mỗi phiên nửa ngày). Ưu điểm: giải quyết ngay các quan điểm mâu thuẫn giữa các bên. Nhược điểm: cần thời gian trống của nhiều người cùng lúc; hiệu quả phụ thuộc lớn vào văn hóa tổ chức (cởi mở hay nghiêm ngặt) để chọn chiến lược gợi mở thông tin phù hợp.
- Cần hiểu văn hóa và "tình cảm" của tổ chức trước khi bắt đầu khám phá quy trình.

## 3. Phương pháp mô hình hóa quy trình

Từ thông tin đã thu thập, nhà phân tích xây dựng giả thuyết bằng cách vẽ sơ đồ theo trình tự các bước:

1. **Xác định ranh giới (scope) quy trình:** yếu tố kích hoạt, kết quả tích cực/tiêu cực có thể xảy ra, đầu vào/đầu ra, và quy trình được xây dựng theo góc nhìn của ai.
2. **Xác định sự kiện và hoạt động:** liệt kê các hoạt động chính (tuần tự) và các sự kiện liên quan.
3. **Xác định nguồn lực/tác nhân:** gắn nhân sự, tài liệu, dữ liệu liên quan vào từng bước của quy trình.
4. **Xác định luồng điều khiển:** vẽ các đường dẫn kết nối và các cổng logic (gateway độc lập/loại trừ, đồng thời).
5. **Xác định yếu tố bổ sung:** đối tượng dữ liệu, cách xử lý ngoại lệ, các loại sự kiện khác, và kịch bản thành công (positive) hay thất bại (negative).

## 4. Đảm bảo chất lượng quy trình

- **Chất lượng cú pháp (Syntactic Quality):**
  - Quy tắc đặt tên: Event = *Danh từ + Động từ (quá khứ)*; Activity = *Động từ + Danh từ*.
  - Mỗi hoạt động chỉ có 1 luồng vào và 1 luồng ra — nếu cần nhiều luồng, phải dùng Gateway.
  - Gateway đã mở (split) phải được đóng (join) đúng loại tương ứng.
  - Luôn có sự kiện Bắt đầu và sự kiện Kết thúc; dùng đúng ký hiệu chuẩn BPMN.
- **Chất lượng hành vi (Behavioral Quality)** — mô hình phải có khả năng hoàn thành đúng tiến trình, không có hoạt động "chết". Các lỗi nghiêm trọng cần tránh:
  - **Deadlock (bế tắc):** quy trình bị kẹt, không thể tiến triển. VD: dùng cổng AND để gom nhánh xuất phát từ một cổng XOR — một trong các nhánh sẽ không bao giờ có dữ liệu tới, khiến cổng AND kẹt chờ mãi.
  - **Livelock (vòng lặp không lối thoát):** hệ thống quay vòng liên tục, không bao giờ đạt tới sự kiện kết thúc.
  - **Lack of synchronization (thiếu đồng bộ):** tách nhánh (split) bằng một loại cổng nhưng gom nhánh (join) bằng cổng khác loại (VD: mở bằng XOR nhưng đóng bằng AND).
  - **Dead activity (hoạt động chết):** hoạt động được vẽ ra nhưng trong thực tế không có điều kiện/luồng nào kích hoạt được nó.
- **7 nguyên tắc vàng (G1–G7)** — checklist kiểm tra chất lượng mô hình:
  1. Dùng ít yếu tố nhất có thể.
  2. Giảm thiểu số đường dẫn rẽ nhánh.
  3. Luôn có 1 sự kiện bắt đầu và 1 sự kiện kết thúc cho mỗi kết quả.
  4. Mô hình hóa có cấu trúc — cổng nào mở thì cổng cùng loại đó đóng.
  5. Hạn chế dùng cổng OR nếu có thể thay bằng cổng khác.
  6. Chuẩn hóa nhãn hoạt động bằng động từ.
  7. Nếu mô hình có trên 30 yếu tố, cần phân rã (decompose) thành các quy trình con.
