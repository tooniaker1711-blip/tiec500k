import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(
    page_title="Hệ thống Quản lý Soạn đồ_Dr BÌNH",
    page_icon="🍽️",
    layout="wide"
)

# ==========================================
# KHỞI TẠO DỮ LIỆU (SESSION STATE)
# ==========================================
if "items_data" not in st.session_state:
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

if "history_log" not in st.session_state:
    st.session_state.history_log = [
        {"Thời gian": "2023-10-01 08:00:00", "Hành động": "Khởi tạo checklist tiệc 500 khách", "Người thực hiện": "Admin"}
    ]

if "party_info" not in st.session_state:
    st.session_state.party_info = {
        "ten_tiec": "Tiệc Cưới 500 Khách",
        "ngay_to_chuc": datetime.today(),
        "nguoi_phu_trach": "Nhóm Soạn Đồ 1 & 2"
    }

data = st.session_state.items_data

# ==========================================
# GIAO DIỆN HEADER 
# ==========================================
st.markdown("<h1>[🏩] Hệ thống Quản lý Soạn đồ_Dr BÌNH</h1>", unsafe_allow_html=True)
st.success(f"✅ Đang quản lý: **{st.session_state.party_info['ten_tiec']}** - Phụ trách: {st.session_state.party_info['nguoi_phu_trach']}.")

# Các Tabs chức năng
tabs = st.tabs([
    "📊 Tổng quan", 
    "⚙️ Cấu hình Yến tiệc", 
    "📋 Danh sách Checklist", 
    "➕ Thêm/Sửa Hạng mục", 
    "📝 Cập nhật Tiến độ", 
    "📜 Lịch sử Thao tác"
])

# ==========================================
# TAB 0: TỔNG QUAN
# ==========================================
with tabs[0]:
    tong_hang_muc = len(data)
    hoan_thanh = sum(1 for item in data.values() if item["đã_soạn"] >= item["cần"])
    dang_soan = sum(1 for item in data.values() if 0 < item["đã_soạn"] < item["cần"])
    chua_soan = sum(1 for item in data.values() if item["đã_soạn"] == 0)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.caption("Tổng số hạng mục")
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
        st.caption("Hư hỏng / Bổ sung")
        st.subheader("0")

    tien_do = hoan_thanh / tong_hang_muc if tong_hang_muc > 0 else 0
    st.caption(f"**Tiến độ tổng thể: Đã hoàn thành {hoan_thanh}/{tong_hang_muc} hạng mục ({int(tien_do*100)}%)**")
    st.progress(tien_do)
    st.markdown("---")
    
    st.subheader("Trạng thái chi tiết từng vật dụng")
    cols = st.columns(6)
    for idx, (ten_do, thong_tin) in enumerate(data.items()):
        col_index = idx % 6
        can = thong_tin["cần"]
        da_soan = thong_tin["đã_soạn"]
        nhom = thong_tin["nhóm"]
        
        if da_soan >= can:
            dot = "🟢"
        elif 0 < da_soan < can:
            dot = "🟡"
        else:
            dot = "🔴"
            
        with cols[col_index]:
            st.markdown(f"**{dot} {ten_do}**")
            st.caption(f"*{nhom}*")
            st.write(f"{da_soan} / {can}")
            st.write("") 

# ==========================================
# TAB 1: CẤU HÌNH YẾN TIỆC
# ==========================================
with tabs[1]:
    st.subheader("Cài đặt thông tin chung của Yến tiệc")
    with st.form("form_cau_hinh"):
        col_ch1, col_ch2 = st.columns(2)
        with col_ch1:
            ten = st.text_input("Tên sự kiện / Tiệc", value=st.session_state.party_info['ten_tiec'])
            khach = st.number_input("Số lượng khách dự kiến", value=500, step=50)
        with col_ch2:
            ngay = st.date_input("Ngày tổ chức", value=st.session_state.party_info['ngay_to_chuc'])
            phu_trach = st.text_input("Đội ngũ/Người phụ trách", value=st.session_state.party_info['nguoi_phu_trach'])
            
        submit_cau_hinh = st.form_submit_button("Lưu Cấu Hình")
        if submit_cau_hinh:
            st.session_state.party_info.update({
                "ten_tiec": ten, "ngay_to_chuc": ngay, "nguoi_phu_trach": phu_trach
            })
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.history_log.append({"Thời gian": now, "Hành động": f"Cập nhật cấu hình tiệc: {ten}", "Người thực hiện": phu_trach})
            st.success("Cập nhật thông tin tiệc thành công!")
            st.rerun()

# ==========================================
# TAB 2: DANH SÁCH CHECKLIST
# ==========================================
with tabs[2]:
    st.subheader("Bảng tổng hợp vật dụng cần chuẩn bị")
    df_list = []
    for k, v in data.items():
        thieu = v['cần'] - v['đã_soạn']
        df_list.append({
            "Nhóm": v['nhóm'],
            "Tên vật dụng": k,
            "Cần chuẩn bị": v['cần'],
            "Đã soạn": v['đã_soạn'],
            "Còn thiếu": thieu if thieu > 0 else 0,
            "Trạng thái": "✅ Hoàn tất" if v['đã_soạn'] >= v['cần'] else ("⚠️ Đang soạn" if v['đã_soạn'] > 0 else "❌ Chưa soạn")
        })
    if df_list:
        df = pd.DataFrame(df_list)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("Chưa có danh sách vật dụng.")

# ==========================================
# TAB 3: THÊM / SỬA HẠNG MỤC
# ==========================================
with tabs[3]:
    st.subheader("Quản lý danh sách đồ cần soạn")
    col_add1, col_add2 = st.columns(2)
    
    with col_add1:
        st.write("**Thêm vật dụng mới**")
        with st.form("form_them"):
            new_name = st.text_input("Tên vật dụng mới")
            new_group = st.selectbox("Thuộc nhóm", ["Khăn vải", "Vật dụng bàn", "Bàn ghế", "Nước uống", "Khác"])
            new_target = st.number_input("Số lượng cần", min_value=1, value=50)
            if st.form_submit_button("Thêm vào danh sách"):
                if new_name and new_name not in st.session_state.items_data:
                    st.session_state.items_data[new_name] = {"cần": new_target, "đã_soạn": 0, "nhóm": new_group}
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    st.session_state.history_log.append({"Thời gian": now, "Hành động": f"Thêm mới: {new_name} ({new_target} cái)", "Người thực hiện": "Nhân viên"})
                    st.success(f"Đã thêm {new_name}!")
                    st.rerun()
                else:
                    st.error("Tên vật dụng bị trống hoặc đã tồn tại!")

    with col_add2:
        st.write("**Chỉnh sửa chỉ tiêu (Số lượng cần)**")
        edit_name = st.selectbox("Chọn vật dụng cần sửa", list(data.keys()))
        if edit_name:
            current_target = data[edit_name]['cần']
            with st.form("form_sua"):
                edit_target = st.number_input("Chỉ tiêu mới", min_value=1, value=current_target)
                if st.form_submit_button("Cập nhật chỉ tiêu"):
                    st.session_state.items_data[edit_name]['cần'] = edit_target
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    st.session_state.history_log.append({"Thời gian": now, "Hành động": f"Sửa chỉ tiêu {edit_name}: {current_target} -> {edit_target}", "Người thực hiện": "Quản lý"})
                    st.success("Đã cập nhật chỉ tiêu!")
                    st.rerun()

# ==========================================
# TAB 4: CẬP NHẬT TIẾN ĐỘ
# ==========================================
with tabs[4]:
    st.subheader("Cập nhật số lượng đồ đã soạn thực tế")
    st.caption("Chỉnh sửa trực tiếp trên cột **Đã soạn** và bấm nút Lưu lại.")
    
    # Tạo DataFrame để edit
    df_progress = pd.DataFrame([
        {"Vật dụng": k, "Nhóm": v['nhóm'], "Cần soạn": v['cần'], "Đã soạn": v['đã_soạn']} 
        for k, v in data.items()
    ])
    
    edited_df = st.data_editor(
        df_progress,
        column_config={
            "Vật dụng": st.column_config.TextColumn(disabled=True),
            "Nhóm": st.column_config.TextColumn(disabled=True),
            "Cần soạn": st.column_config.NumberColumn(disabled=True),
            "Đã soạn": st.column_config.NumberColumn(min_value=0)
        },
        hide_index=True,
        use_container_width=True
    )
    
    if st.button("💾 Lưu Tiến Độ Soạn Đồ", type="primary"):
        changes_made = 0
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for idx, row in edited_df.iterrows():
            item_name = row["Vật dụng"]
            new_val = row["Đã soạn"]
            old_val = st.session_state.items_data[item_name]["đã_soạn"]
            
            if new_val != old_val:
                st.session_state.items_data[item_name]["đã_soạn"] = new_val
                changes_made += 1
                
        if changes_made > 0:
            st.session_state.history_log.append({
                "Thời gian": now, 
                "Hành động": f"Cập nhật tiến độ hàng loạt ({changes_made} mục)", 
                "Người thực hiện": st.session_state.party_info['nguoi_phu_trach']
            })
            st.success(f"✅ Đã lưu tiến độ cho {changes_made} hạng mục!")
            st.rerun()
        else:
            st.info("Không có thay đổi nào để lưu.")

# ==========================================
# TAB 5: LỊCH SỬ THAO TÁC
# ==========================================
with tabs[5]:
    st.subheader("Nhật ký hoạt động hệ thống")
    if st.session_state.history_log:
        df_log = pd.DataFrame(st.session_state.history_log)
        # Đảo ngược để thao tác mới nhất lên đầu
        st.dataframe(df_log.iloc[::-1], use_container_width=True, hide_index=True)
    else:
        st.info("Chưa có lịch sử thao tác.")
