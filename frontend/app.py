import streamlit as st
import requests

st.set_page_config(page_title="GenAI Doc Assistant", layout="wide")
st.title("📄 GenAI Smart Research Assistant")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("Uploading and summarizing..."):
        try:
            res = requests.post(
            "http://localhost:8000/upload/",
            files={"file": uploaded_file},
            timeout=60
           )
        except Exception as e:
            st.error(f"❌ Upload failed: {str(e)}")
            st.stop()

        #data = res.json()
        try:
           data = res.json()
        except Exception as e:
            st.error("❌ Backend did not return JSON. Here's the raw response:")
            st.text(res.text)  # See what's coming back
            st.stop()

        text = data["content"]
        st.success("✅ Summary Generated")
        st.info(data["summary"])

        mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

        if mode == "Ask Anything":
            question = st.text_input("Ask a question based on the document:")
            if st.button("Submit Question") and question:
                res = requests.post(
                    "http://localhost:8000/ask/",
                    data={"text": text, "question": question}
                )
                st.markdown("**Answer:**")
                st.write(res.json()["answer"])

        elif mode == "Challenge Me":
            if st.button("Generate Challenge Questions"):
                res = requests.post(
                    "http://localhost:8000/challenge/",
                    data={"text": text}
                )
                st.markdown("### Challenge Questions")
                st.markdown(res.json()["challenge"])
