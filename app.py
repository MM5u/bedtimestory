import streamlit as st

# 页面基础配置
st.set_page_config(
    page_title="🌙 睡前故事小屋", 
    page_icon="🌌", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 全局温馨 CSS 样式
st.markdown("""
    <style>
    .main { background-color: #1a1a2e; color: #e0e0e0; }
    h1, h2, h3 { color: #f9d342; text-align: center; }
    
    /* 按钮样式 */
    .stButton>button { 
        background-color: #16213e; 
        color: #f9d342; 
        border: 1px solid #f9d342; 
        border-radius: 20px;
        width: 100%;
    }
    .stButton>button:hover { background-color: #f9d342; color: #1a1a2e; }
    
    /* 文本框样式 */
    .stTextArea textarea { 
        background-color: #16213e; 
        color: #e0e0e0; 
        border: 1px solid #f9d342; 
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 首页欢迎语
st.title("🌙 睡前故事小屋")
st.caption("在这里，你可以记录下睡前最温柔的想法。")
st.markdown("---")

st.markdown("""
    ### 👋 欢迎来到这里！
    在左侧菜单（或左上角 `≡`）中选择：**睡前随笔**
    在这里，我们可以安静地用文字陪伴彼此入睡。
""")

# 底部晚安语
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888; padding: 20px;'>
        🌟 无论今天过得怎样，现在都是休息的时间。晚安，好梦。 🌟
    </div>
    """, 
    unsafe_allow_html=True
)
