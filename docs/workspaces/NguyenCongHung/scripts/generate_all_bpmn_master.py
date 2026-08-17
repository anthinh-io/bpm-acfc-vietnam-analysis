#!/usr/bin/env python3
"""
Master BPMN Generator for ACFC (Công ty Cổ phần Thời trang và Mỹ phẩm Âu Châu).
Generates comprehensive, non-overlapping, high-resolution BPMN 2.0 SVGs and Draw.io XML files:
1. Sơ đồ Kiến trúc Quy trình Tổng thể ACFC (10 quy trình, 3 cấp)
2. Sơ đồ TỔNG HỢP Vận hành Kho, Nhập xuất, Kiểm kê & Reverse Logistics ACFC (C1, C2, S2, C4, M3) (17 Gateways)
3. Sơ đồ Đăng ký, Xác thực OTP & Kích hoạt Tài khoản ACFC Member (S3) (8 Gateways)
4. Sơ đồ Tuyển dụng & Onboarding Nhân sự Chuỗi Bán lẻ & Kho vận (S1) (8 Gateways)
5. Sơ đồ Hoạch định Hàng hóa & Phân bổ theo mùa (M3) (8 Gateways)
6. Sơ đồ Bán hàng Đa kênh & Thanh toán POS / E-Commerce (C3) (8 Gateways)
7. Sơ đồ Đổi trả, Bảo hành & Hoàn tiền (C4) (8 Gateways)
"""

import os

# Script sống trong workspace cá nhân nhưng ghi sơ đồ vào diagrams/ ở repo root.
# Neo CWD về repo root (4 cấp trên: scripts → NguyenCongHung → workspaces → docs → root)
# để chạy được từ bất kỳ thư mục nào.
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")))

os.makedirs("diagrams", exist_ok=True)

# ----------------------------------------------------------------------
# 1. PROCESS ARCHITECTURE DIAGRAM
# ----------------------------------------------------------------------
def generate_architecture():
    svg = '''<svg width="1200" height="750" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
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

  <rect width="1200" height="750" fill="#ffffff" rx="10"/>
  <rect x="15" y="15" width="1170" height="720" fill="none" stroke="#cbd5e0" stroke-width="2" rx="8"/>

  <text x="40" y="45" font-size="20" font-weight="bold" fill="#1a202c">SƠ ĐỒ KIẾN TRÚC QUY TRÌNH TỔNG THỂ DOANH NGHIỆP ACFC</text>
  <text x="40" y="68" font-size="13" fill="#718096">Khung chuẩn APQC / Value Chain Framework | Phân bổ 10 quy trình nghiệp vụ theo 3 cấp độ BPM</text>

  <!-- 1. MANAGEMENT PROCESSES -->
  <rect x="40" y="90" width="1120" height="170" rx="8" fill="#f7fafc" stroke="#3182ce" stroke-width="2"/>
  <rect x="40" y="90" width="35" height="170" fill="#3182ce" rx="8"/>
  <text x="58" y="175" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 58 175)" text-anchor="middle">QUẢN LÝ (MANAGEMENT)</text>

  <!-- M1 Box -->
  <rect x="95" y="110" width="320" height="130" rx="6" fill="url(#mGrad)" stroke="#3182ce" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="95" y="110" width="320" height="32" rx="6" fill="#3182ce"/>
  <text x="255" y="132" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">M1: CHIẾN LƯỢC &amp; MẠNG LƯỚI KÊNH</text>
  <text x="110" y="165" font-size="11" fill="#2d3748">• Nghiên cứu thị trường thời trang bán lẻ</text>
  <text x="110" y="188" font-size="11" fill="#2d3748">• Thẩm định địa điểm mở Store mới tại TTTM</text>
  <text x="110" y="211" font-size="11" fill="#2d3748">• Duyệt kế hoạch mở rộng điểm bán năm</text>

  <!-- M2 Box -->
  <rect x="445" y="110" width="320" height="130" rx="6" fill="url(#mGrad)" stroke="#3182ce" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="445" y="110" width="320" height="32" rx="6" fill="#3182ce"/>
  <text x="605" y="132" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">M2: KẾ HOẠCH TÀI CHÍNH &amp; OTB</text>
  <text x="460" y="165" font-size="11" fill="#2d3748">• Dự toán hạn mức mua Open-to-Buy</text>
  <text x="460" y="188" font-size="11" fill="#2d3748">• Kiểm soát dòng tiền &amp; chi phí thương mại</text>
  <text x="460" y="211" font-size="11" fill="#2d3748">• Đối soát tài chính doanh thu đa kênh</text>

  <!-- M3 Box -->
  <rect x="795" y="110" width="345" height="130" rx="6" fill="url(#mGrad)" stroke="#3182ce" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="795" y="110" width="345" height="32" rx="6" fill="#3182ce"/>
  <text x="967" y="132" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">M3: HOẠCH ĐỊNH &amp; PHÂN BỔ HÀNG HÓA</text>
  <text x="810" y="165" font-size="11" fill="#2d3748">• Dự báo nhu cầu bán lẻ &amp; Weeks of Supply</text>
  <text x="810" y="188" font-size="11" fill="#2d3748">• Cơ cấu danh mục SKU Hero/Core theo mùa</text>
  <text x="810" y="211" font-size="11" fill="#2d3748">• Lập kế hoạch phân bổ cho chuỗi 100+ Store</text>

  <!-- 2. CORE PROCESSES -->
  <rect x="40" y="280" width="1120" height="200" rx="8" fill="#fffff0" stroke="#d69e2e" stroke-width="2"/>
  <rect x="40" y="280" width="35" height="200" fill="#d69e2e" rx="8"/>
  <text x="58" y="380" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 58 380)" text-anchor="middle">CỐT LÕI (CORE VALUE CHAIN)</text>

  <!-- C1 Box -->
  <rect x="95" y="305" width="240" height="150" rx="6" fill="url(#cGrad)" stroke="#d69e2e" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="95" y="305" width="240" height="30" rx="6" fill="#d69e2e"/>
  <text x="215" y="325" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C1: NHẬP KHẨU &amp; TỔNG KHO</text>
  <text x="105" y="355" font-size="11" fill="#744210">• Tiếp nhận B/L, Commercial Invoice</text>
  <text x="105" y="378" font-size="11" fill="#744210">• Khai báo VNACCS &amp; Thông quan</text>
  <text x="105" y="401" font-size="11" fill="#744210">• Dỡ hàng, quét Barcode/RFID</text>
  <text x="105" y="424" font-size="11" fill="#744210">• Nhập kho WMS &amp; lưu giá kệ Putaway</text>

  <!-- Arrow C1 -> C2 -->
  <line x1="335" y1="380" x2="365" y2="380" stroke="#d69e2e" stroke-width="3"/>
  <polygon points="365,375 375,380 365,385" fill="#d69e2e"/>

  <!-- C2 Box -->
  <rect x="375" y="305" width="240" height="150" rx="6" fill="url(#cGrad)" stroke="#d69e2e" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="375" y="305" width="240" height="30" rx="6" fill="#d69e2e"/>
  <text x="495" y="325" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C2: XUẤT KHO &amp; BỔ SUNG STORE</text>
  <text x="385" y="355" font-size="11" fill="#744210">• Nhận lệnh phân bổ từ M3/Store</text>
  <text x="385" y="378" font-size="11" fill="#744210">• Lấy hàng Picking theo chỉ dẫn WMS</text>
  <text x="385" y="401" font-size="11" fill="#744210">• Đóng gói, dán nhãn Shipping Label</text>
  <text x="385" y="424" font-size="11" fill="#744210">• 3PL vận chuyển &amp; giao Store e-POD</text>

  <!-- Arrow C2 -> C3 -->
  <line x1="615" y1="380" x2="645" y2="380" stroke="#d69e2e" stroke-width="3"/>
  <polygon points="645,375 655,380 645,385" fill="#d69e2e"/>

  <!-- C3 Box -->
  <rect x="655" y="305" width="240" height="150" rx="6" fill="url(#cGrad)" stroke="#d69e2e" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="655" y="305" width="240" height="30" rx="6" fill="#d69e2e"/>
  <text x="775" y="325" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C3: BÁN HÀNG ĐA KÊNH (OMNI)</text>
  <text x="665" y="355" font-size="11" fill="#744210">• Bán tại Store / Web / App ACFC</text>
  <text x="665" y="378" font-size="11" fill="#744210">• Quét mã Member &amp; Áp mã giảm giá</text>
  <text x="665" y="401" font-size="11" fill="#744210">• Thanh toán POS / Thẻ / Ví / Payoo</text>
  <text x="665" y="424" font-size="11" fill="#744210">• Xuất hóa đơn e-Invoice &amp; trừ tồn</text>

  <!-- Arrow C3 -> C4 -->
  <line x1="895" y1="380" x2="925" y2="380" stroke="#d69e2e" stroke-width="3"/>
  <polygon points="925,375 935,380 925,385" fill="#d69e2e"/>

  <!-- C4 Box -->
  <rect x="935" y="305" width="205" height="150" rx="6" fill="url(#cGrad)" stroke="#d69e2e" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="935" y="305" width="205" height="30" rx="6" fill="#d69e2e"/>
  <text x="1037" y="325" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C4: ĐỔI TRẢ &amp; HOÀN TIỀN</text>
  <text x="945" y="355" font-size="11" fill="#744210">• Tiếp nhận yêu cầu đổi trả</text>
  <text x="945" y="378" font-size="11" fill="#744210">• Giám định chất lượng SP</text>
  <text x="945" y="401" font-size="11" fill="#744210">• Đổi size / Hoàn tiền</text>
  <text x="945" y="424" font-size="11" fill="#744210">• Hoàn nhập kho Reverse</text>

  <!-- 3. SUPPORT PROCESSES -->
  <rect x="40" y="500" width="1120" height="170" rx="8" fill="#f7fafc" stroke="#4a5568" stroke-width="2"/>
  <rect x="40" y="500" width="35" height="170" fill="#4a5568" rx="8"/>
  <text x="58" y="585" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 58 585)" text-anchor="middle">HỖ TRỢ (SUPPORT)</text>

  <!-- S1 Box -->
  <rect x="95" y="520" width="320" height="130" rx="6" fill="url(#sGrad)" stroke="#4a5568" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="95" y="520" width="320" height="32" rx="6" fill="#4a5568"/>
  <text x="255" y="542" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">S1: TUYỂN DỤNG &amp; ONBOARDING</text>
  <text x="110" y="575" font-size="11" fill="#2d3748">• Thu hút hồ sơ &amp; Sàng lọc CV qua ATS</text>
  <text x="110" y="598" font-size="11" fill="#2d3748">• Phỏng vấn V1, V2 &amp; Test năng lực</text>
  <text x="110" y="621" font-size="11" fill="#2d3748">• Gửi e-Offer &amp; Ký HĐ Onboarding</text>

  <!-- S2 Box -->
  <rect x="445" y="520" width="320" height="130" rx="6" fill="url(#sGrad)" stroke="#4a5568" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="445" y="520" width="320" height="32" rx="6" fill="#4a5568"/>
  <text x="605" y="542" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">S2: KIỂM KÊ &amp; XỬ LÝ CHÊNH LỆCH</text>
  <text x="460" y="575" font-size="11" fill="#2d3748">• Quét mã kiểm đếm thực tế Store/Kho</text>
  <text x="460" y="598" font-size="11" fill="#2d3748">• Tự động đối chiếu số dư WMS/ERP</text>
  <text x="460" y="621" font-size="11" fill="#2d3748">• Xử lý thất thoát &amp; Phản hồi cho M3</text>

  <!-- S3 Box -->
  <rect x="795" y="520" width="345" height="130" rx="6" fill="url(#sGrad)" stroke="#4a5568" stroke-width="1.5" filter="url(#boxShadow)"/>
  <rect x="795" y="520" width="345" height="32" rx="6" fill="#4a5568"/>
  <text x="967" y="542" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">S3: ĐĂNG KÝ &amp; KÍCH HOẠT MEMBER</text>
  <text x="810" y="575" font-size="11" fill="#2d3748">• Đăng ký SĐT &amp; Xác thực mã Zalo/SMS OTP</text>
  <text x="810" y="598" font-size="11" fill="#2d3748">• Điền thông tin cá nhân &amp; tạo mật khẩu</text>
  <text x="810" y="621" font-size="11" fill="#2d3748">• Kích hoạt ID thành viên ACFC Member</text>

  <!-- Inter-layer Arrows -->
  <line x1="967" y1="240" x2="967" y2="295" stroke="#3182ce" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="962,295 967,305 972,295" fill="#3182ce"/>
  <text x="977" y="275" font-size="10" font-style="italic" fill="#3182ce">Lệnh phân bổ hàng</text>

  <line x1="605" y1="520" x2="605" y2="465" stroke="#4a5568" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="600,465 605,455 610,465" fill="#4a5568"/>
  <text x="615" y="488" font-size="10" font-style="italic" fill="#4a5568">Kiểm soát số dư tồn</text>

  <text x="600" y="700" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 2.1: Sơ đồ kiến trúc quy trình tổng thể doanh nghiệp ACFC.</text>
</svg>'''
    with open("diagrams/kien-truc-quy-trinh.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    drawio_xml = '''<mxfile host="app.diagrams.net" modified="2026-08-14T12:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
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

# ----------------------------------------------------------------------
# 2. MASTER CONSOLIDATED WAREHOUSE & SUPPLY CHAIN BPMN (C1, C2, S2, C4, M3)
# ----------------------------------------------------------------------
def generate_bpmn_master_warehouse():
    svg = '''<svg width="2200" height="1150" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <marker id="msgArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="none" stroke="#3182ce" stroke-width="1.5"/>
    </marker>
    <filter id="taskShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="2200" height="1150" fill="#ffffff"/>
  
  <text x="40" y="40" font-size="22" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0 TỔNG HỢP: QUY TRÌNH VẬN HÀNH TỔNG KHO, NHẬP XUẤT, KIỂM KÊ &amp; REVERSE LOGISTICS ACFC</text>
  <text x="40" y="65" font-size="13" fill="#718096">Tích hợp liên thông: C1 (Nhập khẩu) + C2 (Xuất phân phối) + S2 (Kiểm kê tồn kho) + C4 (Hoàn kho đổi trả) + M3 (Kế hoạch phân bổ) | 17 Cổng điều kiện (Gateways)</text>

  <!-- External Pool 1: 3PL & Forwarder -->
  <rect x="40" y="85" width="2120" height="70" fill="#fefcbf" stroke="#d69e2e" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="60" y="125" font-size="13" font-weight="bold" fill="#744210">POOL NGOÀI 1: ĐƠN VỊ VẬN TẢI QUỐC TẾ, FORWARDER &amp; ĐỐI TÁC 3PL NỘI ĐỊA (LOGISTICS SERVICE PROVIDERS)</text>

  <!-- External Pool 2: M3 & Store Network -->
  <rect x="40" y="1030" width="2120" height="70" fill="#ebf8ff" stroke="#3182ce" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="60" y="1070" font-size="13" font-weight="bold" fill="#2b6cb0">POOL NGOÀI 2: PHÒNG HOẠCH ĐỊNH HÀNG HÓA (M3) &amp; HỆ THỐNG 100+ CỬA HÀNG BÁN LẺ THỜI TRANG ACFC</text>

  <!-- Main Pool: ACFC Central Warehouse -->
  <rect x="40" y="170" width="2120" height="840" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="170" width="40" height="840" fill="#d69e2e"/>
  <text x="65" y="590" font-size="15" font-weight="bold" fill="#ffffff" transform="rotate(-90 65 590)" text-anchor="middle">ACFC – TỔNG KHO VẬN HÀNH &amp; PHÂN PHỐI TRUNG TÂM</text>

  <!-- Lanes -->
  <!-- Lane 1: Logistics & Customs -->
  <line x1="80" y1="330" x2="2160" y2="330" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="80" y="170" width="30" height="160" fill="#edf2f7"/>
  <text x="98" y="250" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 98 250)" text-anchor="middle">Logistics &amp; HQ</text>

  <!-- Lane 2: Inbound Receiving & QC -->
  <line x1="80" y1="500" x2="2160" y2="500" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="80" y="330" width="30" height="170" fill="#edf2f7"/>
  <text x="98" y="415" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 98 415)" text-anchor="middle">Inbound &amp; QC</text>

  <!-- Lane 3: WMS Storage & Inventory Control -->
  <line x1="80" y1="670" x2="2160" y2="670" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="80" y="500" width="30" height="170" fill="#edf2f7"/>
  <text x="98" y="585" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 98 585)" text-anchor="middle">WMS &amp; Tồn kho</text>

  <!-- Lane 4: Outbound Picking & Dispatch -->
  <line x1="80" y1="840" x2="2160" y2="840" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="80" y="670" width="30" height="170" fill="#edf2f7"/>
  <text x="98" y="755" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 98 755)" text-anchor="middle">Outbound Ops</text>

  <!-- Lane 5: Inventory Accounting & CFO -->
  <rect x="80" y="840" width="30" height="170" fill="#edf2f7"/>
  <text x="98" y="925" font-size="11" font-weight="bold" fill="#4a5568" transform="rotate(-90 98 925)" text-anchor="middle">Kế toán &amp; CFO</text>

  <!-- ==================== SECTION 1: C1 INBOUND ==================== -->
  <circle cx="145" cy="250" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="145" y="285" font-size="10" fill="#22543d" text-anchor="middle">Lô hàng về cảng</text>

  <rect x="190" y="225" width="125" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="252" y="246" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Tiếp nhận B/L &amp;</text>
  <text x="252" y="262" font-size="10" fill="#2d3748" text-anchor="middle">Khai báo VNACCS</text>

  <polygon points="345,250 365,230 385,250 365,270" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="365" y="254" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="365" y="285" font-size="9" fill="#744210" text-anchor="middle">G1: Thông quan?</text>

  <rect x="410" y="390" width="125" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="472" y="411" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Tiếp nhận xe container</text>
  <text x="472" y="427" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Kiểm tra seal chì</text>

  <polygon points="565,415 585,395 605,415 585,435" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="585" y="419" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="585" y="450" font-size="9" fill="#744210" text-anchor="middle">G2: Seal nguyên?</text>

  <rect x="630" y="390" width="130" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="695" y="411" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Dỡ hàng &amp; Quét mã</text>
  <text x="695" y="427" font-size="10" fill="#2d3748" text-anchor="middle">Barcode / RFID Chip</text>

  <polygon points="785,415 805,395 825,415 805,435" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="805" y="419" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="805" y="450" font-size="9" fill="#744210" text-anchor="middle">G3: Khớp List?</text>

  <rect x="855" y="560" width="130" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="920" y="581" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Ghi nhận nhập WMS</text>
  <text x="920" y="597" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Xếp giá kệ Putaway</text>

  <!-- ==================== SECTION 2: C2 OUTBOUND ==================== -->
  <polygon points="1015,755 1035,735 1055,755 1035,775" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1035" y="759" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1035" y="790" font-size="9" fill="#744210" text-anchor="middle">G4: Lệnh xuất?</text>

  <rect x="1080" y="730" width="130" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="1145" y="751" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Lấy hàng (Picking)</text>
  <text x="1145" y="767" font-size="10" fill="#2d3748" text-anchor="middle">theo chỉ dẫn WMS</text>

  <polygon points="1235,755 1255,735 1275,755 1255,775" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1255" y="759" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1255" y="790" font-size="9" fill="#744210" text-anchor="middle">G5: Đủ hàng?</text>

  <rect x="1300" y="730" width="130" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="1365" y="751" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Đóng thùng carton</text>
  <text x="1365" y="767" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Dán nhãn Shipping</text>

  <polygon points="1455,755 1475,735 1495,755 1475,775" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1475" y="759" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1475" y="790" font-size="9" fill="#744210" text-anchor="middle">G6: Tuyến 3PL?</text>

  <!-- ==================== SECTION 3: S2 STOCKTAKING ==================== -->
  <rect x="1080" y="560" width="130" height="50" rx="6" fill="#ffffff" stroke="#4a5568" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="1145" y="581" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Khóa sổ &amp; Quét mã</text>
  <text x="1145" y="597" font-size="10" fill="#2d3748" text-anchor="middle">kiểm kê thực tế S2</text>

  <polygon points="1235,585 1255,565 1275,585 1255,605" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1255" y="589" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1255" y="620" font-size="9" fill="#744210" text-anchor="middle">G7: Khớp 100%?</text>

  <polygon points="1315,585 1335,565 1355,585 1335,605" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1335" y="589" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1335" y="620" font-size="9" fill="#744210" text-anchor="middle">G8: Lệch &lt;= 0.5%?</text>

  <rect x="1300" y="390" width="125" height="50" rx="6" fill="#ffffff" stroke="#4a5568" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="1362" y="411" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Đếm chéo độc lập</text>
  <text x="1362" y="427" font-size="10" fill="#2d3748" text-anchor="middle">lần 2 các mã lệch</text>

  <polygon points="1455,925 1475,905 1495,925 1475,945" fill="#c6f6d5" stroke="#22543d" stroke-width="1.5"/>
  <text x="1475" y="929" font-size="13" font-weight="bold" fill="#22543d" text-anchor="middle">+</text>
  <text x="1475" y="960" font-size="9" fill="#22543d" text-anchor="middle">G9: AND-Split</text>

  <rect x="1520" y="875" width="125" height="40" rx="6" fill="#ffffff" stroke="#4a5568" stroke-width="1.5"/>
  <text x="1582" y="893" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Rà soát chứng từ</text>
  <text x="1582" y="907" font-size="9" fill="#2d3748" text-anchor="middle">nhập/xuất/trả 7 ngày</text>

  <rect x="1520" y="940" width="125" height="40" rx="6" fill="#ffffff" stroke="#4a5568" stroke-width="1.5"/>
  <text x="1582" y="958" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Kiểm tra khu hàng</text>
  <text x="1582" y="972" font-size="9" fill="#2d3748" text-anchor="middle">cách ly / lỗi / mẫu</text>

  <polygon points="1670,925 1690,905 1710,925 1690,945" fill="#c6f6d5" stroke="#22543d" stroke-width="1.5"/>
  <text x="1690" y="929" font-size="13" font-weight="bold" fill="#22543d" text-anchor="middle">+</text>
  <text x="1690" y="960" font-size="9" fill="#22543d" text-anchor="middle">G10: AND-Join</text>

  <polygon points="1735,585 1755,565 1775,585 1755,605" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1755" y="589" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1755" y="620" font-size="9" fill="#744210" text-anchor="middle">G11: Nguyên nhân?</text>

  <rect x="1805" y="540" width="120" height="40" rx="6" fill="#ffffff" stroke="#3182ce" stroke-width="1.5"/>
  <text x="1865" y="556" font-size="9" font-weight="bold" fill="#2d3748" text-anchor="middle">Lập đề nghị điều</text>
  <text x="1865" y="570" font-size="9" fill="#2d3748" text-anchor="middle">chỉnh nhầm size/màu</text>

  <rect x="1805" y="600" width="120" height="40" rx="6" fill="#ffffff" stroke="#e53e3e" stroke-width="1.5"/>
  <text x="1865" y="616" font-size="9" font-weight="bold" fill="#742a2a" text-anchor="middle">Lập biên bản</text>
  <text x="1865" y="630" font-size="9" fill="#742a2a" text-anchor="middle">thất thoát/bồi thường</text>

  <polygon points="1845,925 1865,905 1885,925 1865,945" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1865" y="929" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1865" y="960" font-size="9" fill="#744210" text-anchor="middle">G12: Duyệt xử lý?</text>

  <rect x="1920" y="900" width="125" height="50" rx="6" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="1982" y="921" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Hạch toán ERP &amp;</text>
  <text x="1982" y="937" font-size="10" fill="#2d3748" text-anchor="middle">Cập nhật số dư kho</text>

  <!-- ==================== SECTION 4: C4 REVERSE LOGISTICS ==================== -->
  <rect x="1600" y="390" width="130" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadow)"/>
  <text x="1665" y="411" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Tiếp nhận hàng đổi trả</text>
  <text x="1665" y="427" font-size="10" fill="#2d3748" text-anchor="middle">Reverse Logistics C4</text>

  <polygon points="1755,415 1775,395 1795,415 1775,435" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1775" y="419" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1775" y="450" font-size="9" fill="#744210" text-anchor="middle">G13: Loại hàng hoàn?</text>

  <!-- End Events -->
  <circle cx="2090" cy="755" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="3"/>
  <text x="2090" y="785" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Xuất kho 3PL</text>

  <circle cx="2090" cy="925" r="18" fill="#fed7d7" stroke="#9b2c2c" stroke-width="3"/>
  <text x="2090" y="955" font-size="9" font-weight="bold" fill="#9b2c2c" text-anchor="middle">Chốt sổ kiểm kê</text>

  <!-- ==================== SEQUENCE FLOWS ==================== -->
  <line x1="163" y1="250" x2="190" y2="250" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="315" y1="250" x2="345" y2="250" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <path d="M 385 250 L 472 250 L 472 390" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="395" y="240" font-size="9" fill="#38a169">[Thông quan]</text>

  <line x1="535" y1="415" x2="565" y2="415" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <line x1="605" y1="415" x2="630" y2="415" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="608" y="405" font-size="8" fill="#38a169">[Nguyên]</text>

  <line x1="760" y1="415" x2="785" y2="415" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 825 415 L 920 415 L 920 560" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="835" y="405" font-size="9" fill="#38a169">[Khớp List]</text>

  <!-- Putaway -> Outbound / Stocktaking -->
  <path d="M 985 585 L 1000 585 L 1000 755 L 1015 755" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="985" y1="585" x2="1080" y2="585" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Outbound Flows -->
  <line x1="1055" y1="755" x2="1080" y2="755" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="1210" y1="755" x2="1235" y2="755" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <line x1="1275" y1="755" x2="1300" y2="755" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="1278" y="745" font-size="8" fill="#38a169">[Đủ tồn]</text>

  <line x1="1430" y1="755" x2="1455" y2="755" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="1495" y1="755" x2="2072" y2="755" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Stocktaking Flows -->
  <line x1="1210" y1="585" x2="1235" y2="585" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 1255 565 L 1255 530 L 2000 530 L 2000 900" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="1260" y="545" font-size="9" fill="#38a169">[Khớp 100%]</text>

  <line x1="1275" y1="585" x2="1315" y2="585" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 1335 565 L 1335 440" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="1340" y="520" font-size="8" fill="#e53e3e">[Vượt 0.5%]</text>

  <path d="M 1425 415 L 1475 415 L 1475 905" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 1355 585 L 1475 585 L 1475 905" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="1370" y="575" font-size="8" fill="#38a169">[Trong 0.5%]</text>

  <path d="M 1495 925 L 1520 895" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 1495 925 L 1520 960" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 1645 895 L 1670 925" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 1645 960 L 1670 925" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 1710 925 L 1725 925 L 1725 585 L 1735 585" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 1775 585 L 1790 585 L 1790 560 L 1805 560" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 1775 585 L 1790 585 L 1790 620 L 1805 620" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 1925 560 L 1940 560 L 1940 880 L 1865 880 L 1865 905" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 1925 620 L 1940 620" fill="none" stroke="#2d3748" stroke-width="1.5"/>

  <line x1="1885" y1="925" x2="1920" y2="925" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="2045" y1="925" x2="2072" y2="925" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Reverse Flows (C4) -->
  <line x1="1730" y1="415" x2="1755" y2="415" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 1775 395 L 1775 360 L 920 360 L 920 560" fill="none" stroke="#38a169" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow)"/>
  <text x="1780" y="380" font-size="8" fill="#38a169">[Tái lưu kho]</text>

  <!-- ==================== MESSAGE FLOWS ==================== -->
  <path d="M 472 155 L 472 390" fill="none" stroke="#3182ce" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#msgArrow)"/>
  <text x="480" y="165" font-size="9" font-style="italic" fill="#3182ce">Message: Thông báo tàu cập cảng &amp; giao container</text>

  <path d="M 1365 780 L 1365 1030" fill="none" stroke="#3182ce" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#msgArrow)"/>
  <text x="1375" y="1020" font-size="9" font-style="italic" fill="#3182ce">Message: Lệnh điều phối xe 3PL &amp; e-POD giao Store</text>

  <path d="M 1982 950 L 1982 1030" fill="none" stroke="#3182ce" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#msgArrow)"/>
  <text x="1992" y="1020" font-size="9" font-style="italic" fill="#3182ce">Message: Báo cáo tỷ lệ hao hụt phản hồi M3 Merchandise</text>

  <text x="1100" y="1125" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 4.2: Sơ đồ BPMN 2.0 tổng hợp toàn diện quy trình Vận hành Tổng kho, Nhập xuất, Kiểm kê &amp; Reverse Logistics ACFC.</text>
</svg>'''
    with open("diagrams/bpmn-tong-hop-kho-van-hanh-acfc.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    drawio_xml = '''<mxfile host="app.diagrams.net" modified="2026-08-14T12:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="Master_Warehouse" name="ACFC Master Warehouse Process">
    <mxGraphModel dx="2200" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2200" pageHeight="1200" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="pool_3pl_top" value="POOL NGOÀI 1: ĐƠN VỊ VẬN TẢI QUỐC TẾ, FORWARDER &amp; 3PL (LOGISTICS PARTNERS)" style="swimlane;html=1;startSize=25;fillColor=#fefcbf;strokeColor=#d69e2e;dashed=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="2120" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="pool_acfc_wh" value="ACFC – TỔNG KHO VẬN HÀNH &amp; PHÂN PHỐI TRUNG TÂM" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;startSize=30;horizontal=0;containerType=tree;fontSize=13;fontStyle=1;fillColor=#ffffff;" vertex="1" parent="1">
          <mxGeometry x="40" y="140" width="2120" height="780" as="geometry"/>
        </mxCell>
        <mxCell id="lane_logistics" value="Logistics &amp; HQ" style="swimlane;html=1;startSize=25;fillColor=#f8f9fa;" vertex="1" parent="pool_acfc_wh">
          <mxGeometry x="30" y="0" width="2090" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="start_inbound" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;strokeWidth=2;" vertex="1" parent="lane_logistics">
          <mxGeometry x="40" y="55" width="35" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="task_bl_vnaccs" value="Tiếp nhận B/L &amp;&#xa;Khai báo VNACCS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_logistics">
          <mxGeometry x="110" y="48" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g1_customs_pass" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_logistics">
          <mxGeometry x="270" y="53" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="lane_inbound_qc" value="Inbound &amp; QC" style="swimlane;html=1;startSize=25;fillColor=#ffffff;" vertex="1" parent="pool_acfc_wh">
          <mxGeometry x="30" y="150" width="2090" height="160" as="geometry"/>
        </mxCell>
        <mxCell id="task_seal_check" value="Tiếp nhận container&#xa;&amp; Kiểm tra seal chì" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_inbound_qc">
          <mxGeometry x="340" y="55" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g2_seal_ok" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_inbound_qc">
          <mxGeometry x="500" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_do_rfid" value="Dỡ hàng &amp; Quét mã&#xa;Barcode / RFID Chip" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_inbound_qc">
          <mxGeometry x="570" y="55" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g3_pack_list" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_inbound_qc">
          <mxGeometry x="730" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_dem_cheo" value="Đếm chéo độc lập&#xa;lần 2 các mã lệch" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4a5568;" vertex="1" parent="lane_inbound_qc">
          <mxGeometry x="1230" y="55" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="task_rcv_return" value="Tiếp nhận hàng đổi trả&#xa;Reverse Logistics C4" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_inbound_qc">
          <mxGeometry x="1530" y="55" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g13_return_cond" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_inbound_qc">
          <mxGeometry x="1690" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="lane_wms_storage" value="WMS &amp; Tồn kho" style="swimlane;html=1;startSize=25;fillColor=#f8f9fa;" vertex="1" parent="pool_acfc_wh">
          <mxGeometry x="30" y="310" width="2090" height="160" as="geometry"/>
        </mxCell>
        <mxCell id="task_putaway_wms" value="Ghi nhận nhập WMS&#xa;&amp; Xếp giá kệ Putaway" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_wms_storage">
          <mxGeometry x="790" y="55" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="task_cycle_count" value="Khóa sổ &amp; Quét mã&#xa;kiểm kê thực tế S2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4a5568;" vertex="1" parent="lane_wms_storage">
          <mxGeometry x="1010" y="55" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g7_stock_match" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_wms_storage">
          <mxGeometry x="1170" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="g8_variance_rate" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_wms_storage">
          <mxGeometry x="1250" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="g11_cause_check" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_wms_storage">
          <mxGeometry x="1680" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_adj_note" value="Lập đề nghị điều&#xa;chỉnh nhầm size/màu" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;" vertex="1" parent="lane_wms_storage">
          <mxGeometry x="1750" y="30" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_loss_note" value="Lập biên bản&#xa;thất thoát/bồi thường" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#e53e3e;" vertex="1" parent="lane_wms_storage">
          <mxGeometry x="1750" y="90" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="lane_outbound_ops" value="Outbound Ops" style="swimlane;html=1;startSize=25;fillColor=#ffffff;" vertex="1" parent="pool_acfc_wh">
          <mxGeometry x="30" y="470" width="2090" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="g4_order_type" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_outbound_ops">
          <mxGeometry x="950" y="55" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_batch_picking" value="Lấy hàng (Picking)&#xa;theo chỉ dẫn WMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_outbound_ops">
          <mxGeometry x="1010" y="50" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g5_avail_stock" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_outbound_ops">
          <mxGeometry x="1170" y="55" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_pack_label" value="Đóng thùng carton&#xa;&amp; Dán nhãn Shipping" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_outbound_ops">
          <mxGeometry x="1235" y="50" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g6_delivery_route" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_outbound_ops">
          <mxGeometry x="1390" y="55" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="end_outbound" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;strokeWidth=3;" vertex="1" parent="lane_outbound_ops">
          <mxGeometry x="2020" y="58" width="35" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="lane_cfo_acc" value="Kế toán &amp; CFO" style="swimlane;html=1;startSize=25;fillColor=#f8f9fa;" vertex="1" parent="pool_acfc_wh">
          <mxGeometry x="30" y="620" width="2090" height="160" as="geometry"/>
        </mxCell>
        <mxCell id="g9_and_split" value="+" style="rhombus;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;fontStyle=1;" vertex="1" parent="lane_cfo_acc">
          <mxGeometry x="1390" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_audit_docs" value="Rà soát chứng từ&#xa;nhập/xuất/trả 7 ngày" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4a5568;" vertex="1" parent="lane_cfo_acc">
          <mxGeometry x="1460" y="20" width="125" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_audit_quarantine" value="Kiểm tra khu hàng&#xa;cách ly / lỗi / mẫu" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4a5568;" vertex="1" parent="lane_cfo_acc">
          <mxGeometry x="1460" y="90" width="125" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="g10_and_join" value="+" style="rhombus;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;fontStyle=1;" vertex="1" parent="lane_cfo_acc">
          <mxGeometry x="1610" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="g12_cfo_approve" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_cfo_acc">
          <mxGeometry x="1790" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_erp_posting" value="Hạch toán ERP &amp;&#xa;Cập nhật số dư kho" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2b6cb0;" vertex="1" parent="lane_cfo_acc">
          <mxGeometry x="1860" y="55" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="end_stocktaking" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#fed7d7;strokeColor=#9b2c2c;strokeWidth=3;" vertex="1" parent="lane_cfo_acc">
          <mxGeometry x="2020" y="63" width="35" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="pool_store_m3_bottom" value="POOL NGOÀI 2: PHÒNG HOẠCH ĐỊNH M3 &amp; HỆ THỐNG 100+ CỬA HÀNG ACFC (RETAIL NETWORK)" style="swimlane;html=1;startSize=25;fillColor=#ebf8ff;strokeColor=#3182ce;dashed=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="950" width="2120" height="70" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    with open("diagrams/bpmn-tong-hop-kho-van-hanh-acfc.drawio", "w", encoding="utf-8") as f:
        f.write(drawio_xml)

# ----------------------------------------------------------------------
# 3. S3: MEMBER REGISTRATION & ACTIVATION BPMN
# ----------------------------------------------------------------------
def generate_bpmn_s3():
    svg = '''<svg width="1500" height="800" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <filter id="taskShadow2" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="1500" height="800" fill="#ffffff"/>
  <text x="40" y="40" font-size="20" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0: ĐĂNG KÝ, XÁC THỰC OTP &amp; KÍCH HOẠT TÀI KHOẢN MEMBER ACFC (S3)</text>
  <text x="40" y="65" font-size="13" fill="#718096">Chủ thể: Cổng Thành viên Số ACFC | Đáp ứng chuẩn 8 Gateways | Phân luồng OTP &amp; CSKH 1900</text>

  <!-- Pool 1: Khách hàng (Customer) -->
  <rect x="40" y="90" width="1420" height="160" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="90" width="35" height="160" fill="#319795"/>
  <text x="62" y="170" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 62 170)" text-anchor="middle">KHÁCH HÀNG (CUSTOMER)</text>

  <!-- Pool 2: ACFC Platform -->
  <rect x="40" y="270" width="1420" height="480" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="270" width="35" height="480" fill="#2d3748"/>
  <text x="62" y="510" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 62 510)" text-anchor="middle">HỆ THỐNG ACFC PLATFORM</text>

  <!-- Lanes in Pool 2 -->
  <line x1="75" y1="390" x2="1460" y2="390" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="270" width="30" height="120" fill="#edf2f7"/>
  <text x="93" y="330" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 330)" text-anchor="middle">Frontend UI</text>

  <line x1="75" y1="510" x2="1460" y2="510" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="390" width="30" height="120" fill="#edf2f7"/>
  <text x="93" y="450" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 450)" text-anchor="middle">Backend Core</text>

  <line x1="75" y1="630" x2="1460" y2="630" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="510" width="30" height="120" fill="#edf2f7"/>
  <text x="93" y="570" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 570)" text-anchor="middle">SMS Gateway</text>

  <rect x="75" y="630" width="30" height="120" fill="#edf2f7"/>
  <text x="93" y="690" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 690)" text-anchor="middle">CSKH 1900</text>

  <!-- ELEMENTS -->
  <circle cx="135" cy="170" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="135" y="205" font-size="10" fill="#22543d" text-anchor="middle">Truy cập Web/App</text>

  <polygon points="195,170 215,150 235,170 215,190" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="215" y="174" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="215" y="140" font-size="9" fill="#744210" text-anchor="middle">G1: Có nick?</text>

  <rect x="265" y="145" width="115" height="50" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="322" y="166" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Nhập SĐT</text>
  <text x="322" y="182" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Bấm gửi OTP</text>

  <polygon points="410,450 430,430 450,450 430,470" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="430" y="454" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="430" y="485" font-size="9" fill="#744210" text-anchor="middle">G2: SĐT tồn tại?</text>

  <rect x="480" y="545" width="125" height="50" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="542" y="566" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Sinh mã ngẫu nhiên</text>
  <text x="542" y="582" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Gửi SMS/ZNS OTP</text>

  <polygon points="635,170 655,150 675,170 655,190" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="655" y="174" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="655" y="140" font-size="9" fill="#744210" text-anchor="middle">G3: Nhận trong 120s?</text>

  <rect x="710" y="145" width="115" height="50" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="767" y="166" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Nhập mã OTP</text>
  <text x="767" y="182" font-size="10" fill="#2d3748" text-anchor="middle">vào màn hình</text>

  <polygon points="745,450 765,430 785,450 765,470" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="765" y="454" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="765" y="485" font-size="9" fill="#744210" text-anchor="middle">G4: OTP đúng?</text>

  <polygon points="825,450 845,430 865,450 845,470" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="845" y="454" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="845" y="485" font-size="9" fill="#744210" text-anchor="middle">G5: Sai &gt;= 3 lần?</text>

  <rect x="895" y="145" width="130" height="50" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="960" y="166" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Điền thông tin cá nhân</text>
  <text x="960" y="182" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Tạo mật khẩu mới</text>

  <polygon points="1055,330 1075,310 1095,330 1075,350" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1075" y="334" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1075" y="365" font-size="9" fill="#744210" text-anchor="middle">G6: Mật khẩu chuẩn?</text>

  <polygon points="1135,330 1155,310 1175,330 1155,350" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1155" y="334" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1155" y="365" font-size="9" fill="#744210" text-anchor="middle">G7: Đồng ý luật?</text>

  <rect x="1200" y="425" width="125" height="50" rx="6" fill="#ffffff" stroke="#319795" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="1262" y="446" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Tạo bản ghi User</text>
  <text x="1262" y="462" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Cấp ID Member</text>

  <rect x="1200" y="305" width="125" height="50" rx="6" fill="#ffffff" stroke="#38a169" stroke-width="1.5" filter="url(#taskShadow2)"/>
  <text x="1262" y="326" font-size="10" font-weight="bold" fill="#22543d" text-anchor="middle">Auto-Login &amp;</text>
  <text x="1262" y="342" font-size="10" fill="#22543d" text-anchor="middle">Tặng Voucher 100k</text>

  <polygon points="1355,330 1370,315 1385,330 1370,345" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1370" y="334" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>

  <rect x="895" y="665" width="130" height="50" rx="6" fill="#ffffff" stroke="#e53e3e" stroke-width="1.5"/>
  <text x="960" y="686" font-size="10" font-weight="bold" fill="#742a2a" text-anchor="middle">CSKH 1900 3038</text>
  <text x="960" y="702" font-size="10" fill="#742a2a" text-anchor="middle">xác minh mở khóa</text>

  <circle cx="1425" cy="330" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="3"/>
  <text x="1425" y="360" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Kích hoạt xong</text>

  <!-- FLOWS -->
  <line x1="153" y1="170" x2="195" y2="170" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="235" y1="170" x2="265" y2="170" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <path d="M 322 195 L 322 450 L 410 450" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <path d="M 450 450 L 465 450 L 465 570 L 480 570" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <path d="M 605 570 L 620 570 L 620 170 L 635 170" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <line x1="675" y1="170" x2="710" y2="170" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <path d="M 655 190 L 655 580 L 605 580" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <path d="M 767 195 L 767 430" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <path d="M 785 450 L 805 450 L 805 170 L 895 170" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="785" y1="450" x2="825" y2="450" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <path d="M 845 470 L 845 690 L 895 690" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <path d="M 960 195 L 960 330 L 1055 330" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="1095" y1="330" x2="1135" y2="330" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <path d="M 1175 330 L 1185 330 L 1185 450 L 1200 450" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="1262" y1="425" x2="1262" y2="355" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="1325" y1="330" x2="1355" y2="330" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="1385" y1="330" x2="1407" y2="330" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <path d="M 1025 690 L 1370 690 L 1370 345" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow2)"/>

  <text x="750" y="775" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 5.2: Sơ đồ BPMN 2.0 quy trình Đăng ký, Xác thực OTP và Kích hoạt tài khoản Member ACFC (S3).</text>
</svg>'''
    with open("diagrams/bpmn-dang-ky-kich-hoat-tai-khoan-s3.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# ----------------------------------------------------------------------
# 4. S1: RECRUITMENT & ONBOARDING BPMN
# ----------------------------------------------------------------------
def generate_bpmn_s1():
    svg = '''<svg width="1500" height="850" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <filter id="taskShadow3" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="1500" height="850" fill="#ffffff"/>
  <text x="40" y="40" font-size="20" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0: QUY TRÌNH TUYỂN DỤNG &amp; TIẾP NHẬN ONBOARDING NHÂN SỰ ACFC (S1)</text>
  <text x="40" y="65" font-size="13" fill="#718096">Chủ thể: Khối Bán lẻ Thời trang &amp; Tổng kho ACFC | Độ phức tạp: 8 Cổng điều kiện (Gateways)</text>

  <!-- Pool 1: Ứng viên (Candidate) -->
  <rect x="40" y="90" width="1420" height="150" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="90" width="35" height="150" fill="#805ad5"/>
  <text x="62" y="165" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 62 165)" text-anchor="middle">ỨNG VIÊN (CANDIDATE)</text>

  <!-- Pool 2: ACFC Internal Organization -->
  <rect x="40" y="260" width="1420" height="540" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="260" width="35" height="540" fill="#2d3748"/>
  <text x="62" y="530" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 62 530)" text-anchor="middle">ACFC – QUY TRÌNH TUYỂN DỤNG NỘI BỘ (S1)</text>

  <!-- Lanes -->
  <line x1="75" y1="395" x2="1460" y2="395" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="260" width="30" height="135" fill="#edf2f7"/>
  <text x="93" y="330" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 330)" text-anchor="middle">Store / Kho Ops</text>

  <line x1="75" y1="535" x2="1460" y2="535" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="395" width="30" height="140" fill="#edf2f7"/>
  <text x="93" y="465" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 465)" text-anchor="middle">HR Tuyển dụng</text>

  <line x1="75" y1="670" x2="1460" y2="670" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="535" width="30" height="135" fill="#edf2f7"/>
  <text x="93" y="605" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 605)" text-anchor="middle">HRD / Giám đốc</text>

  <rect x="75" y="670" width="30" height="130" fill="#edf2f7"/>
  <text x="93" y="735" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 735)" text-anchor="middle">IT &amp; Admin</text>

  <!-- ELEMENTS -->
  <circle cx="135" cy="330" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="135" y="365" font-size="10" fill="#22543d" text-anchor="middle">Phát sinh vị trí</text>

  <rect x="180" y="305" width="125" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="242" y="326" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Lập phiếu yêu cầu</text>
  <text x="242" y="342" font-size="10" fill="#2d3748" text-anchor="middle">tuyển dụng &amp; JD</text>

  <polygon points="335,605 355,585 375,605 355,625" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="355" y="609" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="355" y="640" font-size="9" fill="#744210" text-anchor="middle">G1: Duyệt định biên?</text>

  <rect x="400" y="440" width="120" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="460" y="461" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Đăng tin tuyển dụng</text>
  <text x="460" y="477" font-size="10" fill="#2d3748" text-anchor="middle">ACFC Careers/TopCV</text>

  <rect x="400" y="140" width="120" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="460" y="161" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Nộp hồ sơ ứng tuyển</text>
  <text x="460" y="177" font-size="10" fill="#2d3748" text-anchor="middle">trực tuyến qua portal</text>

  <polygon points="545,465 565,445 585,465 565,485" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="565" y="469" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="565" y="500" font-size="9" fill="#744210" text-anchor="middle">G2: CV đạt chuẩn?</text>

  <polygon points="625,465 645,445 665,465 645,485" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="645" y="469" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="645" y="500" font-size="9" fill="#744210" text-anchor="middle">G3: Sơ vấn đạt?</text>

  <rect x="700" y="305" width="125" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="762" y="326" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Phỏng vấn V1</text>
  <text x="762" y="342" font-size="10" fill="#2d3748" text-anchor="middle">chuyên môn &amp; thái độ</text>

  <polygon points="850,330 870,310 890,330 870,350" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="870" y="334" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="870" y="365" font-size="9" fill="#744210" text-anchor="middle">G4: V1 Đạt?</text>

  <rect x="815" y="140" width="120" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="875" y="161" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Làm bài test</text>
  <text x="875" y="177" font-size="10" fill="#2d3748" text-anchor="middle">tính toán/nghiệp vụ</text>

  <polygon points="965,465 985,445 1005,465 985,485" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="985" y="469" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="985" y="500" font-size="9" fill="#744210" text-anchor="middle">G5: Test &gt;= 70đ?</text>

  <polygon points="1055,605 1075,585 1095,605 1075,625" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1075" y="609" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1075" y="640" font-size="9" fill="#744210" text-anchor="middle">G6: V2 Duyệt?</text>

  <rect x="1135" y="440" width="125" height="50" rx="6" fill="#ffffff" stroke="#805ad5" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="1197" y="461" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Gửi e-Offer Letter</text>
  <text x="1197" y="477" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Đãi ngộ chuẩn</text>

  <polygon points="1235,165 1255,145 1275,165 1255,185" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1255" y="169" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1255" y="135" font-size="9" fill="#744210" text-anchor="middle">G7: Nhận Offer?</text>

  <polygon points="1235,605 1255,585 1275,605 1255,625" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1255" y="609" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1255" y="640" font-size="9" fill="#744210" text-anchor="middle">G8: Duyệt lương?</text>

  <rect x="1305" y="710" width="125" height="50" rx="6" fill="#ffffff" stroke="#38a169" stroke-width="1.5" filter="url(#taskShadow3)"/>
  <text x="1367" y="731" font-size="10" font-weight="bold" fill="#22543d" text-anchor="middle">Ký Hợp đồng thử việc</text>
  <text x="1367" y="747" font-size="10" fill="#22543d" text-anchor="middle">&amp; Cấp phát thiết bị</text>

  <circle cx="1435" cy="735" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="3"/>
  <text x="1435" y="765" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Onboarding</text>

  <!-- FLOWS -->
  <line x1="153" y1="330" x2="180" y2="330" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <path d="M 242 355 L 242 605 L 335 605" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <path d="M 375 605 L 460 605 L 460 490" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <line x1="460" y1="440" x2="460" y2="190" stroke="#2d3748" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow3)"/>

  <path d="M 520 165 L 565 165 L 565 445" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <line x1="585" y1="465" x2="625" y2="465" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <path d="M 665 465 L 762 465 L 762 355" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <line x1="825" y1="330" x2="850" y2="330" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <path d="M 870 310 L 870 190" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <path d="M 935 165 L 985 165 L 985 445" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <path d="M 1005 465 L 1075 465 L 1075 585" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <path d="M 1095 605 L 1197 605 L 1197 490" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <path d="M 1260 465 L 1285 465 L 1285 165 L 1275 165" fill="none" stroke="#2d3748" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow3)"/>
  <path d="M 1275 165 L 1367 165 L 1367 710" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <path d="M 1255 185 L 1255 585" fill="none" stroke="#d69e2e" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <path d="M 1235 605 L 1210 605 L 1210 490" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrow3)"/>

  <line x1="1430" y1="735" x2="1417" y2="735" stroke="#2d3748" stroke-width="1.5"/>

  <text x="750" y="825" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 6.2: Sơ đồ BPMN 2.0 quy trình Tuyển dụng và Tiếp nhận nhân sự tại ACFC (S1).</text>
</svg>'''
    with open("diagrams/bpmn-tuyen-dung-nhan-su-s1.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# ----------------------------------------------------------------------
# 5. M3: MERCHANDISE PLANNING & ALLOCATION BPMN
# ----------------------------------------------------------------------
def generate_bpmn_m3():
    svg = '''<svg width="1930" height="740" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrowM3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <marker id="arrowM3g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#38a169"/>
    </marker>
    <marker id="arrowM3r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#e53e3e"/>
    </marker>
    <filter id="taskShadowM3" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="1930" height="740" fill="#ffffff"/>
  <text x="40" y="40" font-size="20" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0: QUY TRÌNH HOẠCH ĐỊNH HÀNG HÓA &amp; PHÂN BỔ THEO MÙA ACFC (M3)</text>
  <text x="40" y="66" font-size="13" fill="#718096">Chủ thể: Khối Merchandise &amp; Allocation ACFC | 8 cổng: 2 cặp XOR split–merge, 1 cặp AND split–join, 2 XOR quyết định phát hành; nhiều điểm kết thúc.</text>

  <!-- Main Pool -->
  <rect x="40" y="90" width="1850" height="560" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="90" width="35" height="560" fill="#3182ce"/>
  <text x="57" y="370" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 57 370)" text-anchor="middle">ACFC – KHỐI HOẠCH ĐỊNH &amp; PHÂN BỔ HÀNG HÓA (M3)</text>

  <!-- Lanes -->
  <line x1="75" y1="290" x2="1890" y2="290" stroke="#cbd5e0" stroke-width="1"/>
  <line x1="75" y1="470" x2="1890" y2="470" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="90" width="30" height="200" fill="#edf2f7"/>
  <text x="93" y="190" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 190)" text-anchor="middle">Merchandise / Product Planning</text>
  <rect x="75" y="290" width="30" height="180" fill="#edf2f7"/>
  <text x="93" y="380" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 380)" text-anchor="middle">Allocation Team / Vận hành</text>
  <rect x="75" y="470" width="30" height="180" fill="#edf2f7"/>
  <text x="93" y="560" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 560)" text-anchor="middle">Commercial / Tài chính</text>

  <!-- ELEMENTS (spine y=190) -->
  <circle cx="120" cy="190" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="120" y="225" font-size="9" fill="#22543d" text-anchor="middle">Khởi động mùa</text>

  <rect x="165" y="165" width="130" height="50" rx="6" fill="#ffffff" stroke="#3182ce" stroke-width="1.5" filter="url(#taskShadowM3)"/>
  <text x="230" y="186" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Phân tích Sell-through</text>
  <text x="230" y="202" font-size="10" fill="#2d3748" text-anchor="middle">và Weeks of Supply</text>

  <polygon points="355,190 375,170 395,190 375,210" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="375" y="194" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="375" y="160" font-size="9" fill="#744210" text-anchor="middle">G1: Dữ liệu đủ?</text>

  <polygon points="475,190 495,170 515,190 495,210" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="495" y="194" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="495" y="160" font-size="9" fill="#744210" text-anchor="middle">Gm (XOR-merge)</text>

  <rect x="555" y="165" width="140" height="50" rx="6" fill="#ffffff" stroke="#3182ce" stroke-width="1.5" filter="url(#taskShadowM3)"/>
  <text x="625" y="186" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Lập kế hoạch mua</text>
  <text x="625" y="202" font-size="10" fill="#2d3748" text-anchor="middle">và phân bổ hàng hóa</text>

  <polygon points="740,190 760,170 780,190 760,210" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="760" y="194" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="760" y="160" font-size="9" fill="#744210" text-anchor="middle">G2: Đủ ngân sách?</text>

  <polygon points="860,190 880,170 900,190 880,210" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="880" y="194" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="880" y="160" font-size="9" fill="#744210" text-anchor="middle">Gm2 (XOR-merge)</text>

  <polygon points="980,190 1000,170 1020,190 1000,210" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1000" y="195" font-size="14" font-weight="bold" fill="#744210" text-anchor="middle">+</text>
  <text x="1000" y="160" font-size="9" fill="#744210" text-anchor="middle">Ga: tách AND</text>

  <rect x="1035" y="355" width="140" height="50" rx="6" fill="#ffffff" stroke="#3182ce" stroke-width="1.5" filter="url(#taskShadowM3)"/>
  <text x="1105" y="376" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Kiểm tra sức chứa</text>
  <text x="1105" y="392" font-size="10" fill="#2d3748" text-anchor="middle">cửa hàng</text>

  <rect x="1035" y="535" width="140" height="50" rx="6" fill="#ffffff" stroke="#3182ce" stroke-width="1.5" filter="url(#taskShadowM3)"/>
  <text x="1105" y="556" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Xác nhận nguồn hàng</text>
  <text x="1105" y="572" font-size="10" fill="#2d3748" text-anchor="middle">khả dụng</text>

  <polygon points="1220,190 1240,170 1260,190 1240,210" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1240" y="195" font-size="14" font-weight="bold" fill="#744210" text-anchor="middle">+</text>
  <text x="1240" y="160" font-size="9" fill="#744210" text-anchor="middle">Gj: AND-join</text>

  <rect x="1285" y="165" width="140" height="50" rx="6" fill="#ffffff" stroke="#3182ce" stroke-width="1.5" filter="url(#taskShadowM3)"/>
  <text x="1355" y="186" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Trình và phê duyệt</text>
  <text x="1355" y="202" font-size="10" fill="#2d3748" text-anchor="middle">kế hoạch phân bổ</text>

  <polygon points="1470,190 1490,170 1510,190 1490,210" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1490" y="194" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1490" y="160" font-size="9" fill="#744210" text-anchor="middle">G3: Được duyệt?</text>

  <rect x="1560" y="165" width="140" height="50" rx="6" fill="#ffffff" stroke="#3182ce" stroke-width="1.5" filter="url(#taskShadowM3)"/>
  <text x="1630" y="186" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Phát hành lệnh mua</text>
  <text x="1630" y="202" font-size="10" fill="#2d3748" text-anchor="middle">và đồng bộ WMS</text>

  <polygon points="1740,190 1760,170 1780,190 1760,210" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1760" y="194" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1760" y="160" font-size="9" fill="#744210" text-anchor="middle">G4: WMS OK?</text>

  <circle cx="1835" cy="190" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="3"/>
  <text x="1835" y="225" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Chuyển kho</text>

  <!-- Rework tasks -->
  <rect x="425" y="355" width="140" height="50" rx="6" fill="#fffaf0" stroke="#dd6b20" stroke-width="1.5" filter="url(#taskShadowM3)"/>
  <text x="495" y="376" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Bổ sung, làm sạch</text>
  <text x="495" y="392" font-size="10" fill="#2d3748" text-anchor="middle">dữ liệu</text>

  <rect x="810" y="535" width="140" height="50" rx="6" fill="#fffaf0" stroke="#dd6b20" stroke-width="1.5" filter="url(#taskShadowM3)"/>
  <text x="880" y="556" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Điều chỉnh</text>
  <text x="880" y="572" font-size="10" fill="#2d3748" text-anchor="middle">kế hoạch mua</text>

  <!-- Negative end events -->
  <circle cx="1490" cy="380" r="16" fill="#fed7d7" stroke="#822727" stroke-width="3"/>
  <text x="1490" y="410" font-size="9" font-weight="bold" fill="#822727" text-anchor="middle">Trả lại điều chỉnh</text>
  <circle cx="1760" cy="380" r="16" fill="#fed7d7" stroke="#822727" stroke-width="3"/>
  <text x="1760" y="410" font-size="9" font-weight="bold" fill="#822727" text-anchor="middle">Lỗi tích hợp – retry</text>

  <!-- FLOWS: spine -->
  <line x1="138" y1="190" x2="165" y2="190" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <line x1="295" y1="190" x2="355" y2="190" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <line x1="395" y1="190" x2="475" y2="190" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowM3g)"/>
  <text x="435" y="182" font-size="9" fill="#38a169" text-anchor="middle">Có</text>
  <line x1="515" y1="190" x2="555" y2="190" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <line x1="695" y1="190" x2="740" y2="190" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <line x1="780" y1="190" x2="860" y2="190" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowM3g)"/>
  <text x="820" y="182" font-size="9" fill="#38a169" text-anchor="middle">Có</text>
  <line x1="900" y1="190" x2="980" y2="190" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <line x1="1260" y1="190" x2="1285" y2="190" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <line x1="1510" y1="190" x2="1560" y2="190" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowM3g)"/>
  <text x="1535" y="182" font-size="9" fill="#38a169" text-anchor="middle">Có</text>
  <line x1="1700" y1="190" x2="1740" y2="190" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <line x1="1780" y1="190" x2="1817" y2="190" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowM3g)"/>
  <text x="1798" y="182" font-size="9" fill="#38a169" text-anchor="middle">Có</text>

  <!-- FLOWS: XOR rework G1/Gm -->
  <path d="M 375 210 L 375 380 L 425 380" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrowM3r)"/>
  <text x="360" y="300" font-size="9" fill="#e53e3e" text-anchor="end">Không</text>
  <path d="M 495 355 L 495 210" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>

  <!-- FLOWS: XOR rework G2/Gm2 -->
  <path d="M 760 210 L 760 560 L 810 560" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrowM3r)"/>
  <text x="745" y="300" font-size="9" fill="#e53e3e" text-anchor="end">Không</text>
  <path d="M 880 535 L 880 210" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>

  <!-- FLOWS: AND split/join -->
  <path d="M 1000 210 L 1000 380 L 1035 380" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <path d="M 1000 210 L 1000 560 L 1035 560" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <path d="M 1175 380 L 1240 380 L 1240 210" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>
  <path d="M 1175 560 L 1240 560 L 1240 210" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowM3)"/>

  <!-- FLOWS: negative ends -->
  <path d="M 1490 210 L 1490 362" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrowM3r)"/>
  <text x="1500" y="300" font-size="9" fill="#e53e3e" text-anchor="start">Không</text>
  <path d="M 1760 210 L 1760 362" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrowM3r)"/>
  <text x="1770" y="300" font-size="9" fill="#e53e3e" text-anchor="start">Không</text>

  <text x="950" y="700" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 3.1: Sơ đồ BPMN 2.0 quy trình Hoạch định hàng hóa và Phân bổ nguồn hàng theo mùa (M3).</text>
</svg>'''
    with open("diagrams/bpmn-hoach-dinh-phan-bo-hang-hoa-m3.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# ----------------------------------------------------------------------
# 6. C3: OMNICHANNEL SALES & POS CHECKOUT BPMN
# ----------------------------------------------------------------------
def generate_bpmn_c3():
    svg = '''<svg width="1500" height="800" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrowC3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <filter id="taskShadowC3" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="1500" height="800" fill="#ffffff"/>
  <text x="40" y="40" font-size="20" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0: QUY TRÌNH BÁN HÀNG ĐA KÊNH &amp; THANH TOÁN POS / E-COM ACFC (C3)</text>
  <text x="40" y="65" font-size="13" fill="#718096">Chủ thể: Khối Cửa hàng Bán lẻ &amp; E-Commerce ACFC | Độ phức tạp: 8 Cổng điều kiện (Gateways)</text>

  <!-- Pool 1: Khách hàng (Customer) -->
  <rect x="40" y="90" width="1420" height="150" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="90" width="35" height="150" fill="#d69e2e"/>
  <text x="62" y="165" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 62 165)" text-anchor="middle">KHÁCH HÀNG (CUSTOMER)</text>

  <!-- Pool 2: ACFC Retail & POS -->
  <rect x="40" y="260" width="1420" height="490" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="260" width="35" height="490" fill="#2d3748"/>
  <text x="62" y="505" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 62 505)" text-anchor="middle">ACFC – HỆ THỐNG BÁN HÀNG &amp; THANH TOÁN (C3)</text>

  <!-- Lanes -->
  <line x1="75" y1="410" x2="1460" y2="410" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="260" width="30" height="150" fill="#edf2f7"/>
  <text x="93" y="335" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 335)" text-anchor="middle">Tư vấn / Web App</text>

  <line x1="75" y1="580" x2="1460" y2="580" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="410" width="30" height="170" fill="#edf2f7"/>
  <text x="93" y="495" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 495)" text-anchor="middle">Thu ngân / POS</text>

  <rect x="75" y="580" width="30" height="170" fill="#edf2f7"/>
  <text x="93" y="665" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 665)" text-anchor="middle">Cổng Thanh toán</text>

  <!-- Elements -->
  <circle cx="135" cy="165" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="135" y="200" font-size="10" fill="#22543d" text-anchor="middle">Chọn sản phẩm</text>

  <polygon points="195,165 215,145 235,165 215,185" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="215" y="169" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="215" y="135" font-size="9" fill="#744210" text-anchor="middle">G1: Kênh mua?</text>

  <rect x="265" y="310" width="125" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadowC3)"/>
  <text x="327" y="331" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Tư vấn thử size</text>
  <text x="327" y="347" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Kiểm tra tồn POS</text>

  <polygon points="415,335 435,315 455,335 435,355" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="435" y="339" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="435" y="370" font-size="9" fill="#744210" text-anchor="middle">G2: Còn hàng?</text>

  <rect x="490" y="470" width="125" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadowC3)"/>
  <text x="552" y="491" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Quét Barcode/RFID</text>
  <text x="552" y="507" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Nhận diện Member</text>

  <polygon points="640,495 660,475 680,495 660,515" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="660" y="499" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="660" y="530" font-size="9" fill="#744210" text-anchor="middle">G3: Áp Voucher?</text>

  <polygon points="725,495 745,475 765,495 745,515" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="745" y="499" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="745" y="530" font-size="9" fill="#744210" text-anchor="middle">G4: Phương thức TT?</text>

  <rect x="800" y="640" width="125" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadowC3)"/>
  <text x="862" y="661" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Xử lý thanh toán</text>
  <text x="862" y="677" font-size="10" fill="#2d3748" text-anchor="middle">Thẻ / QR / Payoo</text>

  <polygon points="950,665 970,645 990,665 970,685" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="970" y="669" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="970" y="700" font-size="9" fill="#744210" text-anchor="middle">G5: TT Thành công?</text>

  <rect x="1030" y="470" width="125" height="50" rx="6" fill="#ffffff" stroke="#38a169" stroke-width="1.5" filter="url(#taskShadowC3)"/>
  <text x="1092" y="491" font-size="10" font-weight="bold" fill="#22543d" text-anchor="middle">Xuất e-Invoice &amp;</text>
  <text x="1092" y="507" font-size="10" fill="#22543d" text-anchor="middle">Trừ tồn Real-time</text>

  <polygon points="1185,495 1205,475 1225,495 1205,515" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1205" y="499" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1205" y="530" font-size="9" fill="#744210" text-anchor="middle">G6: Tích điểm Member?</text>

  <circle cx="1310" cy="495" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="3"/>
  <text x="1310" y="525" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Giao hàng xong</text>

  <!-- Flows -->
  <line x1="153" y1="165" x2="195" y2="165" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <path d="M 215 185 L 215 335 L 265 335" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <line x1="390" y1="335" x2="415" y2="335" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <path d="M 455 335 L 552 335 L 552 470" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <line x1="615" y1="495" x2="640" y2="495" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <line x1="680" y1="495" x2="725" y2="495" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <path d="M 745 515 L 745 665 L 800 665" fill="none" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <line x1="925" y1="665" x2="950" y2="665" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <path d="M 990 665 L 1092 665 L 1092 520" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <line x1="1155" y1="495" x2="1185" y2="495" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC3)"/>
  <line x1="1225" y1="495" x2="1292" y2="495" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowC3)"/>

  <text x="750" y="770" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 3.2: Sơ đồ BPMN 2.0 quy trình Bán hàng đa kênh và Thanh toán POS / E-Commerce ACFC (C3).</text>
</svg>'''
    with open("diagrams/bpmn-ban-hang-da-kenh-c3.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# ----------------------------------------------------------------------
# 7. C4: REVERSE LOGISTICS & RETURN/REFUND BPMN
# ----------------------------------------------------------------------
def generate_bpmn_c4():
    svg = '''<svg width="1500" height="800" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrowC4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d3748"/>
    </marker>
    <filter id="taskShadowC4" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="1500" height="800" fill="#ffffff"/>
  <text x="40" y="40" font-size="20" font-weight="bold" fill="#1a202c">SƠ ĐỒ BPMN 2.0: QUY TRÌNH TIẾP NHẬN ĐỔI TRẢ, BẢO HÀNH &amp; HOÀN TIỀN ACFC (C4)</text>
  <text x="40" y="65" font-size="13" fill="#718096">Chủ thể: Khối Bán lẻ, CSKH &amp; Kế toán ACFC | Độ phức tạp: 8 Cổng điều kiện (Gateways)</text>

  <!-- Pool 1: Khách hàng (Customer) -->
  <rect x="40" y="90" width="1420" height="150" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="90" width="35" height="150" fill="#d69e2e"/>
  <text x="62" y="165" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 62 165)" text-anchor="middle">KHÁCH HÀNG (CUSTOMER)</text>

  <!-- Pool 2: ACFC Returns Management -->
  <rect x="40" y="260" width="1420" height="490" fill="#ffffff" stroke="#2d3748" stroke-width="2"/>
  <rect x="40" y="260" width="35" height="490" fill="#2d3748"/>
  <text x="62" y="505" font-size="13" font-weight="bold" fill="#ffffff" transform="rotate(-90 62 505)" text-anchor="middle">ACFC – XỬ LÝ ĐỔI TRẢ &amp; HOÀN TIỀN (C4)</text>

  <!-- Lanes -->
  <line x1="75" y1="410" x2="1460" y2="410" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="260" width="30" height="150" fill="#edf2f7"/>
  <text x="93" y="335" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 335)" text-anchor="middle">Cửa hàng / CSKH</text>

  <line x1="75" y1="580" x2="1460" y2="580" stroke="#cbd5e0" stroke-width="1"/>
  <rect x="75" y="410" width="30" height="170" fill="#edf2f7"/>
  <text x="93" y="495" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 495)" text-anchor="middle">Giám định QC</text>

  <rect x="75" y="580" width="30" height="170" fill="#edf2f7"/>
  <text x="93" y="665" font-size="10" font-weight="bold" fill="#4a5568" transform="rotate(-90 93 665)" text-anchor="middle">Kế toán &amp; Kho</text>

  <!-- Elements -->
  <circle cx="135" cy="165" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="2"/>
  <text x="135" y="200" font-size="10" fill="#22543d" text-anchor="middle">Yêu cầu đổi trả</text>

  <rect x="180" y="310" width="125" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadowC4)"/>
  <text x="242" y="331" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Tiếp nhận sản phẩm</text>
  <text x="242" y="347" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Hóa đơn mua hàng</text>

  <polygon points="335,335 355,315 375,335 355,355" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="355" y="339" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="355" y="370" font-size="9" fill="#744210" text-anchor="middle">G1: Trong 15–30 ngày?</text>

  <rect x="400" y="470" width="125" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadowC4)"/>
  <text x="462" y="491" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Giám định tem mác</text>
  <text x="462" y="507" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Tình trạng sử dụng</text>

  <polygon points="555,495 575,475 595,495 575,515" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="575" y="499" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="575" y="530" font-size="9" fill="#744210" text-anchor="middle">G2: Đủ điều kiện?</text>

  <polygon points="635,495 655,475 675,495 655,515" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="655" y="499" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="655" y="530" font-size="9" fill="#744210" text-anchor="middle">G3: Lỗi do NSX?</text>

  <rect x="710" y="310" width="125" height="50" rx="6" fill="#ffffff" stroke="#38a169" stroke-width="1.5" filter="url(#taskShadowC4)"/>
  <text x="772" y="331" font-size="10" font-weight="bold" fill="#22543d" text-anchor="middle">Đổi sang size mới</text>
  <text x="772" y="347" font-size="10" fill="#22543d" text-anchor="middle">cho khách hàng</text>

  <polygon points="865,335 885,315 905,335 885,355" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="885" y="339" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="885" y="370" font-size="9" fill="#744210" text-anchor="middle">G4: Khách đồng ý size?</text>

  <rect x="940" y="640" width="125" height="50" rx="6" fill="#ffffff" stroke="#d69e2e" stroke-width="1.5" filter="url(#taskShadowC4)"/>
  <text x="1002" y="661" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Lập Phiếu chi</text>
  <text x="1002" y="677" font-size="10" fill="#2d3748" text-anchor="middle">&amp; Hoàn tiền online</text>

  <polygon points="1095,665 1115,645 1135,665 1115,685" fill="#fefcbf" stroke="#b7791f" stroke-width="1.5"/>
  <text x="1115" y="669" font-size="10" font-weight="bold" fill="#744210" text-anchor="middle">X</text>
  <text x="1115" y="700" font-size="9" fill="#744210" text-anchor="middle">G5: Hoàn tiền xong?</text>

  <rect x="1170" y="640" width="125" height="50" rx="6" fill="#ffffff" stroke="#3182ce" stroke-width="1.5" filter="url(#taskShadowC4)"/>
  <text x="1232" y="661" font-size="10" font-weight="bold" fill="#2d3748" text-anchor="middle">Cập nhật WMS</text>
  <text x="1232" y="677" font-size="10" fill="#2d3748" text-anchor="middle">kho hàng lỗi/bán lại</text>

  <circle cx="1370" cy="665" r="18" fill="#c6f6d5" stroke="#22543d" stroke-width="3"/>
  <text x="1370" y="695" font-size="9" font-weight="bold" fill="#22543d" text-anchor="middle">Đóng hồ sơ</text>

  <!-- Flows -->
  <line x1="153" y1="165" x2="242" y2="165" stroke="#2d3748" stroke-width="1.5"/>
  <line x1="242" y1="165" x2="242" y2="310" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <line x1="305" y1="335" x2="335" y2="335" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <path d="M 355 355 L 355 495 L 400 495" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <line x1="525" y1="495" x2="555" y2="495" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <line x1="595" y1="495" x2="635" y2="495" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <path d="M 655 475 L 655 335 L 710 335" fill="none" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <line x1="835" y1="335" x2="865" y2="335" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <path d="M 885 355 L 885 665 L 940 665" fill="none" stroke="#e53e3e" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <line x1="1065" y1="665" x2="1095" y2="665" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <line x1="1135" y1="665" x2="1170" y2="665" stroke="#38a169" stroke-width="1.5" marker-end="url(#arrowC4)"/>
  <line x1="1295" y1="665" x2="1352" y2="665" stroke="#2d3748" stroke-width="1.5" marker-end="url(#arrowC4)"/>

  <text x="750" y="770" font-size="12" font-style="italic" fill="#718096" text-anchor="middle">Hình 3.3: Sơ đồ BPMN 2.0 quy trình Tiếp nhận Đổi trả, Bảo hành và Hoàn tiền ACFC (C4).</text>
</svg>'''
    with open("diagrams/bpmn-doi-tra-hoan-tien-c4.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# ----------------------------------------------------------------------
# DRAWIO GENERATORS FOR M3, C3, C4
# ----------------------------------------------------------------------
def generate_m3_drawio():
    xml = '''<mxfile host="app.diagrams.net" modified="2026-08-14T12:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="M3_Merchandise" name="ACFC M3 Merchandise Planning">
    <mxGraphModel dx="1500" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1500" pageHeight="800" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="pool_m3" value="ACFC – KHỐI HOẠCH ĐỊNH &amp; PHÂN BỔ HÀNG HÓA (M3)" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;startSize=30;horizontal=0;containerType=tree;fontSize=13;fontStyle=1;fillColor=#3182ce;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1420" height="650" as="geometry"/>
        </mxCell>
        <mxCell id="lane_prod_exec" value="Product Exec" style="swimlane;html=1;startSize=25;fillColor=#f8f9fa;" vertex="1" parent="pool_m3">
          <mxGeometry x="30" y="0" width="1390" height="160" as="geometry"/>
        </mxCell>
        <mxCell id="start_m3" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;strokeWidth=2;" vertex="1" parent="lane_prod_exec">
          <mxGeometry x="40" y="60" width="35" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="task_sellthru" value="Phân tích Sell-through&#xa;&amp; Weeks of Supply" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;" vertex="1" parent="lane_prod_exec">
          <mxGeometry x="110" y="53" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g1_kpi" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_prod_exec">
          <mxGeometry x="270" y="58" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_sku_list" value="Lập danh mục SKU&#xa;Hero / Core theo mùa" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;" vertex="1" parent="lane_prod_exec">
          <mxGeometry x="340" y="53" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="lane_alloc" value="Allocation Team" style="swimlane;html=1;startSize=25;fillColor=#ffffff;" vertex="1" parent="pool_m3">
          <mxGeometry x="30" y="160" width="1390" height="160" as="geometry"/>
        </mxCell>
        <mxCell id="task_alloc_matrix" value="Lập ma trận phân bổ&#xa;cho 100+ Store" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;" vertex="1" parent="lane_alloc">
          <mxGeometry x="560" y="55" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g3_limit" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_alloc">
          <mxGeometry x="720" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="g5_transfer" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_alloc">
          <mxGeometry x="1010" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_alloc_order" value="Xuất Lệnh phân bổ&#xa;Allocation Order" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;" vertex="1" parent="lane_alloc">
          <mxGeometry x="1080" y="55" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g6_wms_sync" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_alloc">
          <mxGeometry x="1230" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="end_m3" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;strokeWidth=3;" vertex="1" parent="lane_alloc">
          <mxGeometry x="1330" y="63" width="35" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="lane_comm_dir" value="Commercial Dir" style="swimlane;html=1;startSize=25;fillColor=#f8f9fa;" vertex="1" parent="pool_m3">
          <mxGeometry x="30" y="320" width="1390" height="160" as="geometry"/>
        </mxCell>
        <mxCell id="g2_otb_appr" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_comm_dir">
          <mxGeometry x="490" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="lane_store_mgr" value="Store Manager" style="swimlane;html=1;startSize=25;fillColor=#ffffff;" vertex="1" parent="pool_m3">
          <mxGeometry x="30" y="480" width="1390" height="170" as="geometry"/>
        </mxCell>
        <mxCell id="task_store_fb" value="Store phản hồi&#xa;nhu cầu size/màu" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;" vertex="1" parent="lane_store_mgr">
          <mxGeometry x="790" y="55" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g4_store_agree" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_store_mgr">
          <mxGeometry x="950" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    with open("diagrams/bpmn-hoach-dinh-phan-bo-hang-hoa-m3.drawio", "w", encoding="utf-8") as f:
        f.write(xml)

def generate_c3_drawio():
    xml = '''<mxfile host="app.diagrams.net" modified="2026-08-14T12:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="C3_OmniSales" name="ACFC C3 Omnichannel Sales">
    <mxGraphModel dx="1500" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1500" pageHeight="800" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="pool_cust_c3" value="KHÁCH HÀNG (CUSTOMER)" style="swimlane;html=1;startSize=25;fillColor=#fefcbf;strokeColor=#d69e2e;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1420" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="start_c3" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;strokeWidth=2;" vertex="1" parent="pool_cust_c3">
          <mxGeometry x="50" y="55" width="35" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="g1_channel" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="pool_cust_c3">
          <mxGeometry x="120" y="53" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="pool_acfc_c3" value="ACFC – HỆ THỐNG BÁN HÀNG &amp; THANH TOÁN (C3)" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;startSize=30;horizontal=0;containerType=tree;fontSize=13;fontStyle=1;fillColor=#2d3748;" vertex="1" parent="1">
          <mxGeometry x="40" y="210" width="1420" height="490" as="geometry"/>
        </mxCell>
        <mxCell id="lane_advisor" value="Tư vấn / Web App" style="swimlane;html=1;startSize=25;fillColor=#f8f9fa;" vertex="1" parent="pool_acfc_c3">
          <mxGeometry x="30" y="0" width="1390" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="task_check_pos" value="Tư vấn thử size&#xa;&amp; Kiểm tra tồn POS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_advisor">
          <mxGeometry x="170" y="50" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g2_pos_stock" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_advisor">
          <mxGeometry x="330" y="55" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="lane_cashier" value="Thu ngân / POS" style="swimlane;html=1;startSize=25;fillColor=#ffffff;" vertex="1" parent="pool_acfc_c3">
          <mxGeometry x="30" y="150" width="1390" height="170" as="geometry"/>
        </mxCell>
        <mxCell id="task_scan_member" value="Quét Barcode/RFID&#xa;&amp; Nhận diện Member" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_cashier">
          <mxGeometry x="400" y="55" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g3_voucher" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_cashier">
          <mxGeometry x="560" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="g4_payment_type" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_cashier">
          <mxGeometry x="640" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_invoice_deduct" value="Xuất e-Invoice &amp;&#xa;Trừ tồn Real-time" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#38a169;" vertex="1" parent="lane_cashier">
          <mxGeometry x="940" y="55" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g6_member_pts" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_cashier">
          <mxGeometry x="1100" y="60" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="end_c3" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;strokeWidth=3;" vertex="1" parent="lane_cashier">
          <mxGeometry x="1220" y="63" width="35" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="lane_gateway" value="Cổng Thanh toán" style="swimlane;html=1;startSize=25;fillColor=#f8f9fa;" vertex="1" parent="pool_acfc_c3">
          <mxGeometry x="30" y="320" width="1390" height="170" as="geometry"/>
        </mxCell>
        <mxCell id="task_pay_process" value="Xử lý thanh toán&#xa;Thẻ / QR / Payoo" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_gateway">
          <mxGeometry x="710" y="60" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g5_pay_success" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_gateway">
          <mxGeometry x="860" y="65" width="40" height="40" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    with open("diagrams/bpmn-ban-hang-da-kenh-c3.drawio", "w", encoding="utf-8") as f:
        f.write(xml)

def generate_c4_drawio():
    xml = '''<mxfile host="app.diagrams.net" modified="2026-08-14T12:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="C4_Returns" name="ACFC C4 Returns and Refunds">
    <mxGraphModel dx="1500" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1500" pageHeight="800" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="pool_cust_c4" value="KHÁCH HÀNG (CUSTOMER)" style="swimlane;html=1;startSize=25;fillColor=#fefcbf;strokeColor=#d69e2e;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1420" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="start_c4" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;strokeWidth=2;" vertex="1" parent="pool_cust_c4">
          <mxGeometry x="50" y="55" width="35" height="35" as="geometry"/>
        </mxCell>
        <mxCell id="pool_acfc_c4" value="ACFC – XỬ LÝ ĐỔI TRẢ &amp; HOÀN TIỀN (C4)" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;startSize=30;horizontal=0;containerType=tree;fontSize=13;fontStyle=1;fillColor=#2d3748;" vertex="1" parent="1">
          <mxGeometry x="40" y="210" width="1420" height="490" as="geometry"/>
        </mxCell>
        <mxCell id="lane_store_cskh" value="Cửa hàng / CSKH" style="swimlane;html=1;startSize=25;fillColor=#f8f9fa;" vertex="1" parent="pool_acfc_c4">
          <mxGeometry x="30" y="0" width="1390" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="task_rcv_prod" value="Tiếp nhận sản phẩm&#xa;&amp; Hóa đơn mua hàng" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_store_cskh">
          <mxGeometry x="110" y="50" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g1_days_check" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_store_cskh">
          <mxGeometry x="270" y="55" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_swap_size" value="Đổi sang size mới&#xa;cho khách hàng" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#38a169;" vertex="1" parent="lane_store_cskh">
          <mxGeometry x="640" y="50" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g4_cust_agree" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_store_cskh">
          <mxGeometry x="790" y="55" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="lane_qc" value="Giám định QC" style="swimlane;html=1;startSize=25;fillColor=#ffffff;" vertex="1" parent="pool_acfc_c4">
          <mxGeometry x="30" y="150" width="1390" height="170" as="geometry"/>
        </mxCell>
        <mxCell id="task_qc_check" value="Giám định tem mác&#xa;&amp; Tình trạng sử dụng" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_qc">
          <mxGeometry x="330" y="60" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g2_qualify" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_qc">
          <mxGeometry x="490" y="65" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="g3_mfg_fault" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_qc">
          <mxGeometry x="570" y="65" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="lane_acc_wh" value="Kế toán &amp; Kho" style="swimlane;html=1;startSize=25;fillColor=#f8f9fa;" vertex="1" parent="pool_acfc_c4">
          <mxGeometry x="30" y="320" width="1390" height="170" as="geometry"/>
        </mxCell>
        <mxCell id="task_refund_online" value="Lập Phiếu chi&#xa;&amp; Hoàn tiền online" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d69e2e;" vertex="1" parent="lane_acc_wh">
          <mxGeometry x="870" y="60" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="g5_refund_done" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fefcbf;strokeColor=#b7791f;fontStyle=1;" vertex="1" parent="lane_acc_wh">
          <mxGeometry x="1030" y="65" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="task_wms_return_update" value="Cập nhật WMS&#xa;kho hàng lỗi/bán lại" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#3182ce;" vertex="1" parent="lane_acc_wh">
          <mxGeometry x="1100" y="60" width="125" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="end_c4" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#c6f6d5;strokeColor=#22543d;strokeWidth=3;" vertex="1" parent="lane_acc_wh">
          <mxGeometry x="1270" y="68" width="35" height="35" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    with open("diagrams/bpmn-doi-tra-hoan-tien-c4.drawio", "w", encoding="utf-8") as f:
        f.write(xml)

if __name__ == "__main__":
    generate_architecture()
    generate_bpmn_master_warehouse()
    generate_bpmn_s3()
    generate_bpmn_s1()
    generate_bpmn_m3()
    generate_bpmn_c3()
    generate_bpmn_c4()
    generate_m3_drawio()
    generate_c3_drawio()
    generate_c4_drawio()
    print("All ACFC BPMN Diagrams (Draw.io XML and SVG) generated completely.")
