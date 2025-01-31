from tools.generate_letter import generate_research_letter
from tools.pdf_extract import extract_text_from_pdf


if __name__ == "__main__":
    prof_name = "Kaiming He"
    university = "Massachusetts Institute of Technology"
    model = "qwen-max-0125"
    special_pref = "Try to be close to the professor's research direction."
    resume = extract_text_from_pdf("cv\my_cv.pdf")

    letter = generate_research_letter(prof_name, university, model, special_pref, resume)

    with open("letter.txt", "w") as f:
        f.write(letter)