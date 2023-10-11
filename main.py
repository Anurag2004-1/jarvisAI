
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import openai
import datetime as dt
from config import apikey
import random

chatstr= ""

def chat(query):
# write code to use open ai key to chat with openai
    global chatstr

    print(chatstr)
    openai.api_key = apikey
    # chatstr += f"User: {query}\n"
    chatstr += f"anurag: {query}\n jarvis: "


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"{chatstr}\n"
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0  # Corrected the parameter name
    )

    chatstr +=f"{response.choices[0].message['content']}\n"
    return response.choices[0].message['content']

def ai(prompt):
    openai.api_key = apikey
    text= f"open AI response for prompt: {prompt}\n***************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"{prompt}\n"
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0  # Corrected the parameter name
    )
    # print(response.choices[0].message['content'])
    text +=response.choices[0].message['content']
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    # todo:do increment of prompt for better search
    with open(f"Openai/prompt -{random.randint(1 ,2445749395)}","w")as f:
        f.write(text)


    # # Define the directory path
    # directory_path = "openai"
    #
    # # Create the directory if it doesn't exist
    # if not os.path.exists(directory_path):
    #     os.mkdir(directory_path)
    #
    # # Generate a random filename
    # random_filename = f"prompt-{random.randint(1, 2445749395)}"
    #
    # # Specify the full path to the file
    # full_path = os.path.join(directory_path, random_filename)
    #
    # # Open the file for writing
    # with open(full_path, "w") as f:
    #     # Write data to the file
    #     f.write("Your data here")


def say(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()  as source:
        r.pause_threshold = 1.2  # wait for user to speak for start from .6 sec

        # r.energy_threshold = 100
        # r.adjust_for_ambient_noise(.5)

        audio = r.listen(source)
        try:
            print("recognising.......")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said{query}")
            return query   #return query
        except Exception as E:
            return "1"



if __name__ == '__main__':
    say("hello i am jarvis a.i.")
    while (True):
        print("listening....")
        query = takecommand()
        # query="play raabta"


        sites = [['youtube','https://youtube.com'],['wikipedia','https://wikipedia.com'],['google','https://google.com'],['spotify','spotify:'],['whatsapp','whatsapp:'],['vs code','vscode:']]
        for site in sites:
            if f"open {site[0]}" in query.lower():
                # 1. "open youtube".lower(): This converts the string "open youtube" to lowercase and results in "open youtube"( in lowercase).
                # 2.  query.lower(): This converts the user's input (held in the query variable) to lowercase.
                # 3.The in operator checks if the string from step 1 is contained within the string from step 2
                say(f"opening {site[0]} sir")
                webbrowser.open(site[1])


        songs =[['ik vaari aa ',   ['ik vaari aa', r'C:\Users\ASUS\Downloads\01 - Ik Vaari Aa - DownloadMing.SE.mp3']]  ,  ['raabta',  r'C:\Users\ASUS\Downloads\02 - Raabta (Title Track) - DownloadMing.SE.mp3']]
        #['raabta',  r'C:\Users\ASUS\Downloads\02 - Raabta (Title Track) - DownloadMing.SE.mp3'] r'path'   We use the  r-prefix before the file path to treat it as a raw string, which avoids the need to escape backslashes.
        for song in songs:
            if f"play {song[0]}".lower() in query.lower():

                musicpath=song[1]
                # os.system(f"open{musicpath}")
                say(f"playing {song[0]} sir")
                print(musicpath)
                os.system(f'start "" "{musicpath}"')


        if "the time" in query.lower():
            time= dt.datetime.now().strftime("%H:%M:%S")
            print(dt.MAXYEAR)

            say(f"sir time is {time}")

        if "the time" in query.lower():
            current_time = dt.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {current_time}")



        if "using AI".lower() in query.lower():
            ai(prompt=query)
        elif (query == "1"):
                say("some error occured !! sorry from jarvis")
                break






        else:
            chat(query)







        if "thanks" in query.lower():
            say("welcome")
            break



       #say(query)

