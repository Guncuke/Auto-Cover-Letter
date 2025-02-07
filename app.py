import streamlit as st
from tools.generate_letter import generate_research_letter
from tools.extract import extract_text


def main():
    st.title("Research Letter Generator")

    # 输入框
    prof_name = st.text_input("Professor's Name", "Kaiming He")
    university = st.text_input("University", "Massachusetts Institute of Technology")
    model = st.text_input("Model", "qwen-max-0125")
    special_pref = st.text_input("Special Preferences", "Try to be close to the professor's research direction.")
    
    # PDF 上传
    resume_file = st.file_uploader("Upload your CV (PDF/DOCX)", type=["pdf", "docx"])
    
    if resume_file:
        # 提取简历文本
        resume = extract_text(resume_file)
        
        # 生成信件
        if st.button("Generate Letter"):
            letter = generate_research_letter(prof_name, university, model, special_pref, resume)
            st.text_area("Generated Letter", letter, height=300)

if __name__ == "__main__":
    main()
