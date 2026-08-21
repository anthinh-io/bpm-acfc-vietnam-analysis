# BPM ACFC Vietnam Analysis

Đồ án môn học **Hệ thống quản trị quy trình nghiệp vụ (Business Process Management Systems)** phân tích, mô hình hóa và đề xuất cải tiến các quy trình nghiệp vụ thực tế của ACFC tại Việt Nam.

## 1. Giới thiệu

ACFC (thành viên Tập đoàn Liên Thái Bình Dương – IPPG, thành lập năm 2009) là nhà phân phối và bán lẻ chính hãng hàng đầu Việt Nam cho hơn 25 thương hiệu thời trang quốc tế như Nike, Levi's, Tommy Hilfiger, Calvin Klein, Polo Ralph Lauren, Mango, Swarovski..., vận hành mạng lưới hơn 250 cửa hàng trên toàn quốc song song với kênh thương mại điện tử. Đồ án này tập trung vào ba mục tiêu cốt lõi:

- **Phân tích (Analysis):** khảo sát, mô tả và làm rõ cách các quy trình nghiệp vụ hiện đang vận hành.
- **Mô hình hóa (Modeling):** trực quan hóa quy trình bằng chuẩn BPMN (Business Process Model and Notation).
- **Đề xuất cải tiến (Improvement):** chỉ ra các điểm lãng phí, kém hiệu quả và đề xuất phương án khắc phục.

Đây là đồ án nhóm, chiếm 70% tổng điểm môn học; điểm số được đánh giá dựa trên mức độ đóng góp thực tế của từng thành viên thông qua lịch sử commit trên GitHub.

## 2. Phạm vi dự án

- Liệt kê và phân tích tối thiểu **10 quy trình nghiệp vụ**, phân bổ theo 3 cấp độ:
  - Quy trình quản lý (management)
  - Quy trình cốt lõi (core)
  - Quy trình hỗ trợ (support)
- Mô hình hóa chi tiết bằng BPMN tối thiểu **6 quy trình** chuỗi giá trị cốt lõi (tối thiểu 2 quy trình mỗi cấp: quản lý, cốt lõi, hỗ trợ).
- Mỗi sơ đồ BPMN cần đủ độ phức tạp (khuyến nghị trên 7 cổng điều kiện/gateway) để thể hiện đúng bản chất quy trình thực tế.

## 3. Phương pháp luận

Báo cáo được tổ chức theo đúng cấu trúc mà báo cáo mẫu FUTA Bus Lines tự công bố ở phần "Giới thiệu & Tóm tắt" của họ: phần mở đầu (Giới thiệu & Tóm tắt nội dung) + 4 chương nội dung + Tài liệu tham khảo. Bốn chương nội dung, bám sát rubric đánh giá của giảng viên:

### Giới thiệu & Tóm tắt nội dung

- Bối cảnh ngành và lý do chọn ACFC làm đối tượng phân tích
- Tổng quan về ACFC: lịch sử hình thành, đối thủ cạnh tranh, quy mô/lĩnh vực kinh doanh, thành tựu nổi bật, cơ cấu tổ chức, hoạt động kinh doanh
- Thách thức vận hành, mục tiêu và phạm vi báo cáo, cấu trúc báo cáo

### Chương 1. Liệt kê quy trình nghiệp vụ

- Phân loại quy trình theo 3 cấp Quản lý/Cốt lõi/Hỗ trợ, kèm sơ đồ kiến trúc quy trình tổng quát
- Kiến trúc quy trình tổng thể: danh sách các quy trình dự kiến phân tích theo 3 cấp

### Chương 2. Mô hình hóa quy trình nghiệp vụ

**Khám phá & mô tả quy trình (đầu vào cho mô hình hóa):**

- Phương pháp thu thập dữ liệu: dựa trên tài liệu/biểu mẫu có sẵn hoặc quan sát thực tế
- Xác định các tác nhân (actor): ai kích hoạt quy trình, ai là người hưởng lợi
- Mô tả quy trình bằng lời: từ bước khởi tạo đến kết quả (thành công/thất bại)
- Bộ câu hỏi workshop/phỏng vấn: 10 câu định tính (cảm xúc, ý kiến) + 10 câu định lượng (thời gian, chi phí) cho mỗi quy trình

**Mô hình hóa bằng BPMN:**

- Sơ đồ trực quan cho từng quy trình đã chọn, tuân thủ đúng ký hiệu, quy tắc đặt tên và luồng BPMN
- Phân rõ pool, lane, tác nhân tham gia

### Chương 3. Phân tích quy trình

- **Định tính:** phân loại hoạt động theo VA (Value-Added) / BVA (Business Value-Added) / NVA (Non-Value-Added); phân tích 4 nguyên nhân lãng phí — Move, Hold, Over-processing, Defects
- **Định lượng:** đo lường thời gian và chi phí thực hiện
- Bảng đề xuất khắc phục (vấn đề – mô tả – đề xuất) cho từng điểm lãng phí đã phát hiện
- Tổng kết giá trị mang lại

### Chương 4. Đánh giá & Kết luận

- Tổng kết giá trị mang lại

## 4. Công cụ sử dụng

| Công cụ    | Mục đích                        |
| ---------- | ------------------------------- |
| Lucidchart | Vẽ sơ đồ BPMN                   |
| Word / PDF | Định dạng nộp báo cáo cuối cùng |

> Lưu ý: được phép dùng AI hỗ trợ thiết kế/tinh chỉnh, nhưng nghiêm cấm giao toàn bộ việc vẽ và phân tích quy trình cho AI thực hiện tự động.

## 5. Cấu trúc thư mục

```
├── docs/                       # Tài liệu báo cáo, biểu mẫu khảo sát, bảng câu hỏi
│   ├── lectures/               # Tóm tắt lý thuyết BPMN dùng làm tài liệu tham khảo
│   └── workspaces/             # Không gian làm việc riêng của từng thành viên
├── diagrams/                   # Sơ đồ BPMN, hình minh họa quy tắc vẽ
├── reports/                    # Bản Word/PDF hoàn chỉnh, slide thuyết trình
├── BPMN_DRAWING_GUIDELINES.md  # Quy tắc vẽ và rà soát sơ đồ BPMN
├── ROADMAP.md                  # Lộ trình thực hiện theo tuần, đối chiếu rubric giảng viên
├── CONTRIBUTING.md             # Quy tắc đóng góp, phân công nhiệm vụ nhóm
└── README.md
```

## 6. Thành viên nhóm

| Thành viên         | GitHub                                          | Mã sinh viên |
| ------------------ | ----------------------------------------------- | ------------ |
| Nguyễn Thanh Thịnh | **[anthinh-io](https://github.com/anthinh-io)** | 22730096     |
| Lương Triệu Khang  | **[khang-code](https://github.com/khang-code)** | 24730105     |
| Huỳnh Gia Bảo      | **[jiabao77](https://github.com/jiabao77)**     | 24730157     |
| Nguyễn Công Hưng   | **[nc-hung](https://github.com/nc-hung)**       | 24730100     |

## 7. Đóng góp

Xem lộ trình thực hiện tại [ROADMAP.md](ROADMAP.md) và quy tắc đóng góp tại [CONTRIBUTING.md](CONTRIBUTING.md).

## 8. Giấy phép

Dự án phục vụ mục đích học tập trong khuôn khổ môn IE203, không nhằm mục đích thương mại.
