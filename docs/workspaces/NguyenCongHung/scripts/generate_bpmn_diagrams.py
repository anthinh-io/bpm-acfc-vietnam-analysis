#!/usr/bin/env python3
"""
Generate comprehensive BPMN 2.0 SVG and Draw.io XML files for ACFC (Công ty Cổ phần Thời trang và Mỹ phẩm Âu Châu):
1. Architecture Diagram
2. S2: Stocktaking & Reconciliation (>=8 Gateways)
3. C1/C2: Warehouse Inbound & Outbound Fulfillment (>=8 Gateways)
4. S3: Member Registration & OTP Activation (>=8 Gateways)
5. S1: Retail & Supply Chain Recruitment (>=8 Gateways)
"""

import os

# Script sống trong workspace cá nhân nhưng ghi sơ đồ vào diagrams/ ở repo root.
# Neo CWD về repo root (4 cấp trên: scripts → NguyenCongHung → workspaces → docs → root)
# để chạy được từ bất kỳ thư mục nào.
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")))

os.makedirs("diagrams", exist_ok=True)

# -------------------------------------------------------------
# 1. PROCESS ARCHITECTURE SVG & DRAW.IO
# -------------------------------------------------------------
def generate_architecture():
    svg = '''<svg width="1100" height="700" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <linearGradient id="mGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ebf8ff"/>
      <stop offset="100%" stop-color="#bee3f8"/>
    </linearGradient>
    <linearGradient id="cGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fefcbf"/>
      <stop offset="100%" stop-color="#faf089"/>
    </linearGradient>
    <linearGradient id="sGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#edf2f7"/>
      <stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <filter id="boxShadow" x="-2%" y="-2%" width="104%" height="106%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.1"/>
    </filter>
  </defs>

  <rect width="1100" height="700" fill="#ffffff" rx="10"/>
  <rect x="15" y="15" width="1070" height="670" fill="none" stroke="#cbd5e0" stroke-width="2" rx="8"/>

  <text x="40" y="50" font-size="20" font-weight="bold" fill="#1a202c">SƠ ĐỒ KIẾN TRÚC QUY TRÌNH TỔNG THỂ DOANH NGHIỆP ACFC</text>
  <text x="40" y="75" font-size="13" fill="#718096">Khung chuẩn APQC / Value Chain Framework | Phân bổ 10 quy trình nghiệp vụ theo 3 cấp độ BPM</text>

  <!-- 1. MANAGEMENT PROCESSES -->
  <rect x="40" y="100" width="1020" height="150" rx="8" fill="#f7fafc" stroke="#3182ce" stroke-width="2"/>
  <rect x="40" y="100" width="35" height="150" fill="#3182ce" rx="8"/>
  <text x="58" y="175" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 58 175)" text-anchor="middle">QUẢN LÝ (MANAGEMENT)</text>

  <!-- M1 Box -->
  <rect x="95" y="120" width="290" height="110" rx="6" fill="url(#mGrad)" stroke="#3182ce" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="95" y="120" width="290" height="30" rx="6" fill="#3182ce"/>
  <text x="240" y="140" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">M1: CHIẾN LƯỢC &amp; MẠNG LƯỚI KÊNH</text>
  <text x="110" y="170" font-size="11" fill="#2d3748">• Nghiên cứu thị trường thời trang bán lẻ</text>
  <text x="110" y="190" font-size="11" fill="#2d3748">• Thẩm định địa điểm mở cửa hàng ACFC mới</text>
  <text x="110" y="210" font-size="11" fill="#2d3748">• Duyệt kế hoạch mở rộng chuỗi điểm bán năm</text>

  <!-- M2 Box -->
  <rect x="410" y="120" width="290" height="110" rx="6" fill="url(#mGrad)" stroke="#3182ce" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="410" y="120" width="290" height="30" rx="6" fill="#3182ce"/>
  <text x="555" y="140" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">M2: KẾ HOẠCH TÀI CHÍNH &amp; OTB</text>
  <text x="425" y="170" font-size="11" fill="#2d3748">• Dự toán hạn mức mua hàng (Open-to-Buy)</text>
  <text x="425" y="190" font-size="11" fill="#2d3748">• Kiểm soát dòng tiền &amp; chi phí nhượng quyền</text>
  <text x="425" y="210" font-size="11" fill="#2d3748">• Đối soát tài chính thương mại &amp; doanh thu</text>

  <!-- M3 Box -->
  <rect x="725" y="120" width="315" height="110" rx="6" fill="url(#mGrad)" stroke="#3182ce" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="725" y="120" width="315" height="30" rx="6" fill="#3182ce"/>
  <text x="882" y="140" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">M3: HOẠCH ĐỊNH &amp; PHÂN BỔ HÀNG HÓA</text>
  <text x="740" y="170" font-size="11" fill="#2d3748">• Dự báo nhu cầu bán hàng &amp; vòng quay tồn</text>
  <text x="740" y="190" font-size="11" fill="#2d3748">• Cơ cấu danh mục sản phẩm chủ lực theo mùa</text>
  <text x="740" y="210" font-size="11" fill="#2d3748">• Lập kế hoạch phân bổ cho chuỗi 100+ Store</text>

  <!-- 2. CORE PROCESSES -->
  <rect x="40" y="270" width="1020" height="180" rx="8" fill="#fffff0" stroke="#d69e2e" stroke-width="2"/>
  <rect x="40" y="270" width="35" height="180" fill="#d69e2e" rx="8"/>
  <text x="58" y="360" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 58 360)" text-anchor="middle">CỐT LÕI (CORE VALUE CHAIN)</text>

  <!-- C1 Box -->
  <rect x="95" y="295" width="220" height="135" rx="6" fill="url(#cGrad)" stroke="#d69e2e" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="95" y="295" width="220" height="28" rx="6" fill="#d69e2e"/>
  <text x="205" y="314" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C1: NHẬP KHẨU &amp; TỔNG KHO</text>
  <text x="105" y="340" font-size="11" fill="#744210">• Tiếp nhận chứng từ B/L, Invoice</text>
  <text x="105" y="360" font-size="11" fill="#744210">• Khai báo &amp; thông quan Hải quan</text>
  <text x="105" y="380" font-size="11" fill="#744210">• Dỡ hàng, quét Barcode/RFID</text>
  <text x="105" y="400" font-size="11" fill="#744210">• Nhập kho WMS &amp; lưu giá kệ</text>

  <!-- Arrow C1 -> C2 -->
  <line x1="315" y1="362" x2="340" y2="362" stroke="#d69e2e" stroke-width="3"/>
  <polygon points="340,357 350,362 340,367" fill="#d69e2e"/>

  <!-- C2 Box -->
  <rect x="350" y="295" width="220" height="135" rx="6" fill="url(#cGrad)" stroke="#d69e2e" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="350" y="295" width="220" height="28" rx="6" fill="#d69e2e"/>
  <text x="460" y="314" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C2: XUẤT KHO &amp; BỔ SUNG STORE</text>
  <text x="360" y="340" font-size="11" fill="#744210">• Nhận lệnh phân bổ từ M3/Store</text>
  <text x="360" y="360" font-size="11" fill="#744210">• Lấy hàng (Picking) theo WMS</text>
  <text x="360" y="380" font-size="11" fill="#744210">• Đóng gói, dán Shipping Label</text>
  <text x="360" y="400" font-size="11" fill="#744210">• 3PL vận chuyển &amp; giao Store</text>

  <!-- Arrow C2 -> C3 -->
  <line x1="570" y1="362" x2="595" y2="362" stroke="#d69e2e" stroke-width="3"/>
  <polygon points="595,357 605,362 595,367" fill="#d69e2e"/>

  <!-- C3 Box -->
  <rect x="605" y="295" width="220" height="135" rx="6" fill="url(#cGrad)" stroke="#d69e2e" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="605" y="295" width="220" height="28" rx="6" fill="#d69e2e"/>
  <text x="715" y="314" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C3: BÁN HÀNG ĐA KÊNH (OMNI)</text>
  <text x="615" y="340" font-size="11" fill="#744210">• Bán tại Store / Web / App ACFC</text>
  <text x="615" y="360" font-size="11" fill="#744210">• Quét mã thành viên &amp; Voucher</text>
  <text x="615" y="380" font-size="11" fill="#744210">• Thanh toán POS / Ví / Thẻ / Payoo</text>
  <text x="615" y="400" font-size="11" fill="#744210">• Xuất hóa đơn e-Invoice &amp; trừ tồn</text>

  <!-- Arrow C3 -> C4 -->
  <line x1="825" y1="362" x2="850" y2="362" stroke="#d69e2e" stroke-width="3"/>
  <polygon points="850,357 860,362 850,367" fill="#d69e2e"/>

  <!-- C4 Box -->
  <rect x="860" y="295" width="180" height="135" rx="6" fill="url(#cGrad)" stroke="#d69e2e" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="860" y="295" width="180" height="28" rx="6" fill="#d69e2e"/>
  <text x="950" y="314" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C4: ĐỔI TRẢ &amp; HOÀN TIỀN</text>
  <text x="870" y="340" font-size="11" fill="#744210">• Tiếp nhận yêu cầu đổi trả</text>
  <text x="870" y="360" font-size="11" fill="#744210">• Giám định lỗi kỹ thuật</text>
  <text x="870" y="380" font-size="11" fill="#744210">• Đổi size / Hoàn tiền</text>
  <text x="870" y="400" font-size="11" fill="#744210">• Hoàn nhập kho Reverse</text>

  <!-- 3. SUPPORT PROCESSES -->
  <rect x="40" y="470" width="1020" height="150" rx="8" fill="#f7fafc" stroke="#4a5568" stroke-width="2"/>
  <rect x="40" y="470" width="35" height="150" fill="#4a5568" rx="8"/>
  <text x="58" y="545" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 58 545)" text-anchor="middle">HỖ TRỢ (SUPPORT)</text>

  <!-- S1 Box -->
  <rect x="95" y="490" width="290" height="110" rx="6" fill="url(#sGrad)" stroke="#4a5568" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="95" y="490" width="290" height="30" rx="6" fill="#4a5568"/>
  <text x="240" y="510" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">S1: TUYỂN DỤNG &amp; ONBOARDING</text>
  <text x="110" y="540" font-size="11" fill="#2d3748">• Thu hút &amp; Sàng lọc hồ sơ ứng viên</text>
  <text x="110" y="560" font-size="11" fill="#2d3748">• Phỏng vấn V1, V2 &amp; Test năng lực</text>
  <text x="110" y="580" font-size="11" fill="#2d3748">• Gửi Offer Letter &amp; Ký HĐ thử việc</text>

  <!-- S2 Box -->
  <rect x="410" y="490" width="290" height="110" rx="6" fill="url(#sGrad)" stroke="#4a5568" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="410" y="490" width="290" height="30" rx="6" fill="#4a5568"/>
  <text x="555" y="510" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">S2: KIỂM KÊ &amp; XỬ LÝ CHÊNH LỆCH</text>
  <text x="425" y="540" font-size="11" fill="#2d3748">• Quét mã kiểm đếm thực tế Store/Kho</text>
  <text x="425" y="560" font-size="11" fill="#2d3748">• Tự động đối chiếu số dư WMS/ERP</text>
  <text x="425" y="580" font-size="11" fill="#2d3748">• Xử lý thất thoát &amp; Phản hồi cho M3</text>

  <!-- S3 Box -->
  <rect x="725" y="490" width="315" height="110" rx="6" fill="url(#sGrad)" stroke="#4a5568" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="725" y="490" width="315" height="30" rx="6" fill="#4a5568"/>
  <text x="882" y="510" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">S3: ĐĂNG KÝ &amp; KÍCH HOẠT MEMBER</text>
  <text x="740" y="540" font-size="11" fill="#2d3748">• Đăng ký SĐT &amp; Xác thực mã SMS OTP</text>
  <text x="740" y="560" font-size="11" fill="#2d3748">• Điền thông tin cá nhân &amp; tạo mật khẩu</text>
  <text x="740" y="580" font-size="11" fill="#2d3748">• Kích hoạt ID thành viên ACFC Member</text>

  <!-- Inter-layer Arrows -->
  <line x1="882" y1="230" x2="882" y2="280" stroke="#3182ce" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="877,280 882,290 887,280" fill="#3182ce"/>
  <text x="895" y="260" font-size="10" font-style="italic" fill="#3182ce">Lệnh phân bổ hàng</text>

  <line x1="555" y1="490" x2="555" y2="445" stroke="#4a5568" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="550,445 555,435 560,445" fill="#4a5568"/>
  <text x="565" y="465" font-size="10" font-style="italic" fill="#4a5568">Kiểm soát số dư tồn</text>

  <text x="550" y="650" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 2.1: Sơ đồ kiến trúc quy trình tổng thể doanh nghiệp ACFC.</text>
</svg>'''
    with open("diagrams/kien-truc-quy-trinh.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    drawio_xml = '''<mxfile host="app.diagrams.net" modified="2026-08-14T11:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="Architecture" name="Process Architecture ACFC">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="arch_group" value="KIẾN TRÚC QUY TRÌNH DOANH NGHIỆP ACFC" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;startSize=30;horizontal=1;containerType=tree;fontSize=14;fontStyle=1;fillColor=#f8f9fa;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1080" height="720" as="geometry"/>
        </mxCell>
        <mxCell id="mgmt_lane" value="QUY TRÌNH QUẢN LÝ (MANAGEMENT)" style="swimlane;html=1;startSize=30;fontSize=12;fontStyle=1;fillColor=#ebf8ff;strokeColor=#3182ce;" vertex="1" parent="arch_group">
          <mxGeometry y="30" width="1080" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="m1" value="M1: Chiến lược &amp; Phát triển Mạng lưới Kênh" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;fontStyle=1;" vertex="1" parent="mgmt_lane">
          <mxGeometry x="60" y="60" width="280" height="90" as="geometry"/>
        </mxCell>
        <mxCell id="m2" value="M2: Kế hoạch Tài chính &amp; Ngân sách OTB" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;fontStyle=1;" vertex="1" parent="mgmt_lane">
          <mxGeometry x="390" y="60" width="280" height="90" as="geometry"/>
        </mxCell>
        <mxCell id="m3" value="M3: Hoạch định &amp; Phân bổ Hàng hóa" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;fontStyle=1;" vertex="1" parent="mgmt_lane">
          <mxGeometry x="720" y="60" width="310" height="90" as="geometry"/>
        </mxCell>
        <mxCell id="core_lane" value="QUY TRÌNH CỐT LÕI (CORE VALUE CHAIN)" style="swimlane;html=1;startSize=30;fontSize=12;fontStyle=1;fillColor=#fefcbf;strokeColor=#d69e2e;" vertex="1" parent="arch_group">
          <mxGeometry y="230" width="1080" height="240" as="geometry"/>
        </mxCell>
        <mxCell id="c1" value="C1: Nhập khẩu &amp; Nhận hàng Tổng kho" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;fontStyle=1;" vertex="1" parent="core_lane">
          <mxGeometry x="40" y="70" width="220" height="100" as="geometry"/>
        </mxCell>
        <mxCell id="c2" value="C2: Xuất kho &amp; Bổ sung Chuỗi Cửa hàng" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;fontStyle=1;" vertex="1" parent="core_lane">
          <mxGeometry x="300" y="70" width="220" height="100" as="geometry"/>
        </mxCell>
        <mxCell id="c3" value="C3: Bán hàng Đa kênh &amp; Thanh toán (Omni)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;fontStyle=1;" vertex="1" parent="core_lane">
          <mxGeometry x="560" y="70" width="220" height="100" as="geometry"/>
        </mxCell>
        <mxCell id="c4" value="C4: Đổi trả, Bảo hành &amp; Hoàn tiền" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;fontStyle=1;" vertex="1" parent="core_lane">
          <mxGeometry x="820" y="70" width="220" height="100" as="geometry"/>
        </mxCell>
        <mxCell id="edge_c1_c2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#d69e2e;" edge="1" parent="core_lane" source="c1" target="c2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge_c2_c3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#d69e2e;" edge="1" parent="core_lane" source="c2" target="c3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge_c3_c4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#d69e2e;" edge="1" parent="core_lane" source="c3" target="c4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="supp_lane" value="QUY TRÌNH HỖ TRỢ (SUPPORT)" style="swimlane;html=1;startSize=30;fontSize=12;fontStyle=1;fillColor=#edf2f7;strokeColor=#4a5568;" vertex="1" parent="arch_group">
          <mxGeometry y="470" width="1080" height="220" as="geometry"/>
        </mxCell>
        <mxCell id="s1" value="S1: Tuyển dụng &amp; Onboarding Nhân sự" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4a5568;fontStyle=1;" vertex="1" parent="supp_lane">
          <mxGeometry x="60" y="70" width="280" height="90" as="geometry"/>
        </mxCell>
        <mxCell id="s2" value="S2: Kiểm kê &amp; Xử lý Chênh lệch Tồn kho" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4a5568;fontStyle=1;" vertex="1" parent="supp_lane">
          <mxGeometry x="390" y="70" width="280" height="90" as="geometry"/>
        </mxCell>
        <mxCell id="s3" value="S3: Đăng ký &amp; Kích hoạt Tài khoản Member" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4a5568;fontStyle=1;" vertex="1" parent="supp_lane">
          <mxGeometry x="720" y="70" width="310" height="90" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    with open("diagrams/kien-truc-quy-trinh.drawio", "w", encoding="utf-8") as f:
        f.write(drawio_xml)

# -------------------------------------------------------------
# 2. S2: STOCKTAKING BPMN (>=8 Gateways)
# -------------------------------------------------------------
def generate_bpmn_s2():
    svg = '''<svg width="1400" height="850" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <marker id="msgArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="none" stroke="#2d3748" stroke-width="1.5"/>
    </marker>
    <filter id="taskShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1400" height="850" fill="#ffffff"/>

  <!-- Title -->
  <text x="30" y="35" font-size="18" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0: QUY TRÌNH KIỂM KÊ &amp; XỬ LÝ CHÊNH LỆCH TỒN KHO (S2)</text>
  <text x="30" y="55" font-size="12" fill="#718096">Chủ thể: Công ty Cổ phần Thời trang và Mỹ phẩm Âu Châu (ACFC) | Độ phức tạp: 8 Cổng điều kiện (Gateways)</text>

  <!-- External Pool: M3 Merchandise Planning -->
  <rect x="30" y="70" width="1340" height="60" fill="#ebf8ff" stroke="#3182ce" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="50" y="105" font-size="12" font-weight="bold" fill="#2b6cb0">POOL NGOÀI: BỘ PHẬN HOẠCH ĐỊNH HÀNG HÓA &amp; PHÂN BỔ (M3 - MERCHANDISING PLANNING)</text>

  <!-- Main Pool: ACFC Internal Stocktaking Process -->
  <rect x="30" y="150" width="1340" height="640" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="30" y="150" width="35" height="640" fill="#2d3748"/>
  <text x="48" y="470" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 48 470)" text-anchor="middle">ACFC – QUY TRÌNH KIỂM KÊ TỒN KHO NỘI BỘ (S2)</text>

  <!-- Lanes -->
  <!-- Lane 1: Quản lý Kho / Cửa hàng trưởng -->
  <line x1="65" y1="270" x2="1370" y2="270" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="65" y="150" width="30" height="120" fill="#edf2f7"/>
  <text x="80" y="210" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 80 210)" text-anchor="middle">Store / Kho</text>

  <!-- Lane 2: Đội kiểm kê thực tế -->
  <line x1="65" y1="390" x2="1370" y2="390" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="65" y="270" width="30" height="120" fill="#edf2f7"/>
  <text x="80" y="330" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 80 330)" text-anchor="middle">Đội kiểm đếm</text>

  <!-- Lane 3: Chuyên viên Kiểm soát tồn kho -->
  <line x1="65" y1="520" x2="1370" y2="520" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="65" y="390" width="30" height="130" fill="#edf2f7"/>
  <text x="80" y="455" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 80 455)" text-anchor="middle">Kiểm soát tồn</text>

  <!-- Lane 4: Kế toán Kho &amp; Doanh thu -->
  <line x1="65" y1="650" x2="1370" y2="650" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="65" y="520" width="30" height="130" fill="#edf2f7"/>
  <text x="80" y="585" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 80 585)" text-anchor="middle">Kế toán Kho</text>

  <!-- Lane 5: Ban Giám đốc / CFO -->
  <rect x="65" y="650" width="30" height="140" fill="#edf2f7"/>
  <text x="80" y="720" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 80 720)" text-anchor="middle">CFO / Giám đốc</text>

  <!-- BPMN ELEMENTS -->
  <!-- Start Event: Đến kỳ kiểm kê -->
  <circle cx="130" cy="210" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="130" y="245" font-size="10" fill="#22543d" text-anchor="middle">Đến kỳ kiểm kê</text>

  <!-- Task 1: Lập kế hoạch kiểm kê (Lane 1) -->
  <rect x="180" y="185" width="110" height="50" rx="8" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="235" y="206" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Lập kế hoạch</text>
  <text x="235" y="222" font-size="10" fill="#2d3748" text-anchor="middle">kiểm kê chi tiết</text>

  <!-- Gateway 1: Duyệt kế hoạch? (Lane 5) -->
  <polygon points="320,720 345,695 370,720 345,745" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="345" y="724" font-size="12" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="345" y="760" font-size="9" fill="#744210" text-anchor="middle">G1: Duyệt kế hoạch?</text>

  <!-- Task 2: Khóa sổ kho (Lane 1) -->
  <rect x="390" y="185" width="100" height="50" rx="8" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="440" y="206" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Khóa sổ</text>
  <text x="440" y="222" font-size="10" fill="#2d3748" text-anchor="middle">giao dịch kho</text>

  <!-- Task 3: Quét mã đếm lần 1 (Lane 2) -->
  <rect x="390" y="305" width="100" height="50" rx="8" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="440" y="326" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Quét mã đếm</text>
  <text x="440" y="342" font-size="10" fill="#2d3748" text-anchor="middle">thực tế lần 1</text>

  <!-- Task 4: Đối chiếu sổ tồn WMS (Lane 3) -->
  <rect x="390" y="430" width="100" height="50" rx="8" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="440" y="451" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Tự động đối chiếu</text>
  <text x="440" y="467" font-size="10" fill="#2d3748" text-anchor="middle">số dư sổ tồn</text>

  <!-- Gateway 2: Khớp 100%? (Lane 3) -->
  <polygon points="520,455 545,430 570,455 545,480" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="545" y="459" font-size="12" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="545" y="495" font-size="9" fill="#744210" text-anchor="middle">G2: Khớp 100%?</text>

  <!-- Gateway 3: Lệch <= 0.5%? (Lane 3) -->
  <polygon points="610,455 635,430 660,455 635,480" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="635" y="459" font-size="12" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="635" y="495" font-size="9" fill="#744210" text-anchor="middle">G3: Lệch &lt;= 0.5%?</text>

  <!-- Task 5: Đếm chéo lần 2 (Lane 2) -->
  <rect x="585" y="305" width="100" height="50" rx="8" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="635" y="326" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Đếm chéo</text>
  <text x="635" y="342" font-size="10" fill="#2d3748" text-anchor="middle">độc lập lần 2</text>

  <!-- Gateway 4: AND-Split tra soát (Lane 4) -->
  <polygon points="700,585 725,560 750,585 725,610" fill="#c6f6d5" stroke="#22543d" stroke-width="1.5"/>
  <text x="725" y="589" font-size="14" font-weight="bold" fill="#22543d" text-anchor="middle">+</text>
  <text x="725" y="625" font-size="9" fill="#22543d" text-anchor="middle">G4: AND-Split</text>

  <!-- Parallel Task A: Rà soát chứng từ -->
  <rect x="770" y="540" width="105" height="40" rx="6" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5"/>
  <text x="822" y="556" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Rà soát chứng từ</text>
  <text x="822" y="570" font-size="9" fill="#2d3748" text-anchor="middle">nhập/xuất/trả</text>

  <!-- Parallel Task B: Kiểm tra hàng cách ly -->
  <rect x="770" y="595" width="105" height="40" rx="6" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5"/>
  <text x="822" y="611" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Kiểm tra khu</text>
  <text x="822" y="625" font-size="9" fill="#2d3748" text-anchor="middle">hàng lỗi/cách ly</text>

  <!-- Gateway 5: AND-Join đồng bộ (Lane 4) -->
  <polygon points="900,585 925,560 950,585 925,610" fill="#c6f6d5" stroke="#22543d" stroke-width="1.5"/>
  <text x="925" y="589" font-size="14" font-weight="bold" fill="#22543d" text-anchor="middle">+</text>
  <text x="925" y="625" font-size="9" fill="#22543d" text-anchor="middle">G5: AND-Join</text>

  <!-- Gateway 6: Lỗi nhập liệu hay Thất thoát? (Lane 3) -->
  <polygon points="980,455 1005,430 1030,455 1005,480" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1005" y="459" font-size="12" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1005" y="495" font-size="9" fill="#744210" text-anchor="middle">G6: Nguyên nhân?</text>

  <!-- Task 6a: Lập đề nghị điều chỉnh kho -->
  <rect x="1050" y="420" width="100" height="40" rx="6" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5"/>
  <text x="1100" y="436" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Lập đề nghị</text>
  <text x="1100" y="450" font-size="9" fill="#2d3748" text-anchor="middle">điều chỉnh kho</text>

  <!-- Task 6b: Lập biên bản thất thoát & bồi thường -->
  <rect x="1050" y="475" width="100" height="40" rx="6" fill="#ffffff" stroke="#e53e3e" stroke-width="1.5"/>
  <text x="1100" y="491" font-size="9" font-weight="bold" fill="#742a2a" text-anchor="middle">Lập biên bản</text>
  <text x="1100" y="505" font-size="9" fill="#742a2a" text-anchor="middle">thất thoát/xử lý</text>

  <!-- Gateway 7: CFO Duyệt xử lý? (Lane 5) -->
  <polygon points="1080,720 1105,695 1130,720 1105,745" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1105" y="724" font-size="12" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1105" y="760" font-size="9" fill="#744210" text-anchor="middle">G7: Duyệt xử lý?</text>

  <!-- Task 7: Hạch toán & cập nhật ERP (Lane 4) -->
  <rect x="1170" y="560" width="100" height="45" rx="6" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5"/>
  <text x="1220" y="578" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Cập nhật số dư</text>
  <text x="1220" y="592" font-size="9" fill="#2d3748" text-anchor="middle">vào ERP/WMS</text>

  <!-- Task 8: Mở khóa kho & lưu hồ sơ (Lane 1) -->
  <rect x="1170" y="185" width="100" height="45" rx="6" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5"/>
  <text x="1220" y="203" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Mở khóa kho</text>
  <text x="1220" y="217" font-size="9" fill="#2d3748" text-anchor="middle">&amp; lưu hồ sơ</text>

  <!-- Gateway 8: XOR-Join Hoàn tất (Lane 1) -->
  <polygon points="1285,210 1300,195 1315,210 1300,225" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1300" y="214" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1283" y="180" font-size="9" fill="#744210" text-anchor="end">G8: XOR-Join</text>

  <!-- End Event: Hoàn tất kiểm kê -->
  <circle cx="1345" cy="210" r="16" fill="#fed7d7" stroke="#9b2c2c" stroke-width="3"/>
  <text x="1345" y="240" font-size="9" font-weight="bold" fill="#9b2c2c" text-anchor="middle">Đóng hồ sơ</text>

  <!-- SEQUENCE FLOWS -->
  <line x1="148" y1="210" x2="180" y2="210" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Task 1 -> G1 (Lane 1 -> Lane 5) -->
  <path d="M 235 235 L 235 720 L 320 720" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- G1 [Yes] -> Task 2 (Lane 5 -> Lane 1) -->
  <path d="M 370 720 L 440 720 L 440 235" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="380" y="710" font-size="9" fill="#2d3748">[Duyệt]</text>

  <!-- G1 [No] -> Task 1 -->
  <path d="M 345 695 L 345 660 L 260 660 L 260 235" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="310" y="680" font-size="9" fill="#e53e3e">[Không duyệt]</text>

  <!-- Task 2 -> Task 3 -->
  <line x1="440" y1="235" x2="440" y2="305" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Task 3 -> Task 4 -->
  <line x1="440" y1="355" x2="440" y2="430" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Task 4 -> G2 -->
  <line x1="490" y1="455" x2="520" y2="455" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- G2 [Khớp] -> G8 (Bỏ qua xử lý) -->
  <path d="M 545 430 L 545 170 L 1300 170 L 1300 195" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="555" y="420" font-size="9" fill="#38a169">[Khớp 100%]</text>

  <!-- G2 [Lệch] -> G3 -->
  <line x1="570" y1="455" x2="610" y2="455" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="575" y="445" font-size="9" fill="#e53e3e">[Lệch]</text>

  <!-- G3 [>0.5%] -> Task 5 (Đếm lại) -->
  <line x1="635" y1="430" x2="635" y2="355" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="640" y="400" font-size="9" fill="#e53e3e">[Vượt 0.5%]</text>

  <!-- Task 5 -> G4 -->
  <path d="M 685 330 L 725 330 L 725 560" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- G3 [<=0.5%] -> G4 -->
  <path d="M 660 455 L 725 455 L 725 560" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="665" y="445" font-size="9" fill="#38a169">[Trong 0.5%]</text>

  <!-- G4 -> Parallel Task A & B -->
  <path d="M 750 585 L 770 560" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 750 585 L 770 615" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Parallel Tasks -> G5 -->
  <path d="M 875 560 L 900 585" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 875 615 L 900 585" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- G5 -> G6 -->
  <path d="M 950 585 L 965 585 L 965 455 L 980 455" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- G6 -> Task 6a & 6b -->
  <path d="M 1030 455 L 1040 455 L 1040 440 L 1050 440" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="1035" y="430" font-size="8" fill="#2d3748">[Lỗi sổ]</text>

  <path d="M 1030 455 L 1040 455 L 1040 495 L 1050 495" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="1035" y="515" font-size="8" fill="#e53e3e">[Mất mát]</text>

  <!-- Task 6a, 6b -> G7 -->
  <path d="M 1150 440 L 1160 440 L 1160 680 L 1105 680 L 1105 695" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 1150 495 L 1160 495 L 1160 680" fill="none" stroke="#2d3748" stroke-width="1.5"/>

  <!-- G7 [Duyệt] -> Task 7 -->
  <path d="M 1130 720 L 1220 720 L 1220 605" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="1140" y="710" font-size="9" fill="#38a169">[Duyệt xử lý]</text>

  <!-- Task 7 -> Task 8 -->
  <line x1="1220" y1="560" x2="1220" y2="230" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Task 8 -> G8 -> End -->
  <line x1="1270" y1="210" x2="1285" y2="210" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="1315" y1="210" x2="1329" y2="210" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- MESSAGE FLOW: Báo cáo phản hồi cho M3 Pool -->
  <path d="M 1220 185 L 1220 130" fill="none" stroke="#3182ce" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#msgArrow)"/>
  <text x="1230" y="145" font-size="9" font-style="italic" fill="#3182ce">Message: Báo cáo tỷ lệ hao hụt phản hồi M3</text>

  <!-- Caption -->
  <text x="700" y="820" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 4.2: Sơ đồ BPMN 2.0 quy trình Kiểm kê và Xử lý chênh lệch tồn kho (S2) tại ACFC.</text>
</svg>'''
    with open("diagrams/bpmn-kiem-ke-ton-kho-s2.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 3. S3: ACCOUNT ACTIVATION BPMN (>=8 Gateways)
# -------------------------------------------------------------
def generate_bpmn_s3():
    svg = '''<svg width="1350" height="750" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <filter id="taskShadow2" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="1350" height="750" fill="#ffffff"/>
  <text x="30" y="35" font-size="18" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0: ĐĂNG KÝ, XÁC THỰC OTP &amp; KÍCH HOẠT TÀI KHOẢN MEMBER (S3)</text>
  <text x="30" y="55" font-size="12" fill="#718096">Chủ thể: Cổng Thành viên Số ACFC | Đáp ứng chuẩn 8 Gateways | Phân luồng OTP &amp; CSKH</text>

  <!-- Pool 1: Khách hàng (Customer) -->
  <rect x="30" y="80" width="1290" height="150" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="30" y="80" width="30" height="150" fill="#319795"/>
  <text x="45" y="155" font-size="12" font-weight="bold" fill="#ffffff" transform="rotate(-90 45 155)" text-anchor="middle">KHÁCH HÀNG (CUSTOMER)</text>

  <!-- Pool 2: ACFC Platform -->
  <rect x="30" y="250" width="1290" height="450" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="30" y="250" width="30" height="450" fill="#2d3748"/>
  <text x="45" y="475" font-size="12" font-weight="bold" fill="#ffffff" transform="rotate(-90 45 475)" text-anchor="middle">HỆ THỐNG ACFC PLATFORM</text>

  <!-- Lanes in Pool 2 -->
  <!-- Lane 1: Web / App Frontend -->
  <line x1="60" y1="360" x2="1320" y2="360" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="60" y="250" width="25" height="110" fill="#edf2f7"/>
  <text x="73" y="305" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 305)" text-anchor="middle">Frontend UI</text>

  <!-- Lane 2: Backend Core & DB -->
  <line x1="60" y1="480" x2="1320" y2="480" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="60" y="360" width="25" height="120" fill="#edf2f7"/>
  <text x="73" y="420" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 420)" text-anchor="middle">Backend Core</text>

  <!-- Lane 3: SMS / ZNS OTP Gateway -->
  <line x1="60" y1="590" x2="1320" y2="590" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="60" y="480" width="25" height="110" fill="#edf2f7"/>
  <text x="73" y="535" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 535)" text-anchor="middle">SMS Gateway</text>

  <!-- Lane 4: CSKH Support -->
  <rect x="60" y="590" width="25" height="110" fill="#edf2f7"/>
  <text x="73" y="645" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 645)" text-anchor="middle">CSKH 1900</text>

  <!-- ELEMENTS -->
  <!-- Start Event -->
  <circle cx="110" cy="155" r="16" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="110" y="190" font-size="9" fill="#22543d" text-anchor="middle">Truy cập Web/App</text>

  <!-- G1: Đã có nick hay Đăng ký mới? -->
  <polygon points="170,155 190,135 210,155 190,175" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="190" y="159" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="190" y="125" font-size="8" fill="#744210" text-anchor="middle">G1: Có nick?</text>

  <!-- Task 1: Nhập SĐT -->
  <rect x="235" y="130" width="95" height="50" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="282" y="152" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Nhập SĐT</text>
  <text x="282" y="166" font-size="9" fill="#2d3748" text-anchor="middle">&amp; Bấm gửi OTP</text>

  <!-- G2: SĐT đã tồn tại? (Backend) -->
  <polygon points="360,420 380,400 400,420 380,440" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="380" y="424" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="380" y="455" font-size="8" fill="#744210" text-anchor="middle">G2: SĐT tồn tại?</text>

  <!-- Task 2: Sinh mã & gửi SMS OTP (SMS Gateway) -->
  <rect x="425" y="515" width="105" height="45" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="477" y="533" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Sinh mã ngẫu nhiên</text>
  <text x="477" y="547" font-size="9" fill="#2d3748" text-anchor="middle">&amp; Gửi SMS OTP</text>

  <!-- G3: Nhận OTP trong 120s? (Customer) -->
  <polygon points="560,155 580,135 600,155 580,175" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="580" y="159" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="580" y="125" font-size="8" fill="#744210" text-anchor="middle">G3: Nhận trong 120s?</text>

  <!-- Task 3: Nhập mã OTP (Customer) -->
  <rect x="630" y="130" width="90" height="50" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="675" y="152" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Nhập mã OTP</text>
  <text x="675" y="166" font-size="9" fill="#2d3748" text-anchor="middle">vào màn hình</text>

  <!-- G4: OTP chính xác? (Backend) -->
  <polygon points="655,420 675,400 695,420 675,440" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="675" y="424" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="675" y="455" font-size="8" fill="#744210" text-anchor="middle">G4: OTP đúng?</text>

  <!-- G5: Sai quá 3 lần? (Backend) -->
  <polygon points="730,420 750,400 770,420 750,440" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="750" y="424" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="750" y="455" font-size="8" fill="#744210" text-anchor="middle">G5: Sai &gt;= 3 lần?</text>

  <!-- Task 4: Điền thông tin & Mật khẩu (Customer) -->
  <rect x="790" y="130" width="110" height="50" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="845" y="152" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Điền thông tin</text>
  <text x="845" y="166" font-size="9" fill="#2d3748" text-anchor="middle">&amp; Tạo mật khẩu</text>

  <!-- G6: Mật khẩu đạt chuẩn? (Frontend) -->
  <polygon points="930,305 950,285 970,305 950,325" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="950" y="309" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="950" y="340" font-size="8" fill="#744210" text-anchor="middle">G6: Mật khẩu chuẩn?</text>

  <!-- G7: Đồng ý điều khoản? (Frontend) -->
  <polygon points="1010,305 1030,285 1050,305 1030,325" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1030" y="309" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1030" y="340" font-size="8" fill="#744210" text-anchor="middle">G7: Đồng ý luật?</text>

  <!-- Task 5: Tạo User & Cấp ID Member (Backend) -->
  <rect x="1070" y="395" width="105" height="50" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="1122" y="416" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Tạo bản ghi User</text>
  <text x="1122" y="430" font-size="9" fill="#2d3748" text-anchor="middle">&amp; Cấp ID Member</text>

  <!-- Task 6: Tự động đăng nhập & hiển thị Voucher (Frontend) -->
  <rect x="1070" y="280" width="105" height="50" rx="6" fill="#ffffff" stroke="#38a169" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="1122" y="301" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Auto-Login &amp;</text>
  <text x="1122" y="315" font-size="9" fill="#22543d" text-anchor="middle">Tặng Voucher 100k</text>

  <!-- G8: XOR-Join Hoàn tất -->
  <polygon points="1210,305 1225,290 1240,305 1225,320" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1225" y="309" font-size="9" font-weight="bold" fill="#744210" text-anchor="middle">X</text>

  <!-- Task 7: CSKH xử lý ngoại lệ (CSKH Lane) -->
  <rect x="790" y="625" width="100" height="45" rx="6" fill="#ffffff" stroke="#e53e3e" stroke-width="1.5"/>
  <text x="840" y="643" font-size="9" font-weight="bold" fill="#742a2a" text-anchor="middle">CSKH 1900 3038</text>
  <text x="840" y="657" font-size="9" fill="#742a2a" text-anchor="middle">xác minh mở khóa</text>

  <!-- End Event -->
  <circle cx="1285" cy="305" r="16" fill="#c6f6d5" stroke="#22543d" stroke-width="3"/>
  <text x="1285" y="335" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Kích hoạt xong</text>

  <!-- FLOWS -->
  <line x1="126" y1="155" x2="170" y2="155" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="210" y1="155" x2="235" y2="155" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <path d="M 282 180 L 282 420 L 360 420" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- G2 [Chưa có] -> SMS Gateway -->
  <path d="M 400 420 L 415 420 L 415 537 L 425 537" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <!-- SMS -> G3 -->
  <path d="M 530 537 L 545 537 L 545 155 L 560 155" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- G3 [Nhận được] -> Task 3 -->
  <line x1="600" y1="155" x2="630" y2="155" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <!-- G3 [Hết hạn] -> SMS Task -->
  <path d="M 580 175 L 580 550 L 530 550" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- Task 3 -> G4 -->
  <path d="M 675 180 L 675 400" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- G4 [Đúng] -> Task 4 -->
  <path d="M 695 420 L 715 420 L 715 155 L 790 155" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- G4 [Sai] -> G5 -->
  <line x1="695" y1="420" x2="730" y2="420" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- G5 [Sai >=3] -> CSKH -->
  <path d="M 750 440 L 750 647 L 790 647" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- Task 4 -> G6 -->
  <path d="M 845 180 L 845 305 L 930 305" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- G6 [Đạt] -> G7 -->
  <line x1="970" y1="305" x2="1010" y2="305" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- G7 [Đồng ý] -> Task 5 -->
  <path d="M 1050 305 L 1060 305 L 1060 420 L 1070 420" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- Task 5 -> Task 6 -->
  <line x1="1122" y1="395" x2="1122" y2="330" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- Task 6 -> G8 -> End -->
  <line x1="1175" y1="305" x2="1210" y2="305" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="1240" y1="305" x2="1269" y2="305" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <!-- CSKH -> G8 -->
  <path d="M 890 647 L 1225 647 L 1225 320" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <text x="675" y="725" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 5.2: Sơ đồ BPMN 2.0 quy trình Đăng ký, Xác thực OTP và Kích hoạt tài khoản Member (S3) tại ACFC.</text>
</svg>'''
    with open("diagrams/bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 4. S1: RECRUITMENT BPMN (>=8 Gateways)
# -------------------------------------------------------------
def generate_bpmn_s1():
    svg = '''<svg width="1400" height="800" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <filter id="taskShadow3" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="1400" height="800" fill="#ffffff"/>
  <text x="30" y="35" font-size="18" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0: QUY TRÌNH TUYỂN DỤNG &amp; TIẾP NHẬN NHÂN SỰ (S1)</text>
  <text x="30" y="55" font-size="12" fill="#718096">Chủ thể: Khối Bán lẻ Thời trang &amp; Tổng kho ACFC | Độ phức tạp: 8 Cổng điều kiện (Gateways)</text>

  <!-- Pool 1: Ứng viên (Candidate) -->
  <rect x="30" y="80" width="1340" height="130" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="30" y="80" width="30" height="130" fill="#805ad5"/>
  <text x="45" y="145" font-size="12" font-weight="bold" fill="#ffffff" transform="rotate(-90 45 145)" text-anchor="middle">ỨNG VIÊN (CANDIDATE)</text>

  <!-- Pool 2: ACFC Internal Organization -->
  <rect x="30" y="230" width="1340" height="520" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="30" y="230" width="30" height="520" fill="#2d3748"/>
  <text x="45" y="490" font-size="12" font-weight="bold" fill="#ffffff" transform="rotate(-90 45 490)" text-anchor="middle">ACFC – QUY TRÌNH TUYỂN DỤNG NỘI BỘ (S1)</text>

  <!-- Lanes -->
  <!-- Lane 1: Bộ phận Vận hành yêu cầu (Store/Warehouse Manager) -->
  <line x1="60" y1="360" x2="1370" y2="360" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="60" y="230" width="25" height="130" fill="#edf2f7"/>
  <text x="73" y="295" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 295)" text-anchor="middle">Store / Kho Ops</text>

  <!-- Lane 2: Chuyên viên Tuyển dụng (HR Talent Acquisition) -->
  <line x1="60" y1="500" x2="1370" y2="500" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="60" y="360" width="25" height="140" fill="#edf2f7"/>
  <text x="73" y="430" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 430)" text-anchor="middle">HR Tuyển dụng</text>

  <!-- Lane 3: Ban Giám đốc Khối &amp; HRD -->
  <line x1="60" y1="630" x2="1370" y2="630" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="60" y="500" width="25" height="130" fill="#edf2f7"/>
  <text x="73" y="565" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 565)" text-anchor="middle">HRD / Giám đốc</text>

  <!-- Lane 4: IT &amp; Hành chính Onboarding -->
  <rect x="60" y="630" width="25" height="120" fill="#edf2f7"/>
  <text x="73" y="690" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 690)" text-anchor="middle">IT &amp; Admin</text>

  <!-- ELEMENTS -->
  <!-- Start Event -->
  <circle cx="110" cy="295" r="16" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="110" y="325" font-size="9" fill="#22543d" text-anchor="middle">Phát sinh vị trí</text>

  <!-- Task 1: Lập phiếu yêu cầu tuyển dụng (Lane 1) -->
  <rect x="150" y="270" width="105" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="202" y="291" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Lập phiếu yêu cầu</text>
  <text x="202" y="305" font-size="9" fill="#2d3748" text-anchor="middle">tuyển dụng &amp; JD</text>

  <!-- G1: Duyệt định biên? (Lane 3) -->
  <polygon points="275,565 295,545 315,565 295,585" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="295" y="569" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="295" y="600" font-size="8" fill="#744210" text-anchor="middle">G1: Duyệt định biên?</text>

  <!-- Task 2: Đăng tin tuyển dụng (Lane 2) -->
  <rect x="335" y="405" width="100" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="385" y="426" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Đăng tin tuyển dụng</text>
  <text x="385" y="440" font-size="9" fill="#2d3748" text-anchor="middle">Website/TopCV</text>

  <!-- Task 3: Ứng viên nộp CV (Candidate Pool) -->
  <rect x="335" y="120" width="100" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="385" y="141" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Nộp hồ sơ</text>
  <text x="385" y="155" font-size="9" fill="#2d3748" text-anchor="middle">ứng tuyển trực tuyến</text>

  <!-- G2: CV đạt chuẩn cứng? (Lane 2) -->
  <polygon points="460,430 480,410 500,430 480,450" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="480" y="434" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="480" y="465" font-size="8" fill="#744210" text-anchor="middle">G2: CV đạt?</text>

  <!-- G3: Phone Screening đạt? (Lane 2) -->
  <polygon points="530,430 550,410 570,430 550,450" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="550" y="434" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="550" y="465" font-size="8" fill="#744210" text-anchor="middle">G3: Sơ vấn đạt?</text>

  <!-- Task 4: Phỏng vấn V1 chuyên môn (Lane 1) -->
  <rect x="600" y="270" width="105" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="652" y="291" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Phỏng vấn V1</text>
  <text x="652" y="305" font-size="9" fill="#2d3748" text-anchor="middle">chuyên môn &amp; thái độ</text>

  <!-- G4: Vòng 1 Đạt? (Lane 1) -->
  <polygon points="730,295 750,275 770,295 750,315" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="750" y="299" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="750" y="330" font-size="8" fill="#744210" text-anchor="middle">G4: V1 Đạt?</text>

  <!-- Task 5: Làm bài Test nghiệp vụ (Candidate) -->
  <rect x="700" y="120" width="100" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="750" y="141" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Làm bài test</text>
  <text x="750" y="155" font-size="9" fill="#2d3748" text-anchor="middle">tính toán/nghiệp vụ</text>

  <!-- G5: Test >= 70đ? (Lane 2) -->
  <polygon points="820,430 840,410 860,430 840,450" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="840" y="434" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="840" y="465" font-size="8" fill="#744210" text-anchor="middle">G5: Test &gt;= 70đ?</text>

  <!-- G6: Vòng 2 Giám đốc Duyệt? (Lane 3) -->
  <polygon points="900,565 920,545 940,565 920,585" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="920" y="569" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="920" y="600" font-size="8" fill="#744210" text-anchor="middle">G6: V2 Duyệt?</text>

  <!-- Task 6: Gửi Thư mời nhận việc Offer (Lane 2) -->
  <rect x="970" y="405" width="105" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="1022" y="426" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Gửi Offer Letter</text>
  <text x="1022" y="440" font-size="9" fill="#2d3748" text-anchor="middle">&amp; Đãi ngộ</text>

  <!-- G7: Ứng viên chấp nhận Offer? (Candidate) -->
  <polygon points="1080,145 1100,125 1120,145 1100,165" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1100" y="149" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1100" y="115" font-size="8" fill="#744210" text-anchor="middle">G7: Nhận Offer?</text>

  <!-- G8: Duyệt đàm phán lương? (Lane 3) -->
  <polygon points="1080,565 1100,545 1120,565 1100,585" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1100" y="569" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1100" y="600" font-size="8" fill="#744210" text-anchor="middle">G8: Duyệt lương?</text>

  <!-- Task 7: Ký HĐ & Cấp phát tài khoản Onboarding (Lane 4) -->
  <rect x="1150" y="665" width="110" height="50" rx="6" fill="#ffffff" stroke="#38a169" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="1205" y="686" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Ký Hợp đồng thử việc</text>
  <text x="1205" y="700" font-size="9" fill="#22543d" text-anchor="middle">&amp; Cấp phát thiết bị</text>

  <!-- End Event -->
  <circle cx="1310" cy="690" r="16" fill="#c6f6d5" stroke="#22543d" stroke-width="3"/>
  <text x="1310" y="720" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Onboarding</text>

  <!-- FLOWS -->
  <line x1="126" y1="295" x2="150" y2="295" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <path d="M 202 320 L 202 565 L 275 565" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- G1 [Yes] -> Task 2 -->
  <path d="M 315 565 L 385 565 L 385 455" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <!-- Task 2 -> Task 3 -->
  <line x1="385" y1="405" x2="385" y2="170" stroke="#2d3748" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow3)"/>

  <!-- Task 3 -> G2 -->
  <path d="M 435 145 L 480 145 L 480 410" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- G2 -> G3 -->
  <line x1="500" y1="430" x2="530" y2="430" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- G3 [Đạt] -> Task 4 -->
  <path d="M 570 430 L 652 430 L 652 320" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- Task 4 -> G4 -->
  <line x1="705" y1="295" x2="730" y2="295" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- G4 [Đạt] -> Task 5 (Test) -->
  <path d="M 750 275 L 750 170" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- Task 5 -> G5 -->
  <path d="M 800 145 L 840 145 L 840 410" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- G5 [Đạt] -> G6 -->
  <path d="M 860 430 L 920 430 L 920 545" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- G6 [Duyệt] -> Task 6 (Offer) -->
  <path d="M 940 565 L 1022 565 L 1022 455" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- Task 6 -> G7 (Candidate) -->
  <path d="M 1075 430 L 1100 430 L 1100 165" fill="none" stroke="#2d3748" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow3)"/>

  <!-- G7 [Nhận] -> Task 7 -->
  <path d="M 1120 145 L 1205 145 L 1205 665" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- G7 [Đàm phán] -> G8 -->
  <path d="M 1100 165 L 1100 545" fill="none" stroke="#d69e2e" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- G8 [Duyệt lương] -> Task 6 -->
  <path d="M 1080 565 L 1040 565 L 1040 455" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <!-- Task 7 -> End -->
  <line x1="1260" y1="690" x2="1294" y2="690" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <text x="700" y="775" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 6.2: Sơ đồ BPMN 2.0 quy trình Tuyển dụng và Tiếp nhận nhân sự tại ACFC.</text>
</svg>'''
    with open("diagrams/bpmn-tuyen-dung-nhan-su-s1.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 5. C1/C2: WAREHOUSE INBOUND & OUTBOUND BPMN (>=8 Gateways)
# -------------------------------------------------------------
def generate_bpmn_c1_c2():
    svg = '''<svg width="1400" height="850" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <filter id="taskShadow4" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="1400" height="850" fill="#ffffff"/>
  <text x="30" y="35" font-size="18" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0: QUY TRÌNH NHẬP KHO TRUNG TÂM &amp; XUẤT KHO BỔ SUNG CỬA HÀNG (C1/C2)</text>
  <text x="30" y="55" font-size="12" fill="#718096">Chủ thể: Tổng kho Phân phối ACFC &amp; Chuỗi Điểm bán Bán lẻ | Độ phức tạp: 8 Cổng điều kiện (Gateways)</text>

  <!-- Pool 1: 3PL & Forwarder -->
  <rect x="30" y="80" width="1340" height="110" fill="#fefcbf" stroke="#d69e2e" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="50" y="110" font-size="12" font-weight="bold" fill="#744210">POOL NGOÀI: ĐƠN VỊ VẬN TẢI QUỐC TẾ &amp; 3PL NỘI ĐỊA (LOGISTICS SERVICE PROVIDERS)</text>

  <!-- Pool 2: ACFC Warehouse Operations -->
  <rect x="30" y="210" width="1340" height="600" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="30" y="210" width="30" height="600" fill="#d69e2e"/>
  <text x="48" y="510" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 48 510)" text-anchor="middle">ACFC – QUY TRÌNH VẬN HÀNH KHO &amp; ĐIỀU PHỐI (C1/C2)</text>

  <!-- Lanes -->
  <!-- Lane 1: Logistics & Thông quan -->
  <line x1="60" y1="340" x2="1370" y2="340" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="60" y="210" width="25" height="130" fill="#edf2f7"/>
  <text x="73" y="275" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 275)" text-anchor="middle">Logistics &amp; HQ</text>

  <!-- Lane 2: Nhận hàng & QC Nhập kho (Inbound) -->
  <line x1="60" y1="480" x2="1370" y2="480" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="60" y="340" width="25" height="140" fill="#edf2f7"/>
  <text x="73" y="410" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 410)" text-anchor="middle">Inbound &amp; QC</text>

  <!-- Lane 3: Quản lý vị trí & Lưu kho WMS -->
  <line x1="60" y1="620" x2="1370" y2="620" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="60" y="480" width="25" height="140" fill="#edf2f7"/>
  <text x="73" y="550" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 550)" text-anchor="middle">WMS &amp; Storage</text>

  <!-- Lane 4: Lấy hàng, Đóng gói & Xuất kho (Outbound) -->
  <rect x="60" y="620" width="25" height="190" fill="#edf2f7"/>
  <text x="73" y="715" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 73 715)" text-anchor="middle">Outbound Ops</text>

  <!-- ELEMENTS -->
  <!-- Start Event: Container về cảng/kho -->
  <circle cx="110" cy="275" r="16" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="110" y="305" font-size="9" fill="#22543d" text-anchor="middle">Lô hàng về cảng</text>

  <!-- Task 1: Tiếp nhận B/L & Khai báo HQ (Lane 1) -->
  <rect x="150" y="250" width="105" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow4)"/>
  <text x="202" y="271" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Tiếp nhận B/L &amp;</text>
  <text x="202" y="285" font-size="9" fill="#2d3748" text-anchor="middle">Khai báo Hải quan</text>

  <!-- G1: Thông quan hợp lệ? (Lane 1) -->
  <polygon points="280,275 300,255 320,275 300,295" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="300" y="279" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="300" y="310" font-size="8" fill="#744210" text-anchor="middle">G1: Thông quan?</text>

  <!-- Task 2: Tiếp nhận container & Kiểm tra seal (Lane 2) -->
  <rect x="340" y="385" width="105" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow4)"/>
  <text x="392" y="406" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Tiếp nhận xe &amp;</text>
  <text x="392" y="420" font-size="9" fill="#2d3748" text-anchor="middle">Kiểm tra seal chì</text>

  <!-- G2: Seal nguyên vẹn? (Lane 2) -->
  <polygon points="470,410 490,390 510,410 490,430" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="490" y="414" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="490" y="445" font-size="8" fill="#744210" text-anchor="middle">G2: Seal nguyên?</text>

  <!-- Task 3: Dỡ hàng & Quét mã kiểm tra số lượng/SKU (Lane 2) -->
  <rect x="530" y="385" width="110" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow4)"/>
  <text x="585" y="406" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Dỡ hàng &amp; Quét</text>
  <text x="585" y="420" font-size="9" fill="#2d3748" text-anchor="middle">Barcode/RFID</text>

  <!-- G3: Khớp Packing List? (Lane 2) -->
  <polygon points="665,410 685,390 705,410 685,430" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="685" y="414" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="685" y="445" font-size="8" fill="#744210" text-anchor="middle">G3: Khớp List?</text>

  <!-- Task 4: Nhập kho & Phân bổ vị trí Putaway (Lane 3) -->
  <rect x="730" y="525" width="110" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow4)"/>
  <text x="785" y="546" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Ghi nhận nhập WMS</text>
  <text x="785" y="560" font-size="9" fill="#2d3748" text-anchor="middle">&amp; Xếp hàng lên kệ</text>

  <!-- G4: Nhận lệnh phân bổ M3 hay Bổ sung Store? (Lane 4) -->
  <polygon points="870,715 890,695 910,715 890,735" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="890" y="719" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="890" y="750" font-size="8" fill="#744210" text-anchor="middle">G4: Lệnh xuất?</text>

  <!-- Task 5: Tạo Pick List & Lấy hàng theo lộ trình (Lane 4) -->
  <rect x="940" y="690" width="105" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow4)"/>
  <text x="992" y="711" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Lấy hàng (Picking)</text>
  <text x="992" y="725" font-size="9" fill="#2d3748" text-anchor="middle">theo chỉ dẫn WMS</text>

  <!-- G5: Đủ số lượng & đúng SKU? (Lane 4) -->
  <polygon points="1070,715 1090,695 1110,715 1090,735" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1090" y="719" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1090" y="750" font-size="8" fill="#744210" text-anchor="middle">G5: Đủ hàng?</text>

  <!-- Task 6: Đóng gói, dán niêm phong & In nhãn (Lane 4) -->
  <rect x="1135" y="690" width="105" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow4)"/>
  <text x="1187" y="711" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Đóng thùng carton</text>
  <text x="1187" y="725" font-size="9" fill="#2d3748" text-anchor="middle">&amp; Dán nhãn Shipping</text>

  <!-- G6: Kênh giao: Nội thành hay Liên tỉnh? (Lane 4) -->
  <polygon points="1265,715 1285,695 1305,715 1285,735" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1285" y="719" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1285" y="750" font-size="8" fill="#744210" text-anchor="middle">G6: Phương thức 3PL?</text>

  <!-- End Event: Xuất kho thành công bàn giao 3PL -->
  <circle cx="1340" cy="715" r="16" fill="#c6f6d5" stroke="#22543d" stroke-width="3"/>
  <text x="1340" y="745" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Xuất hàng</text>

  <!-- FLOWS -->
  <line x1="126" y1="275" x2="150" y2="275" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow4)"/>
  <line x1="255" y1="275" x2="280" y2="275" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- G1 [Duyệt] -> Task 2 -->
  <path d="M 320 275 L 392 275 L 392 385" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow4)"/>
  <text x="330" y="265" font-size="9" fill="#38a169">[Thông quan]</text>

  <!-- Task 2 -> G2 -->
  <line x1="445" y1="410" x2="470" y2="410" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- G2 [Nguyên] -> Task 3 -->
  <line x1="510" y1="410" x2="530" y2="410" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- Task 3 -> G3 -->
  <line x1="640" y1="410" x2="665" y2="410" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- G3 [Khớp] -> Task 4 -->
  <path d="M 705 410 L 785 410 L 785 525" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- Task 4 -> G4 -->
  <path d="M 785 575 L 785 715 L 870 715" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- G4 -> Task 5 -->
  <line x1="910" y1="715" x2="940" y2="715" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- Task 5 -> G5 -->
  <line x1="1045" y1="715" x2="1070" y2="715" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- G5 [Đủ] -> Task 6 -->
  <line x1="1110" y1="715" x2="1135" y2="715" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- Task 6 -> G6 -> End -->
  <line x1="1240" y1="715" x2="1265" y2="715" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow4)"/>
  <line x1="1305" y1="715" x2="1324" y2="715" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <text x="700" y="825" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 4.3: Sơ đồ BPMN 2.0 quy trình Nhập kho trung tâm &amp; Xuất kho bổ sung cửa hàng (C1/C2) tại ACFC.</text>
</svg>'''
    with open("diagrams/bpmn-nhap-xuat-kho-c1-c2.svg", "w", encoding="utf-8") as f:
        f.write(svg)

print("All BPMN SVGs and Draw.io XML files regenerated cleanly for ACFC.")
generate_architecture()
generate_bpmn_s2()
generate_bpmn_s3()
generate_bpmn_s1()
generate_bpmn_c1_c2()
