#!/usr/bin/python2.7

import os
import os.path
import sys, traceback

if "kDEBUG" in os.environ:
	debug = int(os.environ['kDEBUG'])

sys.path.insert(0, '/usr/bin/katlib')

if debug:
	sys.path.insert(0, './katlib')	

from katlib.ui import UI

ui = UI()

# prepare
# colors
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[33m"
cyan = "\033[1;36m"
reset = "\033[0m"

# constants
constants = {
	"aptKey": "ED444FF07D8D0BF6",
	"kaliSourceString": "# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free\n",
	"pathToSourcesList": "/etc/apt/sources.list.d/kali.list"
}

cmdInstall = "apt-get install -y "

# method 1
def reposAdd():
	print ('Fetching key')
	cmd11 = os.system("wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add")
	print ('Cleaning')
	sourcefile = constants["pathToSourcesList"];
	if os.path.isfile(sourcefile):
		print ("Sources list already installed: " + sourcefile)
	else:
		cmd10 = os.system("cp ./tmpl/kali.list " + constants["pathToSourcesList"])
		print('Added sources repo')

# method 2
def updateAptGet():
	cmd20 = os.system("apt-get update")
	cmd21 = os.system("${cmdInstall} -y software-properties-common && apt-get update -m")
	if "Ubuntu" in os.name or "Debian" in os.name:
		cmd5 = os.system("add-apt-repository ppa:apt-fast/stable && apt-get update && apt-get install -y aria2 apt-fast")

# method 3
def removeData():
	cmd30 = os.system("rm " + constants["pathToSourcesList"] + " && apt-get autoclean -y && apt-get update")
	if "Ubuntu" in os.name or "Debian" in os.name:
		cmd11 = os.system("apt-get --purge autoremove aria2 apt-fast")
	print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")

# method 4
def showSources():
	filepath = constants["pathToSourcesList"];
	if os.path.isfile(filepath):
		file = open(filepath, 'r')
		print (file.read())
	else:
		print ("sources file path: " + filepath + " does not exist")

def main():
	try:
		if "Ubuntu" in os.name or "Debian" in os.name:
			cmdInstall = "apt-fast install -y "
		ui.printBanner()
		def enterMainMenu():
			while True:
				ui.printMainMenu()

				choiceMainMenu = raw_input("\033[1;36mkat > \033[1;m")

				while choiceMainMenu == "1":
					ui.printSourcesMenu()
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						reposAdd()
					elif repo == "2":
						updateAptGet()
					elif repo == "3":
						removeData()
					elif repo == "5":
						removeData()
						reposAdd()
						updateAptGet()
					elif repo == "back":
						enterMainMenu()
					elif repo == "gohome":
						enterMainMenu()
					elif repo == "4":
						showSources()
					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						
				def enterCategoryMenu():
					while choiceMainMenu == "2":
						ui.printCategories()
						choiceCategoryMenu = raw_input("\033[1;36mkat > \033[1;m")
						if choiceCategoryMenu == "back":
							enterMainMenu()
						elif choiceCategoryMenu == "gohome":
							enterMainMenu()
						elif choiceCategoryMenu == "0":
							cmd = os.system("${cmdInstall} -qq install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan webscarab websploit wfuzz wpscan xsser burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia cryptcat cymothoa dbd httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/ && rm -Rf ./bing-ip2hosts-0.4*")	
							if "Ubuntu" in os.name:
								cmd3 = os.system("snap install zaproxy --classic")
							else:
								cmd3 = os.system("apt-get -f install zaproxy")
						while choiceCategoryMenu == "1":
							ui.printCategoryInfo()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install acccheck")

							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install -y ace-voip")

							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install -y amap")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install -y automater")
							elif choiceSubCategory == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install -y braa")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install -y casefile")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install -y cdpsnarf")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install -y cisco-torch")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install -y cookie-cadger")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install -y copy-router-config")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install -y dmitry")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install -y dnmap")
							elif choiceSubCategory == "14":
								cmd = os.system("apt-get install -y dnsenum")
							elif choiceSubCategory == "15":
								cmd = os.system("apt-get install -y dnsmap")
							elif choiceSubCategory == "16":
								cmd = os.system("apt-get install -y dnsrecon")
							elif choiceSubCategory == "17":
								cmd = os.system("apt-get install -y dnstracer")
							elif choiceSubCategory == "18":
								cmd = os.system("apt-get install -y dnswalk")
							elif choiceSubCategory == "19":
								cmd = os.system("apt-get install -y dotdotpwn")
							elif choiceSubCategory == "20":
								cmd = os.system("apt-get install -y enum4linux")
							elif choiceSubCategory == "21":
								cmd = os.system("apt-get install -y enumiax")
							elif choiceSubCategory == "22":
								cmd = os.system("apt-get install -y exploitdb")
							elif choiceSubCategory == "23":
								cmd = os.system("apt-get install -y fierce")
							elif choiceSubCategory == "24":
								cmd = os.system("apt-get install -y firewalk")
							elif choiceSubCategory == "25":
								cmd = os.system("apt-get install -y fragroute")
							elif choiceSubCategory == "26":
								cmd = os.system("apt-get install -y fragrouter")
							elif choiceSubCategory == "27":
								cmd = os.system("apt-get install -y ghost-phisher")
							elif choiceSubCategory == "28":
								cmd = os.system("apt-get install -y golismero")
							elif choiceSubCategory == "29":
								cmd = os.system("apt-get install -y goofile")
							elif choiceSubCategory == "30":
								cmd = os.system("apt-get install -y lbd")
							elif choiceSubCategory == "31":
								cmd = os.system("apt-get install -y maltego-teeth")
							elif choiceSubCategory == "32":
								cmd = os.system("apt-get install -y masscan")
							elif choiceSubCategory == "33":
								cmd = os.system("apt-get install -y metagoofil")
							elif choiceSubCategory == "34":
								cmd = os.system("apt-get install -y miranda")
							elif choiceSubCategory == "35":
								cmd = os.system("apt-get install nmap")
							elif choiceSubCategory == "36":
								print ('ntop is unavailable')
							elif choiceSubCategory == "37":
								cmd = os.system("apt-get install p0f")
							elif choiceSubCategory == "38":
								cmd = os.system("apt-get install parsero")
							elif choiceSubCategory == "39":
								cmd = os.system("apt-get install recon-ng")
							elif choiceSubCategory == "40":
								cmd = os.system("apt-get install set")
							elif choiceSubCategory == "41":
								cmd = os.system("apt-get install smtp-user-enum")
							elif choiceSubCategory == "42":
								cmd = os.system("apt-get install snmpcheck")
							elif choiceSubCategory == "43":
								cmd = os.system("apt-get install sslcaudit")
							elif choiceSubCategory == "44":
								cmd = os.system("apt-get install sslsplit")
							elif choiceSubCategory == "45":
								cmd = os.system("apt-get install sslstrip")
							elif choiceSubCategory == "46":
								cmd = os.system("apt-get install sslyze")
							elif choiceSubCategory == "47":
								cmd = os.system("apt-get install thc-ipv6")
							elif choiceSubCategory == "48":
								cmd = os.system("apt-get install theharvester")
							elif choiceSubCategory == "49":
								cmd = os.system("apt-get install tlssled")
							elif choiceSubCategory == "50":
								cmd = os.system("apt-get install twofi")
							elif choiceSubCategory == "51":
								cmd = os.system("apt-get install urlcrazy")
							elif choiceSubCategory == "52":
								cmd = os.system("apt-get install wireshark")
							elif choiceSubCategory == "53":
								cmd = os.system("apt-get install wol-e")
							elif choiceSubCategory == "54":
								cmd = os.system("apt-get install xplico")
							elif choiceSubCategory == "55":
								cmd = os.system("apt-get install ismtp")
							elif choiceSubCategory == "56":
								cmd = os.system("apt-get install intrace")
							elif choiceSubCategory == "57":
								cmd = os.system("apt-get install hping3")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()		
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while choiceCategoryMenu == "2":
							ui.printCategoryVulnAnaly()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install bbqsql")

							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install bed")

							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install cisco-auditing-tool")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install cisco-global-exploiter")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install cisco-ocs")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install cisco-torch")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install copy-router-config")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif choiceSubCategory == "9":
								cmd = os.system("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install doona")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install dotdotpwn")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install greenbone-security-assistant")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gsd.git")
							elif choiceSubCategory == "14":
								cmd = os.system("apt-get install hexorbase")
							elif choiceSubCategory == "15":
								print ("Please download inguma from : http://inguma.sourceforge.net")
							elif choiceSubCategory == "16":
								cmd = os.system("apt-get install jsql")
							elif choiceSubCategory == "17":
								cmd = os.system("apt-get install lynis")
							elif choiceSubCategory == "18":
								cmd = os.system("apt-get install nmap")
							elif choiceSubCategory == "19":
								cmd = os.system("apt-get install ohrwurm")
							elif choiceSubCategory == "20":
								cmd = os.system("apt-get install openvas-administrator")
							elif choiceSubCategory == "21":
								cmd = os.system("apt-get install openvas-cli")
							elif choiceSubCategory == "22":
								cmd = os.system("apt-get install openvas-manager")
							elif choiceSubCategory == "23":
								cmd = os.system("apt-get install openvas-scanner")
							elif choiceSubCategory == "24":
								cmd = os.system("apt-get install oscanner")
							elif choiceSubCategory == "25":
								cmd = os.system("apt-get install powerfuzzer")
							elif choiceSubCategory == "26":
								cmd = os.system("apt-get install sfuzz")
							elif choiceSubCategory == "27":
								cmd = os.system("apt-get install sidguesser")
							elif choiceSubCategory == "28":
								cmd = os.system("apt-get install siparmyknife")
							elif choiceSubCategory == "29":
								cmd = os.system("apt-get install sqlmap")
							elif choiceSubCategory == "30":
								cmd = os.system("apt-get install sqlninja")
							elif choiceSubCategory == "31":
								cmd = os.system("apt-get install sqlsus")
							elif choiceSubCategory == "32":
								cmd = os.system("apt-get install thc-ipv6")
							elif choiceSubCategory == "33":
								cmd = os.system("apt-get install tnscmd10g")
							elif choiceSubCategory == "34":
								cmd = os.system("apt-get install unix-privesc-check")
							elif choiceSubCategory == "35":
								cmd = os.system("apt-get install yersinia")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()						
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")						
							else:
								ui.printErrorInvalidCommand()
								#print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while choiceCategoryMenu == "3":
							ui.printCategoryWirelessAttacks()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install aircrack-ng")

							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install asleap")

							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install bluelog")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluemaho.git")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluepot.git")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install blueranger")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install bluesnarfer")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install bully")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install cowpatty")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install crackle")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install eapmd5pass")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install fern-wifi-cracker")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install ghost-phisher")
							elif choiceSubCategory == "14":
								cmd = os.system("apt-get install giskismet")
							elif choiceSubCategory == "16":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
							elif choiceSubCategory == "17":
								cmd = os.system("apt-get install kalibrate-rtl")
							elif choiceSubCategory == "18":
								cmd = os.system("apt-get install killerbee")
							elif choiceSubCategory == "19":
								cmd = os.system("apt-get install kismet")
							elif choiceSubCategory == "20":
								cmd = os.system("apt-get install mdk3")
							elif choiceSubCategory == "21":
								cmd = os.system("apt-get install mfcuk")
							elif choiceSubCategory == "22":
								cmd = os.system("apt-get install mfoc")
							elif choiceSubCategory == "23":
								cmd = os.system("apt-get install mfterm")
							elif choiceSubCategory == "24":
								cmd = os.system("apt-get install multimon-ng")
							elif choiceSubCategory == "25":
								cmd = os.system("apt-get install pixiewps")
							elif choiceSubCategory == "26":
								cmd = os.system("apt-get install reaver")
							elif choiceSubCategory == "27":
								cmd = os.system("apt-get install redfang")
							elif choiceSubCategory == "28":
								cmd = os.system("apt-get install rtlsdr-scanner")
							elif choiceSubCategory == "29":
								cmd = os.system("apt-get install spooftooph")
							elif choiceSubCategory == "30":
								cmd = os.system("apt-get install wifi-honey")
							elif choiceSubCategory == "31":
								cmd = os.system("apt-get install wifitap")
							elif choiceSubCategory == "32":
								cmd = os.system("apt-get install wifite")
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()						
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "4":
							ui.printCategoryWebApps()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install apache-users")

							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install arachni")

							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install bbqsql")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install blindelephant")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install burpsuite")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install cutycapt")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install davtest")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install deblaze")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install dirb")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install dirbuster")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install fimap")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install funkload")
							elif choiceSubCategory == "14":
								cmd = os.system("apt-get install grabber")
							elif choiceSubCategory == "15":
								cmd = os.system("apt-get install jboss-autopwn")
							elif choiceSubCategory == "16":
								cmd = os.system("apt-get install joomscan")
							elif choiceSubCategory == "17":
								cmd = os.system("apt-get install jsql")
							elif choiceSubCategory == "18":
								cmd = os.system("apt-get install maltego-teeth")
							elif choiceSubCategory == "19":
								cmd = os.system("apt-get install padbuster")
							elif choiceSubCategory == "20":
								cmd = os.system("apt-get install paros")
							elif choiceSubCategory == "21":
								cmd = os.system("apt-get install parsero")
							elif choiceSubCategory == "22":
								cmd = os.system("apt-get install plecost")
							elif choiceSubCategory == "23":
								cmd = os.system("apt-get install powerfuzzer")
							elif choiceSubCategory == "24":
								cmd = os.system("apt-get install proxystrike")
							elif choiceSubCategory == "25":
								cmd = os.system("apt-get install recon-ng")
							elif choiceSubCategory == "26":
								cmd = os.system("apt-get install skipfish")
							elif choiceSubCategory == "27":
								cmd = os.system("apt-get install sqlmap")
							elif choiceSubCategory == "28":
								cmd = os.system("apt-get install sqlninja")
							elif choiceSubCategory == "29":
								cmd = os.system("apt-get install sqlsus")
							elif choiceSubCategory == "30":
								cmd = os.system("apt-get install ua-tester")
							elif choiceSubCategory == "31":
								cmd = os.system("apt-get install uniscan")
							elif choiceSubCategory == "32":
								ui.printErrorInvalidCommand()
								# cmd = os.system("wget https://dist.subgraph.com/downloads/VegaBuild-linux.gtk.x86_64.zip && unzip VegaBuild-linux.gtk.x86_64.zip && cd vega && ./Vega")
							elif choiceSubCategory == "33":
								ui.printErrorInvalidCommand()
								# cmd = os.system("apt-get install -y python-pip && git clone https://github.com/andresriancho/w3af.git && cd w3af/ && ./w3af_console && . /tmp/w3af_dependency_install.sh")
							elif choiceSubCategory == "34":
								cmd = os.system("apt-get install webscarab")
							elif choiceSubCategory == "35":
								print ("Webshag is unavailable")
							elif choiceSubCategory == "36":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/webslayer.git")
							elif choiceSubCategory == "37":
								cmd = os.system("apt-get install websploit")
							elif choiceSubCategory == "38":
								cmd = os.system("apt-get install wfuzz")
							elif choiceSubCategory == "39":
								cmd = os.system("apt-get install wpscan")
							elif choiceSubCategory == "40":
								cmd = os.system("apt-get install xsser")
							elif choiceSubCategory == "41":
								if "Ubuntu" in os.name:
									cmd = os.system("snap install zaproxy --classic")
								else:
									cmd = os.system("apt-get install zaproxy")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()	
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan webscarab websploit wfuzz wpscan xsser")												
								if "Ubuntu" in os.name:
									cmd = os.system("snap install zaproxy --classic")
								else:
									cmd = os.system("apt-get install -y zaproxy")
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "5":
							ui.printCategorySniffSpoof()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install burpsuite")
							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install dnschef")
							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install fiked")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install hamster-sidejack")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install hexinject")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install iaxflood")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install inviteflood")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install ismtp")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install mitmproxy")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install ohrwurm")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install protos-sip")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install rebind")
							elif choiceSubCategory == "14":
								cmd = os.system("apt-get install responder")
							elif choiceSubCategory == "15":
								cmd = os.system("apt-get install rtpbreak")
							elif choiceSubCategory == "16":
								cmd = os.system("apt-get install rtpinsertsound")
							elif choiceSubCategory == "17":
								cmd = os.system("apt-get install rtpmixsound")
							elif choiceSubCategory == "18":
								cmd = os.system("apt-get install sctpscan")
							elif choiceSubCategory == "19":
								cmd = os.system("apt-get install siparmyknife")
							elif choiceSubCategory == "20":
								cmd = os.system("apt-get install sipp")
							elif choiceSubCategory == "21":
								cmd = os.system("apt-get install sipvicious")
							elif choiceSubCategory == "22":
								cmd = os.system("apt-get install sniffjoke")
							elif choiceSubCategory == "23":
								cmd = os.system("apt-get install sslsplit")
							elif choiceSubCategory == "24":
								cmd = os.system("apt-get install sslstrip")
							elif choiceSubCategory == "25":
								cmd = os.system("apt-get install thc-ipv6")
							elif choiceSubCategory == "26":
								cmd = os.system("apt-get install voiphopper")
							elif choiceSubCategory == "27":
								cmd = os.system("apt-get install webscarab")
							elif choiceSubCategory == "28":
								cmd = os.system("apt-get install wifi-honey")
							elif choiceSubCategory == "29":
								cmd = os.system("apt-get install wireshark")
							elif choiceSubCategory == "30":
								cmd = os.system("apt-get install xspy")
							elif choiceSubCategory == "31":
								cmd = os.system("apt-get install yersinia")
							elif choiceSubCategory == "32":
								if "Ubuntu" in os.name:
									cmd = os.system("snap install zaproxy --classic")
								else:
									cmd = os.system("apt-get install zaproxy")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia")  
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "6":
							ui.printCategoryMaintainAccess()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install cryptcat")

							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install cymothoa")

							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install dbd")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install dns2tcp")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install httptunnel")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install intersect")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install nishang")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install polenum")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install powersploit")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install pwnat")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install ridenum")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install sbd")
							elif choiceSubCategory == "14":
								cmd = os.system("apt-get install u3-pwn")
							elif choiceSubCategory == "15":
								cmd = os.system("apt-get install webshells")
							elif choiceSubCategory == "16":
								cmd = os.system("apt-get install weevely")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()   
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} cryptcat cymothoa dbd dns2tcp httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "7":
							ui.printCategoryReportTools()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install casefile")

							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install cutycapt")

							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install dos2unix")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install dradis")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install keepnote")
							elif choiceSubCategory == "6":
								print ("Visit http://www.gremwell.com/sites/default/files/MagicTree-build1814.jar for download")
								#cmd = os.system("apt-get install magictree")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install metagoofil")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install nipper-ng")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install pipal")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()   
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} casefile cutycapt dos2unix dradis keepnote metagoofil nipper-ng pipal")  
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "8":
							ui.printCategoryExploitationTools()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install armitage")
							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install backdoor-factory")
							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install beef-xss")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install cisco-auditing-tool")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install cisco-global-exploiter")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install cisco-ocs")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install cisco-torch")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install crackle")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install jboss-autopwn")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install linux-exploit-suggester")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install maltego-teeth")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install set")
							elif choiceSubCategory == "14":
								cmd = os.system("apt-get install shellnoob")
							elif choiceSubCategory == "15":
								cmd = os.system("apt-get install sqlmap")
							elif choiceSubCategory == "16":
								cmd = os.system("apt-get install thc-ipv6")
							elif choiceSubCategory == "17":
								cmd = os.system("apt-get install yersinia")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()   
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")  						
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "9":
							ui.printCategoryForensicTools()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install binwalk")
							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install bulk-extractor")
							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/capstone.git")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install chntpw")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install cuckoo")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install dc3dd")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install ddrescue")
							elif choiceSubCategory == "8":
								print ('dff is unavailable')
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/distorm3.git")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install dumpzilla")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install extundelete")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install foremost")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install galleta")
							elif choiceSubCategory == "14":
								cmd = os.system("apt-get install guymager")
							elif choiceSubCategory == "16":
								cmd = os.system("apt-get install p0f")
							elif choiceSubCategory == "17":
								cmd = os.system("apt-get install pdf-parser")
							elif choiceSubCategory == "18":
								cmd = os.system("apt-get install pdfid")
							elif choiceSubCategory == "19":
								cmd = os.system("apt-get install pdgmail")
							elif choiceSubCategory == "20":
								cmd = os.system("apt-get install peepdf")
							elif choiceSubCategory == "21":
								print ("Regripper is unavailable")
							elif choiceSubCategory == "22":
								cmd = os.system("apt-get install volatility")
							elif choiceSubCategory == "23":
								cmd = os.system("apt-get install xplico")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()   
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")						
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "10":
							ui.printCategoryStress()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install dhcpig")
							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install funkload")
							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install iaxflood")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/inundator.git")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install inviteflood")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install ipv6-toolkit")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install mdk3")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install reaver")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install rtpflood")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install slowhttptest")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install t50")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install termineter")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install thc-ipv6")
							elif choiceSubCategory == "14":
								cmd = os.system("apt-get install thc-ssl-dos ")    				             										
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()   
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "11":
							ui.printCategoryPwAttacks()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install acccheck")
							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install burpsuite")
							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install cewl")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install chntpw")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install cisco-auditing-tool")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install cmospwd")
							elif choiceSubCategory == "7":
								cmd = os.system("apt-get install creddump")
							elif choiceSubCategory == "8":
								cmd = os.system("apt-get install crunch")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
							elif choiceSubCategory == "10":
								cmd = os.system("apt-get install findmyhash")
							elif choiceSubCategory == "11":
								cmd = os.system("apt-get install gpp-decrypt")
							elif choiceSubCategory == "12":
								cmd = os.system("apt-get install hash-identifier")
							elif choiceSubCategory == "13":
								cmd = os.system("apt-get install hexorbase")
							elif choiceSubCategory == "14":
								cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
							elif choiceSubCategory == "15":
								cmd = os.system("apt-get install john")
							elif choiceSubCategory == "16":
								cmd = os.system("apt-get install johnny")
							elif choiceSubCategory == "17":
								cmd = os.system("apt-get install keimpx")
							elif choiceSubCategory == "18":
								cmd = os.system("apt-get install maltego-teeth")
							elif choiceSubCategory == "19":
								cmd = os.system("apt-get install maskprocessor")
							elif choiceSubCategory == "20":
								cmd = os.system("apt-get install multiforcer")
							elif choiceSubCategory == "21":
								cmd = os.system("apt-get install ncrack")
							elif choiceSubCategory == "22":
								cmd = os.system("apt-get install oclgausscrack")
							elif choiceSubCategory == "23":
								cmd = os.system("apt-get install pack")
							elif choiceSubCategory == "24":
								cmd = os.system("apt-get install patator")
							elif choiceSubCategory == "25":
								cmd = os.system("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
							elif choiceSubCategory == "26":
								cmd = os.system("apt-get install polenum")
							elif choiceSubCategory == "27":
								cmd = os.system("apt-get install rainbowcrack")
							elif choiceSubCategory == "28":
								cmd = os.system("apt-get install rcracki-mt")
							elif choiceSubCategory == "29":
								cmd = os.system("apt-get install rsmangler")
							elif choiceSubCategory == "30":
								print ("Sqldict is unavailable")
							elif choiceSubCategory == "31":
								cmd = os.system("apt-get install statsprocessor")
							elif choiceSubCategory == "32":
								cmd = os.system("apt-get install thc-pptp-bruter")
							elif choiceSubCategory == "33":
								cmd = os.system("apt-get install truecrack")
							elif choiceSubCategory == "34":
								cmd = os.system("apt-get install webscarab")
							elif choiceSubCategory == "35":
								cmd = os.system("apt-get install wordlists")
							elif choiceSubCategory == "36":
								if "Ubuntu" in os.name:
									cmd = os.system("snap install zaproxy --classic")
								else:
									cmd = os.system("apt-get install zaproxy")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()   
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists")
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "12" :
							ui.printCategoryReverse()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install apktool")
							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install dex2jar")
							elif choiceSubCategory == "3":
								print ("python-diStorm3 is not available at present")
								#cmd = os.system("apt-get install python-diStorm3")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install edb-debugger")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install jad")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install javasnoop")
							elif choiceSubCategory == "7":
								print ("JD is not available at present")
								#cmd = os.system("apt-get install JD")
							elif choiceSubCategory == "8":
								print ("OllyDbg is not available at present")
								#cmd = os.system("apt-get install OllyDbg")
							elif choiceSubCategory == "9":
								cmd = os.system("apt-get install smali")
							elif choiceSubCategory == "10":
								print ("Valgrind is not available at present")
								#cmd = os.system("apt-get install Valgrind")
							elif choiceSubCategory == "11":
								print ("YARA is not available at present")
								#cmd = os.system("apt-get install YARA")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()   
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} apktool dex2jar edb-debugger jad javasnoop smali")
							else:
								ui.printErrorInvalidCommand()

						while choiceCategoryMenu == "13" :
							ui.printCategoryHardware()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("apt-get install android-sdk")
							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install apktool")
							elif choiceSubCategory == "3":
								cmd = os.system("apt-get install arduino")
							elif choiceSubCategory == "4":
								cmd = os.system("apt-get install dex2jar")
							elif choiceSubCategory == "5":
								cmd = os.system("apt-get install sakis3g")
							elif choiceSubCategory == "6":
								cmd = os.system("apt-get install smali")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()   
							elif choiceSubCategory == "0":
								cmd = os.system("${cmdInstall} android-sdk apktool arduino dex2jar sakis3g smali")
							else:
								ui.printErrorInvalidCommand()
								
						while choiceCategoryMenu == "14" :
							ui.printCategoryExtras()
							choiceSubCategory = raw_input("\033[1;36mkat > \033[1;m")
							if choiceSubCategory == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print (" ")
							elif choiceSubCategory == "2":
								cmd = os.system("apt-get install squid3")
								print (" ")
							elif choiceSubCategory == "R":
								repo = raw_input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
								if repo == "y":
									cmd = os.system("apt-get --purge --allow-downgrades --allow-remove-essential --allow-change-held-packages -qq autoremove acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/ && rm -Rf bing-ip2hosts-0.*")	
									cmd21 = os.system("apt-get autoclean && apt-get clean")
							elif choiceSubCategory == "back":
								enterCategoryMenu()
							elif choiceSubCategory == "gohome":
								enterMainMenu()

				enterCategoryMenu()
		enterMainMenu()
	except KeyboardInterrupt:
		ui.printExit()
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
	main()
