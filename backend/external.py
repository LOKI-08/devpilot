import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])

def chat(query, chatStr, prg=False):    
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("this is sending ",query)
    response = model.generate_content(query)
    response = response.text
    response = response.split("```")
    response = response[1].split("\n")[1:]
    # print(response)
    return '\n'.join(response)