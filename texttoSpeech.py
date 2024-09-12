from gtts import gTTS #Import du module de Text pour la parole

language = input('Choisissez votre langue ("fr" pour le français et "en" pour l\'anlais) \n')
text = input("Entrer votre texte à transformer en fichier vocal \n")

if (language=="en"):
    obj = gTTS(text=text, lang=language, slow=False)
elif(language=="fr"):
    obj = gTTS(text=text, lang=language, slow=False)   
obj.save("sample.mp3")