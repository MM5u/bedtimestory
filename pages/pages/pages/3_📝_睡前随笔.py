import streamlit as st

st.title("📝 睡前随笔")
st.caption("写下你的故事，愿文字伴你入眠。")

story_text = st.text_area("在这里敲下你的故事...", height=250, placeholder="从前，在一片星空下...")

if story_text:
    st.markdown("---")
    st.markdown(f"### 📖 你的故事：\n\n{story_text}")
    word_count = len(story_text)
    st.caption(f"已写下 {word_count} 个字。")
