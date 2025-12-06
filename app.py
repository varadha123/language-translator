
from deep_translator import GoogleTranslator
import streamlit as st

# Streamlit UI  
st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌐 Language Translator")

# Input text
text = st.text_input("Enter text to translate:")

# Language options
lang_options = {
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Hindi': 'hi',
    'Chinese (Simplified)': 'zh-CN',
    'Arabic': 'ar',
    'Russian': 'ru',
    'Japanese': 'ja'
}
target_language = st.selectbox("Choose target language:", list(lang_options.keys()))

# Translate
if st.button("Translate"):
    if text:
        try:
            translated = GoogleTranslator(source='auto', target=lang_options[target_language]).translate(text)
            st.success(f"**Translated Text ({target_language}):**\n{translated}")
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter text to translate.")
