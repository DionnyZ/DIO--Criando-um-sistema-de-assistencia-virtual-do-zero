from gtts import gTTS # pip install gTTS
import playsound # pip install playsound

text_to_say = input("Digite um texto para ser convertido em áudio: ")

language_option = input("Opções de idioma:\n" +
                        "1 - Português\n" +
                        "2 - Inglês\n" +
                        "3 - Espanhol\n" +
                        "4 - Francês\n" +
                        "Selecione um idioma: ")

if language_option == "1":
    language = "pt"
elif language_option == "2":
    language = "en"
elif language_option == "3":
    language = "es"
elif language_option == "4":
    language = "fr"
else:
    print("Opção inválida.")
    exit()

gtts_object = gTTS(text = text_to_say,
                  lang = language,
                  slow = False)

gtts_object.save("audio.mp3")
playsound.playsound("audio.mp3")
