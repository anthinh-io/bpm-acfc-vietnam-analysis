# M3 – HIỆN TRẠNG SƠ BỘ: LẬP KẾ HOẠCH MUA HÀNG VÀ PHÂN BỔ

## 1. Tóm tắt

Quy trình bắt đầu khi Hàng hóa/Phân bổ bước vào kỳ kế hoạch hoặc phát hiện doanh số, tỷ lệ bán qua hay số tháng tồn kho lệch mục tiêu. Nhóm thu thập báo cáo bán hàng, tồn kho, dự báo, biên lợi nhuận, sức chứa cửa hàng và kế hoạch thương mại. Hàng hóa/Phân bổ phân tích nhu cầu theo nhãn hàng/mã hàng/cửa hàng và lập kế hoạch mua hoặc phân bổ; Tài chính thương mại kiểm tra biên lợi nhuận và ngân sách; Vận hành kiểm tra sức chứa và khả năng triển khai. Nếu được duyệt, kế hoạch phát hành yêu cầu lô hàng/nhập kho và điều chuyển/bổ sung cho bộ phận vận hành kho/cửa hàng thực hiện; các bước nhận hàng và điều chuyển nội bộ nằm ngoài phạm vi mô tả của M3 trong bản này.

## 2. Actor kích hoạt và hưởng lợi

- **Actor kích hoạt:** Hàng hóa/Phân bổ (theo lịch mùa) hoặc hệ thống cảnh báo lệch tỷ lệ bán qua/số tháng tồn kho.
- **Actor hưởng lợi trực tiếp:** Vận hành/cửa hàng (nhận đúng cơ cấu hàng), Tài chính thương mại (kiểm soát ngân sách).
- **Actor hưởng lợi gián tiếp:** khách hàng cuối (hàng đúng nhu cầu tại cửa hàng).

## 3. Các bước thực hiện

| # | Actor | Bước (Động từ + Danh từ) | Ghi chú/hệ thống |
|---|---|---|---|
| 1 | Hàng hóa/Phân bổ | Thu thập dữ liệu bán hàng, tồn kho và dự báo | Hệ thống ERP/báo cáo bán hàng — `C` |
| 2 | Hàng hóa/Phân bổ | Chốt dự báo nhu cầu theo mùa | — |
| 3 | Hàng hóa/Phân bổ | Phân tích tỷ lệ bán qua và số tháng tồn kho | So với mục tiêu theo nhãn hàng/mã hàng |
| 4 | Hàng hóa/Phân bổ | Lập kế hoạch mua hàng và phân bổ theo cửa hàng/nhãn hàng | Đầu ra: bản nháp kế hoạch |
| 5 | Tài chính thương mại | Kiểm tra biên lợi nhuận và ngân sách | Cổng điều kiện |
| 6 | Vận hành | Kiểm tra sức chứa cửa hàng | Cổng điều kiện |
| 7 | Hàng hóa/Phân bổ | Xác nhận nguồn hàng khả dụng | Có thể cần Message Flow tới Pool Chủ thương hiệu — `C` |
| 8 | Hàng hóa/Phân bổ | Trình kế hoạch phân bổ để phê duyệt | Cấp duyệt cụ thể — `C – cần xác thực` |
| 9 | Cấp phê duyệt (`C`) | Phê duyệt kế hoạch phân bổ | Cổng điều kiện |
| 10 | Hàng hóa/Phân bổ | Phát hành kế hoạch mua hàng/yêu cầu điều chuyển | Bàn giao — kết thúc phạm vi mô tả của M3 |
| 11 | Hàng hóa/Phân bổ | Theo dõi kết quả thực hiện và tiếp nhận dữ liệu chênh lệch từ S3 | Đầu vào cho chu kỳ lập kế hoạch tiếp theo |

## 4. Kịch bản thành công

Dữ liệu đầy đủ → dự báo được chốt → tỷ lệ bán qua/số tháng tồn kho xác nhận lệch mục tiêu → kế hoạch nằm trong biên lợi nhuận/ngân sách → cửa hàng đủ sức chứa → hàng nguồn khả dụng → kế hoạch được duyệt ngay lần trình đầu tiên → phát hành. **Kết quả:** "Kế hoạch mua hàng và phân bổ đã được duyệt và phát hành."

## 5. Kịch bản thất bại/ngoại lệ

- Dữ liệu bán hàng/tồn kho thiếu hoặc chưa khớp nguồn → trả lại Bước 1 để bổ sung trước khi phân tích.
- Nhu cầu vượt biên lợi nhuận/ngân sách (Bước 5) → Tài chính thương mại yêu cầu điều chỉnh kế hoạch (quay lại Bước 4) hoặc từ chối nếu vượt quá nhiều.
- Cửa hàng không đủ sức chứa (Bước 6) → điều chỉnh số lượng phân bổ hoặc giãn lịch giao.
- Hàng nguồn không khả dụng (Bước 7) → ghi nhận thiếu hàng, tìm nguồn thay thế hoặc lùi kế hoạch; có thể phải chuyển cấp nếu ảnh hưởng mùa vụ.
- Kế hoạch không được duyệt (Bước 9) → trả về Bước 4 để chỉnh sửa; nếu lặp lại nhiều lần, chuyển cấp phê duyệt cao hơn — ngưỡng số lần/thời hạn `C – cần xác thực`.
- Sau theo dõi (Bước 11), nếu S3 phát hiện chênh lệch vượt ngưỡng hoặc bộ phận vận hành báo thiếu/dư hàng kéo dài → kích hoạt lập lại kế hoạch ở chu kỳ tiếp theo (không chờ hết mùa).

**Nguồn/trạng thái:** EV02, EV04, EV07; các ngưỡng dự báo, biên lợi nhuận, số tháng tồn kho, cấp/thẩm quyền duyệt cụ thể và số lần lặp trước khi chuyển cấp là `C – cần xác thực` bằng phỏng vấn Hàng hóa/Phân bổ, Tài chính thương mại và Vận hành.
