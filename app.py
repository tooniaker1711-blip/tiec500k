import streamlit as st
import pandas as pd

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(
    page_title="Hệ thống Quản lý Soạn đồ_Dr BÌNH",
    page_icon="🍽️",
    layout="wide"
)

# ==========================================
# DỮ LIỆU MẶC ĐỊNH (Dựa trên yêu cầu của bạn)
# ==========================================
if "items_data" not in st.session_state:
    # Cấu trúc: [Tên vật dụng, Cần soạn, Đã soạn]
    # (Đã soạn được giả lập các số liệu khác nhau để hiển thị đủ 3 màu 🔴 🟡 🟢 như ảnh)
    st.session_state.items_data = {
        # 1. Khăn vải
        "Khăn trải bàn tròn": {"cần": 60, "đã_soạn": 60, "nhóm": "Khăn vải"},
        "Khăn ăn (Napkin)": {"cần": 600, "đã_soạn": 450, "nhóm": "Khăn vải"},
        "Áo bọc ghế": {"cần": 600, "đã_soạn": 0, "nhóm": "Khăn vải"},
        "Nơ ghế": {"cần": 600, "đã_soạn": 0, "nhóm": "Khăn vải"},
        "Khăn lau bàn": {"cần": 30, "đã_soạn": 30, "nhóm": "Khăn vải"},
        
        # 2. Vật dụng trên bàn
        "Chén ăn": {"cần": 600, "đã_soạn": 600, "nhóm": "Vật dụng bàn"},
        "Dĩa lót chén": {"cần": 600, "đã_soạn": 550, "nhóm": "Vật dụng bàn"},
        "Đũa (đôi)": {"cần": 600, "đã_soạn": 600, "nhóm": "Vật dụng bàn"},
        "Muỗng ăn": {"cần": 600, "đã_soạn": 600, "nhóm": "Vật dụng bàn"},
        "Gác đũa/muỗng": {"cần": 600, "đã_soạn": 0, "nhóm": "Vật dụng bàn"},
        "Ly thủy tinh": {"cần": 650, "đã_soạn": 200, "nhóm": "Vật dụng bàn"},
        "Dĩa lớn (dọn món)": {"cần": 275, "đã_soạn": 275, "nhóm": "Vật dụng bàn"},
        "Thố đựng súp/lẩu": {"cần": 55, "đã_soạn": 55, "nhóm": "Vật dụng bàn"},
        "Vá múc súp/canh": {"cần": 110, "đã_soạn": 110, "nhóm": "Vật dụng bàn"},
        "Chén nhỏ (nước chấm)": {"cần": 165, "đã_soạn": 100, "nhóm": "Vật dụng bàn"},
        "Xô đá & kẹp gắp": {"cần": 55, "đã_soạn": 55, "nhóm": "Vật dụng bàn"},
        "Đồ khui bia": {"cần": 55, "đã_soạn": 10, "nhóm": "Vật dụng bàn"},
        "Hũ tăm & Khăn giấy": {"cần": 55, "đã_soạn": 0, "nhóm": "Vật dụng bàn"},
        "Bảng số bàn": {"cần": 55, "đã_soạn": 55, "nhóm": "Vật dụng bàn"},
        
        # 3. Bàn ghế
        "Bàn tròn (1.2m-1.4m)": {"cần": 55, "đã_soạn": 55, "nhóm": "Bàn ghế"},
        "Ghế tiệc": {"cần": 580, "đã_soạn": 580, "nhóm": "Bàn ghế"},
        "Bàn chữ nhật dài": {"cần": 6, "đã_soạn": 2, "nhóm": "Bàn ghế"},
        
        # 4. Nước uống
        "Coca-Cola (lon)": {"cần": 500, "đã_soạn": 500, "nhóm": "Nước uống"},
        "Sprite (lon)": {"cần": 250, "đã_soạn": 250, "nhóm": "Nước uống"},
        "Fanta (lon)": {"cần": 150, "đã_soạn": 0, "nhóm": "Nước uống"},
        "Nước suối (chai)": {"cần": 250, "đã_soạn": 100, "nhóm": "Nước uống"},
        "Bia (lon)": {"cần": 1440, "đã_soạn": 1440, "nhóm": "Nước uống"},
        "Đá viên (bao 20kg)": {"cần": 200, "đã_soạn": 0, "nhóm": "Nước uống"},
    }

data = st.session_state.items_data

# ==========================================
# GIAO DIỆN HEADER (Giống ảnh gốc)
# ==========================================
st.markdown("<h1>[🏩] Hệ thống Quản lý Soạn đồ_Dr BÌNH</h1>", unsafe_allow_html=True)
st.success("✅ Dữ liệu quy chuẩn yến tiệc 500 khách. Trạng thái cập nhật theo thời gian thực.")

# Các Tabs chức năng giống trong ảnh
tabs = st.tabs([
    "📊 Tổng quan", 
    "⚙️ Thiết lập danh sách", 
    "🛏️ Danh mục vật dụng", 
    "➕ Thêm/Sửa đồ", 
    "📝 Cập nhật tiến độ", 
    "📜 Lịch sử thao tác"
])

with tabs[0]:
    # ==========================================
    # TÍNH TOÁN KPI
    # ==========================================
    tong_hang_muc = len(data)
    hoan_thanh = sum(1 for item in data.values() if item["đã_soạn"] >= item["cần"])
    dang_soan = sum(1 for item in data.values() if 0 < item["đã_soạn"] < item["cần"])
    chua_soan = sum(1 for item in data.values() if item["đã_soạn"] == 0)
    
    # Render các cột số liệu (Giống phần "Tổng số phòng, Đang sử dụng...")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.caption("Tổng hạng mục")
        st.subheader(f"{hoan_thanh}/{tong_hang_muc}")
    with col2:
        st.caption("Đang soạn dở (Vàng)")
        st.subheader(f"{dang_soan}")
    with col3:
        st.caption("Đã đủ (Xanh)")
        st.subheader(f"{hoan_thanh}")
    with col4:
        st.caption("Chưa chuẩn bị (Đỏ)")
        st.subheader(f"{chua_soan}")
    with col5:
        st.caption("Hư hỏng / Thiếu")
        st.subheader("0")

    # Thanh Tiến Độ (Progress Bar)
    tien_do = hoan_thanh / tong_hang_muc
    st.caption(f"**Đã hoàn thành {hoan_thanh}/{tong_hang_muc} hạng mục**")
    st.progress(tien_do)
    st.markdown("---")
    
    # ==========================================
    # LƯỚI TRẠNG THÁI (GRID CARD)
    # ==========================================
    st.subheader("Trạng thái các hạng mục")
    
    # Tạo 6 cột trên mỗi hàng y hệt như lưới giao diện Phòng Khách Sạn
    cols = st.columns(6)
    
    for idx, (ten_do, thong_tin) in enumerate(data.items()):
        col_index = idx % 6
        can = thong_tin["cần"]
        da_soan = thong_tin["đã_soạn"]
        nhom = thong_tin["nhóm"]
        
        # Xác định logic màu sắc của dấu chấm
        if da_soan >= can:
            dot = "🟢"  # Đủ số lượng
        elif 0 < da_soan < can:
            dot = "🟡"  # Đang chuẩn bị, còn thiếu
        else:
            dot = "🔴"  # Chưa chuẩn bị tí nào
            
        # Hiển thị vào cột
        with cols[col_index]:
            st.markdown(f"**{dot} {ten_do}**")
            st.caption(f"*{nhom}*")
            st.write(f"{da_soan}/{can}")
            st.write("") # Dòng trống để cách đều đặn giống ảnh
