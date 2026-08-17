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
  diagrams/bpmn-hoach-dinh-phan-bo-hang-hoa-m3.svg \
  diagrams/bpmn-kiem-ke-ton-kho-s2.svg \
  diagrams/bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg \
  diagrams/kien-truc-quy-trinh.svg \
  --out docs/workspaces/NguyenCongHung/hinh-anh/png-nocap --width 2600 --pad 14 --drop-caption
```

(Bỏ `--drop-caption` và đổi `--out … png` để tạo bộ có caption.)
