# Scripts sinh sơ đồ BPMN (workspace Nguyễn Công Hưng)

Hai script Python sinh sơ đồ BPMN 2.0 (SVG + Draw.io) cho các quy trình ACFC.
Chúng **ghi kết quả vào `diagrams/` ở repo root** (tầng tổng hợp dùng chung), không ghi
vào workspace. Đầu mỗi script có shim `os.chdir(...)` neo về repo root nên **chạy từ
bất kỳ thư mục nào cũng đúng**:

```bash
# từ repo root
.venv/bin/python "docs/workspaces/NguyenCongHung/scripts/generate_bpmn_diagrams.py"
.venv/bin/python "docs/workspaces/NguyenCongHung/scripts/generate_all_bpmn_master.py"
```

| Script | Sinh ra (trong `diagrams/`) |
|---|---|
| `generate_bpmn_diagrams.py` | kiến trúc, S3-kiểm-kê (`bpmn-kiem-ke-ton-kho-s2`), S4-kích-hoạt (`bpmn-dang-ky-kich-hoat-tai-khoan-s3`), S1 tuyển dụng, C1/C2 kho |
| `generate_all_bpmn_master.py` | kiến trúc, tổng hợp kho, S4-kích-hoạt, S1, M3, C3, C4 (+ `.drawio`) |

## ⚠️ CẢNH BÁO — đừng chạy đè bản đã chốt

Sơ đồ **S4/kích hoạt tài khoản** (`diagrams/bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg`) đã được
**chỉnh tay và chốt ở commit `932c579` (9 cổng XOR)**. Code trong hai script này hiện vẫn tạo
ra **bản 8 cổng cũ** — **chạy lại generator sẽ GHI ĐÈ bản chốt về bản 8 cổng sai**.

- Trước khi chạy bất kỳ script nào: kiểm tra `git status diagrams/` và, nếu cần, khôi phục bằng
  `git checkout HEAD -- diagrams/bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg`.
- Việc đồng bộ code generator cho khớp bản chốt 9 cổng thuộc phần **review/update sau**.

## Kiểm tra sơ đồ sau khi sinh

Dùng skill `bpm-quy-trinh-acfc` (`.claude/skills/…`):
- `scripts/render_and_crop.py` — render PNG để soi mắt (bắt buộc trước khi coi là xong).
- `scripts/export_png.py` — xuất PNG nền trắng, cắt lề, `--drop-caption` để nhúng Word/PPTX
  (ảnh kết quả đã lưu ở `../hinh-anh/`).
