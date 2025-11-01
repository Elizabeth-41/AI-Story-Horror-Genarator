import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

@st.cache_resource
def init_google_ai():
    """
    Inisialisasi Google AI dengan cache
    """
    try:
        # Load environment variables
        load_dotenv()
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("⚠ Google API Key tidak ditemukan! Silakan tambahkan ke file .env")
            st.stop()
        
        # Configure Google AI
        genai.configure(api_key=api_key)
        
        # Initialize model
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        st.error(f"❌ Error saat menginisialisasi Google AI: {str(e)}")
        st.stop()

def generate_content(topic, selected_emotion, word_count, model):
    """
    Generate konten menggunakan Google Gemini AI
    """
    try:
        # Prompt template untuk AI
        prompt = f"""
        Buatkan Cerita horror yang menarik tentang topik: "{topic}"
        
        Emosi/Tema cerita: {selected_emotion}
        Panjang kata: sekitar {word_count} kata
        
        Format konten:
        1. Judul yang menarik minat penyuka horror dengan tema {selected_emotion}
        2. Pendahuluan singkat dan menegangkan
        3. 3-5 poin utama dengan awal yang santai namun secara bertahap berakhir dengan twist yang menakutkan dan mengejutkan
        4. Kesimpulan
        5. Call to action
        
        Konten harus:
        - Memiliki alur cerita yang menarik dengan nuansa {selected_emotion}
        - Memiliki Plot Twist yang tak terduga
        - Membangun suasana tegang dan misterius
        - Engaging untuk pembaca
        - Panjang sekitar {word_count} kata untuk tiap poin utama
        
        Gunakan bahasa Indonesia yang baik dan benar.
        """
        
        # Generate menggunakan Google AI
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"❌ Terjadi error saat generate konten: {str(e)}"

def run():
    """
    Stage 4: Add AI Integration
    Menambahkan integrasi penuh dengan Google Gemini AI
    """
    
    # Konfigurasi halaman
    st.set_page_config(
        page_title="👻 Horror Story Generator by Fatih",
        page_icon="�",
        layout="wide"
    )
    
    # Custom CSS untuk tema horror
    st.markdown("""
        <style>
        /* Import font horror */
        @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Nosifer&family=Eater&display=swap');
        
        /* Background dan tema gelap */
        .stApp {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a0000 50%, #000000 100%);
            color: #ff0000;
        }
        
        /* Styling untuk judul utama */
        h1 {
            font-family: 'Creepster', cursive !important;
            color: #ff0000 !important;
            text-align: center;
            font-size: 4rem !important;
            text-shadow: 0 0 20px #ff0000, 0 0 30px #ff0000, 0 0 40px #ff0000;
            animation: flicker 2s infinite alternate;
            margin-bottom: 0 !important;
        }
        
        @keyframes flicker {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.8; }
        }
        
        /* Styling untuk teks biasa */
        .stMarkdown p {
            color: #cccccc !important;
            font-size: 1.1rem;
            text-align: center;
        }
        
        /* Styling untuk input boxes */
        .stTextInput input {
            background-color: #1a0000 !important;
            color: #ff6666 !important;
            border: 2px solid #660000 !important;
            border-radius: 10px !important;
            font-size: 1.1rem !important;
        }
        
        .stTextInput input:focus {
            border-color: #ff0000 !important;
            box-shadow: 0 0 15px #ff0000 !important;
        }
        
        /* Styling untuk selectbox */
        .stSelectbox select {
            background-color: #1a0000 !important;
            color: #ff6666 !important;
            border: 2px solid #660000 !important;
            border-radius: 10px !important;
        }
        
        /* Styling untuk slider */
        .stSlider {
            color: #ff0000 !important;
        }
        
        /* Styling untuk tombol */
        .stButton button {
            background: linear-gradient(45deg, #8b0000, #ff0000) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 15px 40px !important;
            font-size: 1.3rem !important;
            font-weight: bold !important;
            box-shadow: 0 0 20px #ff0000 !important;
            transition: all 0.3s ease !important;
            font-family: 'Eater', cursive !important;
        }
        
        .stButton button:hover {
            background: linear-gradient(45deg, #ff0000, #ff6666) !important;
            box-shadow: 0 0 30px #ff0000 !important;
            transform: scale(1.05) !important;
        }
        
        /* Styling untuk info box */
        .stInfo {
            background-color: #1a0000 !important;
            color: #cccccc !important;
            border-left: 5px solid #ff0000 !important;
            border-radius: 10px !important;
        }
        
        /* Styling untuk success message */
        .stSuccess {
            background-color: #001a00 !important;
            color: #00ff00 !important;
            border-left: 5px solid #00ff00 !important;
        }
        
        /* Styling untuk warning */
        .stWarning {
            background-color: #1a1a00 !important;
            color: #ffff00 !important;
            border-left: 5px solid #ffff00 !important;
        }
        
        /* Styling untuk divider */
        hr {
            border-color: #660000 !important;
            box-shadow: 0 0 10px #660000 !important;
        }
        
        /* Styling untuk subheader */
        h3 {
            color: #ff6666 !important;
            font-family: 'Nosifer', cursive !important;
            text-shadow: 0 0 10px #ff0000;
        }
        
        /* Styling untuk columns */
        .stColumn {
            background-color: rgba(26, 0, 0, 0.3);
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #660000;
        }
        
        /* Spinner animation */
        .stSpinner > div {
            border-top-color: #ff0000 !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header dengan emoji horror
    st.markdown("<h1>👻 HORROR STORY GENERATOR 💀</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Teks pembuka dengan styling
    st.markdown("""
        <div style='text-align: center; margin-bottom: 30px;'>
            <p style='font-size: 1.3rem; color: #ff6666;'>🕯️ Selamat datang di dimensi gelap kreativitas... 🕯️</p>
            <p style='font-size: 1.1rem; color: #999999;'>Biarkan AI menciptakan kisah horror yang akan menghantui mimpi Anda</p>
            <p style='font-size: 0.9rem; color: #666666;'>⚠️ Powered by Google Gemini AI ⚠️</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Inisialisasi Google AI
    model = init_google_ai()
    
    # Divider dengan styling horror
    st.markdown("<hr style='margin: 40px 0;'>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center;'>🎭 Konfigurasi Cerita Horror Anda 🎭</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Input dari user - selectbox dan slider
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        selected_emotion = st.selectbox("🎭 Pilih Emosi/Tema", ["Sedih", "Senang", "Takut", "Khawatir", "Marah"])
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        word_count = st.slider("📏 Pilih panjang konten (dalam kata)", 100, 500, 250)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Input teks dari user
    user_topic = st.text_input(
        "�️ Masukkan topik horror Anda:",
        placeholder="Contoh: Rumah tua di ujung desa, Boneka yang hidup, Hantu di sekolah..."
    )
    
    # Tampilkan topik yang dimasukkan user
    if user_topic:
        st.markdown(f"<p style='text-align: center; color: #ff9999;'>🔮 <i>Topik yang akan diproses: <b>{user_topic}</b></i> 🔮</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tombol untuk generate konten (centered)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button("🔥 SUMMON THE STORY 🔥", type="primary", use_container_width=True)
    
    if generate_button:
        if not user_topic.strip():
            st.warning("⚠️ Mohon masukkan topik terlebih dahulu! Cerita tidak bisa muncul dari kekosongan...")
        else:
            # Generate konten menggunakan AI
            with st.spinner("🕯️ AI sedang membangkitkan cerita dari kegelapan... Harap bersabar... 🕯️"):
                hasil_konten = generate_content(user_topic, selected_emotion, word_count, model)
            
            st.success("✅ Cerita horror berhasil diciptakan! Siap untuk dibaca?")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center;'>📖 KISAH DARI KEGELAPAN 📖</h3>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Tampilkan hasil dengan styling
            st.markdown(f"""
                <div style='background-color: rgba(26, 0, 0, 0.8); 
                            padding: 30px; 
                            border-radius: 15px; 
                            border: 2px solid #660000;
                            box-shadow: 0 0 20px rgba(255, 0, 0, 0.3);'>
                    <p style='color: #cccccc; line-height: 1.8; font-size: 1.1rem; white-space: pre-wrap;'>{hasil_konten}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #666666; font-size: 0.9rem;'>👻 Terima kasih telah menggunakan Horror Story Generator 👻</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    run()