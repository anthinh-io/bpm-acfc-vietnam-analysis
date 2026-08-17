# ĐẠI HỌC QUỐC GIA TP. HỒ CHÍ MINH
## TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN
### KHOA HỆ THỐNG THÔNG TIN

---

# BÁO CÁO ĐỒ ÁN MÔN HỌC
## HỆ THỐNG QUẢN TRỊ QUI TRÌNH NGHIỆP VỤ (IE203)

### ĐỀ TÀI:
# KHÁM PHÁ, MÔ HÌNH HÓA VÀ PHÂN TÍCH QUY TRÌNH NGHIỆP VỤ CHUỖI CUNG ỨNG VÀ BÁN LẺ THỜI TRANG ĐA KÊNH TẠI CÔNG TY CỔ PHẦN THỜI TRANG VÀ MỸ PHẨM ÂU CHÂU (ACFC)

**Giảng viên hướng dẫn:** ThS. Hà Lê Hoài Trung  
**Lớp học phần:** IE203.F31.CN1.CNTT  
**Nhóm sinh viên thực hiện:**
1. Nguyễn Thanh Thịnh – MSSV: 22730096
2. Lương Triệu Khang – MSSV: 24730105
3. Huỳnh Gia Bảo – MSSV: 24730157
4. Nguyễn Công Hưng – MSSV: 24730100

*Thành phố Hồ Chí Minh, Tháng 08 Năm 2026*

---

## LỜI CẢM ƠN
Nhóm nghiên cứu chân thành cảm ơn ThS. Hà Lê Hoài Trung, giảng viên phụ trách học phần Hệ thống quản trị qui trình nghiệp vụ (IE203), đã tận tình truyền đạt những kiến thức chuyên sâu về quản trị quy trình kinh doanh (BPM), chuẩn mô hình hóa BPMN 2.0 và các phương pháp phân tích định tính, định lượng chuẩn mực. Những định hướng học thuật khắt khe, phương pháp luận dựa trên bằng chứng (Evidence-based) và sự chỉ dẫn tỉ mỉ của Thầy là kim chỉ nam giúp nhóm hoàn thiện đồ án này với chất lượng cao nhất.

---

## 2. KIẾN TRÚC VÀ MÔ HÌNH HÓA QUY TRÌNH NGHIỆP VỤ (AS-IS)

### 2.3. Quy trình Hoạch định hàng hóa và Phân bổ nguồn hàng (M3)

#### Hồ sơ Quy trình (Process Profile)
* **Mã quy trình:** M3
* **Tên quy trình:** Hoạch định hàng hóa và Phân bổ nguồn hàng.
* **Mục tiêu:** Quản lý ngân sách OTB (Open-to-Buy), xây dựng Seasonal buying calendar (SS/FW) và tối ưu hóa doanh thu.
* **Đầu vào:** Dữ liệu bán hàng lịch sử, Ngân sách năm.
* **Đầu ra:** Kế hoạch mua hàng, Kế hoạch Markdown optimization.
* **Kết quả tích cực:** Đạt mục tiêu Sell-through rate cao, tối ưu hóa mức tồn kho.

#### Bảng Trình tự các Bước Thực hiện (Step-by-Step Table)

*Bảng 2.2: Bảng các bước thực hiện quy trình M3.*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Merchandise Dept | *Xây dựng* OTB (Open-to-Buy) budget | Báo cáo Doanh thu | Ngân sách OTB | **Gateway 1: OTB budget có được Giám đốc Tài chính duyệt?** |
| 2 | Buyer | *Thiết lập* Seasonal buying calendar (SS/FW) | Lịch Hãng | Lịch mua hàng | **Gateway 2: Kho có đủ Capacity trước khi nhập đợt hàng mùa vụ lớn (OTB Budget)?** |
| 3 | Buyer | *Thực hiện* Đặt hàng mùa vụ | Catalogue Hãng | Đơn hàng PO | **Gateway 3: Tỉ lệ mix sản phẩm có đạt chuẩn Core/Seasonal?** |
| 4 | Planner | *Phân bổ* Hàng hóa tới mạng lưới cửa hàng | Danh sách Store | Kế hoạch phân bổ | **Gateway 4: Cửa hàng có đủ Capacity (sức chứa)?** |
| 5 | Merchandise Dept | *Thực hiện* Sell-through rate analysis | Dữ liệu bán hàng | Báo cáo Sell-through | Đánh giá tốc độ bán ra |
| 6 | Merchandise Dept | *Thực thi* Markdown optimization | Báo cáo tồn | Quyết định giảm giá | **Gateway 5: Sell-through rate có $\le$ mức mục tiêu (buộc phải Markdown)?** |
| 7 | Store Manager | *Triển khai* Markdown trên hệ thống | Giá mới | Giá cập nhật POS | Cập nhật hệ thống POS |
| 8 | Inventory Dept | *Thu hồi* Hàng quá mùa (Obsolete) | Danh sách SKU | Hàng trả kho | **Gateway 6: Hàng có thuộc danh sách Clear-out cuối mùa?** |
| 9 | Merchandise Dept | *Lập* Báo cáo đánh giá hiệu quả mùa | Số liệu tồn/bán | Báo cáo mùa | **Gateway 7: Lợi nhuận của đợt bán mùa vụ (SS/FW) có đạt không?** |
| 10 | Ban Giám Đốc | *Phê duyệt* Phương án mua hàng cho mùa tiếp theo | Báo cáo mùa | Kế hoạch mới | **Gateway 8: Phương án mua hàng mới có khả thi về mặt tài chính?** |


### 2.4. Quy trình Bán hàng Đa kênh & Thanh toán POS / E-Commerce (C3)

#### Hồ sơ Quy trình (Process Profile)
* **Mã quy trình:** C3
* **Tên quy trình:** Bán hàng đa kênh và Thanh toán POS / E-Commerce.
* **Mục tiêu:** Cung cấp trải nghiệm mua sắm đồng nhất, tích hợp hệ thống Retail Pro Prism, hỗ trợ các hình thức như Ship-from-Store, Click-and-Collect, và đa phương thức thanh toán.
* **Đầu vào:** Nhu cầu mua hàng của khách (Offline hoặc Online).
* **Đầu ra:** Đơn hàng hoàn tất thanh toán, biên bản giao nhận.
* **Kết quả tích cực:** Trải nghiệm thanh toán nhanh chóng, điều hướng hàng hóa thông minh từ Store hoặc Warehouse.

#### Bảng Trình tự các Bước Thực hiện (Step-by-Step Table)

*Bảng 2.3: Bảng các bước thực hiện quy trình C3.*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Khách hàng | *Lựa chọn* Mua sắm sản phẩm | Catalogue | Đơn hàng chờ | **Gateway 1: Khách mua tại Cửa hàng (POS) hay Web/App (Magento)?** |
| 2 | Hệ thống OMS | *Kiểm tra* Tồn kho trung tâm | Thông tin SKU | Trạng thái tồn | **Gateway 2: Warehouse Online bị Out of Stock (OOS)?** |
| 3 | Hệ thống OMS | *Điều phối* Ship-from-Store | Lệnh điều hướng | Yêu cầu Store | **Gateway 3: Store đích có thực sự sẵn hàng (XOR split) khi Warehouse OOS để cho phép Click-and-Collect?** |
| 4 | Khách hàng | *Chọn* Hình thức nhận hàng | Tùy chọn giao | Lịch trình giao | **Gateway 4: Khách hàng chọn Giao hàng tận nơi hay Click-and-Collect?** |
| 5 | Hệ thống Retail Pro Prism | *Tích hợp* Dữ liệu bán hàng đồng bộ | Data đơn hàng | Đồng bộ Prism | Tích hợp hệ thống quản trị |
| 6 | Khách hàng | *Thực hiện* Thanh toán đa phương thức | Hóa đơn | Giao dịch Payment | **Gateway 5: Phương thức (Cash, Card, QR VNPay/Momo/ZaloPay, Installment)?** |
| 7 | Payment Gateway | *Xác thực* Giao dịch | Dữ liệu thẻ/QR | Trạng thái Pay | **Gateway 6: Giao dịch thanh toán có thành công không?** |
| 8 | Retail Pro Prism | *Phát hành* Hóa đơn điện tử (e-Invoice) | Giao dịch | Hóa đơn | **Gateway 7: Sync API với Cơ quan Thuế (Thông tư 78) có thành công (Async Message Flow)?** |
| 9 | Store / Warehouse | *Đóng gói* Sản phẩm | Sản phẩm | Kiện hàng | Đóng gói theo quy cách chuẩn |
| 10 | 3PL / NV Giao hàng | *Giao hàng* Tới tay khách | Kiện hàng | Chữ ký nhận | **Gateway 8: Khách hàng đã nhận hàng thành công chưa?** |


### 2.5. Quy trình Tiếp nhận Đổi trả, Bảo hành và Hoàn tiền (C4)

#### Hồ sơ Quy trình (Process Profile)
* **Mã quy trình:** C4
* **Tên quy trình:** Đổi trả hàng hóa và Hoàn tiền (Reverse Logistics).
* **Mục tiêu:** Xử lý các yêu cầu đổi/trả dựa trên policy (15-day policy, 1 exchange per invoice), xác minh Excluded items list, cung cấp tính năng online return photo upload, và đảm bảo 5-7 day refund timeline.
* **Đầu vào:** Yêu cầu đổi/trả, hóa đơn mua hàng, ảnh tình trạng hàng hóa.
* **Đầu ra:** Hóa đơn đổi, chứng từ hoàn tiền.
* **Kết quả tích cực:** Khách hàng hài lòng với chính sách đổi trả minh bạch và nhanh chóng.

#### Bảng Trình tự các Bước Thực hiện (Step-by-Step Table)

*Bảng 2.4: Bảng các bước thực hiện quy trình C4.*

| STT | Tác nhân (Actor / Lane) | Hoạt động nghiệp vụ (Động từ + Danh từ) | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Cổng điều kiện / Ghi chú |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | Khách hàng | *Thực hiện* Yêu cầu đổi trả | Sản phẩm, Hóa đơn | Yêu cầu ghi nhận | **Gateway 1: Khách hàng yêu cầu trả Online (có online return photo upload) hay tại Store?** |
| 2 | CSKH / Store Manager | *Kiểm tra* Chính sách thời hạn (15-day policy) | Ngày mua | Hợp lệ thời gian | **Gateway 2: Yêu cầu đổi trả có nằm trong hạn 15-day policy không?** |
| 3 | CSKH / Store Manager | *Kiểm tra* Số lần đổi trả (1 exchange per invoice) | Hóa đơn | Hợp lệ số lần | **Gateway 3: Đơn hàng này đã từng thực hiện đổi trả (1 exchange per invoice) chưa?** |
| 4 | CSKH / Store Manager | *Kiểm tra* Danh mục loại trừ (Excluded items list) | SKU | Phân loại hàng | **Gateway 4: Sản phẩm có thuộc Excluded items (underwear, swimwear, accessories, opened cosmetics)?** |
| 5 | CSKH / Store Manager | *Đánh giá* Tình trạng sản phẩm | Hàng thực tế | Biên bản kiểm tra | **Gateway 5: SP nguyên vẹn và vượt qua Fraud check (không có dấu hiệu Wardrobing - mặc giấu tag)?** |
| 6 | Khách hàng | *Chọn* Phương án giải quyết | Tùy chọn | Yêu cầu cuối | **Gateway 6: Khách hàng chọn phương án Exchange (đổi) hay Refund (Hoàn tiền)?** |
| 7 | Store Manager | *Xử lý* Đổi sản phẩm trên Retail Pro Prism | SP mới | Hóa đơn đổi | (Khách hàng đóng thêm tiền nếu mua sản phẩm giá cao hơn) |
| 8 | Kế toán (Finance) | *Kiểm duyệt* Yêu cầu Hoàn tiền | Hồ sơ hoàn tiền | Lệnh Refund | **Gateway 7: Original payment method là gì (Cash -> Immediate, Card/Transfer -> 5-7 days)?** |
| 9 | Kế toán (Finance) | *Thực thi* Quy trình Hoàn tiền (Refund timeline) | Lệnh Refund | Ủy nhiệm chi | Thực hiện hoàn tiền tương ứng theo Original payment method |
| 10 | Kho / Store | *Nhập lại* Tồn kho sản phẩm trả | Hàng trả | Tồn kho hệ thống | **Gateway 8: Hàng trả về có đáp ứng tiêu chuẩn để tái bán (Resellable) không?** |

EOF
