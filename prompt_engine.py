#Library for GenAI
import google.generativeai as genai

#configuring Gemini API ket
gemini_api_key = "AIzaSyCr8G-Kag_P-SlJruYxFUlbeB61_RZ6JRM"
genai.configure(api_key = gemini_api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash-001")

#create a function to define the prompts
def run_prompt(prompt_type , user_input):
    if prompt_type == "Zero-Shot":
        prompt = f"{user_input}"
    elif prompt_type == "Few-shot":
        prompt = (
            "Q: who is the president of India \n\n"
            "A: Ms. Draupadi Murmu"
            "Q: who is the president of US \n\n"
            "A: Mr.Donald Trump"
            f"Q:{user_input}\n"
            "A: "
        )
    elif prompt_type == "Instruction - Based":
        prompt = (
            "Instruction : Summarize my article in 3 bullet point"
            f"Text: {user_input}"
        )
    elif prompt_type == "Chain-of-Thought":
        prompt = (
            "Solve the neural network backpropagation equation step by step"
            f"Text:{user_input}"
        )
    elif prompt_type == "Role-based":
        prompt = (
            "you are a real estate consultant, pls tell me where and why should i purchase a property in Gurgaon"
            f"text:{user_input}"
        )
    else:
        prompt = user_input

    response = model.generate_content(prompt)
    return response.text.strip()