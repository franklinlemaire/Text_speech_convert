from gtts import gTTS #Import du module de Text pour la parole

language = input("Choisissez votre langue \n")
text = input("Entrer votre texte à traduire \n")

if (language=="en"):
    obj = gTTS(text=text, lang=language, slow=False)
elif(language=="fr"):
    obj = gTTS(text=text, lang=language, slow=False)   
obj.save("sample.mp3")


#text = "Bonjour les amis comment allez vous ?"
#language  = "fr" #choix de la langue

obj = gTTS(text=text, lang=language, slow=False)
obj.save("sample.mp3")


