# Kết quả tìm kiếm trên Internet: Các quy trình nghiệp vụ của Nike tại Việt Nam

**Ngày cập nhật:** 23/07/2026  
**Phương pháp:** rà soát phạm vi trên web có hệ thống và tổng hợp mô tả  
**Mục đích:** lập danh mục quy trình để nhóm chọn phạm vi phân tích và vẽ BPMN 2.0 ở giai đoạn sau

## 1. Kết luận nhanh

Nike có nhiều hoạt động tại Việt Nam hơn marketing và bán hàng. Bằng chứng công khai mạnh nhất tập trung vào bốn cụm:

1. **Quản trị chuỗi cung ứng và nhà cung cấp:** lựa chọn nhà máy, đánh giá năng lực, đặt tiêu chuẩn, kiểm tra, yêu cầu khắc phục và chấm dứt hợp tác có trách nhiệm.
2. **Sản xuất và kỹ thuật:** các nhà máy hợp đồng độc lập tại Việt Nam sản xuất giày và quần áo Nike. FY2026, Việt Nam chiếm khoảng 52% sản lượng giày và 34% sản lượng quần áo Nike Brand; riêng Air Manufacturing Innovation của Nike có cơ sở tại Đồng Nai sản xuất cấu kiện đệm Air-Sole.
3. **Logistics và thương mại:** tin tuyển dụng tại Việt Nam cho thấy Nike bố trí chức năng lập kế hoạch vận tải xuất phát, đặt chỗ, quản lý chứng từ, theo dõi lô hàng và xử lý ngoại lệ; dữ liệu chưa đủ để dựng AS-IS nội bộ hoàn chỉnh.
4. **Bán hàng và dịch vụ khách Việt Nam:** đặt hàng, thanh toán, xác minh thông tin thông quan, giao hàng, theo dõi đơn, trả hàng, hoàn tiền, bảo hành và chăm sóc khách hàng.

Hoạt động bán lẻ và nhiều chiến dịch marketing quan sát được tại Việt Nam do **đối tác như ACFC** thực hiện. Các nhà máy sản xuất thành phẩm cũng chủ yếu là **doanh nghiệp độc lập theo hợp đồng**, không phải nhà máy do Nike sở hữu. Ngoại lệ được xác nhận là cơ sở Air Manufacturing Innovation tại Đồng Nai. Cách phân biệt này quyết định đúng Pool, Lane và message flow khi vẽ BPMN. [Hồ sơ 10-K FY2026 của Nike](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm) xác nhận cả mô hình nhà máy hợp đồng và cơ sở Air Manufacturing Innovation tại Đồng Nai.

**Bốn quy trình nên ưu tiên nếu chỉ dùng dữ liệu công khai:**

1. Sản xuất và kiểm tra chất lượng giày tại nhà máy đối tác TKG Taekwang Vina.
2. Kiểm tra và khắc phục vi phạm của nhà cung cấp hiện hữu.
3. Xử lý đơn Nike.com/vn, xác minh thông tin và thông quan để giao hàng.
4. Tiếp nhận trả hàng, kiểm tra điều kiện và hoàn tiền.

Các quy trình này có chủ thể tương đối rõ, có dữ liệu công khai về thứ tự công việc và có thể bổ sung gateway cùng outcome tích cực/tiêu cực. Quy trình marketing địa phương vẫn có thể chọn, nhưng cần phỏng vấn Nike hoặc ACFC để biết bước phê duyệt, ngân sách, trách nhiệm và chỉ số đo lường.

## 2. Câu hỏi và phạm vi nghiên cứu

### 2.1. Câu hỏi chính

Những quy trình nghiệp vụ nào của Nike, chuỗi cung ứng Nike và kênh thương mại Nike được chứng minh là đang diễn ra tại Việt Nam, chủ thể nào thực hiện, và quy trình nào đủ bằng chứng để tiếp tục mô hình hóa bằng BPMN 2.0?

### 2.2. Câu hỏi phụ

- Hoạt động nào do Nike hoặc công ty con trực tiếp thực hiện?
- Hoạt động nào do nhà máy hợp đồng, nhà phân phối, cửa hàng hoặc đơn vị logistics thực hiện?
- Bằng chứng công khai mô tả được đến mức nào về actor, task, quyết định và outcome?
- Quy trình nào vừa đúng đề tài, vừa khả thi trong thời gian làm môn học?

### 2.3. Giới hạn khái niệm

Trong báo cáo này, "quy trình của Nike tại Việt Nam" được chia thành ba mức:

| Mức | Ý nghĩa | Cách ghi khi làm BPMN |
|---|---|---|
| Nike trực tiếp | Nike Vietnam LLC, công ty con hoặc đội ngũ Nike thực hiện | Pool/Lane của Nike |
| Chuỗi cung ứng Nike | Nhà máy và nhà cung cấp độc lập thực hiện theo hợp đồng, tiêu chuẩn hoặc đơn hàng Nike | Pool riêng của nhà cung cấp, trao đổi với Nike bằng message flow |
| Kênh thương mại Nike | Đối tác phân phối, cửa hàng, đơn vị vận chuyển hoặc kênh số phục vụ sản phẩm Nike | Pool riêng của đối tác; không gộp thành nhân viên Nike |

## 3. Phương pháp rà soát có hệ thống

### 3.1. Nguồn và chiến lược tìm kiếm

Tìm kiếm được thực hiện ngày 23/07/2026 bằng tiếng Việt và tiếng Anh trên:

- SEC EDGAR và báo cáo doanh nghiệp Nike.
- Nike Corporate, Purpose, Manufacturing Map, Nike Careers và Nike.com/vn Help.
- Cổng thông tin Chính phủ Việt Nam.
- Better Work, ILO và IFC.
- Website đối tác ACFC, trung tâm thương mại và các nguồn đối chiếu khác.
- Công cụ tìm kiếm web với giới hạn theo tên miền.

Các cụm truy vấn chính:

```text
site:nike.com/vn Nike Việt Nam giao hàng đổi trả điều khoản
site:careers.nike.com Vietnam Nike operations sourcing logistics
site:careers.nike.com Vietnam Responsible Supply Chain manufacturing engineering
site:baochinhphu.vn Nike Việt Nam nhà máy đối tác sản xuất
site:about.nike.com Vietnam supplier manufacturing sustainability
site:sec.gov Nike 10-K Vietnam manufacturing Air Manufacturing Innovation
site:betterwork.org Vietnam Nike suppliers
site:acfc.com.vn Nike chương trình cửa hàng đặt hàng
Nike Vietnam marketing event ACFC
site:manufacturingmap.nikeinc.com Vietnam Nike factory
```

### 3.2. Tiêu chí đưa vào và loại ra

**Đưa vào khi:**

- Nguồn nêu rõ Nike và Việt Nam, hoặc mô tả một quy trình toàn cầu có bằng chứng áp dụng tại cơ sở/khách hàng Việt Nam.
- Nguồn cho biết ít nhất một trong các yếu tố: chủ thể, công việc, dữ liệu đầu vào, quyết định, đầu ra hoặc điều kiện ngoại lệ.
- Ưu tiên nguồn hiện hành giai đoạn 2015 đến 23/07/2026; chấp nhận nguồn cũ hơn để cung cấp bối cảnh lịch sử.
- Nguồn chính thức, hồ sơ pháp lý, cơ quan nhà nước hoặc tổ chức độc lập có uy tín được ưu tiên.

**Loại ra khi:**

- Bài tập sinh viên, SEO blog, Wikipedia, Reddit hoặc nội dung không truy được nguồn gốc.
- Nội dung chỉ nói về chiến lược Nike toàn cầu nhưng không có liên hệ hợp lý với Việt Nam.
- Nội dung quảng cáo chỉ mô tả sản phẩm, không mô tả hoạt động nghiệp vụ.
- Bản trùng lặp, bản dịch trùng nội dung hoặc thông tin cũ đã có nguồn mới hơn.

### 3.3. Kết quả sàng lọc

Ba nhánh tìm kiếm được thực hiện song song. Do các nhánh dùng nhiều truy vấn trùng nhau và công cụ web không xuất được mã định danh ổn định cho từng kết quả, các số thô không được cộng lại để tránh đếm trùng:

| Nhánh tìm kiếm | Kết quả thô hiển thị | Mở/giữ sau sàng lọc | Trọng tâm |
|---|---:|---:|---|
| Nguồn Việt Nam và quy trình thị trường | 254 | 26 URL duy nhất | Chính phủ, Nike VN, ACFC, tuyển dụng |
| Nguồn Nike/SEC chính thức | 179 | 16 nguồn chính thức | 10-K, Manufacturing Map, Careers, Impact/Sustainability |
| Nguồn độc lập và phản chứng | Khoảng 265 | 23 tài liệu mở, 18 nguồn giữ lại | Hồ sơ môi trường, World Bank, ILO, FLA, WRC, nghiên cứu học thuật |

Báo cáo cuối dùng **40 URL duy nhất** sau khi loại trùng giữa ba nhánh. Mỗi URL được mở ít nhất một lần trong quá trình tìm kiếm và sàng lọc; 28/40 URL cốt lõi được mở lại trong một vòng kiểm tra nguồn riêng trước khi chốt báo cáo. Nguồn đối tác chỉ mô tả phần việc của chính đối tác. Nguồn độc lập được dùng để kiểm tra liệu quy trình tự công bố có được thực thi nhất quán hay không. Đây là rà soát phạm vi trên web có hệ thống, không tuyên bố tuân thủ đầy đủ PRISMA. Protocol không được đăng ký trước; không có hai người sàng lọc độc lập; công cụ tìm kiếm không xuất được danh sách loại trừ hoàn chỉnh. Phương pháp tổng hợp là phân nhóm quy trình, kiểm tra tính trực tiếp, đánh giá xung đột lợi ích và tìm phản chứng.

### 3.4. Thang độ tin cậy

| Mức | Cách hiểu trong báo cáo |
|---|---|
| A | Nguồn pháp lý, cơ quan nhà nước, thủ tục chính thức hoặc nguồn độc lập trực tiếp xác nhận claim |
| B | Nguồn Nike tự công bố, trực tiếp và chi tiết nhưng có nguy cơ chọn lọc thông tin có lợi |
| C | Nguồn đối tác tự mô tả hoạt động của chính họ; không đủ để khẳng định toàn bộ quan hệ với Nike |
| D | Nguồn gián tiếp, cũ hoặc không kiểm chứng; không dùng làm căn cứ chính |

Mức mô tả quy trình được phân biệt như sau:

- **Đã quan sát:** nguồn mô tả nhiều bước hoặc một flow có thứ tự.
- **Có bằng chứng chức năng:** nguồn chứng minh actor/task tồn tại nhưng chưa đủ event, gateway và outcome để gọi là AS-IS.
- **Suy luận cần xác minh:** flow được đề xuất từ nhiều dấu vết rời rạc; phải workshop/phỏng vấn trước khi vẽ.

## 4. Bản đồ chủ thể tại Việt Nam

| Chủ thể | Vai trò được chứng minh | Lưu ý khi vẽ BPMN |
|---|---|---|
| Nike Vietnam LLC | Hiện diện doanh nghiệp và quan hệ với mạng lưới đối tác tại Việt Nam được nguồn Chính phủ xác nhận | Chỉ dùng tên pháp nhân này khi nguồn hoặc workshop xác nhận đúng process owner |
| Đội ngũ Nike đặt tại TP.HCM | Tin tuyển dụng xác nhận các chức năng engineering, supplier management, quality, responsible supply chain và logistics; từng tin không luôn nêu pháp nhân sử dụng lao động | Pool nên ghi "Đơn vị Nike phụ trách tại Việt Nam" cho đến khi xác minh pháp nhân cụ thể |
| Air Manufacturing Innovation, Đồng Nai | Sản xuất cấu kiện Air-Sole và cấu kiện đệm | Là hoạt động Nike trực tiếp, không gộp với nhà máy hợp đồng |
| Nhà máy thành phẩm và nhà cung cấp vật liệu | Mua vật liệu, bố trí lao động, sản xuất, kiểm tra tại cơ sở, đáp ứng Code/CLS | Mỗi tổ chức là Pool ngoài Nike; sequence flow không đi xuyên Pool |
| Đơn vị đánh giá, Better Work, tổ chức đào tạo | Đánh giá, tư vấn, đào tạo hoặc xác minh tuân thủ | Pool ngoài; gửi kết quả bằng message flow |
| Đơn vị logistics và hải quan | Đặt chỗ, vận chuyển, thông quan, theo dõi và giao nhận | Tách Carrier/LSP và Hải quan thành Pool nếu mô hình chi tiết |
| Đơn vị vận hành Nike.com/vn, pháp nhân chưa xác định; Nike App và Consumer Services | Bán hàng số, quản lý đơn, CSKH, trả hàng, hoàn tiền | Có thể dùng Lane hệ thống và Lane nhân viên hỗ trợ; tên Pool phải giữ nguyên trạng thái pháp nhân chưa xác định |
| ACFC và cửa hàng Nike by ACFC | Phân phối/bán lẻ, cửa hàng, thương mại điện tử ACFC, marketing địa phương, after-sales | Pool ACFC, không đặt nhân viên ACFC trong Pool Nike |
| Khách hàng Việt Nam | Tìm sản phẩm, đặt hàng, thanh toán, cung cấp thông tin, nhận/đổi/trả hàng | Pool ngoài, trao đổi với Nike/ACFC bằng message flow |

Nguồn Chính phủ từng mô tả Nike Vietnam LLC điều phối mạng lưới hơn 200 nhà máy đối tác và hàng trăm doanh nghiệp trong chuỗi vào năm 2022. Số lượng này là ảnh chụp tại thời điểm công bố, không nên dùng như số hiện hành năm 2026. [Báo Điện tử Chính phủ, 2022](https://baochinhphu.vn/chinh-phu-viet-nam-da-dieu-hanh-hieu-qua-voi-chien-luoc-tam-nhin-va-su-can-dam-102221201185103517.htm)

## 5. Danh mục quy trình nghiệp vụ được tìm thấy

### 5.1. Chuỗi cung ứng, sản xuất và kỹ thuật

| STT | Quy trình | Chủ thể chính | Bằng chứng và mức tin cậy | Mức đủ dữ liệu để vẽ |
|---:|---|---|---|---|
| 1 | Xây dựng và quản lý mạng lưới nhà cung cấp | Nike Supplier Management/Sourcing, nhà cung cấp | Nike duy trì quan hệ dài hạn, thu thập phản hồi và đánh giá nhà cung cấp; Manufacturing Map công khai các cơ sở độc lập. [Nike: Our Approach to Sourcing](https://about.nike.com/en/resources/supplier-relationships), [Nike Manufacturing Map](https://manufacturingmap.nikeinc.com/) (B) | Khá |
| 2 | Phê duyệt nguồn cung mới | Nike, đơn vị đánh giá, nhà cung cấp tiềm năng | Nhà cung cấp thành phẩm Tier 1 phải qua New Source Approval và đạt tối thiểu Bronze trước khi sản xuất đầy đủ. [Nike: Foundational Expectations](https://about.nike.com/en/mission/initiatives/foundational-expectations-and-code-of-conduct) (B) | Rất tốt |
| 3 | Đánh giá nhà cung cấp bằng scorecard | Nike, nhà cung cấp | Nike đánh giá quality, delivery, cost, sustainability cùng năng lực leadership, operations, innovation và product creation. [Nike: Our Approach to Sourcing](https://about.nike.com/en/resources/supplier-relationships) (B) | Khá |
| 4 | Phát triển vật liệu và đánh giá manufacturing readiness | Nike Materials/Engineering, Product Creation, Quality, nhà máy | Tin tuyển dụng tại TP.HCM mô tả lập readiness plan, pilot, scale-up, early production và xử lý rủi ro cùng nhà cung cấp. [Nike Careers: Lead Footwear Materials Manufacturing Engineering](https://careers.nike.com/en/lead-footwear-materials-manufacturing-engineering-mme/job/R-85220) (B) | Tốt, nhưng cần phỏng vấn để có gateway cụ thể |
| 5 | Mua nguyên vật liệu cho sản xuất | Nhà máy hợp đồng, nhà cung cấp Tier 2, Nike giám sát | 10-K FY2026 nêu nhà máy hợp đồng mua các vật liệu chính từ nhà cung cấp Tier 2. [Nike FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm) (A) | Trung bình |
| 6 | Sản xuất, kiểm tra và đóng gói giày thành phẩm | Nhà máy hợp đồng độc lập | FY2026, Việt Nam chiếm khoảng 52% sản lượng giày và 34% sản lượng quần áo Nike Brand. Hồ sơ KCN xác nhận TKG Taekwang Vina gia công giày Nike; giấy phép môi trường năm 2024 mô tả chuỗi cắt, in/sơn logo, ép, may, mài, quét keo, gia nhiệt, dán/ép đế, kiểm tra và đóng gói. [Nike FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm), [Báo cáo KCN Biên Hòa II](https://thamvan.mae.gov.vn/Uploads/19092023/3GB%C3%A1o%20c%C3%A1o%20GPMT%20KCNBH2_18.8.2023%20signed.pdf), [Giấy phép môi trường TKG Taekwang Vina 2024](https://dnieza.dongnai.gov.vn/Lists/VanBan/Attachments/3331/122_2024.8.30%20GPMT%20-%20TKG%20Taekwang%20ok%20AT_20240904104347.844.signed.signed.signed.signed.pdf) (A) | Đã quan sát, rất tốt cho một nhà máy cụ thể |
| 7 | Sản xuất cấu kiện đệm Air | Air Manufacturing Innovation tại Đồng Nai | 10-K xác nhận cơ sở Nike-owned/leased tại Đồng Nai sản xuất Air-Sole và cấu kiện đệm. Nike cũng công bố chương trình hiện đại hóa Air MI tại Việt Nam. [Nike FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm), [Nike Global Operations Changes, 2026](https://about.nike.com/en/newsroom/releases/nike-inc-april-23-2026-global-operations-announcement) (A/B) | Trung bình, do thiếu SOP nội bộ |
| 8 | Cải tiến hệ thống sản xuất và quản lý chất lượng | Nike Manufacturing Systems/Quality, factory partners | Vai trò Nike tại TP.HCM phối hợp Product Creation, Sourcing, Responsible Supply Chain và Cost Engineering để củng cố hệ thống quản lý chất lượng tại nhà máy, xây dựng năng lực, kết nối số, năng suất, xác nhận kỹ thuật cơ sở và dự án bền vững. [Nike Careers: Senior Manufacturing Systems Engineer](https://careers.nike.com/senior-manufacturing-systems-engineer/job/R-83566) (B) | Khá |
| 9 | Kiểm tra tuân thủ, khắc phục và chấm dứt nhà cung cấp | Nike Responsible Supply Chain, nhà cung cấp, assessor | Nike dùng đánh giá ngành và audit không báo trước; cơ sở vi phạm vào Targeted Remediation; không khắc phục có thể bị sanction, termination và responsible exit. [Nike: Foundational Expectations](https://about.nike.com/en/mission/initiatives/foundational-expectations-and-code-of-conduct) (B) | Rất tốt |
| 10 | Quản lý lao động, sức khỏe, an toàn và môi trường tại cơ sở | Nhà cung cấp; Nike đặt yêu cầu và giám sát | Code/CLS yêu cầu hệ thống về lao động, an toàn, môi trường và xác minh. Giấy phép của TKG Taekwang Vina mô tả thu gom, xử lý nước thải/khí thải, phân loại chất thải và ứng phó sự cố tại một cơ sở gia công Nike. [Bộ quy tắc ứng xử Nike 2025, tiếng Việt](https://media.about.nike.com/files/efd7c3b8-de95-41fe-b158-8c27e484f81c/Nike-Inc.-Code-of-Conduct-2025---Vietnamese.pdf), [Nike Responsible Supply Chain](https://about.nike.com/en/mission/focus-areas/responsible-supply-chain), [Giấy phép môi trường TKG Taekwang Vina 2024](https://dnieza.dongnai.gov.vn/Lists/VanBan/Attachments/3331/122_2024.8.30%20GPMT%20-%20TKG%20Taekwang%20ok%20AT_20240904104347.844.signed.signed.signed.signed.pdf) (A/B) | Đã quan sát ở một cơ sở; tốt nếu chọn một quy trình con |
| 11 | Thu nhận tiếng nói người lao động và lập kế hoạch cải thiện | Người lao động, nhà cung cấp, Nike | Nike tự công bố việc dùng Engagement and Wellbeing Survey, hướng dẫn nhà cung cấp chuyển kết quả thành action plan và duy trì Speak Up Portal. Nguồn này không chứng minh độc lập rằng mọi người lao động đều tiếp cận được hoặc mọi khiếu nại được xử lý hiệu quả. [Nike: Worker Voice](https://about.nike.com/en/mission/initiatives/worker-voice) (B) | Tốt |
| 12 | Phát triển bình đẳng giới và năng lực lãnh đạo nữ | Nhà cung cấp, Nike, CARE/IFC/đối tác đào tạo | Nhà cung cấp làm Self-Diagnostic Tool hằng năm; Nike triển khai capability building và chương trình leadership tại Việt Nam. [Nike: Gender Equity](https://about.nike.com/en/mission/initiatives/supply-chain-gender-equity) (B) | Khá |
| 13 | Quản lý năng lượng, phát thải và chất thải nhà cung cấp | Nike Sustainability, nhà cung cấp, tổ chức ngành, cơ quan nhà nước | Nike mô tả Supplier Climate Action Program và hoạt động hỗ trợ cơ chế điện trực tiếp tại Việt Nam; dữ liệu FY24 nêu các loại đánh giá môi trường và chất thải. [Nike: Reducing Carbon Footprint](https://about.nike.com/en/mission/initiatives/reducing-carbon-footprint), [Nike FY24 Sustainability Data](https://media.about.nike.com/files/f37dfe60-0341-4db1-8ab9-6156da717313/FY24-NIKE%2C-Inc.-Sustainability-Data.pdf) (B) | Khá, nên chọn một quy trình con |
| 14 | Lập kế hoạch và thực thi logistics xuất phát | Nike Logistics, LSP/carrier, nhà máy | Một tin tuyển dụng Nike tại TP.HCM từng mô tả capacity forecast, booking, chứng từ, TMS/track-and-trace và xử lý ngoại lệ với LSP và nhà máy. Trang việc làm đã hết hạn và trả 404 khi kiểm tra ngày 23/07/2026, nên nội dung này chỉ là bằng chứng lịch sử về chức năng, không phải SOP hiện hành. [Nike Careers: Senior Analyst Ocean Operations](https://careers.nike.com/zh-tw/senior-analyst-ocean-operations/job/R-75939) (C) | Trung bình |

Better Work Việt Nam cung cấp nguồn đối chiếu độc lập cho thấy ngành may mặc và giày dép sử dụng assessment, advisory và training để cải thiện điều kiện làm việc và năng lực cạnh tranh. Nguồn này xác nhận mô hình kiểm tra/cải tiến của ngành, nhưng không chứng minh mọi nhà máy trong chương trình đều sản xuất cho Nike. [Better Work Việt Nam](https://www.betterwork.org/vietnam/our-programme/) (A cho mô hình ngành, gián tiếp với từng nhà máy Nike).

Các nghiên cứu và điều tra độc lập cũng chỉ ra rằng **có quy trình audit không đồng nghĩa quy trình luôn hiệu quả**. Nghiên cứu trên dữ liệu nhà cung cấp Nike cho thấy kết quả cải thiện không đồng đều; nghiên cứu tại Việt Nam ghi nhận hiện tượng tuân thủ hình thức; vụ Hansae cho thấy vi phạm vẫn có thể tồn tại và cần corrective action, theo dõi và tiếng nói người lao động. [Locke, Qin, & Brause, 2007](https://journals.sagepub.com/doi/10.1177/001979390706100101), [Kim, 2013](https://doi.org/10.1016/j.worlddev.2012.12.004), [Fair Labor Association: Hansae Vietnam](https://www.fairlabor.org/reports/hansae-viet-nam-second-investigation/), [Worker Rights Consortium: Hansae Vietnam](https://www.workersrights.org/our-work/factory-investigations/hansae-vietnam/) (A/B, dữ liệu lịch sử và không đại diện cho toàn mạng lưới hiện tại).

### 5.2. Bán hàng số, giao nhận và dịch vụ khách hàng

| STT | Quy trình | Chủ thể chính | Bằng chứng và mức tin cậy | Mức đủ dữ liệu để vẽ |
|---:|---|---|---|---|
| 15 | Đặt hàng và thanh toán trên Nike.com/vn/Nike App | Khách hàng, hệ thống của kênh Nike.com/vn, đơn vị thanh toán | Kênh chấp nhận thẻ quốc tế, Google Pay và PayPal; khách hoàn tất checkout và nhận thông tin đơn. [Nike VN: Payment Options](https://www.nike.com/vn/help/a/payment-options) (A cho thủ tục công khai) | Rất tốt |
| 16 | Xác minh thông tin và thông quan đơn hàng xuyên biên giới | Khách hàng, đơn vị vận hành Nike.com/vn, pháp nhân chưa xác định, carrier, Hải quan Việt Nam | Đơn được gửi từ nước ngoài; khách cung cấp CCCD/hộ chiếu; nếu không cung cấp trong bốn ngày làm việc, đơn không thể dispatch và bị hủy; sau xác minh, đơn vị vận hành phối hợp carrier và hải quan để clearance. [Nike VN: Customs Verification](https://www.nike.com/vn/help/a/verify-passport) (A) | Rất tốt |
| 17 | Xử lý, giao và theo dõi đơn | Đơn vị vận hành Nike.com/vn, pháp nhân chưa xác định, carrier, khách hàng | Đơn thường được xử lý ngày làm việc; giao tiêu chuẩn thường trong sáu ngày làm việc; thuế/phí nằm trong tổng checkout. [Nike VN: Shipping and Delivery](https://www.nike.com/vn/help/a/shipping-delivery), [Nike VN: Order Tracking](https://www.nike.com/vn/help/a/order-tracking) (A) | Rất tốt |
| 18 | Tiếp nhận trả hàng và reverse logistics | Khách hàng, hệ thống của kênh Nike.com/vn, đơn vị nhận hàng, trung tâm kiểm tra | Thủ tục công khai gồm xác thực đơn, chọn hàng/lý do, tạo nhãn, đóng gói, giao cho nhân viên nhận và kiểm tra điều kiện. [Nike VN: How to Return](https://www.nike.com/vn/help/a/how-to-return) (A) | Rất tốt |
| 19 | Kiểm tra và hoàn tiền | Trung tâm xử lý, hệ thống thanh toán, khách hàng | Sau khi nhận hàng trả, Nike thường cần bốn ngày làm việc để xử lý và phát hành hoàn tiền; ngân hàng có thể cần thêm thời gian ghi có. [Nike VN: Refund Information](https://www.nike.com/vn/help/a/refund-info) (A) | Rất tốt |
| 20 | Tiếp nhận bảo hành sản phẩm | Khách hàng, Nike.com/App hoặc cửa hàng, CSKH | Sản phẩm lỗi vật liệu/gia công được phân tuyến theo thời gian và kênh mua; thủ tục online và cửa hàng khác nhau. [Nike VN: Shoe Warranty](https://www.nike.com/vn/help/a/shoe-warranty) (A) | Tốt |
| 21 | Chăm sóc khách hàng đa kênh | Khách hàng, chat/hotline, đội hỗ trợ | Nike công bố chat, hotline và nhóm hỗ trợ về orders, payment, delivery, returns, shopping và membership cho Việt Nam. [Nike VN Help](https://www.nike.com/vn/help/), [Nike Contact Directory](https://www.nike.com/vn/help/a/nike-contact-directory) (A) | Tốt |
| 22 | Quản lý membership, ưu đãi và trải nghiệm | Khách hàng, Nike App/CRM, đội event | Membership cung cấp sản phẩm/ưu đãi, vận chuyển, ứng dụng và trải nghiệm; Nike Experiences cho phép đăng ký sự kiện qua App. [Nike VN Membership](https://www.nike.com/vn/membership), [Nike VN: Experiences](https://www.nike.com/vn/help/a/experiences) (B) | Khá |

Kênh Nike.com/vn là bán hàng xuyên biên giới cho khách Việt Nam. Bằng chứng hiện có không xác định chắc pháp nhân nhập khẩu của từng đơn, vì vậy không đặt mặc định Nike Vietnam LLC vào Lane "nhà nhập khẩu".

**Lưu ý bảo vệ dữ liệu:** khi vẽ BPMN, CCCD/hộ chiếu chỉ được biểu diễn bằng Data Object trừu tượng như "Thông tin định danh phục vụ thông quan". Không đưa số định danh, ảnh giấy tờ hoặc dữ liệu khách hàng thật vào sơ đồ hay phụ lục.

### 5.3. Phân phối, bán lẻ và marketing do đối tác thực hiện

| STT | Quy trình | Chủ thể chính | Bằng chứng và mức tin cậy | Mức đủ dữ liệu để vẽ |
|---:|---|---|---|---|
| 23 | Quản lý mạng lưới cửa hàng Nike by ACFC | ACFC, cửa hàng, khách hàng | ACFC tự công bố danh sách 40 cửa hàng Nike tại ngày truy cập 23/07/2026 và tự nhận là nhà phân phối chính thức. Đây là ảnh chụp theo thời điểm, không phải số liệu do Nike xác nhận. [ACFC: Nike Việt Nam](https://www.acfc.com.vn/nike.html) (C) | Khá |
| 24 | Bán hàng trực tuyến trên ACFC | Khách hàng, website ACFC, payment, kho, CSKH | ACFC công bố các bước chọn vùng, đăng nhập/đăng ký, chọn Nike, thêm giỏ, đặt hàng và thanh toán. [ACFC: Hướng dẫn đặt hàng Nike](https://www.acfc.com.vn/huong-dan-dat-hang-nike) (C) | Rất tốt, nhưng là quy trình ACFC |
| 25 | Bán hàng và after-sales tại cửa hàng | Nhân viên ACFC, khách hàng, quản lý cửa hàng | Trang Nike của ACFC nêu mạng lưới cửa hàng, đóng gói, đổi trả, hotline và hỗ trợ khách. [ACFC: Nike Việt Nam](https://www.acfc.com.vn/nike.html) (C) | Tốt, nhưng là quy trình ACFC |
| 26 | Lập và triển khai chiến dịch marketing địa phương | ACFC marketing, agency/KOL, cửa hàng, nền tảng số, khách hàng | ACFC công bố các sự kiện, tài trợ và livestream Nike. Case Aim Da Max năm 2019 mô tả flow Facebook AR -> trò chơi -> quét QR tại cửa hàng -> ưu đãi/mua hàng, nhưng số hiệu quả do bên tham gia chiến dịch báo cáo. [ACFC: Nike livestream 12/06/2024](https://www.acfc.com.vn/blog/su-kien-livestream-doc-quyen-nike-acfc-x-linh-an-12-06-2024.html), [IPPG/ACFC: hành trình bán lẻ](https://ippgroup.vn/en/news/acfc-the-10-year-journey-to-the-success-in-mid-tier-fashion-retail-n1979), [WARC: Nike Aim Da Max](https://www.warc.com/en/article/nike%3A-aim-da-max-02b815e526a14efabc08cbcef48eeb6e) (B/C) | Đã quan sát phần thực thi; phần phê duyệt cần phỏng vấn |
| 27 | Tuyển dụng nhân viên bán lẻ | ACFC HR, ứng viên, quản lý cửa hàng | ACFC công bố hoạt động tuyển tập trung cho nhiều thương hiệu, có Nike. [ACFC Careers](https://tuyendung.acfc.com.vn/news/fly-with-acfc-2023-khu-v%E1%BB%B0c-h%C3%80-n%E1%BB%98i-post88) (C) | Khá, nhưng không phải tuyển dụng Nike Vietnam LLC |

ACFC tự công bố vị thế phân phối chính thức và từng dùng từ "độc quyền". Tuy nhiên, KCONS lại công bố giấy ủy quyền 2025-2027 từ EMERS Vietnam. Chưa có xác nhận hiện hành trực tiếp từ Nike giải quyết mâu thuẫn này. Báo cáo chỉ gọi ACFC là **đối tác bán lẻ/phân phối lớn có bằng chứng hoạt động**, không kết luận ACFC là đơn vị độc quyền hiện nay. [KCONS: Chứng nhận Nike Việt Nam](https://kcons.vn/pages/chung-nhan-nike-viet-nam) chỉ được dùng để nhận diện mâu thuẫn, không dùng làm bằng chứng chính.

### 5.4. Nhóm chưa đủ bằng chứng công khai

Không tìm được tài liệu đủ mạnh để mô tả AS-IS chi tiết cho các nhóm sau:

- Demand planning và phân bổ đơn hàng cụ thể cho từng nhà máy tại Việt Nam.
- Wholesale order, nhập khẩu hàng bán tại Việt Nam, replenishment và quản lý tồn kho cửa hàng.
- Pháp nhân hiện là importer of record hoặc nhà phân phối độc quyền.
- Trung tâm phân phối Nike-owned hoặc cửa hàng Nike-owned tại Việt Nam.
- Finance, thuế, pháp chế, data/privacy và quản trị văn phòng nội bộ của Nike Vietnam LLC.
- Tuyển dụng, onboarding và đánh giá nhân viên Nike tại Việt Nam ngoài các bước tuyển dụng toàn cầu công khai.
- Quy trình phê duyệt, ngân sách và đo hiệu quả của chiến dịch marketing bản địa hiện hành.

Thiếu nguồn công khai không có nghĩa các quy trình này không tồn tại. Chúng chỉ chưa đủ bằng chứng để đưa vào BPMN AS-IS.

## 6. Mô tả bằng lời các quy trình phù hợp nhất trước khi vẽ

### 6.1. Quy trình công nghệ sản xuất giày tại TKG Taekwang Vina, nhà máy đối tác có gia công Nike

**Actors:** các công đoạn hoặc nhóm thực hiện dự kiến gồm kho/nguyên liệu, cắt, in/sơn, ép, may, dán đế, kiểm tra chất lượng và đóng gói; Nike là khách hàng/buyer ở Pool ngoài. Giấy phép xác nhận chuỗi công nghệ, không xác nhận mỗi công đoạn là một phòng ban hoặc Lane riêng.  
**Customer của quy trình:** Nike và đơn vị nhận thành phẩm theo hợp đồng.  
**Thứ tự được hồ sơ môi trường mô tả:** nhận nguyên liệu -> cắt -> in lụa/sơn logo -> ép trang trí -> may mũ giày -> may đế giữa và mũ giày -> mài -> quét keo -> gia nhiệt -> ép định hình dán đế và mũ -> ép tổng lực -> kiểm tra -> đóng gói -> thành phẩm. Subprocess dán đế gồm nhận chi tiết từ kho -> kiểm tra chất lượng -> quét keo lót -> sấy -> quét keo lần một -> sấy -> quét keo lần hai -> sấy -> dán -> ép tổng lực -> lưu trữ cho công đoạn tiếp theo. [Giấy phép môi trường TKG Taekwang Vina 2024](https://dnieza.dongnai.gov.vn/Lists/VanBan/Attachments/3331/122_2024.8.30%20GPMT%20-%20TKG%20Taekwang%20ok%20AT_20240904104347.844.signed.signed.signed.signed.pdf)  
**Gateway cần xác minh khi workshop:** chi tiết có đạt kiểm tra trước dán không; thành phẩm có đạt kiểm tra cuối không; hàng lỗi được sửa, tái chế hay loại bỏ theo tiêu chí nào.  
**Outcome tích cực:** giày đạt chất lượng và được đóng gói.  
**Outcome tiêu cực:** chi tiết/thành phẩm không đạt và chuyển sang luồng xử lý lỗi cần xác minh.

Đây là flow sản xuất cụ thể nhất tìm được, nhưng process owner là nhà máy hợp đồng TKG Taekwang Vina. Tên sơ đồ phải ghi rõ "sản xuất giày Nike tại nhà máy đối tác", không ghi "nhà máy Nike".

### 6.2. Phê duyệt nguồn cung mới

**Actors:** Nike Supplier Management/Responsible Supply Chain, nhà cung cấp tiềm năng, đơn vị đánh giá.  
**Customer của quy trình:** đội Product/Sourcing cần nguồn cung đạt yêu cầu.  
**Bước được nguồn xác nhận:** nhà cung cấp Tier 1 tiềm năng phải qua New Source Approval -> cơ sở được đánh giá theo Code/CLS -> gateway "đạt Bronze?" -> nếu đạt, được phép bắt đầu sản xuất đầy đủ. [Nike: Foundational Expectations](https://about.nike.com/en/mission/initiatives/foundational-expectations-and-code-of-conduct)  
**Bước suy luận cần workshop:** cách nộp hồ sơ, số vòng đánh giá, quyền yêu cầu cải thiện và điều kiện từ chối.
**Outcome tích cực:** nguồn cung mới được phê duyệt.  
**Outcome tiêu cực:** nguồn cung bị từ chối hoặc chưa được phép sản xuất đầy đủ.

### 6.3. Khắc phục vi phạm của nhà cung cấp hiện hữu

**Actors:** Nike Responsible Supply Chain, nhà cung cấp hiện hữu, assessor và các bên liên quan nếu phải responsible exit.  
**Customer của quy trình:** Nike và các bên cần cơ sở sản xuất tuân thủ; gián tiếp là người lao động.  
**Thứ tự chính:** assessment/audit/allegation phát hiện vấn đề -> gateway "có vi phạm?" -> nếu không, đóng đánh giá và tiếp tục hợp tác -> nếu có, lập Targeted Remediation -> nhà cung cấp thực hiện hành động -> kiểm tra lại -> gateway "đã khắc phục?" -> nếu đạt, đóng vấn đề và tiếp tục -> nếu không, sanction hoặc responsible exit.  
**Outcome tích cực:** vi phạm được khắc phục và quan hệ tiếp tục.  
**Outcome tiêu cực:** áp dụng chế tài hoặc chấm dứt có trách nhiệm.

Đây là quy trình chuẩn Nike công bố ở cấp toàn cầu, được dùng làm mô hình tham chiếu cho mạng lưới nhà cung cấp tại Việt Nam. Việc áp dụng, hệ thống và quyền phê duyệt cụ thể tại Việt Nam cần workshop xác nhận. Quy trình phù hợp cho BPMN conceptual nhưng chưa đủ để gọi là AS-IS riêng của Việt Nam. [Nike: Foundational Expectations](https://about.nike.com/en/mission/initiatives/foundational-expectations-and-code-of-conduct)

### 6.4. Xử lý đơn Nike.com/vn và thông quan

**Actors:** khách hàng, đơn vị vận hành Nike.com/vn, pháp nhân chưa xác định, đơn vị thanh toán, carrier, Hải quan Việt Nam, Consumer Services.  
**Customer:** người mua tại Việt Nam.  
**Bước được nguồn xác nhận:** khách đặt hàng -> cung cấp CCCD/hộ chiếu -> gateway "cung cấp trong bốn ngày làm việc?" -> nếu không, đơn bị hủy -> nếu có, đơn vị xử lý đơn phối hợp carrier và hải quan để clearance và giao hàng. [Nike VN: Customs Verification](https://www.nike.com/vn/help/a/verify-passport), [Nike VN: Shipping and Delivery](https://www.nike.com/vn/help/a/shipping-delivery)  
**Giả định mô hình hóa cần workshop:** gateway clearance thành công/thất bại, trách nhiệm khi hồ sơ bị từ chối và escalation sang CSKH.
**Outcome tích cực:** đơn được thông quan và giao thành công.  
**Outcome tiêu cực:** đơn bị hủy do thiếu thông tin, clearance thất bại hoặc giao không thành công.

Quy trình này có dữ liệu front-stage rõ nhất và phù hợp để vẽ BPMN collaboration giữa Customer, Đơn vị vận hành Nike.com/vn, Payment, Carrier và Customs.

### 6.5. Trả hàng và hoàn tiền

**Actors:** khách hàng, hệ thống của kênh Nike.com/vn, carrier/nhân viên nhận hàng, đơn vị vận hành Nike.com/vn, pháp nhân chưa xác định, đơn vị xử lý trả hàng và đơn vị thanh toán.  
**Customer:** người mua yêu cầu trả hàng.  
**Bước được nguồn xác nhận:** khách truy cập đơn -> chọn món và lý do -> xác nhận địa chỉ -> nhận/in nhãn -> đóng gói -> bàn giao cho carrier -> đơn vị xử lý trả hàng kiểm tra tình trạng -> nếu đủ điều kiện, phát hành hoàn tiền và thông báo. [Nike VN: How to Return](https://www.nike.com/vn/help/a/how-to-return), [Nike VN: Refund Information](https://www.nike.com/vn/help/a/refund-info)  
**Giả định mô hình hóa cần workshop:** kiểm tra sơ bộ tự động, pháp nhân kiểm tra hàng, tiêu chí gateway chi tiết và cách xử lý hàng bị từ chối.
**Outcome tích cực:** hoàn tiền thành công.  
**Outcome tiêu cực:** yêu cầu bị từ chối hoặc hàng không thể hoàn trả cho khách sau các lần giao lại thất bại.

### 6.6. Đánh giá manufacturing readiness

**Actors:** Nike Materials Manufacturing Engineering, Product Creation, Quality, Chemical Engineering, Supplier Management và nhà máy.  
**Customer:** đội Product Creation cần vật liệu/sản phẩm sẵn sàng sản xuất hàng loạt.  
**Thứ tự khái quát:** tiếp nhận thiết kế/yêu cầu -> đánh giá năng lực và rủi ro -> lập readiness plan -> pilot -> kiểm tra kết quả -> gateway "đạt yêu cầu?" -> nếu đạt, scale-up và early production -> nếu không, sửa vật liệu/quy trình và thử lại. [Nike Careers: Lead Footwear Materials Manufacturing Engineering](https://careers.nike.com/en/lead-footwear-materials-manufacturing-engineering-mme/job/R-85220)  
**Outcome tích cực:** sẵn sàng sản xuất hàng loạt.  
**Outcome tiêu cực:** trì hoãn, thay đổi giải pháp hoặc không phê duyệt.

Luồng này được tái dựng từ mô tả tuyển dụng, chỉ là bằng chứng chức năng, không phải SOP hoặc AS-IS đã xác nhận. Cần phỏng vấn để xác định tiêu chí quyết định, tài liệu và hệ thống nội bộ.

### 6.7. Lập và thực thi chiến dịch marketing Nike tại Việt Nam

**Actors dự kiến:** Nike regional/brand team, ACFC marketing, agency/KOL, quản lý kênh số/cửa hàng và khách hàng.  
**Customer:** người tiêu dùng mục tiêu tại Việt Nam.  
**Thứ tự mới chỉ là giả thuyết cần kiểm chứng:** nhận global brief/product launch -> nghiên cứu thị trường -> đề xuất local plan và ngân sách -> Nike/ACFC phê duyệt -> sản xuất nội dung -> triển khai trên social, livestream, cửa hàng hoặc sự kiện -> thu dữ liệu -> đánh giá KPI -> tối ưu hoặc kết thúc.  
**Outcome tích cực:** chiến dịch được duyệt và đạt KPI.  
**Outcome tiêu cực:** không được duyệt, trễ phát hành hoặc không đạt KPI và phải điều chỉnh.

Nguồn Internet chỉ chứng minh các hoạt động đầu ra như livestream, sự kiện và ưu đãi. Các bước brief, ngân sách, approval và measurement chưa được chứng minh. Không nên vẽ quy trình này như AS-IS chính thức nếu chưa phỏng vấn người làm tại Nike/ACFC.

## 7. Xếp hạng để chọn đề tài BPMN

Thang 1-5 là đánh giá của nhóm nghiên cứu, không phải số liệu của Nike:

- **Bằng chứng:** 5 = nguồn trực tiếp mô tả nhiều bước và chủ thể; 3 = chỉ chứng minh actor/task cấp cao; 1 = chủ yếu suy luận.
- **Giá trị BPMN:** 5 = có flow, điểm quyết định và kết quả +/-; 3 = có chuỗi task nhưng gateway cần xác minh; 1 = chỉ là chức năng.
- **Dễ thu thập thêm:** 5 = thủ tục công khai; 3 = cần phỏng vấn; 1 = phụ thuộc SOP khó tiếp cận.

Hạng được xếp theo tổng ba điểm. Nếu bằng điểm, ưu tiên quy trình có luồng được quan sát trực tiếp và phù hợp hơn với phạm vi môn học.

| Hạng | Quy trình | Bằng chứng | Giá trị BPMN | Dễ thu thập thêm | Khuyến nghị |
|---:|---|---:|---:|---:|---|
| 1 | Nike.com/vn order-to-delivery và customs | 5 | 5 | 5 | Chọn nếu muốn quy trình rõ, dễ bảo vệ |
| 2 | Return-to-refund và warranty | 5 | 5 | 5 | Chọn nếu muốn quy trình dịch vụ có nhiều nhánh +/- |
| 3 | Khắc phục vi phạm nhà cung cấp hiện hữu | 5 | 5 | 4 | Chọn nếu muốn quy trình chiến lược, nhiều Pool/Lane |
| 4 | Công nghệ sản xuất giày tại TKG Taekwang Vina | 4 | 4 | 4 | Chuỗi công đoạn rõ; gateway chất lượng cần workshop; phải ghi rõ nhà máy đối tác |
| 5 | Manufacturing readiness và scale-up | 4 | 5 | 3 | Chọn nếu phỏng vấn được người trong ngành |
| 6 | Ocean origin logistics và xử lý ngoại lệ | 4 | 5 | 3 | Tốt nhưng cần làm rõ LSP, chứng từ và Incoterm |
| 7 | Worker voice và remediation | 4 | 4 | 3 | Phù hợp chủ đề ESG/nhân sự chuỗi cung ứng |
| 8 | Bán hàng ACFC online/offline | 4 | 4 | 4 | Dễ làm, nhưng tên đề tài phải ghi rõ "Nike by ACFC" |
| 9 | Marketing campaign địa phương | 3 | 5 | 2 | Aim Da Max cho flow lịch sử; AS-IS hiện tại cần phỏng vấn |

### Đề xuất phạm vi theo cách hiểu đề tài

**Nếu giảng viên chấp nhận phạm vi hệ sinh thái/chuỗi cung ứng Nike:**

1. **Sản xuất tại đối tác:** Sản xuất và kiểm tra chất lượng giày tại TKG Taekwang Vina.
2. **Quản trị chuỗi cung ứng:** Khắc phục vi phạm nhà cung cấp hiện hữu.
3. **Bán hàng/logistics:** Xử lý đơn Nike.com/vn và thông quan.

**Nếu giảng viên bắt buộc Nike phải là process owner:**

1. Khắc phục vi phạm nhà cung cấp theo chuẩn Nike, vẽ conceptual và xác nhận quyền quyết định tại Việt Nam.
2. Đánh giá manufacturing readiness và scale-up do đội ngũ Nike phối hợp nhà máy, cần workshop để hoàn thiện AS-IS.
3. Xử lý front-stage đơn Nike.com/vn, đặt tên Pool là "Đơn vị vận hành Nike.com/vn, pháp nhân chưa xác định".

Quy trình **trả hàng và hoàn tiền** là phương án dự phòng có dữ liệu rất tốt. Nếu môn học bắt buộc bám marketing, đổi một quy trình thành **Aim Da Max hoặc lập và triển khai chiến dịch Nike by ACFC**, nhưng phải ghi rõ case lịch sử và bổ sung phỏng vấn để xác nhận AS-IS hiện tại.

## 8. Rủi ro thiên lệch và hạn chế

| Rủi ro | Ảnh hưởng | Cách xử lý trong báo cáo |
|---|---|---|
| Nike tự công bố phần lớn dữ liệu ESG | Có thể chọn lọc thành tích tốt và giảm chi tiết vi phạm | Gắn mức B, đối chiếu Better Work/ILO, không suy diễn kết quả cho mọi nhà máy |
| Tin tuyển dụng mô tả trách nhiệm mong đợi | Chứng minh chức năng tồn tại nhưng không phải SOP hoàn chỉnh | Chỉ dùng để xác định actor/task ở mức cao |
| Chưa thu thập tiếng nói sơ cấp của người lao động | Không thể đánh giá trực tiếp khả năng tiếp cận cơ chế khiếu nại hoặc hiệu quả xử lý hiện tại | Ghi rõ Worker Voice là cơ chế Nike tự công bố; FLA, WRC và Kim là bằng chứng lịch sử, không đại diện toàn mạng lưới hiện tại |
| Trang Help chỉ mô tả phần khách nhìn thấy | Không cho biết hệ thống backend, SLA nội bộ và pháp nhân xử lý | Chỉ vẽ front-stage chắc chắn; ghi bước backend là cần xác minh |
| ACFC và KCONS tự mô tả quyền phân phối | Có xung đột lợi ích và mâu thuẫn về quyền phân phối hiện tại | Không kết luận độc quyền; chỉ gán hoạt động quan sát được cho đúng đối tác |
| Thiếu tài liệu nội bộ nhà máy | Không biết thứ tự chi tiết, tiêu chí quality và cách xử lý phế phẩm | Không vẽ quy trình sản xuất chi tiết nếu chưa phỏng vấn |
| Tìm kiếm web thay đổi theo thời gian | Kết quả và trang tuyển dụng có thể biến mất | Ghi ngày truy cập và lưu evidence log/link trong báo cáo |

Kết luận mạnh nhất có thể bảo vệ là: **Nike vận hành tại Việt Nam qua một hệ sinh thái gồm đội ngũ/cơ sở Nike, nhà máy và nhà cung cấp độc lập, đối tác thương mại, đơn vị logistics và kênh số phục vụ khách Việt Nam.** Báo cáo không đủ bằng chứng để khẳng định toàn bộ trình tự nội bộ của Nike Vietnam LLC hoặc mọi nhà máy.

## 9. Khoảng trống cần phỏng vấn trước khi vẽ AS-IS

1. Ai là process owner tại Việt Nam cho từng quy trình?
2. Nhà cung cấp gửi hồ sơ và kết quả assessment qua hệ thống nào?
3. Tiêu chí Bronze, quality gate và approval authority cụ thể ra sao?
4. Nike Vietnam LLC, Nike regional và factory partner chia trách nhiệm thế nào khi pilot/scale-up?
5. Ai là importer of record và đơn vị fulfillment của đơn Nike.com/vn?
6. ACFC, EMERS và Nike phân chia quyền nhập khẩu, phân phối, retail và marketing hiện nay thế nào?
7. Campaign brief được localize, duyệt ngân sách, duyệt nội dung và đo KPI theo quy trình nào?
8. Trường hợp giao hàng, clearance, return hoặc supplier remediation thất bại được escalation đến ai?

## 10. Tài liệu tham khảo

- ACFC. (2023, September 6). [Fly with ACFC 2023, khu vực Hà Nội](https://tuyendung.acfc.com.vn/news/fly-with-acfc-2023-khu-v%E1%BB%B0c-h%C3%80-n%E1%BB%98i-post88).
- ACFC. (2024, June 12). [Sự kiện livestream độc quyền Nike ACFC](https://www.acfc.com.vn/blog/su-kien-livestream-doc-quyen-nike-acfc-x-linh-an-12-06-2024.html).
- ACFC. (n.d.). [Hướng dẫn đặt hàng Nike](https://www.acfc.com.vn/huong-dan-dat-hang-nike). Truy cập 23/07/2026.
- ACFC. (n.d.). [Nike Việt Nam](https://www.acfc.com.vn/nike.html). Truy cập 23/07/2026.
- Better Work. (n.d.). [Better Work Việt Nam: Our Programme](https://www.betterwork.org/vietnam/our-programme/).
- Báo Điện tử Chính phủ. (2022, December 1). [Chính phủ Việt Nam đã điều hành hiệu quả với chiến lược, tầm nhìn và sự can đảm](https://baochinhphu.vn/chinh-phu-viet-nam-da-dieu-hanh-hieu-qua-voi-chien-luoc-tam-nhin-va-su-can-dam-102221201185103517.htm).
- Ban Quản lý các Khu công nghiệp Đồng Nai. (2024). [Giấy phép môi trường TKG Taekwang Vina](https://dnieza.dongnai.gov.vn/Lists/VanBan/Attachments/3331/122_2024.8.30%20GPMT%20-%20TKG%20Taekwang%20ok%20AT_20240904104347.844.signed.signed.signed.signed.pdf).
- Công ty Cổ phần Sonadezi Long Bình. (2023). [Báo cáo đề xuất cấp giấy phép môi trường KCN Biên Hòa II](https://thamvan.mae.gov.vn/Uploads/19092023/3GB%C3%A1o%20c%C3%A1o%20GPMT%20KCNBH2_18.8.2023%20signed.pdf).
- Fair Labor Association. (2016). [Hansae Vietnam second investigation](https://www.fairlabor.org/reports/hansae-viet-nam-second-investigation/).
- Kim, J. Y. (2013). [The politics of code enforcement and implementation in Vietnam's apparel and footwear factories](https://doi.org/10.1016/j.worlddev.2012.12.004). *World Development, 45*, 286-295.
- Locke, R. M., Qin, F., & Brause, A. (2007). [Does monitoring improve labor standards? Lessons from Nike](https://journals.sagepub.com/doi/10.1177/001979390706100101). *Industrial and Labor Relations Review, 61*(1), 3-31.
- IPPG/ACFC. (2018). [ACFC: The 10-year journey to success in mid-tier fashion retail](https://ippgroup.vn/en/news/acfc-the-10-year-journey-to-the-success-in-mid-tier-fashion-retail-n1979).
- KCONS Vietnam. (n.d.). [Chứng nhận Nike Việt Nam](https://kcons.vn/pages/chung-nhan-nike-viet-nam). Truy cập 23/07/2026.
- NIKE, Inc. (2025). [Bộ quy tắc ứng xử của Nike, bản tiếng Việt](https://media.about.nike.com/files/efd7c3b8-de95-41fe-b158-8c27e484f81c/Nike-Inc.-Code-of-Conduct-2025---Vietnamese.pdf).
- NIKE, Inc. (2026, April 23). [NIKE, Inc. announces global operations changes](https://about.nike.com/en/newsroom/releases/nike-inc-april-23-2026-global-operations-announcement).
- NIKE, Inc. (2026). [Form 10-K for fiscal year ended May 31, 2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm).
- NIKE, Inc. (n.d.). [Foundational Expectations and Code of Conduct](https://about.nike.com/en/mission/initiatives/foundational-expectations-and-code-of-conduct). Truy cập 23/07/2026.
- NIKE, Inc. (n.d.). [Gender Equity](https://about.nike.com/en/mission/initiatives/supply-chain-gender-equity). Truy cập 23/07/2026.
- NIKE, Inc. (n.d.). [Manufacturing Map](https://manufacturingmap.nikeinc.com/). Truy cập 23/07/2026.
- NIKE, Inc. (n.d.). [Our Approach to Sourcing](https://about.nike.com/en/resources/supplier-relationships). Truy cập 23/07/2026.
- NIKE, Inc. (n.d.). [Reducing Our Carbon Footprint](https://about.nike.com/en/mission/initiatives/reducing-carbon-footprint). Truy cập 23/07/2026.
- NIKE, Inc. (n.d.). [Responsible Supply Chain](https://about.nike.com/en/mission/focus-areas/responsible-supply-chain). Truy cập 23/07/2026.
- NIKE, Inc. (n.d.). [Worker Voice](https://about.nike.com/en/mission/initiatives/worker-voice). Truy cập 23/07/2026.
- NIKE Careers. (n.d.). [Lead, Footwear Materials Manufacturing Engineering, R-85220](https://careers.nike.com/en/lead-footwear-materials-manufacturing-engineering-mme/job/R-85220). Truy cập 23/07/2026.
- NIKE Careers. (n.d.). [Senior Analyst, Ocean Operations, R-75939](https://careers.nike.com/zh-tw/senior-analyst-ocean-operations/job/R-75939). Trang đã hết hạn và trả 404 khi kiểm tra ngày 23/07/2026; chỉ dùng như bằng chứng lịch sử từ bản chỉ mục tìm kiếm chính thức.
- NIKE Careers. (n.d.). [Senior Manufacturing Systems Engineer, R-83566](https://careers.nike.com/senior-manufacturing-systems-engineer/job/R-83566). Truy cập 23/07/2026.
- NIKE, Inc. (2024). [FY24 Sustainability Data](https://media.about.nike.com/files/f37dfe60-0341-4db1-8ab9-6156da717313/FY24-NIKE%2C-Inc.-Sustainability-Data.pdf).
- Nike Vietnam. (n.d.). [Customer Service](https://www.nike.com/vn/help/). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [Corporate contact directory](https://www.nike.com/vn/help/a/nike-contact-directory). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [Customs verification for orders](https://www.nike.com/vn/help/a/verify-passport). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [Experiences](https://www.nike.com/vn/help/a/experiences). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [How to return an order](https://www.nike.com/vn/help/a/how-to-return). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [Membership](https://www.nike.com/vn/membership). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [Order tracking](https://www.nike.com/vn/help/a/order-tracking). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [Payment options](https://www.nike.com/vn/help/a/payment-options). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [Refund information](https://www.nike.com/vn/help/a/refund-info). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [Shipping and delivery](https://www.nike.com/vn/help/a/shipping-delivery). Truy cập 23/07/2026.
- Nike Vietnam. (n.d.). [Shoe warranty](https://www.nike.com/vn/help/a/shoe-warranty). Truy cập 23/07/2026.
- Worker Rights Consortium. (n.d.). [Hansae Vietnam](https://www.workersrights.org/our-work/factory-investigations/hansae-vietnam/).
- WARC. (2019). [Nike: Aim Da Max](https://www.warc.com/en/article/nike%3A-aim-da-max-02b815e526a14efabc08cbcef48eeb6e).


