#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, time, py_compile, shutil, sys, platform, threading, subprocess
syslen = len(sys.path)
sys.path.append("./../")
print ("Module LolexToolsMethods is running, using modules os, time, py_compile, shutil, sys, platform, threading.")
print("This module is intended for 9.0nann4, please do not mix and match for compatibility purposes.")
if platform.system() == "Windows":
	if sys.version_info.minor > 5:
		py = "py .\\"
		pyo = "py"
	else:
		py = "python .\\"
		pyo = "python"
	s = "\\"
elif platform.system() == "Linux":
	py = "python3 ./"
	pyo = "python3"
	s = "/"
try:
	import ver
except(ImportError):
	if "arm" in platform.platform() == False:
		pass
	else:
		print("Please redownload this repository to access all features.")
try:
	import menusettings
except(ImportError):
	system = platform.system()
	os.system(py + ".."+ s + "setup" + s + "generic" + s + "LolexToolsInstaller.py")
	exit(0)
class uos:
	uos.useros = platform.system()
	if "arm" in platform.platform():
		uos.useros = "Android"
try:
		import restartsettings, logoffsettings, hibernatesettings, exitsettings, shutdownsettings
except(ImportError):
		pass
def version():
	print(ver.version)
def flicker():
	suretoflash = int(input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy."))
	if suretoflash == 1:
		howlongtoflashfor = int(input("How many loops do you wish to occur?")) 
	print("Here is a list of colours available:")
	print("a - Neon Green")
	print("b - Light Blue")
	print("c - Neon Red")
	print("d - Light Purple/Pink")
	print("e - Neon Yellow")
	print("f - White")
	print("1 - Dark Blue")
	print("2 - Dark Green")
	print("3 - Light Non-Neon Blue")
	print("4 - Dark Red/Brown")
	print("5 - Dark Purple")
	print("6 - Non Neon Yellow")
	print("7 - White/Light Gray")
	print("8 - Dark Gray")
	print("9 - Dark Neon Blue")
	colour = ("color " + input("Please enter your first colour "), "color " + input("Please enter your second colour "), "color " + input("Please enter your third colour "), "color " + input("Please enter your fourth colour "), "color " + input("Please enter your fifth colour  "))
	flickerthread = threading.Thread(target=flickerp2, args=[colour, howlongtoflashfor])
	flickerthread.start()
def flickerp2(colour, howlongtoflashfor):
	currentflashes= int(0)
	while howlongtoflashfor != currentflashes:
		os.system (colour[0])
		time.sleep()
		os.system (colour[1])
		time.sleep()
		os.system (colour[2])
		time.sleep()
		os.system (colour[3])
		time.sleep()
		os.system (colour[4])
		time.sleep()
		currentflashes = currentflashes + 1
	import theme
	os.system(theme.theme)
	exit(0)
def windowspage(page, layout):
	if page == 0:
		print("1  = Settings")
		if restartsettings.hidden == False:
			print("2  = Restart")
		if logoffsettings.hidden == False:
			print("3  = Logoff")
			print("4  = Alternative logoff method")
		if hibernatesettings.hidden == False:
			print("5  = Hibernate")
	elif page == 1:
		if shutdownsettings.hidden == False:
			print("6  = Shutdown")
			print("7  = Alternative shutdown method")		 
		print("8  = Colour Flicker")
		print("9  = Call CMD")
		print("10 = Call documents")
	elif page == 2:
			print("11 = Call a Python shell")
			print("12 = Call Task Manager")
			print("13 = Create folders")
			print("14 = Remove folders")
			print("15 = Create files")
	elif page == 3:
			print("16 = Restart this script")
			print("17 = Perform arithmetic operations")
			print("18 = Call Remote Desktop")
			print("19 = Call Powershell")
			print("20 = Print SystemInfo")
	elif page == 4:
			print("21 = Start Installer")
			if exitsettings.hidden == False:
				print("22 = Exit")
	elif page == 5:
		print("UNSTABLE FEATURES:")
		print("23 = Experimental auto-update")
	if layout == 0:
			print("24 = Next Page")
			print("25 = Back a Page")
	else:
		if page < 5 and page != -1:
			page = page + 1
			windowspage(page, layout)
def linuxpage(page, layout):
	if page == 0:
		print("1  = Settings")
		if restartsettings.hidden == False:
			print("2  = Restart")
		if logoffsettings.hidden == False:
			print("3  = Logoff")
		if hibernatesettings.hidden == False:
			print("4  = Hibernate")
		if shutdownsettings.hidden == False:
			print("5  = Shutdown")
	elif page == 1:
		print("6  = Call a Python Shell")
		print("7  = Create folders")
		print("8  = Remove folders")
		print("9  = Create files")
		print("10 = Restart this script")
	elif page == 2:
		print("11 = Perform arithmetic operations")
		print("12 = Start Installer")
		print("13 = Show Uptime and Average load")
		print("14 = Print SystemInfo")
		if exitsettings.hidden == False:
			print("15 = Exit")
	if layout == 0:
		print("16 = Next Page")
		print("17 = Back a Page")
	else:
		if page < 2 and page != -1:
			page = page + 1
			linuxpage(page, layout)
		else:
			page = 0
			linuxpage (page, layout)
def androidpage(page, layout):
	if page == 0:
		print("1 = Settings")
		if restartsettings.hidden == False:
			print("2  = Restart")
		if shutdownsettings.hidden == False:
			print("3 = Shutdown")
		print("4  = Call a Python Shell")
		print("5  = Create folders")
	elif page == 1:
		print("6  = Remove folders")
		print("7  = Create files")
		print("8 = Restart this script")
		print("9 = Perform arithmetic operations")
		print("10 = Start Installer")
	elif page == 2:
		print("11 = Show Uptime and Average load")
		print("12 = Print SystemInfo")
		if exitsettings.hidden == False:
			print("13 = Exit")
	if layout == 0:
		print("14 = Next Page")
		print("15 = Back a Page")
	else:
		if page < 2 and page != -1:
			page = page + 1
			androidpage(page, layout)
		else:
			page = 0
			androidpage (page, layout)
def restart():
	restart = int(input("Please enter 1 to confirm restart."))
	if restart == 1:
		waittime = int(input("How long, in minutes do you wish to wait?"))
	restartthread = threading.Thread(target = restartthread, args = [waittime])
	restartthread.start()
def logoff(type):
	logoff = input("Please enter 1 to confirm logoff.")
	if logoff == "1":
		waittime = int(input("How long, in minutes do you wish to wait?"))
	loggeroff = threading.Thread(target = logoffthread, args = [waittime, type])
	loggeroff.start()
def logoffthread(waittime, type):
	time.sleep(waittime*60)
	print("LOGOFF thread: Logging off...")
	uos.useros = platform.system()
	if uos.useros != "Linux":
		if type == 0:
			os.system("shutdown -l -f")
		else:
			subprocess.Popen("logoff.exe")
	else:
		os.system("gnome-session-quit --force")
def hibernate():
	hibernate = input("Please enter 1 to confirm logoff.")
	if hibernate == "1":
		waittime = input("How long, in minutes do you wish to wait?")
	hibernatethread = threading.Thread(target = hibernatethread, args = [waittime])
	hibernatethread.start()
def hibernatethread(waittime):
	time.sleep(waittime*60)
	print("HIBERNATE thread: Hibernating...")
	uos.useros = platform.system()
	if uos.useros == "Windows":
		os.system("shutdown -h -f")
	elif uos.useros == "Linux":
		os.system("systemctl suspend")
def restartthread(waittime):
	time.sleep(waittime*60)
	print("RESTART thread: Restarting device...")
	uos.useros = platform.system()
	if uos.useros != "Linux":
		os.system("shutdown -r -f")
	else:
		if "arm" in platform.platform():
			if os.system("su -c reboot") != 0:
				os.system("reboot")
		else:
			os.system("reboot")
def shutdown(type):
	shutdown = input("Please enter 1 to shutdown.")
	if shutdown == "1":
		waittime = int(input("How long, in minutes, do you wish to wait?"))
	shutdownthread = threading.Thread(target = shutdownthread, args = [waittime,type])
	shutdownthread.start()
def shutdownthread(waittime, type):
	time.sleep(waittime*60)
	print("SHUTDOWN thread: shutting device down...")
	if uos.useros == "Windows":
		if type == 0:
			os.system ("shutdown -s -f")
		elif type == 1:
			subprocess.Popen("shutdown.exe")
	elif uos.useros == "Linux":
		os.system("poweroff")
	elif uos.useros == "Android":
		if os.system("su -c reboot -p") != 0:
			if os.system("/system/bin/reboot -p") != 0:
				print("Failed to execute reboot binary.")
def pyshell():
	if uos.useros == "Windows":
		option = input("Please enter 1 for the Python Shell or 0 for the IDLE shell.")
	else:
		option = "0"
	if option == "0":
		subprocess.call(pyo + ".exe")
	elif option == "1":
		subprocess.Popen(pyo + "w.exe")
def scriptrestart():
	confirmscriptrestart = int(input("Please input 1 to confirm restarting of this script."))
	if confirmscriptrestart == 1:
		os.system(py + ".." + s + "start.py")
		exit(0)
def numops():
	print ("Here is a list of operations:")
	print ("1 = Add")
	print ("2 = Take")
	submode = int(input("Please enter the number of the operatino you wish to perform."))
	if submode == 1 or submode == 2:
		addortake()
def addortake():
	startnum = int(input("Please enter your starting number."))
	addortakenum = int(input("Please input the number to be added."))
	endnum = int(input("Please enter your end number."))
	waittime = int(input("How long do you wish to wait before each operation is performed?"))
	if endnum > startnum:
		while endnum > startnum:
			print(startnum)
			if addortakenum < int(0):
				startnum = startnum - addortakenum
			elif addortakenum > int(0):
				startnum = startnum + addortakenum
			time.sleep(waittime)
		if startnum == endnum or startnum > endnum:
			print("The closest number to your target number was:" + (str(startnum)))
			time.sleep (1)
	elif startnum > endnum:
		while startnum > endnum:
			print (startnum)
			if addortakenum < 0:
				startnum = startnum + addortakenum
			if addortakenum > 0:
				startnum = startnum = startnum - addortakenum
			time.sleep (waittime)
		if startnum == endnum or startnum < endnum:
			print ("The closest number to your target end number was:" + (str(startnum)))
			time.sleep (1)
def dumpme():
	if uos.useros == "Windows":
		os.system(".\resources\systeminf")
	elif uos.useros == "Linux":
		os.system("sudo lshw")
	else:
		if os.system("su -c dumpsys") != 0:
			print("Cannot load as much information due to lack of root.")
			if os.system("/system/bin/dumpsys") != 0:
				print("Failed to execute dumpsys binary. Please check your root and SELinux statuses.")
def enterinstall():
	confirm = int(input("Please confirm (with a 1) to enter the installer."))
	if confirm == 1:
		os.system(py + ".." + s + "setup" + s + "generic" + s + "LolexToolsInstaller.py")
		exit(0)
def uptime():
	if "arm" in platform.platform():
		if os.system("su -c uptime") != 0:
			if os.system("/system/bin/uptime") != 0:
				print("Failed to run uptime script.")
	else:
		os.system("uptime")
def logo():
	print("This function has been deprecated.")
def exitnow():
	print("This function has been deprecated.")
def compiler(name):
	try:
		os.remove("./../" + name+".pyc")
	except(IOError):
		pass
	py_compile.compile(name+".py","./../"+name+".pyc")
	os.remove("./../"+name+".py")
def modehide(name, state):
	if state == False:
		newstate = True
	else:
		newstate = False
	try:
		os.remove("./../"+name+".py")
		os.remove("./../"+name+".pyc")
	except(IOError):
		pass
	with open ("./../"+name+"settings.py","a") as outf: 
		outf.write("hidden = ")
		outf.write(str(newstate))
def bak(name, path, reinstall, attrestore, regenerate):
	try:
		os.remove("./../compile.py")
	except(IOError, OSError):
		pass
	if path == 0:
		path = "./../"
	content = os.listdir(path)
	arraypos = 0
	found = False
	while arraypos < len(content):
		if name + ".pyc" in content[arraypos] and len(content[arraypos]) < len(name) + 5:
			found = True
			try:
				os.mkdir("./../Backup")
			except(IOError, OSError):
				pass
			dir1 = ("./../Backup/" + (str(ver.version)) + " " + (str(time.time())) + "/" + name + ".pyc.notpy" + (str(sys.version_info[0])) + (str(sys.version_info[1])))
			os.rename("./../" + name + ".pyc", dir1)
			break;
		arraypos = arraypos + 1
	if found == False:
		print((str(name)) + " not found for backing up.")
	else:
		pass
	if regenerate == 1 and name == "LolexToolsOptions":
		attrestore = 1
		regenerate = 0
		reinstall = 0
	elif name == "verifonboot" or name == "theme" or name == "startplugins" or "settings" in name:
		regenerate = 1
		attrestore = 0
		reinstall = 0
	if "settings" in name:
		if name != "menusettings":
			with open ("./../" + name + ".py", "a") as outf: outf.write("hidden = False")
		else:
			with open ("./../menusettings.py", "a") as outf: outf.write("layout = 0")
		with open ("./../compile.py", "a") as outf:
			outf.write("name = '")
			outf.write(str(name))
			outf.write("'")
		os.system(py + ".." + s + "LolexTools.py")
		exit(None)
	elif name == "verifonboot":
		import LolexToolsOptions
		if LolexToolsOptions.onepintotal > 1:
			oneswappins = True
		else:
			oneswappins = False
		if LolexToolsOptions.onewordtotal > 1:
			oneswapwords = True
		else:
			oneswapwords = False
		if LolexToolsOptions.twopintotal > 1:
			twoswappins = True
		else:
			twoswappins = False
		if LolexToolsOptions.twowordtotal > 1:
			twoswapwords = True
		else:
			twoswapwords = False
		with open ("./../verifonboot.py", "a") as outf:
			outf.write("compiledon = ")
			outf.write(str(ver.version))
			outf.write("\nruntimeone = 0\nruntimetwo = 0\nwordtimeone = 0\nwordtimetwo = 0")
			outf.write("\noneswappins = ")
			outf.write(str(oneswappins))
			outf.write("\noneswapwords = ")
			outf.write(str(oneswapwords))
			outf.write("\ntwoswappins = ")
			outf.write(str(twoswappins))
			outf.write("\ntwoswapwords = ")
			outf.write(str(twoswapwords))
	elif name == "theme":
		# will add theme changing at some point
		with open ("./../theme.py", "a") as outf: pass
	elif name == "startplugins":
		# will add ability to add plugins at some point
		with open ("./../startplugins.py", "a") as outf: pass
	if name == "verifonboot" or name == "theme" or name == "startplugins":
		with open ("./../compile.py", "a") as outf:
			outf.write("name = '")
			outf.write(str(name))
			outf.write("'")
		os.system(py + ".." + s + "LolexTools.py")
		exit(None)
	elif attrestore == 1:
		backup = os.listdir("./../Backup")
		arraypos = 0
		found = False
		while arraypos < len(backup):
			currsub = os.listdir(backup[arraypos])
			tarraypos = 0
			while tarraypos < len(backup):
				if name + ".pyc" in currsub[tarraypos] and (".pycnotpy" + (str(sys.version_info[0])) + (str(sys.version_info[1])) in currsub[tarraypos]) == False:
					found = True
					os.rename("./../Backup" + backup[arraypos] + cursub[tarraypos], "./../" + name + ".pyc")
					with open ("./../compile.py", "a") as outf:
						outf.write("name = '")
						outf.write(str(name))
						outf.write("'")
					os.system(py + ".." + s + "LolexTools.py")
					exit(None)
		if found == False:
			os.system(py + ".." + s + "setup" + s + "generic" + s + "LolexToolsInstaller.py")
			exit(0)
del sys.path[syslen]