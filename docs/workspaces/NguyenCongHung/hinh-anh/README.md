# Hình ảnh sơ đồ (PNG nền trắng, đã cắt lề)

Ảnh PNG xuất từ SVG trong `diagrams/` bằng skill `export_png.py`, dùng để nhúng vào
báo cáo Word / PowerPoint / Marp mà không bị viền trắng thừa.

| Thư mục | Nội dung | Dùng cho |
|---|---|---|
| `png/` | Có sẵn dòng caption "Hình x.y…" vẽ trong SVG | Xem nhanh, chèn ảnh độc lập |
| `png-nocap/` | **Đã bỏ** caption trong SVG (`--drop-caption`) | Nhúng Word/PPTX rồi để phần mềm tự đánh số caption (SEQ) — tránh trùng caption |

Tạo lại khi SVG thay đổi (chạy từ repo root):

```bash
.venv/bin/python .claude/skills/bpm-quy-trinh-acfc/scripts/export_png.py \
  docs/workspaces/NguyenCongHung/diagrams/bpmn-kho-van-hanh-m3-s3.svg \
  docs/workspaces/NguyenCongHung/diagrams/bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg \
  docs/workspaces/NguyenCongHung/diagrams/bpmn-tuyen-dung-nhan-su-s1.svg \
  docs/workspaces/NguyenCongHung/diagrams/bpmn-nhap-kho-qc-k1.svg \
  docs/workspaces/NguyenCongHung/diagrams/bpmn-xuat-kho-dieu-chuyen-k2.svg \
  docs/workspaces/NguyenCongHung/diagrams/bpmn-thu-hoi-hang-tra-k3.svg \
  docs/workspaces/NguyenCongHung/diagrams/bpmn-kho-van-hanh-k1-k2-k3.svg \
  diagrams/kien-truc-quy-trinh.svg \
  --out docs/workspaces/NguyenCongHung/hinh-anh/png-nocap --width 2600 --pad 14 --drop-caption
```

(Bỏ `--drop-caption` và đổi `--out … png` để tạo bộ có caption.)
