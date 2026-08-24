# BÁO CÁO CÁ NHÂN – PHÂN TÍCH QUY TRÌNH NGHIỆP VỤ ACFC

> Báo cáo trình bày **theo từng quy trình**: mỗi quy trình gồm mô tả hiện trạng (AS-IS), phân tích định tính, phân tích định lượng, phân tích nguyên nhân gốc (Pareto + 5 Why), câu hỏi phỏng vấn bổ sung và đề xuất cải tiến (TO-BE). Phạm vi cá nhân gồm bảy quy trình: **Lập kế hoạch mua hàng và phân bổ theo mùa** (cấp Quản lý); **Kiểm kê tồn kho**, **Kích hoạt tài khoản thành viên**, **Tuyển dụng và tiếp nhận nhân sự** cùng **cụm ba quy trình kho vận (Nhận hàng, Xuất kho, Thu hồi hàng trả)** (cấp Hỗ trợ). Mọi con số định lượng chưa phỏng vấn được là **số minh họa cách tính**, gắn nhãn `[giả định]` và sẽ thay bằng số vận hành thật sau phỏng vấn.

---

## Mục lục

1. [Tổng quan phạm vi và danh mục quy trình](#1-tổng-quan-phạm-vi-và-danh-mục-quy-trình)
2. [Lập kế hoạch mua hàng và phân bổ theo mùa](#2-lập-kế-hoạch-mua-hàng-và-phân-bổ-theo-mùa)
3. [Kiểm kê và xử lý chênh lệch tồn kho](#3-kiểm-kê-và-xử-lý-chênh-lệch-tồn-kho)
4. [Đăng ký, xác thực OTP và kích hoạt tài khoản thành viên](#4-đăng-ký-xác-thực-otp-và-kích-hoạt-tài-khoản-thành-viên)
5. [Tuyển dụng và tiếp nhận nhân sự chuỗi bán lẻ/kho vận](#5-tuyển-dụng-và-tiếp-nhận-nhân-sự-chuỗi-bán-lẻkho-vận)
6. [Nhận hàng, kiểm tra chất lượng và nhập kho](#6-nhận-hàng-kiểm-tra-chất-lượng-và-nhập-kho)
7. [Xuất kho và điều chuyển phân bổ tới chuỗi cửa hàng](#7-xuất-kho-và-điều-chuyển-phân-bổ-tới-chuỗi-cửa-hàng)
8. [Thu hồi và xử lý hàng trả về / hàng lỗi](#8-thu-hồi-và-xử-lý-hàng-trả-về--hàng-lỗi)

---

## 1. Tổng quan phạm vi và danh mục quy trình

### 1.1. Phạm vi và ranh giới

Phạm vi cá nhân thuộc mảng **hàng hóa, kho, tồn kho, tài khoản thành viên và tuyển dụng nhân sự** của ACFC, gồm bảy quy trình:

| Mã trên sơ đồ | Cấp | Quy trình | Ranh giới |
|---|---|---|---|
| M3 | Quản lý | Lập kế hoạch mua hàng và phân bổ theo mùa | Dữ liệu bán hàng/tồn → kế hoạch được duyệt và phát hành |
| S3 | Hỗ trợ | Kiểm kê và xử lý chênh lệch tồn kho | Lịch kiểm kê/cảnh báo → điều chỉnh hoặc chuyển cấp và phản hồi khâu hoạch định |
| S4 | Hỗ trợ | Đăng ký, xác thực OTP và kích hoạt tài khoản thành viên | Truy cập App/Web → tài khoản được tạo/kích hoạt hoặc chuyển chăm sóc khách hàng |
| S1 | Hỗ trợ | Tuyển dụng và tiếp nhận nhân sự chuỗi bán lẻ/kho vận | Yêu cầu tuyển dụng → ký hợp đồng sau thử việc hoặc thanh lý |
| K1 | Hỗ trợ | Nhận hàng, kiểm tra chất lượng và nhập kho từ chủ thương hiệu | Báo giao hàng/hàng cập bến → nhập kệ và cập nhật tồn đầu vào |
| K2 | Hỗ trợ | Xuất kho và điều chuyển phân bổ tới chuỗi cửa hàng | Lệnh phân bổ (từ khâu hoạch định) → cửa hàng nhận và cập nhật tồn |
| K3 | Hỗ trợ | Thu hồi và xử lý hàng trả về / hàng lỗi | Yêu cầu trả hàng → đóng hồ sơ trả hàng và (nếu cần) hoàn tiền |

> **Về mã quy trình:** các mã M3/S3/S4/S1/K1/K2/K3 ở cột đầu chỉ dùng để **đối chiếu với nhãn pool trên sơ đồ BPMN**; toàn bộ phần thân báo cáo gọi theo **tên quy trình** cho dễ đọc.

**Liên hệ giữa các quy trình:** *Lập kế hoạch mua & phân bổ* lập kế hoạch mua và phân bổ theo mùa; *Nhận hàng & nhập kho* nhận hàng từ chủ thương hiệu và cấp **tồn đầu vào**; *Xuất kho & điều chuyển* nhận **đầu ra phân bổ của khâu hoạch định** để xuất kho tới cửa hàng; *Thu hồi & xử lý hàng trả* khép vòng bằng thu hồi hàng lỗi/hàng trả rồi cập nhật lại tồn và hao hụt. *Kiểm kê tồn kho* kiểm soát độ chính xác tồn kho và phản hồi chênh lệch cho khâu hoạch định. *Kích hoạt tài khoản thành viên* tạo tài khoản thành viên — nguồn nhu cầu cho hoạch định. *Tuyển dụng & tiếp nhận nhân sự* cấp nguồn nhân lực vận hành cho toàn chuỗi (đếm tồn ở khâu kiểm kê, bán hàng và hỗ trợ tài khoản, vận hành kho ở cụm kho vận).

### 1.2. Sơ đồ BPMN

Các sơ đồ được vẽ bằng BPMN 2.0 (Pool/Lane, cổng XOR/AND có tách và gộp cùng loại, sự kiện chờ Timer, nhiều sự kiện Kết thúc, luồng thông điệp giữa các pool):

- Năm quy trình **Lập kế hoạch mua & phân bổ, Kiểm kê tồn kho, Nhận hàng & nhập kho, Xuất kho & điều chuyển, Thu hồi & xử lý hàng trả** nằm chung trong một **sơ đồ cộng tác** (collaboration) gồm 5 pool nối bằng luồng thông điệp: [svg/bpmn-kho-van-hanh-k1-k2-k3.drawio.svg](svg/bpmn-kho-van-hanh-k1-k2-k3.drawio.svg) — các pool «Khối hoạch định & phân bổ hàng hóa (M3)», «Quy trình kiểm kê tồn kho nội bộ (S3)», «Nhận hàng, QC & nhập kho (K1)», «Xuất kho & điều chuyển (K2)», «Thu hồi & xử lý hàng trả (K3)» (mã trong ngoặc là nhãn pool để đối chiếu bảng §1.1).
- **Kích hoạt tài khoản thành viên:** [svg/bpmn-dang-ky-kich-hoat-tai-khoan-s3.drawio.svg](svg/bpmn-dang-ky-kich-hoat-tai-khoan-s3.drawio.svg).
- **Tuyển dụng & tiếp nhận nhân sự:** [svg/bpmn-tuyen-dung-nhan-su-s1.drawio.svg](svg/bpmn-tuyen-dung-nhan-su-s1.drawio.svg).

Tệp nguồn draw.io: `HỆ SINH THÁI ACFC MEMBER.drawio` (3 trang).

### 1.3. Nguyên tắc số liệu

Hoạt động và quy tắc công khai được lấy từ trang chủ, trang hướng dẫn tài khoản và trang tuyển dụng ACFC. Các ngưỡng, thời hạn, đơn giá và số liệu vận hành nội bộ chưa có nguồn được gắn nhãn `[giả định]` và **không trình bày như số liệu chính thức đã được ACFC xác nhận**. Con số định lượng minh họa dùng để thể hiện *cách tính*; sau phỏng vấn sẽ thay bằng ba mốc thấp – thường gặp – cao từ dữ liệu thật.

Nguồn công khai chính: [trang chủ ACFC](https://www.acfc.com.vn/home); [hướng dẫn tạo tài khoản](https://www.acfc.com.vn/huong-dan-tao-tai-khoan) và [hướng dẫn kích hoạt tài khoản](https://www.acfc.com.vn/huong-dan-kich-hoat-tai-khoan-thanh-vien) (cho quy trình Kích hoạt tài khoản thành viên); [trang tuyển dụng ACFC](https://tuyendung.acfc.com.vn) cùng các mô tả công việc Product Manager, Operations Executive, Store Manager, District Supervisor (cho các quy trình Lập kế hoạch, Kiểm kê tồn kho, Tuyển dụng).

---

## 2. Lập kế hoạch mua hàng và phân bổ theo mùa

### 2.1. Mô tả hiện trạng (AS-IS)

**Người kích hoạt:** bộ phận Hàng hóa/Phân bổ (theo lịch mùa) hoặc hệ thống cảnh báo lệch tỷ lệ bán qua / số tháng tồn kho.
**Người hưởng lợi:** Vận hành và cửa hàng (nhận đúng cơ cấu hàng), Tài chính thương mại (kiểm soát ngân sách) — trực tiếp; khách hàng cuối (có hàng đúng nhu cầu) — gián tiếp.
**Ranh giới:** từ khi bước vào kỳ kế hoạch/phát hiện lệch mục tiêu đến khi phát hành kế hoạch mua hàng/yêu cầu điều chuyển. Các bước nhận và điều chuyển nội bộ nằm ở Nhận hàng & nhập kho/Xuất kho & điều chuyển, ngoài phạm vi mô tả của Lập kế hoạch mua & phân bổ.

| # | Người thực hiện | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Hàng hóa/Phân bổ | Thu thập dữ liệu bán hàng, tồn kho và dự báo | Từ hệ thống ERP/báo cáo bán hàng |
| 2 | Hàng hóa/Phân bổ | Chốt dự báo nhu cầu theo mùa | — |
| 3 | Hàng hóa/Phân bổ | Phân tích tỷ lệ bán qua và số tháng tồn kho | So với mục tiêu theo nhãn hàng/mã hàng |
| 4 | Hàng hóa/Phân bổ | Lập kế hoạch mua hàng và phân bổ theo cửa hàng | Cổng điều kiện: dữ liệu đã đủ và khớp nguồn chưa? |
| 5 | Tài chính thương mại | Kiểm tra biên lợi nhuận và ngân sách | Cổng điều kiện: nằm trong ngân sách không? |
| 6 | Vận hành | Kiểm tra sức chứa cửa hàng | Chạy song song với bước 7 qua cặp cổng AND |
| 7 | Hàng hóa/Phân bổ | Xác nhận nguồn hàng khả dụng | Chạy song song với bước 6 |
| 8 | Hàng hóa/Phân bổ | Trình kế hoạch phân bổ để phê duyệt | — |
| 9 | Cấp phê duyệt | Phê duyệt kế hoạch phân bổ | Cổng điều kiện: được duyệt không? |
| 10 | Hàng hóa/Phân bổ | Phát hành kế hoạch mua hàng/yêu cầu điều chuyển | Cổng điều kiện: đồng bộ WMS thành công không? |
| 11 | Hàng hóa/Phân bổ | Theo dõi kết quả và tiếp nhận dữ liệu chênh lệch từ Kiểm kê tồn kho | Đầu vào cho chu kỳ kế hoạch tiếp theo |

**Kịch bản thành công:** dữ liệu đầy đủ → dự báo được chốt → xác nhận lệch mục tiêu → kế hoạch nằm trong ngân sách → (song song) cửa hàng đủ sức chứa **và** nguồn hàng khả dụng → được duyệt ngay lần trình đầu → phát hành lệnh mua và đồng bộ WMS thành công. **Kết quả:** "Kế hoạch mua hàng và phân bổ đã được duyệt và phát hành."

**Kịch bản thất bại/ngoại lệ:**
- Dữ liệu thiếu hoặc chưa khớp nguồn → quay lại thu thập/bổ sung trước khi phân tích.
- Vượt biên lợi nhuận/ngân sách → Tài chính thương mại yêu cầu điều chỉnh kế hoạch (quay lại bước lập kế hoạch) hoặc từ chối nếu vượt quá nhiều.
- Cửa hàng không đủ sức chứa → điều chỉnh số lượng phân bổ hoặc giãn lịch giao.
- Nguồn hàng không khả dụng → ghi nhận thiếu hàng, tìm nguồn thay thế hoặc lùi kế hoạch.
- Kế hoạch không được duyệt → quay lại chỉnh sửa; nếu lặp lại nhiều lần thì chuyển cấp phê duyệt cao hơn — ngưỡng số lần `[giả định]`.

**Cấu trúc BPMN:** pool «Khối hoạch định & phân bổ hàng hóa (Lập kế hoạch mua & phân bổ)» với các lane Hàng hóa/Phân bổ, Tài chính thương mại, Vận hành và Cấp phê duyệt. Các cổng quyết định đều là cổng XOR (dữ liệu đủ chưa; trong ngân sách không; được duyệt không; đồng bộ WMS thành công không), mỗi cổng rẽ thành nhánh loại trừ nhau và nhánh tiêu cực quay lại bước phù hợp hoặc dẫn tới sự kiện Kết thúc riêng. Hai bước kiểm tra sức chứa và xác nhận nguồn hàng chạy song song qua **một cặp cổng AND tách/gộp cùng loại** nên cân bằng, không gây kẹt luồng.

### 2.2. Phân tích định tính

#### a. Phân loại hoạt động VA/BVA/NVA

| Hoạt động | Phân loại | Nhận xét |
|---|---|---|
| Lập kế hoạch mua hàng và phân bổ | VA | Tạo cơ cấu hàng phù hợp nhu cầu cửa hàng |
| Thu thập dữ liệu bán hàng, tồn kho, dự báo | BVA | Cần cho quyết định; nên dùng một bộ dữ liệu chuẩn |
| Phân tích tỷ lệ bán qua và số tháng tồn kho | BVA | Hỗ trợ lập kế hoạch; tự động hóa bảng theo dõi |
| Kiểm tra biên lợi nhuận và ngân sách | BVA | Kiểm soát tài chính; đặt quy tắc tự động |
| Chờ dữ liệu hoặc chờ phê duyệt | NVA | Chờ (Hold); đặt thời hạn và cảnh báo quá hạn |
| Nhập/đối chiếu trùng cùng một báo cáo | NVA | Xử lý dư (Over-processing); dùng một nguồn dữ liệu gốc |
| Lập lại kế hoạch do dữ liệu sai | NVA | Lỗi (Defects); kiểm tra bắt buộc trước khi trình |

#### b. Phân tích lãng phí (Move – Hold – Over-processing – Defects)

| Bước | Loại lãng phí | Biểu hiện | Tác động | Khắc phục |
|---|---|---|---|---|
| Luân chuyển kế hoạch/báo cáo | Di chuyển (Move) | Bản kế hoạch chuyển qua nhiều kênh rời (email, chat, bảng tính) | Khó truy vết, dễ dùng nhầm phiên bản | Gộp về một nơi lưu trữ dùng chung, một mã kế hoạch theo mùa |
| Chờ phê duyệt/ngân sách | Chờ (Hold) | Chờ báo cáo, ngân sách, phê duyệt không có hạn xử lý | Kéo dài chu kỳ lập kế hoạch, lỡ thời điểm mùa vụ | Đặt thời hạn từng bước duyệt, gắn người phụ trách, cảnh báo quá hạn |
| Đối chiếu dữ liệu nhiều nguồn | Xử lý dư (Over-processing) | Nhập/đối chiếu trùng dữ liệu bán hàng – tồn kho từ nhiều nguồn | Tốn công, dễ sai lệch giữa các bản | Chuẩn hóa một nguồn dữ liệu gốc, tự động hóa bảng theo dõi |
| Lập lại kế hoạch | Lỗi (Defects) | Dự báo/mã hàng sai khiến phải lập lại | Tốn thêm giờ công, chậm phát hành | Kiểm tra dữ liệu gốc và khóa phiên bản trước khi trình |

#### c. Phân tích các bên liên quan

| Bên liên quan | Vai trò trong quy trình này | Mối quan tâm chính | Vấn đề tác động |
|---|---|---|---|
| Hàng hóa/Phân bổ | Chủ quy trình, lập và phát hành kế hoạch | Kế hoạch đúng nhu cầu, phát hành kịp mùa | Dữ liệu chưa đồng nhất, phải lập lại |
| Tài chính thương mại | Kiểm soát biên lợi nhuận và ngân sách | Không vượt ngân sách | Chờ phản hồi, vòng lặp điều chỉnh |
| Vận hành/cửa hàng | Nhận cơ cấu hàng theo kế hoạch | Đúng hàng, đủ sức chứa | Phân bổ lệch nhu cầu gây đọng vốn hoặc thiếu hàng |
| Cấp phê duyệt | Duyệt kế hoạch phân bổ | Kế hoạch hợp lý, đúng thẩm quyền | Thiếu tiêu chí/thời hạn duyệt thống nhất |
| Kiểm kê tồn kho | Cấp dữ liệu chênh lệch/hao hụt phản hồi | Tồn chính xác để hiệu chỉnh kế hoạch | Chênh lệch phát hiện muộn |

#### d. Vấn đề nổi bật (Issue register)

Cấu trúc: **Nguyên nhân** (xác định bằng 5 Why ở mục 2.4, khác với vấn đề tự suy ra từ mô tả) → **Tác động** → **Giải pháp**.

| Vấn đề | Nguyên nhân | Tác động | Giải pháp |
|---|---|---|---|
| Chờ phê duyệt kéo dài | Thiếu thời hạn và tiêu chí duyệt thống nhất giữa các cấp | Lỡ thời điểm mùa vụ, chu kỳ lập kế hoạch dài | Đặt thời hạn từng bước duyệt, hàng đợi quá hạn, tự động chuyển cấp |
| Phân bổ lệch nhu cầu | Số tháng tồn, tỷ lệ bán qua, sức chứa chưa đồng bộ trên một bảng theo dõi | Đọng vốn tồn dư ở nơi này, thiếu hàng ở nơi khác | Bảng theo dõi chung, quy tắc phân bổ theo dữ liệu bán và sức chứa |
| Phải lập lại kế hoạch | Dữ liệu dự báo/tồn/gốc chưa đồng nhất | Tốn giờ công, phát hành trễ | Khóa phiên bản dữ liệu, kiểm tra bắt buộc trước khi trình |

### 2.3. Phân tích định lượng

> Số dưới đây là **số minh họa cách tính** `[giả định]`, chưa phải số vận hành thật của ACFC.

#### a. Phân tích thời gian

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Thời gian chu kỳ lập kế hoạch | Thời điểm phát hành − thời điểm bắt đầu | 09:00 ngày 1 → 17:00 ngày 5 | 40 giờ |
| Thời gian xử lý thực (VA+BVA) | Tổng thời gian các bước tạo/kiểm/duyệt | ≈ 14 giờ | 14 giờ |
| Thời gian chờ (NVA) | Chu kỳ − thời gian xử lý | 40 − 14 | 26 giờ |
| Hiệu suất chu kỳ (PCE) | Thời gian xử lý / chu kỳ | 14 / 40 | ≈ 35% |

PCE ≈ 35% nghĩa là gần hai phần ba thời gian là chờ (NVA), khớp với lãng phí "Chờ (Hold)" ở mục 2.2.b.

#### b. Phân tích chi phí

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Chi phí chờ phê duyệt | Số kế hoạch × giờ chờ × đơn giá giờ | 4 × 26 giờ × 150.000đ | 15.600.000đ / mùa |
| Chi phí đọng vốn tồn dư | Giá trị tồn dư × chi phí giữ hàng/tháng × số tháng | 200 sp × 300.000đ × 2% × 4 | 4.800.000đ / mùa |
| Chi phí lập lại kế hoạch | Số lần lập lại × giờ công × đơn giá giờ | 2 × 8 giờ × 150.000đ | 2.400.000đ / mùa |

### 2.4. Phân tích nguyên nhân gốc

#### Ưu tiên vấn đề bằng Pareto

Ba vấn đề ở mục 2.2.d được quy về **cùng đơn vị** — chi phí kỳ vọng mỗi mùa (nghìn đồng) — để xếp thứ tự ưu tiên. Toàn bộ số liệu là `[giả định]` từ mục 2.3.

| Vấn đề | Chi phí kỳ vọng (nghìn đồng) `[giả định]` | Tỷ trọng | Lũy kế |
|---|---|---|---|
| Chờ phê duyệt kéo dài | 15.600 | 68,4% | 68,4% |
| Phân bổ lệch nhu cầu (đọng vốn tồn dư) | 4.800 | 21,1% | 89,5% |
| Phải lập lại kế hoạch | 2.400 | 10,5% | 100,0% |
| **Tổng** | **22.800** | 100% | — |

Theo nguyên tắc 80/20, hai vấn đề đầu chiếm 89,5% tổng thiệt hại kỳ vọng — là nhóm "số ít quan trọng" cần ưu tiên; riêng **chờ phê duyệt** đã chiếm 68,4% nên xử lý trước.

#### Phân tích 5 Why (cho vấn đề ưu tiên: chờ phê duyệt kéo dài)

1. **Vì sao phê duyệt kéo dài?** → Vì kế hoạch nằm chờ ở từng cấp mà không có hạn xử lý.
2. **Vì sao không có hạn xử lý?** → Vì chưa đặt thời hạn và tiêu chí duyệt thống nhất giữa các cấp.
3. **Vì sao chưa có thời hạn/tiêu chí thống nhất?** → Vì việc trình duyệt qua nhiều kênh rời rạc, không có hàng đợi và trạng thái tập trung.
4. **Vì sao qua nhiều kênh rời rạc?** → Vì chưa có một nơi quản lý luồng duyệt chung, mỗi cấp dùng công cụ riêng.
5. **Vì sao chưa có nơi quản lý chung?** → Vì chưa đo thời gian chờ ở từng cấp để thấy tác động và đặt yêu cầu số hóa luồng duyệt.

**Nguyên nhân gốc:** thiếu cơ chế đo thời gian chờ theo cấp và thiếu một luồng duyệt tập trung có thời hạn → dẫn tới chuỗi hệ quả kết thúc ở chu kỳ lập kế hoạch bị kéo dài.

### 2.5. Phỏng vấn bổ sung

1. Độ chính xác dự báo và tỷ lệ bán qua thực tế theo mùa là bao nhiêu?
2. Số tháng tồn kho bình quân mục tiêu và thực tế là bao nhiêu?
3. Thời gian lập kế hoạch và thời gian phê duyệt trung bình là bao lâu (thay số minh họa 40 giờ / 44 giờ)?
4. Cấp nào phê duyệt kế hoạch và điều kiện/thời hạn duyệt là gì?
5. Đơn giá giờ công lập kế hoạch và chi phí giữ hàng/tháng thực tế là bao nhiêu?

### 2.6. Đề xuất cải tiến (TO-BE)

Theo thứ tự ưu tiên Pareto ở mục 2.4:

1. **Chờ phê duyệt (ưu tiên cao nhất)** — đưa luồng trình duyệt lên một nơi tập trung có thời hạn từng cấp, hàng đợi quá hạn và tự động chuyển cấp; đo thời gian chờ theo cấp để cải tiến liên tục.
2. **Phân bổ lệch nhu cầu** — chuẩn hóa một bảng theo dõi chung tỷ lệ bán qua / số tháng tồn / sức chứa, áp quy tắc phân bổ dựa trên dữ liệu bán và sức chứa cửa hàng.
3. **Lập lại kế hoạch** — khóa phiên bản dữ liệu gốc và bắt buộc kiểm tra trước khi trình để giảm sai sót phải làm lại.

---

## 3. Kiểm kê và xử lý chênh lệch tồn kho

### 3.1. Mô tả hiện trạng (AS-IS)

**Người kích hoạt:** Quản lý/Kiểm soát tồn kho (theo lịch định kỳ) hoặc hệ thống cảnh báo tồn thực tế lệch sổ.
**Người hưởng lợi:** Hàng hóa/Vận hành (Lập kế hoạch mua & phân bổ) và Kế toán doanh thu/Tài chính (cần tồn chính xác) — trực tiếp; cửa hàng (giảm thất thoát) và khách hàng (đúng hàng sẵn có) — gián tiếp.
**Ranh giới:** từ lịch kiểm kê/cảnh báo chênh lệch đến khi đóng hồ sơ và phản hồi cho Lập kế hoạch mua & phân bổ.

| # | Người thực hiện | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Quản lý/Kiểm soát tồn kho | Lập lịch kiểm kê | Sự kiện định kỳ hoặc cảnh báo hệ thống |
| 2 | Kiểm soát tồn kho/Vận hành | Xác định phạm vi và mẫu đếm | — |
| 3 | Quản lý | Duyệt phạm vi kiểm kê | Cổng điều kiện: phạm vi được duyệt không? |
| 4 | Cửa hàng/Kho | Chuẩn bị phiếu kiểm kê và đếm tồn thực tế | — |
| 5 | Kiểm soát tồn kho/Vận hành | Đối chiếu tồn thực tế với sổ tồn | Từ hệ thống ERP/quản lý kho |
| 6 | Kiểm soát tồn kho/Vận hành | Xác định điều kiện đếm lại | Cổng điều kiện: cần đếm lại không? |
| 7 | Kiểm soát tồn kho/Vận hành | Phân loại nguyên nhân chênh lệch | Cổng điều kiện: trong ngưỡng điều chỉnh hay vượt ngưỡng? |
| 8 | Kiểm soát tồn kho/Vận hành | Lập đề nghị điều chỉnh tồn (nếu trong ngưỡng) | Chạy song song với bước 9 qua cặp cổng AND |
| 9 | Kiểm soát tồn kho/Vận hành | Lập báo cáo hao hụt/sự cố và chuyển cấp (nếu vượt ngưỡng) | Chạy song song với bước 8 |
| 10 | Quản lý/Kế toán doanh thu | Phê duyệt điều chỉnh hoặc bút toán hao hụt | Cổng điều kiện: được duyệt không? |
| 11 | Kiểm soát tồn kho/Vận hành | Cập nhật hệ thống tồn kho và đóng hồ sơ | Cổng điều kiện: đóng đúng hạn không? |
| 12 | Kiểm soát tồn kho/Vận hành | Gửi kết quả phản hồi cho Lập kế hoạch mua & phân bổ | Đầu vào chu kỳ lập kế hoạch tiếp theo |

**Kịch bản thành công:** đến kỳ kiểm kê → phạm vi được duyệt → đếm khớp sổ ngay lần đầu → hồ sơ được đóng đúng hạn, không phát sinh điều chỉnh. **Kết quả:** "Kiểm kê khớp sổ, hồ sơ đã đóng đúng hạn." Nếu có chênh lệch trong ngưỡng: xác định đúng nguyên nhân → đề nghị điều chỉnh được duyệt → cập nhật hệ thống → đóng hồ sơ → phản hồi Lập kế hoạch mua & phân bổ.

**Kịch bản thất bại/ngoại lệ:**
- Đếm không khớp sổ và điều kiện đếm lại được kích hoạt → quay lại đếm lại; nếu vẫn lệch thì xác định nguyên nhân sâu hơn.
- Không xác định được nguyên nhân trong thời hạn → lập báo cáo tạm với nhãn "nguyên nhân chưa xác định", có thể chuyển cấp sớm.
- Chênh lệch vượt ngưỡng hoặc có dấu hiệu hao hụt → lập báo cáo sự cố riêng, chuyển cấp xác minh trách nhiệm — ngưỡng và cấp chuyển `[giả định]`.
- Điều chỉnh không được duyệt → yêu cầu bổ sung bằng chứng, quay lại phân loại nguyên nhân.
- Hồ sơ không đóng đúng hạn → gắn cờ quá hạn, báo cáo cho Quản lý.

**Cấu trúc BPMN:** pool «Quy trình kiểm kê tồn kho nội bộ (Kiểm kê tồn kho)» với các lane Quản lý, Kiểm soát tồn kho/Vận hành, Cửa hàng/Kho và Kế toán kho. Các cổng quyết định đều là cổng XOR (duyệt phạm vi; cần đếm lại; trong/vượt ngưỡng; được duyệt; đóng đúng hạn) với nhánh loại trừ nhau và nhánh tiêu cực quay lại hoặc dẫn tới sự kiện Kết thúc riêng. Bước lập đề nghị điều chỉnh và lập báo cáo hao hụt chạy song song qua **một cặp cổng AND tách/gộp cùng loại** nên cân bằng.

### 3.2. Phân tích định tính

#### a. Phân loại hoạt động VA/BVA/NVA

| Hoạt động | Phân loại | Nhận xét |
|---|---|---|
| Điều chỉnh tồn được phê duyệt | VA | Đưa sổ sách về đúng thực tế — cơ sở cho quản trị và tài chính |
| Đếm tồn thực tế | BVA | Bằng chứng tồn thực tế; nên quét mã để giảm sai |
| Đối chiếu với sổ tồn | BVA | Phát hiện sai lệch |
| Đếm lại khi có chênh lệch | BVA | Cần xác minh trước điều chỉnh |
| Chờ phê duyệt hoặc bằng chứng | NVA | Chờ (Hold); đặt thời hạn và chuyển cấp |
| Đếm lại do bàn giao không đủ chứng từ | NVA | Lỗi (Defects); chuẩn hóa biên bản và quét mã |
| Nhập cùng điều chỉnh ở nhiều nơi | NVA | Xử lý dư (Over-processing); dùng một hồ sơ điều chỉnh gốc |

#### b. Phân tích lãng phí (Move – Hold – Over-processing – Defects)

| Bước | Loại lãng phí | Biểu hiện | Tác động | Khắc phục |
|---|---|---|---|---|
| Luân chuyển phiếu/biên bản | Di chuyển (Move) | Phiếu kiểm kê/biên bản chuyển qua nhiều đầu mối giấy tờ | Chậm, dễ thất lạc chứng từ | Chuyển sang hồ sơ điện tử, một mã vụ việc mỗi đợt |
| Chờ đếm lại/giải trình/duyệt | Chờ (Hold) | Chờ phê duyệt điều chỉnh không có hạn rõ ràng | Chênh lệch quá hạn, tồn sai kéo dài | Đặt thời hạn, hàng đợi quá hạn, người phụ trách từng bước |
| Đếm/đối chiếu trùng | Xử lý dư (Over-processing) | Đếm/nhập/đối chiếu trùng dữ liệu tồn ở nhiều nơi | Tốn công, dễ sai lệch | Kiểm kê theo mức rủi ro, dùng một hồ sơ điều chỉnh gốc |
| Chênh lệch lặp lại | Lỗi (Defects) | Chênh lệch lặp lại, thiếu bằng chứng, sai giao dịch | Hao hụt không giải thích được, mất độ tin cậy tồn | Quét mã khi đếm, nhật ký kiểm tra, mã nguyên nhân chuẩn |

#### c. Phân tích các bên liên quan

| Bên liên quan | Vai trò trong quy trình này | Mối quan tâm chính | Vấn đề tác động |
|---|---|---|---|
| Kiểm soát tồn kho/Vận hành | Chủ quy trình, đếm và đối chiếu | Tồn chính xác, đóng đúng hạn | Chênh lệch lặp lại, phải đếm lại |
| Quản lý | Duyệt phạm vi và điều chỉnh | Kiểm soát rủi ro thất thoát | Chờ phê duyệt, chênh lệch quá hạn |
| Cửa hàng/Kho | Đếm tồn thực tế | Ít gián đoạn bán hàng | Chuẩn bị chứng từ chưa đủ |
| Kế toán doanh thu/Tài chính | Duyệt bút toán hao hụt | Sổ sách khớp thực tế | Hao hụt không giải thích được |
| Lập kế hoạch mua & phân bổ | Nhận phản hồi chênh lệch | Tồn chính xác để hoạch định | Chênh lệch phát hiện muộn |

#### d. Vấn đề nổi bật (Issue register)

Cấu trúc: **Nguyên nhân** (xác định bằng 5 Why ở mục 3.4) → **Tác động** → **Giải pháp**.

| Vấn đề | Nguyên nhân | Tác động | Giải pháp |
|---|---|---|---|
| Hao hụt không giải thích được | Giao dịch nhập/xuất chưa cập nhật kịp và đếm thủ công dễ sai | Xóa sổ/bồi thường giá trị thiếu, giảm độ tin cậy tồn | Quét mã khi đếm, khóa thời điểm kiểm kê, đối chiếu giao dịch trước điều chỉnh |
| Chênh lệch quá hạn chưa đóng | Chờ đếm lại/giải trình/phê duyệt không có thời hạn | Tồn sai kéo dài, ảnh hưởng hoạch định Lập kế hoạch mua & phân bổ | Đặt thời hạn từng bước, hàng đợi quá hạn, chuyển cấp theo rủi ro |
| Điều chỉnh lặp lại nhiều kỳ | Chưa phân loại và xử lý nguyên nhân gốc | Lặp lại công kiểm kê, chi phí đếm lại | Mã nguyên nhân chuẩn, nhật ký kiểm tra, phản hồi về Lập kế hoạch mua & phân bổ |

### 3.3. Phân tích định lượng

> Số dưới đây là **số minh họa cách tính** `[giả định]`.

#### a. Phân tích thời gian

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Thời gian chu kỳ kiểm kê | Thời điểm đóng hồ sơ − thời điểm bắt đầu | 20:00 → 08:00 hôm sau | 12 giờ |
| Thời gian đếm thực tế (VA+BVA) | Tổng thời gian đếm + đối chiếu | ≈ 4 giờ | 4 giờ |
| Thời gian chờ (NVA) | Chờ duyệt phạm vi + chờ duyệt điều chỉnh | ≈ 6 giờ | 6 giờ |
| Hiệu suất chu kỳ (PCE) | Thời gian đếm / chu kỳ | 4 / 12 | ≈ 33% |

#### b. Phân tích chi phí

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Chi phí hao hụt phải xóa sổ/bồi thường | Giá trị thiếu không thu hồi được | Theo đợt kiểm kê | 3.000.000đ / đợt |
| Chi phí chờ & chênh lệch quá hạn | Số hồ sơ quá hạn × giờ chờ × đơn giá giờ | 2 × 6 giờ × 120.000đ | 1.440.000đ / đợt |
| Chi phí đếm lại | Số giờ đếm lại × đơn giá giờ | 6 giờ × 120.000đ | 720.000đ / đợt |

### 3.4. Phân tích nguyên nhân gốc

#### Ưu tiên vấn đề bằng Pareto

Ba vấn đề ở mục 3.2.d được quy về **cùng đơn vị** — chi phí kỳ vọng mỗi đợt kiểm kê (nghìn đồng). Toàn bộ số liệu là `[giả định]` từ mục 3.3.

| Vấn đề | Chi phí kỳ vọng (nghìn đồng) `[giả định]` | Tỷ trọng | Lũy kế |
|---|---|---|---|
| Hao hụt không giải thích được | 3.000 | 58,1% | 58,1% |
| Chênh lệch quá hạn (chi phí chờ) | 1.440 | 27,9% | 86,0% |
| Điều chỉnh lặp lại (chi phí đếm lại) | 720 | 14,0% | 100,0% |
| **Tổng** | **5.160** | 100% | — |

Theo nguyên tắc 80/20, hai vấn đề đầu chiếm 86,0% tổng thiệt hại kỳ vọng; riêng **hao hụt** chiếm 58,1% nên ưu tiên trước.

#### Phân tích 5 Why (cho vấn đề ưu tiên: hao hụt không giải thích được)

1. **Vì sao có hao hụt không giải thích được?** → Vì tồn thực tế lệch sổ mà không truy được giao dịch tương ứng.
2. **Vì sao không truy được giao dịch?** → Vì giao dịch nhập/xuất/điều chuyển chưa được cập nhật kịp thời vào hệ thống khi đếm.
3. **Vì sao cập nhật chưa kịp thời?** → Vì thời điểm kiểm kê không được "khóa" và đếm thủ công không quét mã nên khó đối chiếu.
4. **Vì sao chưa khóa thời điểm và chưa quét mã?** → Vì quy trình kiểm kê chưa chuẩn hóa công cụ đếm và mốc đóng băng giao dịch.
5. **Vì sao chưa chuẩn hóa?** → Vì chưa đo tỷ lệ chênh lệch/hao hụt theo nguyên nhân để đặt yêu cầu chuẩn hóa công cụ.

**Nguyên nhân gốc:** thiếu mốc khóa giao dịch khi kiểm kê và thiếu công cụ đếm quét mã kèm mã nguyên nhân → chênh lệch không truy được, kết lại thành hao hụt phải xóa sổ.

### 3.5. Phỏng vấn bổ sung

1. Độ chính xác tồn kho và tỷ lệ hao hụt thực tế mỗi đợt là bao nhiêu?
2. Tỷ lệ đếm lại và tỷ lệ điều chỉnh thực tế là bao nhiêu (thay số minh họa 8% / 15%)?
3. Ngưỡng điều chỉnh tồn và cấp phê duyệt tương ứng là gì?
4. Thời gian kiểm kê trung bình và tỷ lệ đóng hồ sơ đúng hạn là bao nhiêu?
5. Đơn giá giờ công kiểm kê thực tế là bao nhiêu (thay số minh họa 120.000đ/giờ)?

### 3.6. Đề xuất cải tiến (TO-BE)

Theo thứ tự ưu tiên Pareto ở mục 3.4:

1. **Hao hụt (ưu tiên cao nhất)** — khóa thời điểm kiểm kê (đóng băng giao dịch), quét mã khi đếm, đối chiếu giao dịch trước khi điều chỉnh, gắn mã nguyên nhân cho mỗi chênh lệch.
2. **Chênh lệch quá hạn** — đặt thời hạn xử lý từng bước, hàng đợi quá hạn và chuyển cấp theo rủi ro.
3. **Điều chỉnh lặp lại** — dùng mã nguyên nhân chuẩn và nhật ký kiểm tra, phản hồi về Lập kế hoạch mua & phân bổ để xử lý nguyên nhân gốc ở chu kỳ sau.

---

## 4. Đăng ký, xác thực OTP và kích hoạt tài khoản thành viên

### 4.1. Mô tả hiện trạng (AS-IS)

**Người kích hoạt:** khách hàng truy cập App/Web ACFC (hoặc quầy POS) để đăng ký/đăng nhập.
**Người hưởng lợi:** khách hàng (mua sắm, tích điểm, ưu đãi theo hạng thẻ) — trực tiếp; ACFC (dữ liệu khách hàng, kênh bán trực tuyến) và bộ phận chăm sóc khách hàng (giảm tải khi khách tự phục vụ trơn tru) — gián tiếp.
**Ranh giới:** từ khi khách truy cập App/Web đến khi tài khoản được tạo/kích hoạt hoặc chuyển sang chăm sóc khách hàng. Không xử lý yêu cầu về quyền dữ liệu cá nhân của chủ thể dữ liệu.

Tài khoản do quy trình này kích hoạt là cửa ngõ vào chương trình khách hàng thân thiết 5 bậc (Member → Silver → Gold → Platinum → Diamond), quản trị tập trung trên Salesforce CRM kết hợp POS Retail Pro Prism và nền tảng thương mại điện tử Magento. *(Bậc hạng và tỷ lệ tích điểm theo chính sách công khai; các định mức chi tiêu để lên hạng là `[giả định]`.)*

| # | Người thực hiện | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Khách hàng | Truy cập App/Web, đồng ý PDPA và nhập số điện thoại | Cổng điều kiện: khách có đồng ý PDPA không? |
| 2 | Salesforce CRM | Kiểm tra trùng số điện thoại | Cổng điều kiện: số điện thoại đã tồn tại chưa? |
| 3 | Cổng đăng ký (Frontend) | Khởi tạo hồ sơ tạm trên CRM, gộp dữ liệu cũ nếu có | — |
| 4 | Cổng gửi OTP | Gửi OTP qua Zalo ZNS (kênh chính) hoặc SMS (kênh dự phòng) | Thời hạn hiệu lực OTP `[giả định]` |
| 5 | Hệ thống | Kiểm tra trạng thái cổng gửi OTP | Cổng điều kiện: cổng gửi OTP có lỗi không? |
| 6 | Chăm sóc khách hàng | Xác minh thủ công qua tổng đài 1900 3038 (khi cổng OTP lỗi) | Nhánh ngoại lệ |
| 7 | Sự kiện chờ (Timer) | Chờ khách nhập OTP trong thời hạn hiệu lực | Sự kiện trung gian Timer |
| 8 | Khách hàng | Nhập mã xác thực OTP | Cổng điều kiện: OTP hợp lệ và còn hiệu lực không? |
| 9 | Hệ thống | Kiểm tra số lần nhập sai OTP | Cổng điều kiện: sai quá giới hạn cho phép chưa? |
| 10 | Khách hàng | Điền thông tin cá nhân và tạo mật khẩu | Cổng điều kiện: mật khẩu đạt chuẩn và đồng ý điều khoản chưa? |
| 11 | Salesforce CRM | Tạo tài khoản và cấp mã thành viên | — |
| 12 | Hệ thống tích hợp | Đồng bộ hồ sơ sang Magento (Web/App) và Retail Pro Prism (POS) | Cổng điều kiện: đồng bộ có thành công không? |
| 13 | Hệ thống | Kích hoạt tài khoản: tự động đăng nhập, tặng ưu đãi chào mừng, cập nhật hạng thẻ | Kết thúc thành công |

**Kịch bản thành công:** đồng ý PDPA → số điện thoại chưa tồn tại → OTP gửi qua Zalo ZNS thành công → khách nhập đúng OTP trong thời hạn → mật khẩu đạt chuẩn và đồng ý điều khoản → tạo mã thành viên → đồng bộ Magento và Retail Pro thành công → kích hoạt tài khoản kèm ưu đãi. **Kết quả:** "Tài khoản được tạo và kích hoạt thành công."

**Kịch bản thất bại/ngoại lệ:**
- Không đồng ý PDPA → hủy đăng ký (kết thúc).
- Số điện thoại đã tồn tại → điều hướng sang đăng nhập/lấy lại mật khẩu (kết thúc).
- Cổng OTP lỗi → chăm sóc khách hàng xác minh thủ công qua tổng đài 1900 3038.
- Nhập sai OTP quá giới hạn → khóa tạm và chuyển chăm sóc khách hàng; ngưỡng số lần và thời gian khóa `[giả định]`.
- Mật khẩu chưa đạt chuẩn/chưa đồng ý điều khoản → quay lại bước điền thông tin.
- Đồng bộ Magento/Retail Pro thất bại → đưa vào hàng đợi gửi lại và cảnh báo bộ phận kỹ thuật.

**Cấu trúc BPMN:** 1 Pool "Hệ sinh thái ACFC Member" với 5 Lane (Khách hàng; Cổng đăng ký – Frontend; Salesforce CRM; Cổng gửi OTP – ZNS/SMS; Chăm sóc khách hàng & Đồng bộ), 8 cổng điều kiện, 1 sự kiện chờ (Timer) và nhiều sự kiện Kết thúc (hủy đăng ký / điều hướng đăng nhập / khóa tạm → chăm sóc khách hàng / kích hoạt xong).

Về logic cổng: các cổng quyết định là cổng XOR — mỗi cổng rẽ thành các nhánh loại trừ nhau, nhánh tiêu cực dẫn thẳng tới một sự kiện Kết thúc riêng nên không cần gộp lại. Riêng bước chọn kênh gửi OTP là **một cổng XOR tách nhánh** (Zalo ZNS hoặc SMS); hai nhánh này **hợp lại tại một cổng XOR gộp** trước khi kiểm tra trạng thái cổng OTP — cổng tách và cổng gộp **cùng loại XOR** nên cân bằng, không gây kẹt luồng (deadlock).

### 4.2. Phân tích định tính

#### a. Phân loại hoạt động VA/BVA/NVA

| Hoạt động | Phân loại | Nhận xét |
|---|---|---|
| Nhập số điện thoại/thông tin cá nhân | BVA | Cần để tạo hồ sơ và định danh tài khoản |
| Nhận và xác nhận mã OTP | BVA | Xác thực bảo mật trước khi tạo tài khoản |
| Tạo và kích hoạt tài khoản | VA | Giá trị trực tiếp — khách mua sắm và hưởng ưu đãi thành viên |
| Đăng nhập bằng mật khẩu đã lưu | VA | Truy cập ngay quyền lợi thành viên |
| Chờ nhận OTP/mật khẩu tạm | NVA | Chờ (Hold); rút ngắn thời gian gửi và có kênh dự phòng |
| Nhập lại OTP do sai/hết hạn | NVA | Lỗi (Defects); cho gửi lại OTP mà không phải nhập lại toàn bộ thông tin |
| Đăng ký lại từ đầu khi OTP hết hạn | NVA | Xử lý dư (Over-processing); lưu tạm dữ liệu đã nhập trong phiên |
| Liên hệ chăm sóc khách hàng qua nhiều kênh rời rạc | NVA | Di chuyển (Move); hợp nhất đầu mối hỗ trợ ngay trên trang đăng ký/đăng nhập |

Quy trình này có 2 hoạt động VA, 2 hoạt động BVA và 4 hoạt động NVA. Đây là quy trình tự phục vụ nên tỷ trọng NVA cao hơn các quy trình có nhân sự trực tiếp phục vụ — phần lớn NVA gắn với thời gian chờ và các bước phát sinh khi có lỗi (OTP sai/hết hạn, phải đăng ký lại, phải liên hệ chăm sóc khách hàng).

#### b. Phân tích lãng phí (Move – Hold – Over-processing – Defects)

| Bước | Loại lãng phí | Biểu hiện | Tác động | Khắc phục |
|---|---|---|---|---|
| Liên hệ hỗ trợ khi gặp lỗi | Di chuyển (Move) | Khách tự tìm tổng đài/fanpage/Zalo/email khi gặp lỗi, không có đầu mối tại chỗ | Khách rời khỏi luồng đăng ký để tìm kênh hỗ trợ, dễ bỏ dở | Thêm nút hỗ trợ/chatbot ngay trên trang đăng ký/đăng nhập |
| Gửi và xác thực OTP | Chờ (Hold) | Chờ nhận OTP/mật khẩu tạm qua Zalo ZNS/SMS | Kéo dài thời gian hoàn tất, tăng nguy cơ bỏ dở khi chờ lâu | Rút ngắn thời gian gửi, thêm kênh dự phòng, hiển thị đếm ngược hiệu lực OTP |
| Đăng ký lại khi OTP hết hạn | Xử lý dư (Over-processing) | Khách nhập lại toàn bộ thông tin thay vì chỉ gửi lại OTP | Tăng thao tác thừa, tăng khả năng bỏ dở giữa chừng | Lưu tạm dữ liệu đã nhập trong phiên, chỉ yêu cầu gửi lại OTP |
| Nhập lại OTP / số điện thoại đã tồn tại | Lỗi (Defects) | OTP sai/hết hạn, số điện thoại đã tồn tại nhưng thông báo lỗi chung chung | Khách không biết bước tiếp theo, phải tự đoán hoặc gọi hỗ trợ | Thông báo lỗi cụ thể theo từng nguyên nhân kèm hướng dẫn bước tiếp theo |

#### c. Phân tích các bên liên quan

| Bên liên quan | Vai trò trong quy trình này | Mối quan tâm chính | Vấn đề tác động |
|---|---|---|---|
| Khách hàng | Người đăng ký, nhập OTP, tạo tài khoản | Đăng ký nhanh, ít lỗi, nhận ưu đãi ngay | Chờ OTP lâu/hết hạn, thông báo lỗi khó hiểu → bỏ dở |
| Cổng đăng ký (Frontend) | Giao diện đăng ký, khởi tạo hồ sơ tạm | Tỷ lệ hoàn tất cao, ít bước rơi rụng | Chưa lưu tạm dữ liệu phiên, thông báo lỗi chưa chuẩn hóa |
| Salesforce CRM | Kiểm tra trùng, tạo tài khoản, cấp mã thành viên | Hồ sơ sạch, không trùng lặp | Gộp dữ liệu cũ chưa rõ quy tắc `[giả định]` |
| Cổng gửi OTP (Zalo ZNS/SMS) | Gửi OTP qua kênh chính/dự phòng | Gửi đúng hạn, chi phí hợp lý | Nghẽn/độ trễ kênh chính, chưa tự chuyển kênh dự phòng kịp |
| Chăm sóc khách hàng & Đồng bộ | Hỗ trợ khi lỗi, xử lý đồng bộ thất bại | Ít yêu cầu phát sinh, xử lý nhanh | Khối lượng yêu cầu tăng do khách không tự khắc phục được |

*(Có thể còn bộ phận Marketing chương trình thành viên và bộ phận kỹ thuật vận hành hệ thống liên quan; xác nhận qua phỏng vấn — xem mục 4.5.)*

#### d. Vấn đề nổi bật (Issue register)

Cấu trúc: **Nguyên nhân** (xác định bằng 5 Why ở mục 4.4, khác với vấn đề tự suy ra từ mô tả) → **Tác động** → **Giải pháp**.

| Vấn đề | Nguyên nhân | Tác động | Giải pháp |
|---|---|---|---|
| Tỷ lệ bỏ dở đăng ký cao | OTP đến chậm hoặc hết hạn, khách phải nhập lại toàn bộ thông tin | Mất khách tiềm năng và doanh thu cơ hội ngay ở cửa ngõ thành viên | Lưu tạm dữ liệu phiên; giám sát độ trễ để tự chuyển kênh dự phòng; điều chỉnh thời hạn hiệu lực OTP theo dữ liệu thực |
| Khách không tự xử lý được lỗi đăng nhập | Thông báo lỗi chung chung, thiếu hướng dẫn bước kế tiếp | Khách bế tắc, hoặc bỏ dở hoặc dồn sang chăm sóc khách hàng | Chuẩn hóa thông báo lỗi theo từng nguyên nhân (OTP sai, số điện thoại đã tồn tại, tài khoản bị khóa) kèm hướng dẫn |
| Khối lượng yêu cầu chăm sóc khách hàng tăng | Thiếu kênh tự phục vụ rõ ràng trên trang đăng ký/đăng nhập | Tăng chi phí nhân công hỗ trợ, thời gian xử lý kéo dài | Tích hợp chatbot/hướng dẫn tự khắc phục ngay tại bước phát sinh lỗi trước khi chuyển chăm sóc khách hàng |

### 4.3. Phân tích định lượng

> Số dưới đây là **số minh họa cách tính** `[giả định]`, sẽ thay bằng ba mốc thấp – thường gặp – cao sau phỏng vấn.

#### a. Phân tích thời gian

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Thời gian hoàn tất đăng ký (chu kỳ) | Thời điểm kích hoạt − thời điểm bắt đầu | 0 → 90 giây | 90 giây |
| Thời gian chờ nhận OTP | Thời điểm nhận OTP − thời điểm gửi | ≈ 20 giây | 20 giây |
| Hiệu suất chu kỳ (PCE) | (Chu kỳ − thời gian chờ) / Chu kỳ | (90 − 20) / 90 | ≈ 78% |
| Thời gian xử lý một yêu cầu chăm sóc khách hàng | Thời điểm đóng − thời điểm khách liên hệ | 09:00 → 11:00 | 2 giờ |

#### b. Phân tích chi phí

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Chi phí gửi OTP | Tổng lượt gửi × đơn giá SMS/ZNS | 1.000 × 300đ | 300.000đ / 1.000 lượt |
| Chi phí xử lý chăm sóc khách hàng | Số lượt × thời gian trung bình × đơn giá giờ công | 60 × 0,25 giờ × 100.000đ | 1.500.000đ |
| Doanh thu cơ hội mất do bỏ dở đăng ký | Số lượt bỏ dở × giá trị đơn bình quân × tỷ lệ chuyển đổi kỳ vọng | 180 × 500.000đ × 10% | 9.000.000đ |

### 4.4. Phân tích nguyên nhân gốc

#### Ưu tiên vấn đề bằng Pareto

Ba vấn đề ở mục 4.2.d được quy về **cùng đơn vị** — chi phí/doanh thu mất kỳ vọng trên 1.000 lượt đăng ký (nghìn đồng). Toàn bộ số liệu là `[giả định]` từ mục 4.3.

| Vấn đề | Chi phí kỳ vọng (nghìn đồng) `[giả định]` | Tỷ trọng | Lũy kế |
|---|---|---|---|
| Bỏ dở đăng ký (doanh thu cơ hội mất) | 9.000 | 78,3% | 78,3% |
| Yêu cầu chăm sóc khách hàng tăng (chi phí nhân công) | 1.500 | 13,0% | 91,3% |
| Lỗi đăng nhập khách không tự xử lý (gửi lại OTP + thao tác dư) | 1.000 | 8,7% | 100,0% |
| **Tổng** | **11.500** | 100% | — |

Theo nguyên tắc 80/20, riêng **"bỏ dở đăng ký"** đã chiếm 78,3% tổng thiệt hại kỳ vọng — gần chạm ngưỡng 80% — nên là vấn đề phải ưu tiên xử lý trước; cộng thêm "yêu cầu chăm sóc khách hàng tăng" thì hai vấn đề đầu chiếm 91,3%. Đây là nhóm "số ít quan trọng" cần tập trung nguồn lực.

#### Phân tích 5 Why (cho vấn đề ưu tiên: bỏ dở đăng ký)

1. **Vì sao khách bỏ dở đăng ký?** → Vì phải chờ OTP lâu hoặc OTP hết hạn trước khi kịp nhập.
2. **Vì sao OTP đến chậm/hết hạn?** → Vì chủ yếu gửi qua một kênh chính (Zalo ZNS); khi kênh nghẽn không tự chuyển kênh dự phòng kịp, và thời hạn hiệu lực đặt cố định, không theo độ trễ thực tế.
3. **Vì sao không tự chuyển kênh dự phòng và để hiệu lực cố định?** → Vì luồng gửi OTP chưa giám sát độ trễ theo thời gian thực để chủ động chuyển SMS, và chưa hiển thị đếm ngược hiệu lực cho khách.
4. **Vì sao chưa giám sát độ trễ và chưa có đếm ngược?** → Vì thiết kế đăng ký tối ưu cho luồng thuận lợi, chưa xử lý kỹ trường hợp gửi OTP trễ.
5. **Vì sao thiết kế chưa xử lý trường hợp trễ OTP?** → Vì chưa đo tỷ lệ hết hạn/độ trễ OTP thực tế để đặt yêu cầu thiết kế; thiếu vòng đo lường – cải tiến dựa trên dữ liệu vận hành.

**Nguyên nhân gốc:** thiếu cơ chế đo lường độ trễ/tỷ lệ hết hạn OTP và thiếu kênh dự phòng tự động kèm lưu tạm dữ liệu phiên → dẫn tới chuỗi hệ quả kết thúc ở việc khách bỏ dở.

### 4.5. Phỏng vấn bổ sung

1. Tỷ lệ đăng ký thành công và tỷ lệ bỏ dở thực tế là bao nhiêu (thay số minh họa 82% / 18%)?
2. Tỷ lệ OTP xác nhận đúng ngay lần đầu và tỷ lệ khách cần hỗ trợ thực tế là bao nhiêu (thay số minh họa 88% / 6%)?
3. Thời gian hoàn tất đăng ký và thời gian chờ OTP trung bình thực tế là bao lâu (thay số minh họa 90 giây / 20 giây)?
4. Đơn giá SMS/ZNS và đơn giá giờ công chăm sóc khách hàng thực tế là bao nhiêu (thay đơn giá minh họa 300đ/lượt, 100.000đ/giờ)?
5. Ngoài 5 bên đã nêu ở mục 4.2.c, còn bộ phận nào (Marketing chương trình thành viên, kỹ thuật vận hành hệ thống…) có mối quan tâm hoặc bị ảnh hưởng bởi quy trình này?

### 4.6. Đề xuất cải tiến (TO-BE)

Theo thứ tự ưu tiên Pareto ở mục 4.4:

1. **Bỏ dở đăng ký (ưu tiên cao nhất)** — lưu tạm dữ liệu đã nhập trong phiên để khi OTP hết hạn chỉ cần gửi lại OTP; giám sát độ trễ để tự chuyển kênh dự phòng (SMS) khi kênh chính nghẽn; hiển thị đếm ngược hiệu lực OTP; theo dõi tỷ lệ hết hạn OTP để điều chỉnh thời hạn hiệu lực hợp lý thay vì cố định.
2. **Yêu cầu chăm sóc khách hàng tăng** — tích hợp chatbot/hướng dẫn tự khắc phục ngay tại bước phát sinh lỗi, hợp nhất đầu mối hỗ trợ trên trang đăng ký/đăng nhập trước khi khách phải chuyển sang tổng đài.
3. **Lỗi đăng nhập khách không tự xử lý** — chuẩn hóa thông báo lỗi theo từng nguyên nhân cụ thể (OTP sai, số điện thoại đã tồn tại, tài khoản bị khóa) kèm hướng dẫn bước tiếp theo.

---

## 5. Tuyển dụng và tiếp nhận nhân sự chuỗi bán lẻ/kho vận

### 5.1. Mô tả hiện trạng (AS-IS)

**Người kích hoạt:** phòng Nhân sự khi có yêu cầu tuyển dụng từ cửa hàng/kho/khối văn phòng.
**Người hưởng lợi:** cửa hàng/kho/khối văn phòng (được bổ sung nhân sự đúng chuẩn) — trực tiếp; toàn chuỗi vận hành (khâu hoạch định, kiểm kê, tài khoản và kho có người thực thi) và ứng viên (có việc làm, được tiếp nhận) — gián tiếp.
**Ranh giới:** từ khi phát sinh yêu cầu tuyển dụng và đăng tin đến khi ký hợp đồng lao động sau thử việc (hoặc thanh lý nếu không đạt). Không bao gồm quản trị lương thưởng, đào tạo dài hạn hay đánh giá hiệu suất định kỳ sau khi đã ký hợp đồng chính thức.

**Phân nhóm đối tượng:** nhân viên cửa hàng (tuyển số lượng lớn, đặc thù bán lẻ, tỷ lệ nghỉ việc cao) và nhân viên văn phòng/kho vận (yêu cầu chuyên môn cao). Kênh thu hút ứng viên: trang tuyển dụng ACFC, TopCV, LinkedIn, VietnamWorks và các hội nhóm mạng xã hội.

| # | Người thực hiện | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Phòng Nhân sự | Đăng tải tin tuyển dụng | Cổng điều kiện: vị trí là nhân viên cửa hàng hay văn phòng/kho? |
| 2 | Hệ thống sàng lọc hồ sơ | Sàng lọc hồ sơ ứng viên | Cổng điều kiện: ứng viên có kinh nghiệm bán lẻ (vào luồng ưu tiên) không? |
| 3 | Chuyên viên tuyển dụng | Kiểm tra lý lịch | Cổng điều kiện: lý lịch đạt chuẩn không? |
| 4 | Quản lý trực tiếp | Phỏng vấn vòng 1 | Cổng điều kiện: đạt vòng 1 không? |
| 5 | Giám đốc Nhân sự/Ban Giám đốc | Phỏng vấn chuyên sâu vòng 2 và 3 (vị trí cấp cao) | Cổng điều kiện: đạt vòng 2/3 không? |
| 6 | Phòng Nhân sự | Đàm phán và chốt thư mời nhận việc | Cổng điều kiện: ứng viên chấp nhận thư mời không? |
| 7 | Nhân sự/Y tế | Khám sức khỏe trước tuyển dụng | Cổng điều kiện: đạt khám sức khỏe theo luật định không? |
| 8 | Nhân sự & Công nghệ thông tin | Triển khai tiếp nhận (đồng phục, đào tạo, cấp tài khoản POS/Retail Pro Prism) | — |
| 9 | Quản lý trực tiếp | Đánh giá thử việc 2 tháng | Chỉ tiêu: doanh số và mức hài lòng khách hàng |
| 10 | Phòng Nhân sự | Xem xét và ký hợp đồng lao động | Cổng điều kiện: đạt chỉ tiêu thử việc không? (đạt → ký; không → thanh lý) |

**Kịch bản thành công:** yêu cầu tuyển dụng rõ ràng → hệ thống lọc được hồ sơ phù hợp (ứng viên có kinh nghiệm bán lẻ → luồng ưu tiên) → kiểm tra lý lịch đạt → vượt phỏng vấn vòng 1 và vòng 2/3 → chấp nhận thư mời → đạt khám sức khỏe → tiếp nhận đầy đủ → đạt chỉ tiêu thử việc 2 tháng → ký hợp đồng chính thức. **Kết quả:** "Tuyển được nhân sự phù hợp và ký hợp đồng sau thử việc."

**Kịch bản thất bại/ngoại lệ:**
- Không có hồ sơ đạt qua sàng lọc → đăng lại tin/mở rộng kênh tuyển.
- Kiểm tra lý lịch không đạt → loại ứng viên, tránh rủi ro pháp lý/an ninh.
- Trượt phỏng vấn vòng 1 hoặc vòng 2/3 → loại hoặc lưu hồ sơ cho vị trí khác.
- Ứng viên từ chối/không chốt được thư mời → đàm phán lại hoặc chuyển ứng viên dự phòng.
- Không đạt khám sức khỏe theo luật định → dừng tiếp nhận.
- Không đạt chỉ tiêu thử việc → thanh lý hợp đồng thử việc, phỏng vấn thôi việc; nếu tỷ lệ nghỉ việc cao kéo dài → phản hồi lại khâu tuyển chọn/tiếp nhận. Ngưỡng chỉ tiêu, thời hạn từng vòng và cấp duyệt cụ thể `[giả định]`.

**Cấu trúc BPMN:** pool tuyển dụng nhân sự với các lane Phòng Nhân sự, Hệ thống sàng lọc hồ sơ, Quản lý trực tiếp/Ban Giám đốc và Y tế/Công nghệ thông tin. Các cổng quyết định đều là cổng XOR theo luồng tuyển dụng (phân loại vị trí; qua sàng lọc; lý lịch đạt; đạt từng vòng phỏng vấn; chấp nhận thư mời; đạt khám sức khỏe; đạt chỉ tiêu thử việc). Mỗi cổng rẽ thành nhánh loại trừ nhau: nhánh đạt đi tiếp, nhánh không đạt quay lại bước phù hợp (đăng lại tin, đàm phán lại) hoặc dẫn tới sự kiện Kết thúc riêng (loại ứng viên / thanh lý hợp đồng thử việc).

> **Ghi chú kỹ thuật:** mỗi cổng XOR trên sơ đồ đều thể hiện đủ hai nhánh loại trừ nhau — nhánh đạt (có nhãn: Có / Đạt / ≥70đ / Duyệt / Duyệt lại) đi tiếp, nhánh không đạt (có nhãn: Không / Trượt / <70đ) dẫn tới một sự kiện Kết thúc riêng (Đóng yêu cầu tuyển dụng, Loại hồ sơ, Loại sơ vấn, Loại vòng 1, Loại bài test, Loại vòng 2, Dừng do chưa đạt thoả thuận lương). Nhờ đó luồng cân bằng, không còn cổng thiếu nhánh hay treo (deadlock).

### 5.2. Phân tích định tính

#### a. Phân loại hoạt động VA/BVA/NVA

| Hoạt động | Phân loại | Nhận xét |
|---|---|---|
| Phỏng vấn vòng 1 và vòng 2/3 | VA | Trực tiếp chọn đúng người phù hợp vị trí |
| Tiếp nhận (đồng phục, đào tạo, cấp tài khoản) | VA | Biến ứng viên thành nhân sự vận hành được ngay |
| Đăng tin và sàng lọc hồ sơ | BVA | Cần để lọc hồ sơ đạt chuẩn; tối ưu tiêu chí để giảm sót ứng viên tốt |
| Kiểm tra lý lịch/khám sức khỏe | BVA | Tuân thủ pháp lý và kiểm soát rủi ro |
| Chờ phản hồi giữa các vòng phỏng vấn | NVA | Chờ (Hold); đặt thời hạn phản hồi cho từng vòng |
| Trao đổi thư mời/hồ sơ qua nhiều kênh rời rạc | NVA | Di chuyển (Move); tập trung liên lạc trên một hệ thống chuẩn |
| Nhập lại thông tin ứng viên ở nhiều biểu mẫu | NVA | Xử lý dư (Over-processing); dùng một hồ sơ ứng viên xuyên suốt |
| Tuyển lại do nghỉ việc sớm | NVA | Lỗi (Defects); cải thiện chọn lọc và tiếp nhận để giảm nghỉ việc |

#### b. Phân tích lãng phí (Move – Hold – Over-processing – Defects)

| Bước | Loại lãng phí | Biểu hiện | Tác động | Khắc phục |
|---|---|---|---|---|
| Trao đổi thư mời/hồ sơ | Di chuyển (Move) | Trao đổi qua nhiều kênh rời rạc (email, điện thoại, tin nhắn) | Thất lạc thông tin, chậm ra quyết định | Tập trung liên lạc và trạng thái ứng viên trên một hệ thống |
| Chờ giữa các vòng phỏng vấn | Chờ (Hold) | Chờ phản hồi kết quả từng vòng không có thời hạn | Kéo dài thời gian tuyển, mất ứng viên tốt | Đặt thời hạn phản hồi từng vòng, hàng đợi quá hạn, nhắc tự động |
| Nhập lại hồ sơ ứng viên | Xử lý dư (Over-processing) | Nhập lại thông tin ứng viên ở nhiều biểu mẫu qua các vòng | Tốn công, dễ sai lệch dữ liệu | Dùng một hồ sơ ứng viên xuyên suốt, kế thừa dữ liệu giữa các vòng |
| Nghỉ việc sớm phải tuyển lại | Lỗi (Defects) | Nghỉ việc sớm/tỷ lệ nghỉ cao ở nhân viên cửa hàng | Tốn chi phí tuyển lại, gián đoạn vận hành cửa hàng | Chuẩn hóa tiêu chí sàng lọc theo vị trí, hoàn thiện tiếp nhận |

#### c. Phân tích các bên liên quan

| Bên liên quan | Vai trò trong quy trình này | Mối quan tâm chính | Vấn đề tác động |
|---|---|---|---|
| Phòng Nhân sự | Chủ quy trình, đăng tin, chốt thư mời | Tuyển đủ, đúng hạn, chi phí hợp lý | Thời gian tuyển kéo dài, ứng viên từ chối |
| Ứng viên | Nộp hồ sơ, phỏng vấn, nhận việc | Quy trình nhanh, minh bạch | Chờ phản hồi lâu, trao đổi rời rạc |
| Quản lý trực tiếp/Ban Giám đốc | Phỏng vấn, đánh giá thử việc | Chọn đúng người, giữ được người | Chọn lọc chưa sát yêu cầu vị trí |
| Cửa hàng/Kho/Khối văn phòng | Nơi tiếp nhận nhân sự | Có người vận hành đúng chuẩn, ổn định | Nghỉ việc sớm gây thiếu người |
| Công nghệ thông tin/Y tế | Cấp tài khoản, khám sức khỏe | Tiếp nhận đầy đủ, đúng luật | Chậm cấp tài khoản/đồng phục làm chậm hòa nhập |

#### d. Vấn đề nổi bật (Issue register)

Cấu trúc: **Nguyên nhân** (xác định bằng 5 Why ở mục 5.4) → **Tác động** → **Giải pháp**.

| Vấn đề | Nguyên nhân | Tác động | Giải pháp |
|---|---|---|---|
| Nghỉ việc sớm (tỷ lệ nghỉ cao ở nhân viên cửa hàng) | Chọn lọc chưa sát yêu cầu vị trí và tiếp nhận chưa đủ | Phải tuyển lại tốn kém, gián đoạn vận hành cửa hàng | Chuẩn hóa tiêu chí sàng lọc theo vị trí, hoàn thiện tiếp nhận (đồng phục, đào tạo, cấp tài khoản POS) |
| Thời gian tuyển kéo dài | Chờ phản hồi giữa các vòng phỏng vấn, thiếu thời hạn từng vòng | Mất ứng viên tốt, vị trí trống lâu | Đặt thời hạn phản hồi từng vòng, hàng đợi quá hạn, nhắc tự động; áp luồng ưu tiên cho vị trí cửa hàng |
| Ứng viên từ chối thư mời | Quy trình phỏng vấn dài, trao đổi thư mời rời rạc, chậm quyết định | Phải tuyển lại từ vòng trước, tăng chi phí | Rút gọn vòng cho vị trí cửa hàng, tập trung trao đổi thư mời trên một hệ thống |

### 5.3. Phân tích định lượng

> Số dưới đây là **số minh họa cách tính** `[giả định]`.

#### a. Phân tích thời gian

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Thời gian tuyển (từ đăng tin đến nhận thư mời) | Ngày nhận thư mời − ngày mở tin | 01/08 → 21/08 | 20 ngày |
| Thời gian lấp đầy vị trí | Ngày nhân sự đi làm − ngày phát sinh nhu cầu | 28/07 → 04/09 | 38 ngày |
| Thời gian chờ giữa các vòng | Tổng thời gian chờ phản hồi các vòng | ≈ 9 ngày | 9 ngày |
| Hiệu suất chu kỳ (PCE) | (Thời gian tuyển − thời gian chờ) / thời gian tuyển | (20 − 9) / 20 | 55% |

#### b. Phân tích chi phí

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Chi phí trên mỗi tuyển dụng | Tổng chi phí tuyển / số nhân sự tuyển được | 40.000.000đ / 20 | 2.000.000đ / người |
| Chi phí tuyển lại do nghỉ sớm | Số nghỉ sớm × chi phí trên mỗi tuyển dụng | 5 × 2.000.000đ | 10.000.000đ |
| Chi phí năng suất mất do vị trí trống kéo dài | Số vị trí × số ngày trống vượt chuẩn × chi phí cơ hội/ngày | 4 × 10 × 100.000đ | 4.000.000đ |
| Chi phí phỏng vấn lại do ứng viên từ chối thư mời | Số lượt từ chối × giờ phỏng vấn lại × đơn giá giờ | 5 × 3 giờ × 100.000đ | 1.500.000đ |

### 5.4. Phân tích nguyên nhân gốc

#### Ưu tiên vấn đề bằng Pareto

Ba vấn đề ở mục 5.2.d được quy về **cùng đơn vị** — chi phí kỳ vọng mỗi kỳ tuyển (nghìn đồng). Toàn bộ số liệu là `[giả định]` từ mục 5.3.

| Vấn đề | Chi phí kỳ vọng (nghìn đồng) `[giả định]` | Tỷ trọng | Lũy kế |
|---|---|---|---|
| Nghỉ việc sớm (tuyển lại) | 10.000 | 64,5% | 64,5% |
| Thời gian tuyển kéo dài (vị trí trống) | 4.000 | 25,8% | 90,3% |
| Ứng viên từ chối thư mời (phỏng vấn lại) | 1.500 | 9,7% | 100,0% |
| **Tổng** | **15.500** | 100% | — |

Theo nguyên tắc 80/20, hai vấn đề đầu chiếm 90,3% tổng thiệt hại kỳ vọng; riêng **nghỉ việc sớm** chiếm 64,5% nên ưu tiên trước.

#### Phân tích 5 Why (cho vấn đề ưu tiên: nghỉ việc sớm)

1. **Vì sao nhân viên cửa hàng nghỉ việc sớm?** → Vì kỳ vọng công việc không khớp thực tế và chưa hòa nhập tốt trong thời gian đầu.
2. **Vì sao kỳ vọng không khớp và chưa hòa nhập?** → Vì sàng lọc chưa sát yêu cầu vị trí và tiếp nhận (đào tạo/đồng phục/tài khoản) chưa đầy đủ.
3. **Vì sao sàng lọc chưa sát và tiếp nhận chưa đủ?** → Vì tiêu chí sàng lọc chung cho nhiều vị trí và checklist tiếp nhận chưa chuẩn hóa theo vị trí.
4. **Vì sao chưa chuẩn hóa theo vị trí?** → Vì áp lực tuyển số lượng lớn khiến ưu tiên tốc độ lấp đầy hơn chất lượng chọn lọc.
5. **Vì sao ưu tiên tốc độ hơn chất lượng?** → Vì chưa đo chi phí tuyển lại do nghỉ sớm để thấy nó lớn hơn chi phí chọn lọc kỹ; thiếu vòng đo lường – cải tiến theo dữ liệu nghỉ việc.

**Nguyên nhân gốc:** tiêu chí sàng lọc và checklist tiếp nhận chưa chuẩn hóa theo vị trí, cộng với việc chưa đo chi phí tuyển lại → dẫn tới chọn lọc/hòa nhập chưa đạt và nghỉ việc sớm.

### 5.5. Phỏng vấn bổ sung

1. Thời gian tuyển và thời gian lấp đầy vị trí trung bình thực tế là bao nhiêu (thay số minh họa 20 / 38 ngày)?
2. Tỷ lệ hồ sơ qua sàng lọc, tỷ lệ đạt từng vòng và tỷ lệ chấp nhận thư mời thực tế là bao nhiêu?
3. Tỷ lệ nghỉ việc sớm của nhân viên cửa hàng và văn phòng/kho là bao nhiêu (thay số minh họa 25%)?
4. Chi phí trên mỗi tuyển dụng và chi phí đăng tin theo kênh thực tế là bao nhiêu?
5. Chỉ tiêu đánh giá thử việc, số vòng phỏng vấn theo vị trí và cấp duyệt thư mời được quy định thế nào?

### 5.6. Đề xuất cải tiến (TO-BE)

Theo thứ tự ưu tiên Pareto ở mục 5.4:

1. **Nghỉ việc sớm (ưu tiên cao nhất)** — chuẩn hóa tiêu chí sàng lọc theo từng vị trí và checklist tiếp nhận (đồng phục, đào tạo kiến thức sản phẩm, cấp tài khoản POS/Retail Pro Prism); đo chi phí tuyển lại theo nhóm vị trí để điều chỉnh mức độ chọn lọc.
2. **Thời gian tuyển kéo dài** — quản lý ứng viên trên một hệ thống với thời hạn phản hồi từng vòng, hàng đợi quá hạn và nhắc tự động; áp luồng ưu tiên cho các vị trí cửa hàng phổ thông.
3. **Ứng viên từ chối thư mời** — tập trung trao đổi thư mời trên một hệ thống, rút gọn vòng cho vị trí cửa hàng để ra quyết định nhanh.

---

## 6. Nhận hàng, kiểm tra chất lượng và nhập kho

### 6.1. Mô tả hiện trạng (AS-IS)

Nhận hàng, Xuất kho và Thu hồi hàng trả là **cụm ba quy trình kho vận** tại Trung tâm phân phối (DC) đào sâu chuỗi vận hành mà Lập kế hoạch mua & phân bổ chỉ chạm ở ranh giới. Nhận hàng & nhập kho đứng ở **đầu chuỗi**: nhận hàng từ chủ thương hiệu và tạo tồn đầu vào.

**Người kích hoạt:** chủ thương hiệu gửi báo giao hàng (ASN) và lịch giao; xe hàng cập bến DC.
**Người hưởng lợi:** Kiểm kê tồn kho (tồn đầu vào chính xác để kiểm kê) và Lập kế hoạch mua & phân bổ (dữ liệu nguồn hàng khả dụng) — trực tiếp; cửa hàng và khách cuối (có hàng đạt chuẩn) — gián tiếp.
**Ranh giới:** từ khi nhận báo giao hàng/hàng cập bến đến khi hàng lên kệ và cập nhật sổ tồn đầu vào (hoặc tạo yêu cầu trung chuyển thẳng sang Xuất kho & điều chuyển).

| # | Người thực hiện (lane) | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Kho nhận hàng/Bến | Tiếp nhận xe và dỡ hàng tại bến | Bắt đầu: nhận báo giao hàng và lịch giao |
| 2 | Chứng từ & Ngoại lệ | Kiểm tra chứng từ khớp đơn đặt hàng/báo giao | Cổng điều kiện: chứng từ khớp không? |
| 3 | Kho nhận hàng/Bến | Đếm và đối chiếu số lượng thực nhận | Cổng điều kiện: số lượng khớp không? → cổng gộp |
| 4 | Kiểm định chất lượng | Lấy mẫu và kiểm tra chất lượng | Sau cổng gộp |
| 5 | Kiểm định chất lượng | Đánh giá kết quả và mức lỗi | Cổng điều kiện: đạt không? và lỗi toàn bộ hay một phần? |
| 6 | Thủ kho/WMS | Tách lô, nhập phần đạt chất lượng | Nhánh "một phần" → cổng gộp |
| 7 | Thủ kho/WMS | Dán nhãn mã hàng và định vị | Chạy song song với bước 8 qua cổng AND tách |
| 8 | Thủ kho/WMS | Cập nhật dữ liệu tồn WMS/ERP | Chạy song song với bước 7 |
| 9 | Thủ kho/WMS | Cất hàng lên vị trí | Cổng AND gộp |
| 10 | Thủ kho/WMS | Kiểm tra nhu cầu trung chuyển thẳng tới cửa hàng | Cổng điều kiện: cần trung chuyển thẳng không? |
| 11 | Thủ kho/WMS | Cập nhật sổ tồn đầu vào | Thông điệp tồn đầu vào → khâu kiểm kê & hoạch định (hoặc yêu cầu trung chuyển → Xuất kho & điều chuyển) |

**Kịch bản thành công:** hàng cập bến → chứng từ khớp → số lượng thực nhận khớp → mẫu kiểm tra đạt toàn bộ → (song song qua **cặp AND**) dán nhãn/định vị **và** cập nhật tồn WMS/ERP → cất hàng lên kệ → không cần trung chuyển thẳng → cập nhật sổ tồn đầu vào và gửi thông điệp tồn sang khâu kiểm kê & hoạch định. **Kết quả:** "Lô hàng đạt chuẩn được nhập kho và tồn đầu vào đã cập nhật cho khâu kiểm kê & hoạch định."

**Kịch bản thất bại/ngoại lệ:**
- Chứng từ không khớp → lập biên bản sai lệch → Kết thúc "Từ chối nhận lô".
- Số lượng thiếu/thừa → ghi nhận và thông báo nhà cung cấp, sau đó nhập tiếp phần khớp qua cổng gộp.
- Kiểm tra chất lượng không đạt toàn bộ → Kết thúc "Trả lại nhà cung cấp"; nếu chỉ lỗi một phần → tách lô, chỉ nhập phần đạt, phần lỗi trả nhà cung cấp.
- Có nhu cầu trung chuyển thẳng → tạo yêu cầu chuyển thẳng cửa hàng (thông điệp sang Xuất kho & điều chuyển) thay vì lưu kho.

**Cấu trúc BPMN:** pool «Trung tâm phân phối – Nhận hàng, QC & nhập kho (Nhận hàng & nhập kho)» với 4 lane (Kho nhận hàng/Bến; Chứng từ & Ngoại lệ; Kiểm định chất lượng; Thủ kho/WMS). Các cổng quyết định là cổng XOR (chứng từ khớp; số lượng khớp; đạt chất lượng; mức lỗi; cần trung chuyển thẳng) với nhánh loại trừ nhau; các nhánh sai lệch có cổng gộp XOR để hợp lại phần hợp lệ. Bước dán nhãn/định vị và cập nhật tồn chạy song song qua **một cặp cổng AND tách/gộp cùng loại** nên cân bằng, không kẹt luồng.

### 6.2. Phân tích định tính

#### a. Phân loại hoạt động VA/BVA/NVA

| Hoạt động `[giả định]` phân loại theo thông lệ ngành | Phân loại | Nhận xét |
|---|---|---|
| Cất hàng đạt chuẩn lên kệ và cập nhật tồn đầu vào | VA | Tạo tồn khả dụng — giá trị cho khâu kiểm kê & hoạch định và bán hàng |
| Kiểm tra chất lượng (lấy mẫu) | BVA | Ngăn hàng lỗi vào kho; đặt ngưỡng chấp nhận theo rủi ro |
| Kiểm tra chứng từ và đối chiếu số lượng | BVA | Kiểm soát đầu vào, tránh sai lệch tồn |
| Chờ kiểm tra chất lượng/chờ cất kho | NVA | Chờ (Hold); bố trí nguồn lực kiểm định theo lịch giao |
| Đếm/nhập lại do sai lệch số lượng | NVA | Lỗi (Defects); dùng quét mã và đối chiếu điện tử |
| Di chuyển hàng nhiều chặng trong kho | NVA | Di chuyển (Move); bố trí vị trí định vị hợp lý |

#### b. Phân tích lãng phí (Move – Hold – Over-processing – Defects)

| Bước | Loại lãng phí | Biểu hiện `[giả định]` | Tác động | Khắc phục |
|---|---|---|---|---|
| Di chuyển hàng trong kho | Di chuyển (Move) | Hàng đi nhiều chặng từ bến đến vị trí cất | Tốn thời gian và nhân công | Bố trí vị trí định vị theo tần suất, tối ưu tuyến putaway |
| Chờ kiểm tra chất lượng | Chờ (Hold) | Lô hàng chờ lấy mẫu/kiểm định khi thiếu nhân lực | Kéo dài thời gian nhập kho, chậm cập nhật tồn | Bố trí lịch kiểm định theo lịch giao, ưu tiên lô gấp |
| Nhập/đối chiếu chứng từ thủ công | Xử lý dư (Over-processing) | Đối chiếu số lượng bằng tay nhiều lần | Tốn công, dễ sai | Quét mã và đối chiếu điện tử với đơn đặt hàng/báo giao |
| Hàng lỗi/sai lệch số lượng | Lỗi (Defects) | Lô lỗi phải trả, số lượng thiếu/thừa | Chi phí xử lý lô lỗi, sai lệch tồn | Ngưỡng chấp nhận rõ ràng, phản hồi nhà cung cấp sớm |

#### c. Phân tích các bên liên quan

| Bên liên quan | Vai trò trong quy trình này | Mối quan tâm chính | Vấn đề tác động |
|---|---|---|---|
| Kho nhận hàng/Bến | Tiếp nhận, dỡ và đếm hàng | Nhận nhanh, đúng số lượng | Sai lệch chứng từ/số lượng gây chậm |
| Kiểm định chất lượng | Lấy mẫu, đánh giá lỗi | Chặn hàng lỗi, đúng ngưỡng | Chờ kiểm định khi thiếu nhân lực |
| Thủ kho/WMS | Định vị, cất kho, cập nhật tồn | Tồn chính xác, cất đúng vị trí | Di chuyển nhiều chặng, cập nhật trễ |
| Nhà cung cấp/chủ thương hiệu | Giao hàng theo báo giao | Nhận hàng đúng hẹn, ít trả | Bị trả lô lỗi, phản hồi chậm |
| khâu kiểm kê & hoạch định | Nhận tồn đầu vào | Tồn đầu vào chính xác, kịp thời | Cập nhật tồn trễ ảnh hưởng hoạch định |

#### d. Vấn đề nổi bật (Issue register)

Cấu trúc: **Nguyên nhân** (xác định bằng 5 Why ở mục 6.4) → **Tác động** → **Giải pháp**.

| Vấn đề | Nguyên nhân | Tác động | Giải pháp |
|---|---|---|---|
| Hàng không đạt chất lượng phải trả nhà cung cấp | Chất lượng đầu vào không ổn định và ngưỡng chấp nhận chưa rõ | Chi phí xử lý lô lỗi, thiếu hàng theo kế hoạch | Đặt ngưỡng chấp nhận theo rủi ro, phản hồi nhà cung cấp và theo dõi tỷ lệ lỗi theo nguồn |
| Sai lệch chứng từ/số lượng | Đối chiếu thủ công, chứng từ và hàng thực nhận lệch nhau | Xử lý lại, sai lệch tồn đầu vào | Quét mã và đối chiếu điện tử với đơn đặt hàng/báo giao ngay tại bến |
| Chờ kiểm định và cất kho kéo dài | Nhân lực kiểm định bố trí chưa theo lịch giao | Chậm cập nhật tồn, đọng hàng ở bến | Bố trí lịch kiểm định theo lịch giao, ưu tiên lô gấp |

### 6.3. Phân tích định lượng

> Số dưới đây là **số minh họa cách tính** `[giả định]`.

#### a. Phân tích thời gian

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Thời gian chu kỳ nhập kho một lô | Thời điểm cập nhật tồn − thời điểm cập bến | 08:00 → 14:00 | 6 giờ |
| Thời gian xử lý thực (VA+BVA) | Tổng thời gian đếm + kiểm định + cất kho | ≈ 3,5 giờ | 3,5 giờ |
| Thời gian chờ (NVA) | Chu kỳ − thời gian xử lý | 6 − 3,5 | 2,5 giờ |
| Hiệu suất chu kỳ (PCE) | Thời gian xử lý / chu kỳ | 3,5 / 6 | ≈ 58% |

#### b. Phân tích chi phí

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Chi phí xử lý lô hàng lỗi | Giá trị lô lỗi × tỷ lệ lỗi + chi phí trả hàng | 100.000.000đ × 5% + 1.000.000đ | 6.000.000đ / kỳ |
| Chi phí xử lý sai lệch chứng từ/số lượng | Số lô sai lệch × giờ xử lý × đơn giá giờ | 20 × 1 giờ × 100.000đ | 2.000.000đ / kỳ |
| Chi phí chờ kiểm định & cất kho | Số lô chờ × giờ chờ × đơn giá giờ | 10 × 1 giờ × 100.000đ | 1.000.000đ / kỳ |

### 6.4. Phân tích nguyên nhân gốc

#### Ưu tiên vấn đề bằng Pareto

Ba vấn đề ở mục 6.2.d được quy về **cùng đơn vị** — chi phí kỳ vọng mỗi kỳ (nghìn đồng). Toàn bộ số liệu là `[giả định]` từ mục 6.3.

| Vấn đề | Chi phí kỳ vọng (nghìn đồng) `[giả định]` | Tỷ trọng | Lũy kế |
|---|---|---|---|
| Hàng lỗi phải trả nhà cung cấp | 6.000 | 66,7% | 66,7% |
| Sai lệch chứng từ/số lượng | 2.000 | 22,2% | 88,9% |
| Chờ kiểm định và cất kho | 1.000 | 11,1% | 100,0% |
| **Tổng** | **9.000** | 100% | — |

Theo nguyên tắc 80/20, hai vấn đề đầu chiếm 88,9%; riêng **hàng lỗi** chiếm 66,7% nên ưu tiên trước.

#### Phân tích 5 Why (cho vấn đề ưu tiên: hàng lỗi phải trả nhà cung cấp)

1. **Vì sao phải trả lô hàng?** → Vì kiểm tra chất lượng phát hiện lỗi vượt ngưỡng chấp nhận.
2. **Vì sao lỗi vượt ngưỡng?** → Vì chất lượng đầu vào từ nhà cung cấp không ổn định giữa các lô.
3. **Vì sao chất lượng không ổn định mà vẫn nhận?** → Vì chưa theo dõi tỷ lệ lỗi theo từng nguồn để cảnh báo sớm.
4. **Vì sao chưa theo dõi theo nguồn?** → Vì kết quả kiểm tra chất lượng chưa gắn mã nhà cung cấp/lô để tổng hợp.
5. **Vì sao chưa gắn mã theo nguồn?** → Vì quy trình nhập kho tập trung vào thông qua lô hiện tại, chưa có vòng phản hồi chất lượng theo nhà cung cấp.

**Nguyên nhân gốc:** thiếu vòng theo dõi tỷ lệ lỗi theo nhà cung cấp/lô để phản hồi và điều chỉnh sớm → hàng lỗi lặp lại và phải trả.

### 6.5. Phỏng vấn bổ sung

1. Tỷ lệ lô đạt/không đạt kiểm tra chất lượng và ngưỡng chấp nhận thực tế là bao nhiêu?
2. Tỷ lệ sai lệch chứng từ/số lượng khi nhận hàng là bao nhiêu?
3. Thời gian chu kỳ nhập kho một lô trung bình thực tế là bao lâu (thay số minh họa 6 giờ)?
4. Chính sách trung chuyển thẳng được áp dụng trong trường hợp nào?
5. Kết quả kiểm tra chất lượng có được tổng hợp theo nhà cung cấp/lô để phản hồi không?

### 6.6. Đề xuất cải tiến (TO-BE)

Theo thứ tự ưu tiên Pareto ở mục 6.4:

1. **Hàng lỗi phải trả nhà cung cấp (ưu tiên cao nhất)** — gắn mã nhà cung cấp/lô cho kết quả kiểm tra chất lượng, theo dõi tỷ lệ lỗi theo nguồn và phản hồi sớm; đặt ngưỡng chấp nhận theo rủi ro từng nhóm hàng.
2. **Sai lệch chứng từ/số lượng** — quét mã và đối chiếu điện tử với đơn đặt hàng/báo giao ngay tại bến để giảm sai lệch tồn đầu vào.
3. **Chờ kiểm định và cất kho** — bố trí lịch kiểm định theo lịch giao, ưu tiên lô gấp và tối ưu tuyến cất hàng.

---

## 7. Xuất kho và điều chuyển phân bổ tới chuỗi cửa hàng

### 7.1. Mô tả hiện trạng (AS-IS)

Xuất kho & điều chuyển nối tiếp đầu ra phân bổ của Lập kế hoạch mua & phân bổ: xuất kho và điều chuyển hàng tới chuỗi cửa hàng.

**Người kích hoạt:** Điều phối phân bổ nhận **lệnh phân bổ từ Lập kế hoạch mua & phân bổ**.
**Người hưởng lợi:** cửa hàng (nhận đúng cơ cấu hàng đúng hạn) — trực tiếp; Lập kế hoạch mua & phân bổ (đóng vòng thực thi kế hoạch phân bổ) và khách cuối — gián tiếp.
**Ranh giới:** từ khi nhận lệnh phân bổ đến khi cửa hàng nhận, kiểm đếm khớp và cập nhật tồn cửa hàng.

| # | Người thực hiện (lane) | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Điều phối phân bổ | Kiểm tra tồn khả dụng | Bắt đầu: nhận lệnh phân bổ ← Lập kế hoạch mua & phân bổ |
| 2 | Điều phối phân bổ | Xác định tồn có đủ cho lệnh phân bổ | Cổng điều kiện: đủ tồn không? Nếu không → có cho giao một phần không? |
| 3 | Cửa hàng & Ngoại lệ | Giao một phần và tạo đơn chờ hàng | Nhánh "có giao một phần" → cổng gộp |
| 4 | Điều phối phân bổ | Lập phiếu xuất kho | Sau cổng gộp |
| 5 | Kho xuất – Soạn hàng | Soạn hàng theo phiếu xuất | Cổng điều kiện: soạn hàng khớp phiếu không? (không → soạn lại) |
| 6 | Kho xuất – Đóng gói | Đóng gói và dán nhãn kiện | Chạy song song với bước 7 qua cổng AND tách |
| 7 | Kho xuất – Đóng gói | Lập chứng từ xuất và kế hoạch tuyến | Chạy song song với bước 6 → cổng AND gộp |
| 8 | Vận chuyển | Bàn giao đơn vị vận chuyển | Sau cổng AND gộp |
| 9 | Vận chuyển | Vận chuyển tới cửa hàng và xác nhận giao | Cổng điều kiện: giao thành công không? |
| 10 | Cửa hàng & Ngoại lệ | Cửa hàng nhận và kiểm đếm | Cổng điều kiện: kiểm đếm khớp không? → cổng gộp |
| 11 | Cửa hàng & Ngoại lệ | Cập nhật tồn cửa hàng và đóng lệnh | Thông điệp tồn cửa hàng → khâu kiểm kê & hoạch định |

**Kịch bản thành công:** nhận lệnh phân bổ → tồn khả dụng đủ → lập phiếu xuất → soạn hàng khớp → (song song qua **cặp AND**) đóng gói/dán nhãn **và** lập chứng từ xuất/kế hoạch tuyến → bàn giao vận chuyển → giao thành công → cửa hàng nhận, kiểm đếm khớp → cập nhật tồn cửa hàng và gửi thông điệp sang khâu kiểm kê & hoạch định. **Kết quả:** "Hàng được điều chuyển và cửa hàng đã nhận đủ, tồn cửa hàng cập nhật cho khâu kiểm kê & hoạch định."

**Kịch bản thất bại/ngoại lệ:**
- Tồn không đủ → hỏi có cho giao một phần: nếu có → giao một phần và tạo đơn chờ hàng rồi quay lại lập phiếu xuất; nếu không → Kết thúc "Hoãn dòng phân bổ" (thông điệp hoãn → Lập kế hoạch mua & phân bổ).
- Soạn hàng không khớp phiếu → soạn lại trước khi đóng gói.
- Giao không thành công → trả kiện về DC và lập biên bản → Kết thúc "Chuyển Thu hồi & xử lý hàng trả thu hồi" (thông điệp hàng lỗi → Thu hồi & xử lý hàng trả).
- Cửa hàng kiểm đếm không khớp → ghi nhận thiếu/thừa và mở khiếu nại, sau đó vẫn hợp nhất về cổng gộp để cập nhật tồn và đóng lệnh.

**Cấu trúc BPMN:** pool «Trung tâm phân phối – Xuất kho & điều chuyển (Xuất kho & điều chuyển)» với 4 lane (Điều phối phân bổ; Kho xuất – Soạn hàng & Đóng gói; Vận chuyển; Cửa hàng & Ngoại lệ). Các cổng quyết định là cổng XOR (đủ tồn; cho giao một phần; soạn hàng khớp; giao thành công; kiểm đếm khớp) với nhánh loại trừ nhau; nhánh ngoại lệ có cổng gộp XOR hợp lại. Bước đóng gói và lập chứng từ xuất chạy song song qua **một cặp cổng AND tách/gộp cùng loại** nên cân bằng.

### 7.2. Phân tích định tính

#### a. Phân loại hoạt động VA/BVA/NVA

| Hoạt động `[giả định]` phân loại theo thông lệ ngành | Phân loại | Nhận xét |
|---|---|---|
| Giao hàng đúng cơ cấu tới cửa hàng | VA | Đưa hàng tới điểm bán — giá trị cho cửa hàng và khách |
| Soạn hàng và đóng gói theo phiếu xuất | BVA | Cần để giao đúng, đủ; nên quét mã khi soạn |
| Lập chứng từ xuất và kế hoạch tuyến | BVA | Kiểm soát và tối ưu vận chuyển |
| Chờ vận chuyển/chờ xác nhận giao | NVA | Chờ (Hold); đặt thời hạn giao và theo dõi tuyến |
| Soạn lại do không khớp phiếu | NVA | Lỗi (Defects); quét mã khi soạn để giảm sai |
| Trả kiện và xử lý lại khi giao lỗi | NVA | Lỗi (Defects); cải thiện đóng gói và chọn đơn vị vận chuyển |

#### b. Phân tích lãng phí (Move – Hold – Over-processing – Defects)

| Bước | Loại lãng phí | Biểu hiện `[giả định]` | Tác động | Khắc phục |
|---|---|---|---|---|
| Vận chuyển nhiều tuyến rời | Di chuyển (Move) | Giao lẻ nhiều chuyến không gộp tuyến | Tốn chi phí vận chuyển | Gộp tuyến theo khu vực, tối ưu kế hoạch tuyến |
| Chờ vận chuyển/xác nhận giao | Chờ (Hold) | Kiện chờ bàn giao hoặc chờ xác nhận giao | Kéo dài thời gian tới cửa hàng | Đặt thời hạn giao, theo dõi trạng thái tuyến |
| Lập chứng từ trùng lặp | Xử lý dư (Over-processing) | Nhập chứng từ xuất nhiều nơi | Tốn công, dễ sai | Một bộ chứng từ điện tử liên thông |
| Giao lỗi/soạn sai | Lỗi (Defects) | Giao không thành công phải thu hồi, soạn sai phiếu | Chi phí thu hồi, chậm giao | Quét mã khi soạn, cải thiện đóng gói và chọn đơn vị vận chuyển |

#### c. Phân tích các bên liên quan

| Bên liên quan | Vai trò trong quy trình này | Mối quan tâm chính | Vấn đề tác động |
|---|---|---|---|
| Điều phối phân bổ | Kiểm tra tồn, lập phiếu xuất | Giao đủ theo lệnh phân bổ | Thiếu tồn phải hoãn/giao một phần |
| Kho xuất (soạn/đóng gói) | Soạn hàng, đóng gói, lập chứng từ | Soạn đúng, đóng gói chắc | Soạn sai phiếu phải làm lại |
| Vận chuyển | Giao hàng tới cửa hàng | Giao đúng hạn, ít hỏng | Giao không thành công phải thu hồi |
| Cửa hàng | Nhận và kiểm đếm hàng | Nhận đủ, đúng cơ cấu | Kiểm đếm không khớp, khiếu nại |
| khâu hoạch định & kiểm kê | Nhận thông điệp tồn/hoãn | Đóng vòng thực thi kế hoạch, tồn chính xác | Hoãn phân bổ ảnh hưởng kế hoạch |

#### d. Vấn đề nổi bật (Issue register)

Cấu trúc: **Nguyên nhân** (xác định bằng 5 Why ở mục 7.4) → **Tác động** → **Giải pháp**.

| Vấn đề | Nguyên nhân | Tác động | Giải pháp |
|---|---|---|---|
| Giao không thành công phải thu hồi | Đóng gói chưa chắc hoặc đơn vị vận chuyển chưa đạt | Chi phí thu hồi, chậm giao, chuyển Thu hồi & xử lý hàng trả | Cải thiện tiêu chuẩn đóng gói, đánh giá đơn vị vận chuyển theo tỷ lệ giao thành công |
| Thiếu tồn phải hoãn/giao một phần | Tồn khả dụng lệch so với lệnh phân bổ | Cửa hàng thiếu hàng, mất doanh thu cơ hội | Đồng bộ tồn khả dụng theo thời gian thực với Lập kế hoạch mua & phân bổ, chính sách giao một phần rõ ràng |
| Soạn hàng không khớp phiếu | Soạn thủ công, không quét mã | Soạn lại tốn công, chậm giao | Quét mã khi soạn và đối chiếu điện tử với phiếu xuất |

### 7.3. Phân tích định lượng

> Số dưới đây là **số minh họa cách tính** `[giả định]`.

#### a. Phân tích thời gian

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Thời gian chu kỳ xuất – giao một lệnh | Thời điểm cửa hàng nhận − thời điểm nhận lệnh | Ngày 1 08:00 → ngày 2 16:00 | 32 giờ |
| Thời gian xử lý thực (VA+BVA) | Tổng thời gian soạn + đóng gói + giao | ≈ 12 giờ | 12 giờ |
| Thời gian chờ (NVA) | Chu kỳ − thời gian xử lý | 32 − 12 | 20 giờ |
| Hiệu suất chu kỳ (PCE) | Thời gian xử lý / chu kỳ | 12 / 32 | ≈ 38% |

#### b. Phân tích chi phí

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Chi phí thu hồi do giao lỗi | Số lệnh giao lỗi × chi phí thu hồi/lệnh | 10 × 500.000đ | 5.000.000đ / kỳ |
| Chi phí cơ hội do hoãn/giao thiếu | Số lệnh hoãn × giá trị đơn × tỷ lệ mất doanh thu | 10 × 5.000.000đ × 5% | 2.500.000đ / kỳ |
| Chi phí soạn lại do sai phiếu | Số lần soạn lại × giờ × đơn giá giờ | 10 × 1 giờ × 100.000đ | 1.000.000đ / kỳ |

### 7.4. Phân tích nguyên nhân gốc

#### Ưu tiên vấn đề bằng Pareto

Ba vấn đề ở mục 7.2.d được quy về **cùng đơn vị** — chi phí kỳ vọng mỗi kỳ (nghìn đồng). Toàn bộ số liệu là `[giả định]` từ mục 7.3.

| Vấn đề | Chi phí kỳ vọng (nghìn đồng) `[giả định]` | Tỷ trọng | Lũy kế |
|---|---|---|---|
| Giao không thành công phải thu hồi | 5.000 | 58,8% | 58,8% |
| Thiếu tồn phải hoãn/giao một phần | 2.500 | 29,4% | 88,2% |
| Soạn hàng không khớp phiếu | 1.000 | 11,8% | 100,0% |
| **Tổng** | **8.500** | 100% | — |

Theo nguyên tắc 80/20, hai vấn đề đầu chiếm 88,2%; riêng **giao không thành công** chiếm 58,8% nên ưu tiên trước.

#### Phân tích 5 Why (cho vấn đề ưu tiên: giao không thành công phải thu hồi)

1. **Vì sao giao không thành công?** → Vì kiện hàng hư hỏng trên đường hoặc cửa hàng không nhận được đúng hẹn.
2. **Vì sao hư hỏng/không đúng hẹn?** → Vì đóng gói chưa đủ chắc và tuyến giao chưa được theo dõi sát.
3. **Vì sao đóng gói chưa chắc và tuyến chưa theo dõi sát?** → Vì tiêu chuẩn đóng gói chưa thống nhất và đơn vị vận chuyển chưa được đánh giá theo tỷ lệ giao thành công.
4. **Vì sao chưa đánh giá đơn vị vận chuyển?** → Vì chưa thu thập tỷ lệ giao thành công theo đơn vị và theo tuyến.
5. **Vì sao chưa thu thập?** → Vì quy trình tập trung vào xuất hàng, chưa có vòng đo lường chất lượng giao để phản hồi.

**Nguyên nhân gốc:** thiếu tiêu chuẩn đóng gói thống nhất và vòng đo lường tỷ lệ giao thành công theo đơn vị vận chuyển/tuyến → giao lỗi lặp lại và phải thu hồi.

### 7.5. Phỏng vấn bổ sung

1. Tỷ lệ giao thành công và tỷ lệ thu hồi do giao lỗi thực tế là bao nhiêu?
2. Tỷ lệ lệnh phân bổ phải hoãn/giao một phần do thiếu tồn là bao nhiêu?
3. Thời gian chu kỳ xuất – giao một lệnh trung bình thực tế là bao lâu (thay số minh họa 32 giờ)?
4. Chính sách giao một phần/đơn chờ hàng và cam kết dịch vụ với đơn vị vận chuyển là gì?
5. Tồn khả dụng có được đồng bộ theo thời gian thực với Lập kế hoạch mua & phân bổ khi lập lệnh phân bổ không?

### 7.6. Đề xuất cải tiến (TO-BE)

Theo thứ tự ưu tiên Pareto ở mục 7.4:

1. **Giao không thành công (ưu tiên cao nhất)** — thống nhất tiêu chuẩn đóng gói, thu thập tỷ lệ giao thành công theo đơn vị vận chuyển/tuyến và đánh giá định kỳ để chọn đơn vị tốt.
2. **Thiếu tồn phải hoãn/giao một phần** — đồng bộ tồn khả dụng theo thời gian thực với Lập kế hoạch mua & phân bổ khi lập lệnh, chuẩn hóa chính sách giao một phần và đơn chờ hàng.
3. **Soạn hàng không khớp phiếu** — quét mã khi soạn và đối chiếu điện tử với phiếu xuất để giảm soạn lại.

---

## 8. Thu hồi và xử lý hàng trả về / hàng lỗi

### 8.1. Mô tả hiện trạng (AS-IS)

Thu hồi & xử lý hàng trả khép vòng vận hành kho: thu hồi hàng giao lỗi (từ Xuất kho & điều chuyển) hoặc hàng khách trả tại cửa hàng, rồi cập nhật lại tồn và hao hụt.

**Người kích hoạt:** bộ phận Tiếp nhận & Phân loại nhận **yêu cầu trả hàng từ khâu xuất kho hoặc cửa hàng**.
**Người hưởng lợi:** khâu kiểm kê & hoạch định (tồn và hao hụt được cập nhật đúng), Tài chính (cơ sở hoàn tiền), nhà cung cấp/chủ thương hiệu (nhận lại hàng bảo hành) — trực tiếp; khách cuối (được xử lý trả hàng) — gián tiếp.
**Ranh giới:** từ khi nhận yêu cầu trả hàng đến khi đóng hồ sơ trả hàng và (nếu cần) lập đề nghị hoàn tiền chuyển Tài chính.

| # | Người thực hiện (lane) | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Tiếp nhận & Phân loại | Tiếp nhận và lập hồ sơ trả hàng | Bắt đầu: nhận yêu cầu trả hàng ← khâu xuất kho hoặc cửa hàng |
| 2 | Tiếp nhận & Phân loại | Kiểm tra đúng chính sách và thời hạn trả | Cổng điều kiện: đạt chính sách không? (không → từ chối → Kết thúc) |
| 3 | Giám định & Phân hạng | Giám định tình trạng hàng | — |
| 4 | Giám định & Phân hạng | Phân hạng khả năng bán lại nguyên trạng | Cổng điều kiện: bán lại nguyên trạng được không? |
| 5 | Giám định & Phân hạng | Kiểm tra còn bảo hành nhà cung cấp | Cổng điều kiện: còn bảo hành không? |
| 6 | Giám định & Phân hạng | Đánh giá khả năng tân trang | Cổng điều kiện: tân trang được không? và sau tân trang có đạt không? |
| 7 | Xử lý | Gửi trả/đổi với nhà cung cấp | Nhánh còn bảo hành → Kết thúc "Đã chuyển nhà cung cấp" |
| 8 | Xử lý | Tân trang hàng | Nhánh tân trang được → kiểm tra đạt sau tân trang |
| 9 | Xử lý | Loại bỏ/hủy hàng | Nhánh không tân trang được → Kết thúc "Ghi nhận hao hụt" (thông điệp hao hụt → khâu kiểm kê & hoạch định) |
| 10 | Kế toán & Cập nhật tồn | Cất hàng lên kệ | Sau cổng gộp → cổng AND tách (song song với bước 11) |
| 11 | Kế toán & Cập nhật tồn | Cập nhật tồn kho | Chạy song song với bước 10; thông điệp cập nhật tồn → khâu kiểm kê & hoạch định |
| 12 | Kế toán & Cập nhật tồn | Đóng hồ sơ trả hàng | Sau cổng AND gộp |
| 13 | Kế toán & Cập nhật tồn | Lập đề nghị hoàn tiền → Tài chính | Cổng điều kiện: cần hoàn tiền không? Thông điệp đề nghị hoàn tiền → Tài chính |

**Kịch bản thành công:** nhận yêu cầu trả hàng đúng chính sách và thời hạn → giám định → hàng còn bán lại nguyên trạng (hoặc tân trang đạt) → hợp nhất tại cổng gộp → (song song qua **cặp AND**) cất lên kệ **và** cập nhật tồn kho khâu kiểm kê & hoạch định → đóng hồ sơ trả hàng → nếu cần thì lập đề nghị hoàn tiền chuyển Tài chính. **Kết quả:** "Hàng trả được nhập lại/tân trang, tồn cập nhật cho khâu kiểm kê & hoạch định và (nếu có) đề nghị hoàn tiền chuyển Tài chính."

**Kịch bản thất bại/ngoại lệ:**
- Yêu cầu trả sai chính sách/quá thời hạn → từ chối và phản hồi khách → Kết thúc "Đóng (từ chối)".
- Không bán lại nguyên trạng nhưng còn bảo hành nhà cung cấp → gửi trả/đổi với nhà cung cấp → Kết thúc "Đã chuyển nhà cung cấp".
- Không còn bảo hành và không tân trang được, hoặc tân trang không đạt → loại bỏ/hủy → Kết thúc "Ghi nhận hao hụt" (thông điệp hao hụt → khâu kiểm kê & hoạch định).
- Không cần hoàn tiền → đóng hồ sơ và kết thúc tại "Hoàn tất xử lý trả hàng".

**Cấu trúc BPMN:** pool «Trung tâm phân phối – Thu hồi & xử lý hàng trả (Thu hồi & xử lý hàng trả)» với 4 lane (Tiếp nhận & Phân loại; Giám định & Phân hạng; Xử lý; Kế toán & Cập nhật tồn). Các cổng quyết định là cổng XOR (đạt chính sách; bán lại nguyên trạng; còn bảo hành; tân trang được; đạt sau tân trang; cần hoàn tiền) với nhánh loại trừ nhau dẫn tới nhiều sự kiện Kết thúc riêng. Bước cất lên kệ và cập nhật tồn chạy song song qua **một cặp cổng AND tách/gộp cùng loại** nên cân bằng.

### 8.2. Phân tích định tính

#### a. Phân loại hoạt động VA/BVA/NVA

| Hoạt động `[giả định]` phân loại theo thông lệ ngành | Phân loại | Nhận xét |
|---|---|---|
| Nhập lại/tân trang hàng để bán lại | VA | Thu hồi giá trị hàng trả |
| Giám định và phân hạng hàng trả | BVA | Cần để quyết định hướng xử lý đúng |
| Kiểm tra chính sách và thời hạn trả | BVA | Kiểm soát rủi ro và tuân thủ chính sách |
| Chờ giám định/chờ xử lý | NVA | Chờ (Hold); bố trí giám định theo hàng đợi |
| Tân trang lại do lần đầu không đạt | NVA | Lỗi (Defects); chuẩn hóa tiêu chí tân trang |
| Loại bỏ/hủy hàng | NVA | Lỗi (Defects); hao hụt cần giảm qua giám định sớm |

#### b. Phân tích lãng phí (Move – Hold – Over-processing – Defects)

| Bước | Loại lãng phí | Biểu hiện `[giả định]` | Tác động | Khắc phục |
|---|---|---|---|---|
| Luân chuyển hàng trả nhiều chặng | Di chuyển (Move) | Hàng trả đi qua nhiều khu vực chờ xử lý | Tốn thời gian, dễ thất lạc | Bố trí khu vực xử lý trả hàng tập trung |
| Chờ giám định và xử lý | Chờ (Hold) | Hàng trả đọng chờ giám định/phân hạng | Đọng vốn hàng trả, chậm cập nhật tồn | Bố trí giám định theo hàng đợi ưu tiên |
| Nhập hồ sơ trả hàng trùng lặp | Xử lý dư (Over-processing) | Ghi nhận thông tin trả hàng ở nhiều nơi | Tốn công, dễ sai | Một hồ sơ trả hàng điện tử liên thông |
| Hủy hàng (hao hụt) | Lỗi (Defects) | Hàng không bán lại/tân trang được phải hủy | Hao hụt giá trị | Giám định sớm, tăng tỷ lệ tân trang/bán lại |

#### c. Phân tích các bên liên quan

| Bên liên quan | Vai trò trong quy trình này | Mối quan tâm chính | Vấn đề tác động |
|---|---|---|---|
| Tiếp nhận & Phân loại | Nhận và lập hồ sơ trả hàng | Nhận đúng chính sách, nhanh | Yêu cầu sai chính sách gây tranh cãi |
| Giám định & Phân hạng | Giám định, quyết hướng xử lý | Phân hạng đúng, giảm hủy | Chờ giám định, phân hạng thiếu nhất quán |
| Xử lý | Trả nhà cung cấp/tân trang/hủy | Thu hồi tối đa giá trị | Tân trang không đạt phải làm lại |
| Kế toán & Cập nhật tồn | Cập nhật tồn, hoàn tiền | Tồn/hao hụt chính xác | Cập nhật tồn trễ ảnh hưởng khâu kiểm kê & hoạch định |
| Tài chính/nhà cung cấp | Hoàn tiền/nhận hàng bảo hành | Chứng từ đúng, xử lý nhanh | Đề nghị hoàn tiền chậm |

#### d. Vấn đề nổi bật (Issue register)

Cấu trúc: **Nguyên nhân** (xác định bằng 5 Why ở mục 8.4) → **Tác động** → **Giải pháp**.

| Vấn đề | Nguyên nhân | Tác động | Giải pháp |
|---|---|---|---|
| Hàng phải hủy (hao hụt cao) | Giám định muộn và tiêu chí phân hạng thiếu nhất quán | Hao hụt giá trị hàng trả | Giám định sớm, chuẩn hóa tiêu chí phân hạng để tăng tỷ lệ tân trang/bán lại |
| Chờ giám định và xử lý kéo dài | Giám định bố trí chưa theo hàng đợi ưu tiên | Đọng vốn hàng trả, cập nhật tồn trễ | Bố trí giám định theo hàng đợi ưu tiên, đặt thời hạn xử lý |
| Tân trang không đạt phải làm lại | Tiêu chí và tay nghề tân trang chưa chuẩn hóa | Tốn công, kéo dài xử lý | Chuẩn hóa tiêu chí và hướng dẫn tân trang |

### 8.3. Phân tích định lượng

> Số dưới đây là **số minh họa cách tính** `[giả định]`.

#### a. Phân tích thời gian

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Thời gian chu kỳ xử lý một hồ sơ trả hàng | Thời điểm đóng hồ sơ − thời điểm tiếp nhận | Ngày 1 → ngày 4 | 3 ngày |
| Thời gian xử lý thực (VA+BVA) | Tổng thời gian giám định + xử lý + cập nhật | ≈ 1 ngày | 1 ngày |
| Thời gian chờ (NVA) | Chu kỳ − thời gian xử lý | 3 − 1 | 2 ngày |
| Hiệu suất chu kỳ (PCE) | Thời gian xử lý / chu kỳ | 1 / 3 | ≈ 33% |

#### b. Phân tích chi phí

| Chỉ số | Công thức | Số minh họa `[giả định]` | Kết quả |
|---|---|---|---|
| Chi phí hao hụt do hủy hàng | Số hàng hủy × giá trị bình quân | 40 × 100.000đ | 4.000.000đ / kỳ |
| Chi phí đọng vốn hàng trả chờ xử lý | Giá trị hàng trả tồn đọng × chi phí vốn × thời gian | 200.000.000đ × 1% × 1 tháng | 2.000.000đ / kỳ |
| Chi phí tân trang lại | Số lần tân trang lại × giờ × đơn giá giờ | 10 × 1 giờ × 100.000đ | 1.000.000đ / kỳ |

### 8.4. Phân tích nguyên nhân gốc

#### Ưu tiên vấn đề bằng Pareto

Ba vấn đề ở mục 8.2.d được quy về **cùng đơn vị** — chi phí kỳ vọng mỗi kỳ (nghìn đồng). Toàn bộ số liệu là `[giả định]` từ mục 8.3.

| Vấn đề | Chi phí kỳ vọng (nghìn đồng) `[giả định]` | Tỷ trọng | Lũy kế |
|---|---|---|---|
| Hàng phải hủy (hao hụt) | 4.000 | 57,1% | 57,1% |
| Chờ giám định và xử lý kéo dài | 2.000 | 28,6% | 85,7% |
| Tân trang không đạt phải làm lại | 1.000 | 14,3% | 100,0% |
| **Tổng** | **7.000** | 100% | — |

Theo nguyên tắc 80/20, hai vấn đề đầu chiếm 85,7%; riêng **hàng phải hủy** chiếm 57,1% nên ưu tiên trước.

#### Phân tích 5 Why (cho vấn đề ưu tiên: hàng phải hủy)

1. **Vì sao nhiều hàng trả phải hủy?** → Vì hàng không còn bán lại nguyên trạng và không tân trang được.
2. **Vì sao không tân trang được?** → Vì tình trạng hàng xuống cấp thêm trong thời gian chờ và phân hạng thiếu nhất quán.
3. **Vì sao xuống cấp thêm và phân hạng thiếu nhất quán?** → Vì giám định muộn và tiêu chí phân hạng chưa chuẩn hóa.
4. **Vì sao giám định muộn và tiêu chí chưa chuẩn?** → Vì giám định chưa bố trí theo hàng đợi ưu tiên và chưa có hướng dẫn phân hạng thống nhất.
5. **Vì sao chưa có hàng đợi ưu tiên và hướng dẫn thống nhất?** → Vì chưa đo tỷ lệ hủy theo nguyên nhân để thấy tác động và đặt yêu cầu cải tiến.

**Nguyên nhân gốc:** giám định muộn và tiêu chí phân hạng chưa chuẩn hóa (thiếu hàng đợi ưu tiên và hướng dẫn), cộng với chưa đo tỷ lệ hủy theo nguyên nhân → tỷ lệ hủy cao.

### 8.5. Phỏng vấn bổ sung

1. Tỷ lệ hàng trả được bán lại/tân trang/hủy thực tế là bao nhiêu?
2. Thời gian xử lý một hồ sơ trả hàng trung bình thực tế là bao lâu (thay số minh họa 3 ngày)?
3. Chính sách và thời hạn đổi trả áp dụng cho từng nhóm hàng là gì?
4. Tiêu chí phân hạng (bán lại/tân trang/hủy) và điều khoản bảo hành nhà cung cấp được quy định thế nào?
5. Quy trình và thời hạn hoàn tiền phối hợp với Tài chính ra sao?

### 8.6. Đề xuất cải tiến (TO-BE)

Theo thứ tự ưu tiên Pareto ở mục 8.4:

1. **Hàng phải hủy (ưu tiên cao nhất)** — giám định sớm theo hàng đợi ưu tiên, chuẩn hóa tiêu chí phân hạng để tăng tỷ lệ tân trang/bán lại; đo tỷ lệ hủy theo nguyên nhân để cải tiến liên tục.
2. **Chờ giám định và xử lý** — bố trí giám định theo hàng đợi ưu tiên và đặt thời hạn xử lý từng bước để giảm đọng vốn hàng trả.
3. **Tân trang không đạt** — chuẩn hóa tiêu chí và hướng dẫn tân trang để giảm làm lại.
