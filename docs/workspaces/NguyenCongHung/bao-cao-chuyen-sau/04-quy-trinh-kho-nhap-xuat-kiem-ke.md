# BÁO CÁO CHUYÊN SÂU: HỆ THỐNG QUY TRÌNH KHO BÃI, NHẬP XUẤT VÀ KIỂM KÊ TOÀN DIỆN ACFC

**Học phần:** IE203.F31.CN1.CNTT – Hệ thống quản trị qui trình nghiệp vụ  
**Giảng viên hướng dẫn:** ThS. Hà Lê Hoài Trung  
**Đơn vị thực hiện:** Nhóm nghiên cứu Đề tài BPM ACFC Việt Nam  
**Ngày hoàn thiện:** 14/08/2026

---

## 1. Bối cảnh Nghiên cứu & Mục tiêu Quy trình

Trong mô hình phân phối và bán lẻ thời trang, mỹ phẩm cao cấp đa thương hiệu của **ACFC**, hoạt động quản trị kho bãi và logistics đóng vai trò "huyết mạch" kết nối giữa nguồn hàng nhập khẩu và chuỗi hơn 250+ cửa hàng bán lẻ trên toàn quốc cùng nền tảng thương mại điện tử đa kênh. ACFC hiện đang quản lý phân phối cho 20-30+ thương hiệu quốc tế (Levi's, GAP, Calvin Klein, Mango, OVS, Typo, v.v.) và mở rộng mạnh mẽ sang lĩnh vực mỹ phẩm cao cấp.

Với Trung tâm Phân phối (Tổng kho) quy mô 12.000m² tại Bình Dương, tích hợp hệ thống phần mềm **Infolog WMS** (quản trị kho thời gian thực) và **Retail Pro Prism POS** (đồng bộ bán lẻ đa kênh), hoạt động vận hành kho phải đáp ứng đặc thù khắt khe của hai dòng sản phẩm:
- **Thời trang:** Vòng đời ngắn, hàng chục ngàn mã SKU biến động theo mùa, quản lý theo kích cỡ (size), màu sắc và vòng quay hàng hóa nhanh.
- **Mỹ phẩm:** Yêu cầu kiểm soát chặt chẽ điều kiện bảo quản (Nhiệt độ 18-25°C, Độ ẩm 40-60%), quản lý nghiêm ngặt theo Lô/Batch và Hạn sử dụng (Expiry Date) ứng dụng nguyên tắc xuất FEFO.

Để đáp ứng khối lượng vận hành khổng lồ, tài liệu này mô hình hóa chuẩn xác hiện trạng (AS-IS) toàn diện 8 phân hệ (subsystems) cốt lõi tại Tổng kho ACFC:
1. **A1. Nhập kho & Tiếp nhận Hàng hóa Quốc tế (Inbound C1)**
2. **A2. Lưu kho & Quản lý Vị trí (Storage & Put-away)**
3. **A3. Quản lý Hạn sử dụng & FEFO (Shelf-life Management)**
4. **A4. Xuất kho & Phân phối (Outbound C2)**
5. **A5. Kiểm kê & Đối soát (Stocktaking S2)**
6. **A6. Tracking & Truy xuất Hàng hóa (Goods Tracking)**
7. **A7. Quản lý Safety Stock & Dead Stock**
8. **A8. Hoàn nhập kho & Reverse Logistics (C4 Warehouse)**

Mục tiêu của nghiên cứu là thiết lập bộ chuẩn mực quy trình chi tiết với 17 cổng quyết định (Gateways), nhận diện lãng phí (Waste) để từ đó đề xuất cải tiến TO-BE.

---

## 2. Phương pháp Thực hiện & Bằng chứng Thu thập (Evidence-based)

Toàn bộ thông tin mô tả quy trình vận hành được thu thập từ các nguồn bằng chứng công khai, quy định vận hành nội bộ, chính sách hậu mãi và các thông cáo báo chí chính thức của ACFC.

*Bảng 2.1: Nhật ký bằng chứng nghiệp vụ Kho bãi & Logistics ACFC.*

| Mã bằng chứng | Nguồn trích dẫn chính thức | Nội dung nghiệp vụ trích xuất | Mức độ tin cậy |
| :---: | :--- | :--- | :---: |
| **EV01** | [Cổng thông tin ACFC](https://www.acfc.com.vn) | Mạng lưới phân phối 250+ cửa hàng bán lẻ và hạ tầng kho trung tâm 12.000m² | Mức A (Trực tiếp) |
| **EV02** | [Chính sách Đổi trả ACFC](https://www.acfc.com.vn/chinh-sach-doi-tra) | Thời hạn đổi hàng 15 ngày, 1 lần đổi/hóa đơn, điều kiện tem mác nguyên vẹn | Mức A (Trực tiếp) |
| **EV03** | [JD Chuyên viên Logistics Xuất Nhập khẩu](https://tuyendung.acfc.com.vn/) | Trách nhiệm khai báo VNACCS, làm việc với hãng tàu/Forwarder, kiểm soát vận tải | Mức B (Trực tiếp) |
| **EV04** | [JD Quản lý Kho Tổng (Warehouse Manager)](https://tuyendung.acfc.com.vn/) | Yêu cầu kinh nghiệm vận hành Infolog WMS, quản trị không gian, quản lý Date mỹ phẩm | Mức B (Trực tiếp) |
| **EV05** | [JD Chuyên viên Hoạch định (Merchandiser)](https://tuyendung.acfc.com.vn/) | Theo dõi tồn kho an toàn, phân bổ hàng hóa mùa vụ, xử lý hàng cận date (Dead stock) | Mức B (Trực tiếp) |
| **EV06** | [Báo cáo Hợp tác 3PL & Công nghệ](https://retail.acfc.vn) | Tích hợp hệ thống Retail Pro Prism POS và hợp tác với GHN, Ahamove, GHTK, J&T | Mức C (Gián tiếp) |

---

## 3. Khám phá & Mô tả Quy trình AS-IS: 8 Phân hệ Vận hành Kho (Subsystems)

### A1. Nhập kho & Tiếp nhận Hàng hóa Quốc tế (Inbound C1)

**Hồ sơ Quy trình (Process Profile):**
* **Mục tiêu:** Tiếp nhận an toàn, chính xác hàng hóa từ cảng về Tổng kho Binh Dương, đảm bảo 100% hàng qua cửa kiểm tra chất lượng (QC) trước khi nhập hệ thống Infolog WMS.
* **Đầu vào:** Bộ chứng từ nhập khẩu (AWB/B/L, Commercial Invoice, Packing List), Container hàng, Lệnh giao hàng.
* **Đầu ra:** Phiếu nhập kho (GRN), Dữ liệu Lot/Batch ghi nhận trên WMS, Hàng hóa sẵn sàng Put-away hoặc Cross-dock.

*Bảng 3.1: Các bước thực hiện quy trình Nhập kho Inbound (A1).*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | NV Xuất Nhập khẩu | *Tiếp nhận* bộ chứng từ gốc từ Forwarder | AWB/B/L, Invoice, PL | Hồ sơ thông quan | Rà soát tính hợp lệ của chứng từ |
| 2 | NV Xuất Nhập khẩu | *Thực hiện* Khai báo hải quan qua hệ thống VNACCS/VCIS và nộp thuế | Hồ sơ thông quan | Tờ khai hải quan thông quan | **Gateway 1:** Luồng Xanh/Vàng/Đỏ? $\to$ Xanh/Vàng: Qua / Đỏ: Chờ kiểm hóa & Theo dõi DEM/DET (Demurrage/Detention) |
| 3 | Điều độ kho / Thủ kho | *Kiểm tra* tình trạng container khi hạ bãi tại kho | Container, Lệnh giao hàng | Biên bản bàn giao container | Kiểm tra nguyên vẹn Seal chì. **Gateway 2:** Seal rách? $\to$ Cách ly & Gọi giám định bảo hiểm (Insurance Surveyors) |
| 4 | NV QC / Thủ kho | *Kiểm tra* nhiệt độ lọt lòng container (đối với lô hàng mỹ phẩm) | Thiết bị đo nhiệt | Nhật ký nhiệt độ | Đảm bảo không sốc nhiệt mỹ phẩm trong quá trình vận tải biển |
| 5 | Đội QC Inbound | *Thực hiện* QC Inbound: Kiểm đếm số lượng, chất lượng (vải vóc, đường may, bao bì) | Packing List, Hàng hóa | Biên bản QC sơ bộ | Quét mã vạch đối chiếu dữ liệu |
| 6 | NV QC (Mỹ phẩm) | *Kiểm tra* Hạn sử dụng (Expiry Date) và bao bì nguyên vẹn | Mỹ phẩm thực tế | Nhãn phụ Date | Mỹ phẩm yêu cầu Date $\ge 80\%$ tuổi thọ |
| 7 | NV QC (Mỹ phẩm) | *Xác minh & Xử lý* vật liệu nguy hiểm theo MSDS (Handling of Hazardous Materials) | Hồ sơ MSDS | Báo cáo an toàn | Bắt buộc đối với mỹ phẩm dễ cháy/chứa cồn |
| 8 | Trưởng ca QC | *Đánh giá* kết quả kiểm tra chất lượng tổng thể | Biên bản QC sơ bộ | Quyết định nhập/cách ly | **Gateway 3: Pass QC?** $\to$ Pass: Tiếp tục / Fail: Đưa vào khu Quarantine chờ xử lý |
| 9 | Quản lý Kho | *Xử lý* hàng cách ly (Quarantine) | Báo cáo Quarantine | Lệnh xử lý cách ly | **Gateway 4: Phân giải Quarantine?** $\to$ Trả nhà cung cấp (RTV) / Tiêu hủy (Destroy) |
| 10 | NV Cập nhật Dữ liệu | *Ghi nhận* thông tin Lot/Batch ID và Hạn sử dụng vào hệ thống Infolog WMS | Báo cáo QC Pass | Mã ASN cập nhật WMS | Cơ sở để truy xuất FEFO sau này |
| 11 | Quản lý Kho | *Đánh giá* năng lực sức chứa hiện tại của kho | Dữ liệu sức chứa WMS | Lệnh luân chuyển | **Gateway 5: Đủ dung lượng lưu trữ?** $\to$ Có: Put-away / Không: Cross-dock thẳng ra Store |

### A2. Lưu kho & Quản lý Vị trí (Storage & Put-away)

**Hồ sơ Quy trình (Process Profile):**
* **Mục tiêu:** Tối ưu hóa không gian lưu trữ 12.000m², đảm bảo hàng hóa được xếp đúng phân khu bảo quản và tối ưu quãng đường Picking.
* **Đầu vào:** Hàng hóa đã qua Inbound, Chiến lược phân bổ ABC.
* **Đầu ra:** Hàng hóa nằm đúng Bin/Location trên WMS, Báo cáo sức chứa (Capacity alert).

*Bảng 3.2: Các bước thực hiện quy trình Lưu kho (A2).*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Hệ thống WMS | *Phân tích & Chỉ định* chiến lược xếp hàng (Velocity-based slotting) theo phân loại ABC | Dữ liệu hàng Inbound | Lệnh Put-away (Dự kiến) | A=Fast-moving (Gần cửa), B=Medium, C=Slow |
| 2 | NV Vận hành Kho | *Phân loại* hàng hóa theo đặc thù bảo quản và xác minh nhiệt độ nghiêm ngặt (Strict temperature zone verification) | Hàng hóa thực tế | Nhóm hàng Thời trang/Mỹ phẩm | **Gateway 6: Loại hàng?** $\to$ Thời trang: Ambient Zone / Mỹ phẩm: Control Zone (18-25°C) |
| 3 | NV Lái xe Nâng (Forklift) | *Di chuyển & Xếp* hàng lên pallet tại vị trí chỉ định | Lệnh Put-away, Hàng hóa | Hàng trên kệ Rack | Tuân thủ an toàn lao động |
| 4 | NV Vận hành Kho | *Quét* mã vạch Bin Location để xác nhận tọa độ lưu trữ | Máy quét PDA, Mã kệ | Bản ghi Location cập nhật | Xác thực vị trí 3 chiều (Dãy-Tầng-Ô) |
| 5 | Hệ thống WMS | *Đồng bộ* dữ liệu tồn kho thời gian thực | Bản ghi Location | Dashboard tồn kho | Sẵn sàng cho phép lên đơn hàng |
| 6 | Hệ thống WMS | *Giám sát & Cảnh báo* sức chứa kho theo từng Zone | Dữ liệu tồn kho thời gian thực | Cảnh báo ngưỡng 80% | Gửi thông báo đến Quản lý Kho nếu Zone sắp đầy |

### A3. Quản lý Hạn sử dụng & FEFO (Shelf-life Management)

**Hồ sơ Quy trình (Process Profile):**
* **Mục tiêu:** Quản lý nghiêm ngặt tuổi đời hàng mỹ phẩm, ngăn chặn tuyệt đối việc xuất bán hàng hết hạn.
* **Đầu vào:** Dữ liệu Date trên WMS, Hàng tồn mỹ phẩm.
* **Đầu ra:** Báo cáo cận Date, Đề xuất thanh lý, Lệnh xuất chuẩn FEFO.

*Bảng 3.3: Các bước thực hiện quy trình Quản lý Date (A3).*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Hệ thống WMS | *Quét & Phân tích* định kỳ lô hàng theo Date | Cơ sở dữ liệu Lot/Batch | Báo cáo tuổi thọ Tồn kho | Chạy Batch job mỗi đêm |
| 2 | Hệ thống WMS | *Đánh giá* thời hạn sử dụng còn lại của lô hàng | Báo cáo tuổi thọ | Cảnh báo trạng thái | **Gateway 7: Thời hạn còn lại?** $\to$ >6 tháng: Bán bình thường / 3-6 tháng: Cảnh báo Markdown / <3 tháng: Cảnh báo Rút kệ |
| 3 | NV Kiểm soát Tồn kho | *Trích xuất & Gửi* Báo cáo cận hạn hàng tuần | Cảnh báo hệ thống | Báo cáo Near-Expiry | Gửi cho bộ phận M3 để lên chương trình khuyến mãi Outlet |
| 4 | Bộ phận M3 | *Phê duyệt* phương án xử lý hàng cận/hết hạn | Báo cáo Near-Expiry | Lệnh chuyển Outlet/Tiêu hủy | Quyết định đẩy sales hoặc hủy |
| 5 | Hệ thống WMS | *Cấp phát* lệnh Picking dựa trên thuật toán FEFO | Đơn đặt hàng | Lệnh Picking FEFO | First-Expired-First-Out, hệ thống chỉ điểm đúng Bin chứa lô hàng có Date ngắn nhất |

### A4. Xuất kho & Phân phối (Outbound C2)

**Hồ sơ Quy trình (Process Profile):**
* **Mục tiêu:** Soạn hàng và giao đúng đủ, kịp thời cho 250+ cửa hàng.
* **Đầu vào:** Lệnh phân bổ (Allocation Order), Yêu cầu bổ sung (Replenishment).
* **Đầu ra:** Kiện hàng đóng gói, Phiếu xuất kho, Vận đơn 3PL, Trạng thái cập nhật trên Retail Pro.

*Bảng 3.4: Các bước thực hiện quy trình Xuất kho (A4).*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Hệ thống WMS | *Tiếp nhận* Lệnh yêu cầu xuất kho | Dữ liệu từ ERP/M3 | Danh sách lệnh chờ xuất | Từ M3 (Push) hoặc Store (Pull) |
| 2 | NV Điều phối (Dispatcher) | *Phân loại* tính chất Đơn hàng xuất | Danh sách lệnh | Luồng công việc Picking | **Gateway 8: Loại lệnh?** $\to$ Bulk (Phân bổ mùa) vs Urgent (Bổ sung khẩn cấp bù size) |
| 3 | Hệ thống WMS | *Thiết lập* Chiến lược Picking tương ứng đặc thù hàng | Thông tin đơn hàng | Lộ trình Picking | **Gateway 9: Ngành hàng?** $\to$ Thời trang: FIFO/Batch Picking / Mỹ phẩm: FEFO/Wave Picking |
| 4 | NV Picking | *Thực hiện* lấy hàng trên kệ bằng PDA theo luồng WMS | Lộ trình Picking | Xe hàng Picking hoàn tất | Quét mã vạch xác nhận tại từng Location |
| 5 | NV Đóng gói (Packer) | *Đóng gói* carton, dán Shipping Label, đính kèm Delivery Note | Hàng Picking | Kiện hàng Outbound | Ghi hình camera tại bàn Pack (CCTV) để giải quyết khiếu nại |
| 6 | NV Điều phối | *Xác định* phương án giao hàng thực tế | Kiện hàng Outbound | Lệnh xuất xưởng | **Gateway 10: Cross-docking?** $\to$ Có: Giao thẳng thùng nguyên từ Inbound / Không: Chuyển thùng vừa Pack cho 3PL |
| 7 | NV Giao nhận (Dispatcher) | *Lựa chọn* đối tác 3PL theo tuyến đường tối ưu | Lệnh xuất xưởng | Vận đơn 3PL (Waybill) | Nội thành: GHN/Ahamove. Tỉnh: GHTK/J&T |
| 8 | Hệ thống POS | *Cập nhật* Trạng thái hàng "Đang vận chuyển" (In Transit) | API từ WMS/3PL | Trạng thái Retail Pro Prism | Store nhìn thấy hàng sắp về để chuẩn bị nhận |

### A5. Kiểm kê & Đối soát (Stocktaking S2)

**Hồ sơ Quy trình (Process Profile):**
* **Mục tiêu:** Đảm bảo độ chính xác tồn kho $\ge 99.5\%$, phát hiện gian lận, mất mát.
* **Đầu vào:** Sổ dư WMS/POS, Máy quét.
* **Đầu ra:** Báo cáo đối soát chênh lệch, Biên bản điều chỉnh, Hạch toán ERP.

*Bảng 3.5: Các bước thực hiện quy trình Kiểm kê (A5).*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Cửa hàng trưởng / Trưởng kho | *Lập* Kế hoạch kiểm kê (Full hàng quý / Cycle Count hàng ngày) | Lịch kiểm kê định kỳ | Bản kế hoạch kiểm kê | Chuẩn bị nhân sự, thiết bị |
| 2 | NV Hệ thống | *Thực hiện* Freeze (Khóa sổ) WMS/POS toàn bộ giao dịch | Kế hoạch kiểm kê | Trạng thái Freeze hệ thống | Bắt buộc để chốt sổ tĩnh |
| 3 | Đội kiểm kê | *Quét mã & Kiểm đếm* thực tế (Quét Barcode / RFID) | Máy quét, Hàng hóa | Tệp dữ liệu quét lần 1 | Quét từng mã RFID hoặc Barcode |
| 4 | Hệ thống WMS | *Tự động đối chiếu* dữ liệu thực tế với sổ kho tĩnh | Tệp dữ liệu quét | Báo cáo chênh lệch thô | Hệ thống so khớp tự động |
| 5 | Chuyên viên Kiểm soát | *Đánh giá* nguyên nhân chênh lệch tạm thời | Báo cáo chênh lệch | Kết luận phân loại lỗi | **Gateway 11: Nguyên nhân lệch sơ bộ?** $\to$ Lỗi hệ thống / Nhầm Location / Mất mát / Hàng mẫu không track |
| 6 | Đội kiểm kê / Kế toán | *Tiến hành* Tra soát mở rộng song song | Kết luận phân loại | Kết quả tra soát chuyên sâu | **Gateway 12: AND-Split** $\to$ Nhánh 1: Rà soát chứng từ ERP / Nhánh 2: Kiểm tra khu vực cách ly (Quarantine/Consignment) |
| 7 | Chuyên viên Kiểm soát | *Tổng hợp & Lập* Biên bản xử lý thất thoát / Bồi thường | Kết quả tra soát | Biên bản xử lý | **Gateway 13: AND-Join** $\to$ Đồng bộ thông tin từ 2 nhánh |
| 8 | CFO | *Xem xét & Phê duyệt* Biên bản xử lý | Biên bản xử lý | Quyết định duyệt | Duyệt trừ lương, hạch toán giá vốn |
| 9 | Kế toán Kho | *Cập nhật* Số dư đúng lên ERP và Mở khóa hệ thống (Unfreeze) | Quyết định duyệt | Trạng thái Open WMS/POS | Sẵn sàng hoạt động lại bình thường |

### A6. Tracking & Truy xuất Hàng hóa (Goods Tracking) - NEW

**Hồ sơ Quy trình (Process Profile):**
* **Mục tiêu:** Cung cấp tầm nhìn thời gian thực toàn chuỗi cung ứng, từ Kho đến Cửa hàng và Khách hàng.
* **Đầu vào:** Tín hiệu RFID, Cập nhật trạng thái API.
* **Đầu ra:** Dashboard hiển thị hành trình, Cảnh báo Loss Prevention.

*Bảng 3.6: Các bước thực hiện quy trình Tracking (A6).*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Hệ thống RFID | *Kích hoạt & Mã hóa* thẻ RFID (EPC) từ trung tâm Inbound | Hàng nhập kho | Mã định danh duy nhất (EPC) | Mỗi item có 1 ID riêng biệt |
| 2 | Cổng RFID (RFID Portal) | *Ghi nhận* tự động trạng thái khi hàng hóa đi qua cổng (Cửa kho, Cửa Store) | Tín hiệu đọc RFID | Log trạng thái (Timestamp, Vị trí) | Tracking: Kho $\to$ Transit $\to$ Store $\to$ Shelf $\to$ Sold |
| 3 | Bảng điều khiển (Dashboard) | *Hiển thị* tọa độ và trạng thái lô hàng/Lot thời gian thực | Log trạng thái | Bản đồ nhiệt / Lộ trình | Liên thông Infolog WMS & Retail Pro |
| 4 | Hệ thống An ninh (Loss Prevention) | *Giám sát & Phân tích* sự bất thường của tín hiệu | Log trạng thái | Cảnh báo an ninh | **Gateway 14: Phát hiện bất thường?** $\to$ Có (Mất sóng đột ngột chưa qua POS): Kích hoạt báo động / Không: Bình thường |
| 5 | Bộ phận CSKH / Recall | *Thực hiện* Truy xuất ngược nguồn gốc lô hàng khi có khiếu nại (đặc biệt mỹ phẩm) | Số Serial/Batch | Lịch sử truy xuất toàn chuỗi | Khách hàng $\to$ Cửa hàng $\to$ Xe tải 3PL $\to$ Kho $\to$ Container $\to$ Hãng |

### A7. Quản lý Safety Stock & Dead Stock - NEW

**Hồ sơ Quy trình (Process Profile):**
* **Mục tiêu:** Tự động hóa bổ sung tồn kho an toàn, chủ động phát hiện và thanh lý hàng tồn đọng.
* **Đầu vào:** Chính sách Weeks of Supply (WoS), Lịch sử bán hàng POS.
* **Đầu ra:** Lệnh Replenishment tự động, Báo cáo Dead stock, Kế hoạch Markdown.

*Bảng 3.7: Các bước thực hiện quy trình Quản lý Safety/Dead Stock (A7).*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Hệ thống ERP/M3 | *Tính toán* Định mức Safety Stock theo mùa vụ & SKU velocity | Dữ liệu Sales POS (WoS) | Chỉ số Safety Stock (Min/Max) | Động (Dynamic) theo từng mùa |
| 2 | Hệ thống WMS | *So sánh* Tồn kho khả dụng với Định mức an toàn | Tồn kho thực tế | Cảnh báo Restock | **Gateway 15: Dưới mức Safety Stock?** $\to$ Có: Kích hoạt Auto-Replenishment / Không: Bỏ qua |
| 3 | Hệ thống ERP | *Tạo & Gửi* Đơn hàng bổ sung tự động cho M3 duyệt | Cảnh báo Restock | Đề xuất PO/Transfer Order | Tiết kiệm thời gian lập kế hoạch thủ công |
| 4 | Hệ thống ERP/WMS | *Quét & Phân tích* các SKU không phát sinh giao dịch xuất/bán | Dữ liệu giao dịch | Danh sách Aging Inventory | Xác định thời gian ngâm hàng (Aging) |
| 5 | Bộ phận M3 | *Đánh giá* Danh sách hàng Aging | Danh sách Aging | Phân loại trạng thái | **Gateway 16: Là Dead Stock (>180 ngày)?** $\to$ Có: Đưa vào Markdown / Không: Theo dõi tiếp |
| 6 | Bộ phận M3 / Marketing | *Phê duyệt* Phương án xử lý hàng Dead Stock | Danh sách Dead Stock | Chương trình Outlet | Kích hoạt giảm giá 30-50%, luân chuyển sang các cửa hàng Outlet, hoặc Quyên góp (Donate) |

### A8. Hoàn nhập kho & Reverse Logistics (C4 Warehouse) - Enhanced

**Hồ sơ Quy trình (Process Profile):**
* **Mục tiêu:** Xử lý nhanh gọn hàng khách đổi trả trong 15 ngày, tái luân chuyển hàng tốt và xử lý hàng lỗi.
* **Đầu vào:** Hàng hóa hoàn về từ Store/E-commerce, Phiếu yêu cầu đổi trả.
* **Đầu ra:** Hàng tái nhập Put-away, Hàng sửa chữa, Hàng trả Vendor.

*Bảng 3.8: Các bước thực hiện quy trình Reverse Logistics (A8).*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | NV Tiếp nhận Reverse | *Nhận* bưu kiện hoàn trả từ 3PL/Store | Bưu kiện, Hóa đơn | Biên bản nhận hàng trả | Kiểm tra sơ bộ kiện hàng |
| 2 | Đội QC Reverse | *Thực hiện* QC chuyên sâu: Tag mác, dấu hiệu đã sử dụng, Expiry Date (với mỹ phẩm), mùi hương/vết bẩn | Hàng hóa, Chính sách (15 ngày đổi) | Kết quả QC Chi tiết | Áp dụng chính sách 1 lần đổi/hóa đơn |
| 3 | Trưởng ca QC | *Phân loại & Định hướng* luồng xử lý sản phẩm | Kết quả QC Chi tiết | Hướng xử lý | **Gateway 17: Tình trạng hàng?** $\to$ Tốt (Fit for resale) / Lỗi nhỏ (Need repair) / Lỗi SX (Defect) / Rách nát (Cannot sell) |
| 4 | NV Kho Reverse | *Thực hiện* Xử lý điều hướng vật lý theo phân loại | Hướng xử lý | Lô hàng theo phân khu | Theo hướng dẫn phân luồng |
| 5 | NV Hệ thống WMS | *Cập nhật* Trạng thái và điều chỉnh số dư kho theo từng luồng xử lý | Lô hàng, Hướng xử lý | Tồn kho hệ thống cập nhật | Tốt $\to$ Available Put-away / Lỗi nhỏ $\to$ Refurbish Zone / Lỗi SX $\to$ Return to Vendor (RTV) / Nát $\to$ Liquidate/Destroy |

---

## 4. Mô hình hóa Quy trình BPMN 2.0 (Hệ thống Khép kín 17 Gateways)

### 4.1. Cấu trúc Mô hình Tổng thể

Để thể hiện tính liên kết phức tạp của 8 phân hệ, kiến trúc BPMN sử dụng mô hình đa hồ (Multi-Pool) tích hợp thông điệp (Message Flow):
* **Pool Ngoài 1: Đối tác Ngoại vi (External Partners)** (Forwarder, 3PL, Nhà cung cấp - Vendor).
* **Pool Ngoài 2: Khách hàng & Cửa hàng Bán lẻ ACFC (Retail Stores)** (Khách mua, Nhân viên Store yêu cầu bổ sung/trả hàng).
* **Pool Chính: TỔNG KHO VẬN HÀNH TRUNG TÂM ACFC (Central Warehouse):**
  * *Lane 1: Khối XNK & Hoạch định (M3 & Import)*
  * *Lane 2: Kiểm soát Chất lượng (QC Inbound/Reverse)*
  * *Lane 3: Vận hành Kho Bãi (WMS, Put-away, Picking, Inventory Control)*
  * *Lane 4: Điều phối Giao nhận (Dispatcher/Packer)*
  * *Lane 5: Kế toán & Ban Giám đốc (Accounting & CFO)*

### 4.2. Danh sách 17 Cổng điều kiện cốt lõi (Gateways)
1. `G1 (XOR-Split - A1)`: Kết quả thông quan (Luồng Xanh/Vàng/Đỏ). (Bao gồm theo dõi DEM/DET nếu Luồng Đỏ).
2. `G2 (XOR-Split - A1)`: Seal container nguyên vẹn không? (Nếu rách: Cách ly & gọi giám định bảo hiểm).
3. `G3 (XOR-Split - A1)`: Pass QC Inbound (Chất lượng, Bao bì, Hạn SD)?
4. `G4 (XOR-Split - A1)`: Phân giải hàng cách ly Quarantine? (RTV vs Destroy).
5. `G5 (XOR-Split - A1)`: Kho còn đủ năng lực chứa (Capacity)? (Put-away vs Cross-dock).
6. `G6 (XOR-Split - A2)`: Phân loại ngành hàng lưu kho & nhiệt độ bảo quản? (Thời trang Ambient vs Mỹ phẩm Control).
7. `G7 (XOR-Split - A3)`: Thời hạn sử dụng mỹ phẩm còn lại? (>6T, 3-6T, <3T).
8. `G8 (XOR-Split - A4)`: Tính chất lệnh xuất kho? (Bulk theo mùa vs Urgent bù size).
9. `G9 (XOR-Split - A4)`: Chiến lược Picking WMS chỉ định? (FIFO Thời trang vs FEFO Mỹ phẩm).
10. `G10 (XOR-Split - A4)`: Lấy hàng Cross-docking từ Inbound hay Picking từ Shelf?
11. `G11 (XOR-Split - A5)`: Nguyên nhân sơ bộ khi lệch kiểm kê? (Lỗi vị trí/Hệ thống/Thất thoát).
12. `G12 (AND-Split - A5)`: Rẽ nhánh song song tra soát chứng từ ERP VÀ kiểm tra khu vực hàng mẫu/cách ly.
13. `G13 (AND-Join - A5)`: Hội tụ kết quả tra soát từ các nhánh song song để lập biên bản xử lý.
14. `G14 (XOR-Split - A6)`: Phát hiện tín hiệu RFID bất thường/Mất sóng? (Cảnh báo Loss Prevention).
15. `G15 (XOR-Split - A7)`: Tồn kho chạm ngưỡng Safety Stock? (Kích hoạt Auto-Replenishment).
16. `G16 (XOR-Split - A7)`: Sản phẩm là Dead Stock (>180 ngày không bán)? (Duyệt Markdown).
17. `G17 (XOR-Split - A8)`: Đánh giá chất lượng hàng đổi trả? (Fit for Resale, Repair, Return to Vendor, Destroy).

*(Sơ đồ BPMN kỹ thuật số dung lượng lớn được lưu trữ riêng tại tệp `diagrams/bpmn-acfc-8-subsystems.bpmn`)*

---

## 5. Bộ Câu hỏi Phỏng vấn Thu thập Dữ liệu ACFC (Chuẩn hóa)

### 5.1. 10 Câu hỏi Định tính (Qualitative Questions)
* **5 câu hỏi có cấu trúc (Structured):**
  1. Việc khai báo hải quan (VNACCS) tại Inbound thường gặp tắc nghẽn ở luồng Đỏ bao nhiêu lần một quý?
  2. Đối với Mỹ phẩm, ACFC quy định Date (Hạn sử dụng) phải còn tối thiểu bao nhiêu % mới được phép qua cổng QC nhập kho?
  3. Hệ thống Infolog WMS có tự động chuyển đổi sang chiến lược FEFO khi nhận biết mã hàng thuộc Zone Mỹ phẩm hay không?
  4. Quyền quyết định phê duyệt Markdown cho các mặt hàng Dead Stock thuộc về Giám đốc Thương mại hay Bộ phận M3?
  5. Trong quy trình kiểm kê, Kế toán kho có quyền trực tiếp duyệt bù trừ sai lệch âm/dương cho các SKU cùng mức giá mà không qua CFO không?
* **5 câu hỏi không cấu trúc (Unstructured):**
  6. Những thách thức lớn nhất khi duy trì nhiệt độ 18-25°C tại khu lưu trữ mỹ phẩm vào mùa cao điểm nóng nực là gì?
  7. Theo anh/chị, việc dùng 3PL giao hàng tỉnh (GHTK/J&T) thường phát sinh rủi ro mất mát tem nhãn mã vạch ở khâu nào nhất?
  8. Quy trình Reverse Logistics (đổi trả) hiện tại đang bị chậm trễ do khâu QC kiểm tra tính nguyên vẹn hay do hệ thống tích hợp Retail Pro phản hồi chậm?
  9. Nhân viên Picking phàn nàn gì nhiều nhất về cách sắp xếp (Slotting) các mặt hàng Fast-moving trên WMS hiện tại?
  10. Giải pháp Tracking bằng RFID đã thực sự giúp bộ phận Loss Prevention giảm thiểu tỷ lệ thất thoát vô cớ tại các Store lớn như thế nào?

### 5.2. 10 Câu hỏi Định lượng (Quantitative Questions)
* **5 câu hỏi có cấu trúc (Structured):**
  1. Tỷ lệ phần trăm các kiện hàng Inbound thất bại tại cổng QC (Fail) trung bình hàng tháng là bao nhiêu ($<2\%, 2-5\%, >5\%$)?
  2. Thời gian trung bình để hoàn tất Picking một đơn hàng Urgent Replenishment cho 1 Store là bao nhiêu phút ($<30\text{p}, 30-60\text{p}, >60\text{p}$)?
  3. Chi phí điện năng trung bình hàng tháng để duy trì Control Zone (Nhiệt độ/Độ ẩm) cho khu mỹ phẩm tại kho Binh Dương là bao nhiêu VNĐ?
  4. Tỷ lệ hàng hóa trở thành Dead Stock (>180 ngày) của ngành hàng Thời trang cao hơn Mỹ phẩm bao nhiêu $\%$?
  5. Thời gian xử lý trung bình từ lúc nhận hàng Reverse (đổi trả) đến khi hàng quay lại trạng thái Available Put-away là bao nhiêu ngày ($<2\text{ ngày}, 3-5\text{ ngày}, >5\text{ ngày}$)?
* **5 câu hỏi không cấu trúc (Unstructured):**
  6. Tổng số giờ lao động (OT) tiết kiệm được mỗi quý kể từ khi ACFC chuyển từ Kiểm kê toàn diện (Full) sang Kiểm kê cuốn chiếu (Cycle Count) là bao nhiêu?
  7. Khoản chi phí bồi thường hàng hóa phải gánh chịu do các đối tác 3PL làm hư hỏng hàng trong năm vừa qua ước tính là bao nhiêu?
  8. Tốc độ quét kiểm kê bằng súng RFID nhanh gấp bao nhiêu lần so với máy quét Barcode quang học truyền thống?
  9. Số lượng đơn hàng Cross-dock thẳng ra Store chiếm tỷ trọng bao nhiêu % tổng khối lượng Inbound trong các đợt Launching Bộ sưu tập mới?
  10. Mức độ dung sai (Tolerance Level) cho phép đối với chênh lệch tồn kho tại Tổng kho trung tâm khác biệt như thế nào so với Cửa hàng lẻ?

---

## 6. Phân tích Định tính Hệ thống Hiện trạng AS-IS

### 6.1. Phân tích Giá trị Gia tăng (VA / BVA / NVA)

Việc vận hành đồng thời 8 phân hệ tạo ra chuỗi giá trị phức tạp. Đánh giá sơ bộ:
* **Inbound & QC (A1) - BVA & VA:** Khai báo hải quan (BVA) là bắt buộc thủ tục. QC chất lượng (VA) ngăn chặn rủi ro hàng lỗi ngay từ đầu vào.
* **Slotting & Put-away (A2) - VA:** Tối ưu khoảng cách lấy hàng dựa trên ABC, trực tiếp giảm thời gian lead time giao hàng nội bộ.
* **Shelf-life Management (A3) - VA:** Áp dụng thuật toán FEFO bảo vệ trải nghiệm khách hàng (mỹ phẩm), ngăn lãng phí do hết hạn.
* **Tra soát chênh lệch S2 & Rework tại Reverse A8 - NVA:** Các bước đếm đi đếm lại, hoặc sửa lỗi bao bì hàng đổi trả không tạo ra giá trị mới cho khách hàng, chỉ là khắc phục sai sót hệ thống/con người.

### 6.2. Phân tích Lãng phí (Waste Analysis) trong 8 Phân hệ

* **Di chuyển (Motion Waste):** Lãng phí lớn tại phân hệ A2 và A4 nếu chiến lược Slotting WMS không tối ưu. NV Lái xe nâng đi xa để xếp hàng Fast-moving; NV Picking đi chéo qua các Zone thay vì lộ trình hình chữ U.
* **Chờ đợi (Hold/Waiting):** Hàng Inbound chờ thông quan (Luồng Đỏ); Hàng Pack xong chờ xe tải 3PL đến gom; Khách hàng chờ duyệt thủ tục đổi trả từ Store gửi về kho trung tâm (A8).
* **Tồn kho thừa (Inventory Waste):** Lỗi tính toán WoS dẫn đến hàng nhập quá mức, biến thành Dead Stock (A7), chiếm dụng không gian và chi phí vốn.
* **Lỗi (Defects):** Quét nhầm Barcode (ví dụ: quét size L nhưng thực tế đóng size M) tại khâu A4 dẫn đến sai lệch tồn kho lan truyền ra Store, kích hoạt luồng Kiểm kê S2 và đổi trả A8 tốn kém.

---

## 7. Phân tích Định lượng & Chi phí

* **Quy mô hoạt động:** 12.000m², 250+ Store, 30.000+ SKU lưu chuyển liên tục.
* **Chi phí lưu kho mỹ phẩm:** Vận hành Control Zone (18-25°C) tốn kém năng lượng gấp $2.5$ lần so với Ambient Zone (thời trang). Do đó, tỷ lệ luân chuyển (Turnover rate) của mỹ phẩm phải duy trì ở mức cao để bù đắp chi phí giữ hàng (Holding Cost).
* **Thời gian xử lý vòng quay In-Out:**
  $$T_{\text{cycle}} = T_{\text{Inbound/QC}} + T_{\text{Putaway}} + T_{\text{Storage}} + T_{\text{Picking}} + T_{\text{Packing}} + T_{\text{Dispatch}}$$
  Mục tiêu của ACFC là Cross-dock tối đa để giảm $T_{\text{Storage}} \to 0$ cho các đơn hàng Launching.
* **Tỷ lệ độ chính xác hệ thống (Inventory Record Accuracy - IRA):**
  $$\text{IRA} = \left( 1 - \frac{\sum | \text{Chênh lệch thực tế} |}{\text{Tổng tồn kho WMS}} \right) \times 100\%$$
  ACFC đặt KPI $\text{IRA} \ge 99.8\%$ tại Tổng kho và $\ge 99.0\%$ tại các Store.

---

## 8. Tầm nhìn Cải tiến Hệ thống (TO-BE Recommendations)

Dựa trên việc bóc tách 8 phân hệ, các giải pháp số hóa toàn diện được đề xuất:
1. **100% Item-level RFID (Nâng cấp A5 & A6):** Thay thế hoàn toàn Barcode. RFID Tracking từ Inbound, chống thất thoát tự động tại Store cổng Portal, rút ngắn thời gian kiểm kê từ hàng giờ xuống vài phút.
2. **AI-driven Replenishment (Nâng cấp A7):** Tích hợp Machine Learning vào ERP để dự báo Demand (Nhu cầu) thay vì chỉ dùng ngưỡng WoS tĩnh. AI sẽ tính toán yếu tố thời tiết, trend mạng xã hội để kích hoạt Auto-Replenishment.
3. **Automated Sorting & Conveyor (Nâng cấp A2 & A4):** Triển khai băng chuyền phân loại tự động (Auto-sorter) cho luồng Picking đa nhãn hàng, kết nối thẳng với khu vực Packing 3PL, triệt tiêu Motion Waste của nhân viên.
4. **Digital QC for Reverse (Nâng cấp A8):** Ứng dụng công nghệ Computer Vision tại bàn QC đổi trả để tự động phát hiện vết bẩn, dấu hiệu đã sử dụng trên hàng thời trang, giảm phụ thuộc vào cảm tính của con người.

---
*Ghi chú: Toàn bộ sơ đồ BPMN chi tiết 15+ Gateways kết nối 8 phân hệ được lưu trữ tại `diagrams/bpmn-acfc-8-subsystems.bpmn` phục vụ phân tích kỹ thuật sâu.*
