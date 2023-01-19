import openai
import os

def chatGPT(iPrompt):
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=iPrompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return completion.choices[0].text

try:
    with open("api.key", "r") as f:
        openai.api_key = f.read()
except:
    print("No API key found.")

vPrompt = ""
while True:
    vPrompt = input("ChatGPT >>> ")
    if vPrompt in ["stop", "s", "exit", "e", "quit", "q", ""] :
        break
    if vPrompt in ["clear", "c", "cls"]:
        os.system("cls")
        continue
    vResponse = chatGPT(vPrompt)
    print("ChatGPT <<< " + vResponse.replace("\n", "") + "\n")
    


