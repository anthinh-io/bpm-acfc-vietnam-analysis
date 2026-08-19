# Contributing

Hướng dẫn đóng góp cho đồ án IE203 — BPM ACFC Vietnam Analysis.

## 1. Nguyên tắc chung

- Đồ án được chấm điểm dựa trên đóng góp cá nhân (lịch sử commit trên GitHub), không chấm chung cho cả nhóm.
- Mỗi thành viên thực hiện và đẩy (push) phần việc của mình lên GitHub — không nhờ người khác commit hộ, vì lịch sử commit là bằng chứng chấm điểm.

## 2. Thành viên giám sát

- Giảng viên (`trunghlh@uit.edu.vn`) được thêm làm collaborator của dự án để theo dõi tiến độ hàng tuần.
- Giảng viên đánh giá dựa trên lịch sử commit, không chỉ dựa trên kết quả cuối cùng nộp.

## 3. Tần suất hoạt động

- Duy trì hoạt động đều đặn mỗi tuần — tìm tài liệu, làm mục lục, vẽ mô hình... đều được tính là đóng góp.
- Không dồn việc đến cuối kỳ; chia nhỏ công việc và làm dần từng phần theo tiến độ.

## 4. Quy tắc nhánh

- **`master`**: nhánh chính, đại diện cho nội dung đã hoàn thiện/được chốt. Chỉ được thay đổi thông qua Pull Request (PR) — không push trực tiếp lên `master`.
- **Nhánh tính năng**: mỗi thành viên toàn quyền tự chủ trên nhánh riêng của mình (đặt tên, số lượng commit, cách làm việc) trong quá trình thực hiện phần việc được giao.
- Khi một phần việc hoàn chỉnh, mở PR từ nhánh cá nhân vào `master` để xác nhận hoàn thành công việc.

## 5. Quy tắc commit

- Commit message ngắn gọn, rõ ràng, gắn với công việc thực hiện:
  ```
  Thêm mô tả quy trình quản lý chiến dịch marketing
  Cập nhật sơ đồ BPMN quy trình duyệt ngân sách
  ```
- Mỗi commit nên tương ứng với một đơn vị công việc cụ thể, tránh gộp nhiều việc không liên quan vào một commit.
