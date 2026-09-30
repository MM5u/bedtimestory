import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import av

st.title("🎙️ 声音日记")
st.caption("录下你的睡前呢喃，把心事说给星星听。")

class AudioRecorder(AudioProcessorBase):
    def __init__(self):
        self.frames = []
        self.is_recording = False
        
    def recv_audio(self, frame: av.AudioFrame) -> av.AudioFrame:
        if self.is_recording:
            self.frames.append(frame.to_ndarray())
        return frame

if "audio_recorder" not in st.session_state:
    st.session_state.audio_recorder = None

webrtc_ctx = webrtc_streamer(
    key="audio-recorder",
    mode=WebRtcMode.SENDRECV,
    audio_processor_factory=AudioRecorder,
    media_stream_constraints={"audio": True, "video": False},
)

if webrtc_ctx.audio_processor:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔴 开始录音"):
            webrtc_ctx.audio_processor.is_recording = True
            st.toast("正在录音...", icon="🎙️")
    with col2:
        if st.button("⏹️ 停止录音"):
            webrtc_ctx.audio_processor.is_recording = False
            st.toast("录音结束！", icon="✅")
            
st.info("💡 提示：由于浏览器安全限制，录音功能需要在 HTTPS 或 localhost 环境下运行。")
