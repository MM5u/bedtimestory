import streamlit as st

st.title("🖼️ 故事绘本")
st.caption("为故事配上插图，让想象力飞翔。")

uploaded_file = st.file_uploader("选择一张温馨的睡前图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="你的睡前绘本", use_column_width=True)
else:
    st.markdown("### 🌌 *等待一张充满想象力的画...*\n\n点击上方按钮上传图片吧！")
