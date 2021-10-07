import speech_recognition as sr
li = sr.Recognizer()
try:
	with sr.Microphone() as source:
		print("Listening....")
		voice=li.listen(source)
		comm=li.recognize_google(voice)
		comm=command.lower()
		if "alexa" in comm:
			print(comm)
except:
	pass
	
