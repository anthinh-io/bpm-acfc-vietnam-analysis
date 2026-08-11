# S3 – PHÂN TÍCH QUY TRÌNH

## VA/BVA/NVA

| Hoạt động | Phân loại | Lý do/khắc phục |
|---|---|---|
| Lập kế hoạch kiểm kê | BVA | Kiểm soát tài sản và độ chính xác dữ liệu. |
| Đếm tồn thực tế | BVA | Bằng chứng tồn thực tế. |
| So sánh với sổ tồn | BVA | Phát hiện sai lệch. |
| Đếm lại khi có chênh lệch | BVA | Cần xác minh trước điều chỉnh. |
| Điều chỉnh tồn được phê duyệt | BVA | Cần cho sổ sách và quản trị rủi ro. |
| Chờ phê duyệt hoặc bằng chứng | NVA | Chờ (Hold); đặt thời hạn và chuyển cấp. |
| Đếm lại do bàn giao không đủ | NVA | Lỗi (Defects); chuẩn hóa biên bản và quét mã. |
| Nhập cùng điều chỉnh ở nhiều nơi | NVA | Xử lý dư (Over-processing); dùng một hồ sơ điều chỉnh. |

## Bốn loại lãng phí

| Loại | Biểu hiện cần kiểm chứng | Cải tiến |
|---|---|---|
| Di chuyển (Move) | Chuyển phiếu kiểm kê/biên bản qua nhiều đầu mối | Hồ sơ điện tử và một mã vụ việc. |
| Chờ (Hold) | Chờ đếm lại, giải trình hoặc duyệt điều chỉnh | Thời hạn, hàng đợi quá hạn và người phụ trách. |
| Xử lý dư (Over-processing) | Đếm/nhập/đối chiếu trùng | Kiểm kê theo rủi ro và dùng dữ liệu gốc. |
| Lỗi (Defects) | Chênh lệch lặp lại, thiếu bằng chứng, sai giao dịch | Mã vạch, nhật ký kiểm tra và mã nguyên nhân. |

## Vấn đề, nguyên nhân và khắc phục

| Vấn đề cần kiểm chứng | Nguyên nhân giả định | Khắc phục đề xuất |
|---|---|---|
| Độ chính xác tồn kho giảm | Giao dịch chưa cập nhật hoặc đếm sai | Khóa thời điểm kiểm kê, quét mã và đối chiếu sổ trước điều chỉnh. |
| Chênh lệch quá hạn | Đếm lại, giải trình hoặc phê duyệt bị chờ | Đặt thời hạn, hàng đợi quá hạn và chuyển cấp theo rủi ro. |
| Điều chỉnh lặp lại | Chưa phân loại nguyên nhân gốc | Dùng mã nguyên nhân, nhật ký kiểm tra và phản hồi về M3. |

## KPI định lượng

Khung ghi nhận: sau phỏng vấn điền ba mốc **thấp nhất – thường gặp – cao nhất** cho từng KPI; hiện chưa có số ACFC.

| KPI | Công thức/dữ liệu cần lấy | Trạng thái |
|---|---|---|
| Độ chính xác tồn kho | Mã hàng khớp tồn thực tế/sổ / tổng mã hàng | Chưa có số ACFC |
| Tỷ lệ hao hụt | Giá trị thiếu không giải thích / giá trị tồn | Chưa có số ACFC |
| Thời gian chu kỳ kiểm kê | Thời điểm đóng kiểm kê - thời điểm bắt đầu | Chưa có số ACFC |
| Tỷ lệ điều chỉnh | Kiểm kê có điều chỉnh / tổng kiểm kê | Chưa có số ACFC |
| Tuổi chênh lệch chưa đóng | Ngày hiện tại - ngày mở hồ sơ | Chưa có số ACFC |
| Tỷ lệ đóng đúng hạn | Hồ sơ đóng đúng hạn / tổng hồ sơ | Chưa có số ACFC |

## Đề xuất tương lai (TO-BE) sơ bộ

Đặt lịch kiểm kê và phạm vi trên một hệ thống, quét mã khi đếm, tự động tạo đếm lại theo ngưỡng, dùng mã nguyên nhân chuẩn, phê duyệt điều chỉnh theo hạn mức và theo dõi hồ sơ quá hạn.

## Bảng đề xuất khắc phục theo lãng phí

| Loại lãng phí | Vấn đề | Đề xuất khắc phục | Người phụ trách đề xuất | Thời hạn đề xuất |
|---|---|---|---|---|
| Di chuyển (Move) | Phiếu kiểm kê/biên bản chuyển qua nhiều đầu mối giấy tờ | Chuyển sang hồ sơ điện tử và một mã vụ việc duy nhất cho mỗi đợt kiểm kê | Kiểm soát tồn kho/Vận hành | Ngắn hạn — áp dụng từ đợt kiểm kê kế tiếp |
| Chờ (Hold) | Chờ đếm lại, giải trình hoặc duyệt điều chỉnh không có hạn rõ ràng | Đặt thời hạn xử lý, hàng đợi quá hạn và người phụ trách theo từng bước | Quản lý cửa hàng/Kiểm soát tồn kho | Ngắn hạn — thiết lập SLA trong đợt kiểm kê gần nhất |
| Xử lý dư (Over-processing) | Đếm/nhập/đối chiếu trùng dữ liệu tồn ở nhiều nơi | Kiểm kê theo mức rủi ro (không đếm dàn đều), dùng một hồ sơ điều chỉnh gốc | Kiểm soát tồn kho/Vận hành phối hợp IT | Trung hạn — 2–3 đợt kiểm kê |
| Lỗi (Defects) | Chênh lệch lặp lại, thiếu bằng chứng bàn giao, sai giao dịch | Quét mã vạch khi đếm, nhật ký kiểm tra và mã nguyên nhân chuẩn hóa | Kiểm soát tồn kho/Vận hành | Trung hạn — triển khai quét mã trong 1–2 quý |

Ghi chú: người phụ trách và thời hạn ở trên là đề xuất của nhóm dựa trên phân tích lãng phí, chưa phải cam kết chính thức của ACFC; cần xác nhận lại nếu có phỏng vấn/workshop với chủ quy trình.
