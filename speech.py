import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
	print("Please speak");
	audio = r.listen(source);
	print("Thanks")

try:
	print("The text is: "+ r.recognize_google(audio, language = 'ne-NP'));
except:
	pass;