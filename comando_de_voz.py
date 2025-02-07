import speech_recognition as sr # pip install SpeechRecognition
import pyttsx3 # pip install pyttsx3
import webbrowser
from datetime import datetime

# Pegar audio do microfone
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="pt-BR")
            print(f"Você: {said}")
        except sr.UnknownValueError:
            print("Não entendi.")
            speak("Não entendi.")
        except sr.RequestError:
            print("Serviço não disponível.")
            speak("Serviço não disponível.")
    return said.lower()

# Converter texto em audio
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200) # Velocidade da fala
    engine.setProperty('voice', 'brazil') # Idioma
    engine.say(text)
    engine.runAndWait()

# Comandos por voz
def respond(text):
    if 'youtube' in text:
        print("O que você quer assistir?")
        speak("O que você quer assistir?")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            print(f"Veja o que achei sobre {keyword} no YouTube.")
            speak(f"Veja o que achei sobre {keyword} no YouTube.")
    elif 'google' in text:
        print("Sobre o que você quer pesquisar?")
        speak("Sobre o que você quer pesquisar?")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.google.com/search?q={keyword}"
            webbrowser.get().open(url)
            print(f"Aqui estão os resultados da pesquisa sobre {keyword}")
            speak(f"Aqui estão os resultados da pesquisa sobre {keyword}")
    elif 'horário' in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)
    elif 'tchau' in text:
        print("Tchau tchau.")
        speak("Tchau tchau.")
        exit()
    else:
        print(f"{text}?")
        speak(f"{text}?")

while True:
    print("Qual a ordem, chefe?")
    speak("Qual a ordem, chefe?")
    text = get_audio()
    respond(text)