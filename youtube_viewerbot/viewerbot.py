import webbrowser, time
import os
import colorConsole as color
import pyautogui

color = color.mycolors

language = int(input(f"{color.HEADER}Select language \n1- English | 2- Türkçe\n-->{color.ENDC}"))

#English Language
if language==1:
	os.system("cls")
	url = input("Enter video link: ")
	os.system("cls")
	duration = input("Waiting time (seconds): ")
	os.system("cls")
	repeat = input("The number of repetitions: ")
	os.system("cls")
	mute = int(input("Mute the video?\n1-Yes | 2-No\n-->"))
	if mute!=1:
		mute=2

	print("Video link -> "+url+"\nStandby time -> "+duration+" second\nNumber of repetitions -> "+repeat+" time...")
	print("watching starting, 5 seconds...")
	time.sleep(5)

	for i in range(int(repeat)):
		webbrowser.open_new(url)
		time.sleep(int(duration))
		#mute the video
		while mute==1:
			time.sleep(5)
			pyautogui.press("m")
			time.sleep(0.5)
		print(f"{color.OKGREEN}watching Successful{color.ENDC}")

#Türkçe Dil
elif language==2:
	url = input("Video bağlantısını gir: ")
	os.system("cls")
	duration = input("Bekleme süresi (saniye): ")
	os.system("cls")
	tekrar = input("Tekrar sayısı: ")
	os.system("cls")
	mute = int(input("Video sessize alınsın mı?\n1-Evet | 2-Hayır\n-->"))
	if mute!=1:
		mute=2

	print("Video bağlantısı -> "+url+"\nBekleme süresi -> "+duration+" saniye\nTekrar sayısı -> "+tekrar+" kere...")
	print("İzleme başlıyor, 5 saniye...")
	time.sleep(5)

	for i in range(int(tekrar)):
		webbrowser.open_new(url)
		time.sleep(int(duration))
		while mute==1:
			time.sleep(5)
			pyautogui.press("m")
			time.sleep(0.5)
		print(f"{color.OKGREEN}İzleme Başarılı{color.ENDC}")

else:
	os.system("cls")
	exit()