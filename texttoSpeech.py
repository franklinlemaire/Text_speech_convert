from gtts import gTTS #Import du module de Text pour la parole
text = "Bonjour les amis comment allez vous ?"
language  = "fr" #choix de la langue

obj = gTTS(text=text, lang=language, slow=False)
obj.save("sample.mp3")


