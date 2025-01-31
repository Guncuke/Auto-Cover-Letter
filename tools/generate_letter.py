from textwrap import wrap
from tools.search import get_supervisor
from tools.generate_response import generate_response


def generate_research_letter(prof_name, university, model, special_pref, resume):
    N = 10
    academic_info = get_supervisor(prof_name, university, N)
    if not academic_info:
        return None

    oppo = "research internship"
    time = "from June to September, 2024"

    system_prompt = f"""
    Input: Information about my resume and the professor
    Output: A quality letter to ask Professor {prof_name} for {oppo} over {time} 

    Take a deep breath. Keep it Concise & Focus on Research Potential

    Your task is to write an email to introduce the me to professor {prof_name} to get {oppo}. I will be available {time} Show these information in the email. 

    You will be provided with the student's resume and information about the professor. Analyze the research potential, academic skills, and unique qualities. Think step by step and analyse carefully. 

    Importance rank: 
    Research experiences & potential: 70%,
    Academic & technical skills: 25% [eg, technical internship/coding skills/analytical skills/modelling skills/past competition results and etc.]; 
    Unique qualities[eg. communication/leadership/responsibility]: 5% - one or two sentences are enough.

    Write the email in an inviting way to showcase the research potential of the student and how it fits/aligns with the professor's research focus. Extract the most competitive and the most fit experience and analyse in priority. Write in good detail and structure. 

    Things to note when writing the email. {special_pref}
    """

    user_prompt = f"Here's the publications by Professor {prof_name} from {university}: {academic_info} \n Here's my resume: {resume}"

    letter = generate_response(system_prompt, user_prompt, model)
    
    return letter
