#!/usr/bin/python2.7

class UI:

    def printExit(self):
        print ("Shutdown requested...Goodbye...")

    def printErrorInvalidCommand(self):
        print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

    def printBanner(self):
        print ('''
    \033[1;31m	888               888                      888 d8b          
    \033[1;31m	888               888                      888 Y8P          
    \033[1;31m	888               888                      888  \033[1;36m V2.0            
    \033[1;32m	888  888  8888b.  888888  .d88b.   .d88b.  888 888 88888b.  
    \033[1;32m	888 .88P     "88b 888    d88""88b d88""88b 888 888 888 "88b 
    \033[1;32m	888888K  .d888888 888    888  888 888  888 888 888 888  888 
    \033[33m	888 "88b 888  888 Y88b.  Y88..88P Y88..88P 888 888 888  888 
    \033[33m	888  888 "Y888888  "Y888  "Y88P"   "Y88P"  888 888 888  888 
                                                                

    \033[1;36m+ -- -- +=[ \033[1;32mMaintainer: mko-x | https://mko-x.github.io/katoolin \033[1;36m]=+ -- -- +\033[1;m
    \033[0m+ -- -- +=[ 	\033[1;29m Ka\033[1;mli Linux \033[1;29mTool\033[1;m \033[1;29mIn\033[1;mstaller  	]=+ -- -- +\033[1;m
    \033[0m+ -- -- +=[      Original: https://github.com/LionSec/katoolin    ]=+ -- -- +\033[1;m
            ''')

    def printMainMenu(self):
        print ('''
    1) Adding, removing and updating Kali repositories 
    2) Show categories

    0) Help

                ''')

    def printSourcesMenu(self):
        print ('''
    \033[1;93m[W] Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .\033[1;m

    1) Add kali linux repositories
    2) Update kali linux repositories
    3) Remove all kali linux repositories
    4) View the contents of sources.list file
    5) Repair (first removes then reinstalls Kali repos)

    back) return to main menu

                        ''')

    def printCommands(self):
        print (''' 
    ****************** +Commands+ ******************


    \033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

    \033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

            ''')

    def printCategories(self):
        print ('''
    \033[1;36m**************************** All Categories *****************************\033[1;m

    1) Information Gathering			8) Exploitation Tools
    2) Vulnerability Analysis			9) Forensics Tools
    3) Wireless Attacks				10) Stress Testing
    4) Web Applications				11) Password Attacks
    5) Sniffing & Spoofing				12) Reverse Engineering
    6) Maintaining Access				13) Hardware Hacking
    7) Reporting Tools 				14) Extra
                                        
    0) All

                ''')
        print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

    def printCategoryInfo(self):
        print ('''
    \033[1;36m=+[ Information Gathering\033[1;m

    1) acccheck					30) lbd
    2) ace-voip					31) Maltego Teeth
    3) Amap					32) masscan
    4) Automater					33) Metagoofil
    5) bing-ip2hosts				34) Miranda
    6) braa					35) Nmap
    7) CaseFile					36) ntop
    8) CDPSnarf					37) p0f
    9) cisco-torch					38) Parsero
    10) Cookie Cadger				39) Recon-ng
    11) copy-router-config				40) SET
    12) DMitry					41) smtp-user-enum
    13) dnmap					42) snmpcheck
    14) dnsenum					43) sslcaudit
    15) dnsmap					44) SSLsplit
    16) DNSRecon					45) sslstrip
    17) dnstracer					46) SSLyze
    18) dnswalk					47) THC-IPV6
    19) DotDotPwn					48) theHarvester
    20) enum4linux					49) TLSSLed
    21) enumIAX					50) twofi
    22) exploitdb					51) URLCrazy
    23) Fierce					52) Wireshark
    24) Firewalk					53) WOL-E
    25) fragroute					54) Xplico
    26) fragrouter					55) iSMTP
    27) Ghost Phisher				56) InTrace
    28) GoLismero					57) hping3
    29) goofile

    0) Install all Information Gathering tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryVulnAnaly(self):
        print ('''
    \033[1;36m=+[ Vulnerability Analysis\033[1;m

    1) BBQSQL				18) Nmap
    2) BED					19) ohrwurm
    3) cisco-auditing-tool			20) openvas-administrator
    4) cisco-global-exploiter		21) openvas-cli
    5) cisco-ocs				22) openvas-manager
    6) cisco-torch				23) openvas-scanner
    7) copy-router-config			24) Oscanner
    8) commix				25) Powerfuzzer
    9) DBPwAudit				26) sfuzz
    10) DoonaDot				27) SidGuesser
    11) DotPwn				28) SIPArmyKnife
    12) Greenbone Security Assistant 	29) sqlmap
    13) GSD					30) Sqlninja
    14) HexorBase				31) sqlsus
    15) Inguma				32) THC-IPV6
    16) jSQL				33) tnscmd10g
    17) Lynis				34) unix-privesc-check
                        35) Yersinia

    0) Install all Vulnerability Analysis tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryWirelessAttacks(self):
        print ('''
            \033[1;36m=+[ Wireless Attacks\033[1;m

    1) Aircrack-ng				17) kalibrate-rtl
    2) Asleap				18) KillerBee
    3) Bluelog				19) Kismet
    4) BlueMaho				20) mdk3
    5) Bluepot				21) mfcuk
    6) BlueRanger				22) mfoc
    7) Bluesnarfer				23) mfterm
    8) Bully				24) Multimon-NG
    9) coWPAtty				25) PixieWPS
    10) crackle				26) Reaver
    11) eapmd5pass				27) redfang
    12) Fern Wifi Cracker			28) RTLSDR Scanner
    13) Ghost Phisher			29) Spooftooph
    14) GISKismet				30) Wifi Honey				31) Wifitap
    16) gr-scan				32) Wifite 

    0) Install all Wireless Attacks tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryWebApps(self):
        print ('''
    \033[1;36m=+[ Web Applications\033[1;m

    1) apache-users			21) Parsero
    2) Arachni				22) plecost
    3) BBQSQL				23) Powerfuzzer
    4) BlindElephant			24) ProxyStrike
    5) Burp Suite				25) Recon-ng
    6) commix				26) Skipfish
    7) CutyCapt				27) sqlmap
    8) DAVTest				28) Sqlninja
    9) deblaze				29) sqlsus
    10) DIRB				30) ua-tester
    11) DirBuster				31) Uniscan
    12) fimap				--) NO.Vega
    13) FunkLoad				--) NO:w3af
    14) Grabber				34) WebScarab
    15) jboss-autopwn			35) Webshag
    16) joomscan				36) WebSlayer
    17) jSQL				37) WebSploit
    18) Maltego Teeth			38) Wfuzz
    19) PadBuster				39) WPScan
    20) Paros				40) XSSer
                        41) zaproxy

    0) Install all Web Applications tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategorySniffSpoof(self):
        print ('''
    \033[1;36m=+[ Sniffing & Spoofing\033[1;m

    1) Burp Suite				17) rtpmixsound
    2) DNSChef				18) sctpscan
    3) fiked				19) SIPArmyKnife
    4) hamster-sidejack			20) SIPp
    5) HexInject				21) SIPVicious
    6) iaxflood				22) SniffJoke
    7) inviteflood				23) SSLsplit
    8) iSMTP				24) sslstrip
    9) isr-evilgrade			25) THC-IPV6
    10) mitmproxy				26) VoIPHopper
    11) ohrwurm				27) WebScarab
    12) protos-sip				28) Wifi Honey
    13) rebind				29) Wireshark
    14) responder				30) xspy
    15) rtpbreak				31) Yersinia
    16) rtpinsertsound			32) zaproxy 

    0) Install all Sniffing & Spoofing tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryMaintainAccess(self):
        print ('''
    \033[1;36m=+[ Maintaining Access\033[1;m

    1) CryptCat
    2) Cymothoa
    3) dbd
    4) dns2tcp
    --) NO.httptunnel	
    6) HTTPTunnel
    7) Intersect
    8) Nishang
    9) polenum
    10) PowerSploit
    11) pwnat
    12) RidEnum
    13) sbd
    14) U3-Pwn
    15) Webshells
    16) Weevely

    0) Install all Maintaining Access tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryReportTools(self):
        print ('''
    \033[1;36m=+[ Reporting Tools\033[1;m

    1) CaseFile
    2) CutyCapt
    3) dos2unix
    4) Dradis
    5) KeepNote	
    6) MagicTree
    7) Metagoofil
    8) Nipper-ng
    9) pipal

    0) Install all Reporting Tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryExploitationTools(self):
        print ('''
    \033[1;36m=+[ Exploitation Tools\033[1;m

    1) Armitage
    2) Backdoor Factory
    3) BeEF
    4) cisco-auditing-tool
    5) cisco-global-exploiter	
    6) cisco-ocs
    7) cisco-torch
    8) commix
    9) crackle
    10) jboss-autopwn
    11) Linux Exploit Suggester
    12) Maltego Teeth
    13) SET
    14) ShellNoob
    15) sqlmap
    16) THC-IPV6
    17) Yersinia

    0) Install all Exploitation Tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryForensicTools(self):
        print ('''
    \033[1;36m=+[ Forensics Tools\033[1;m

    1) Binwalk				11) extundelete
    2) bulk-extractor			12) Foremost
    3) Capstone				13) Galleta
    4) chntpw				14) Guymager
    5) Cuckoo				15) iPhone Backup Analyzer
    6) dc3dd				16) p0f
    7) ddrescue				17) pdf-parser
    8) DFF					18) pdfid
    9) diStorm3				19) pdgmail
    10) Dumpzilla				20) peepdf
                        21) RegRipper
                        22) Volatility
                        23) Xplico

    0) Install all Forensics Tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryStress(self):
        print ('''
    \033[1;36m=+[ Stress Testing\033[1;m

    1) DHCPig
    2) FunkLoad
    3) iaxflood
    4) Inundator
    5) inviteflood	
    6) ipv6-toolkit
    7) mdk3
    8) Reaver
    9) rtpflood
    10) SlowHTTPTest
    11) t50
    12) Termineter
    13) THC-IPV6
    14) THC-SSL-DOS 		

    0) Install all Stress Testing tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryPwAttacks(self):
        print ('''
    \033[1;36m=+[ Password Attacks\033[1;m

    1) acccheck				19) Maskprocessor
    2) Burp Suite				20) multiforcer
    3) CeWL				21) Ncrack
    4) chntpw				22) oclgausscrack
    5) cisco-auditing-tool			23) PACK
    6) CmosPwd				24) patator
    7) creddump				25) phrasendrescher
    8) crunch				26) polenum
    9) DBPwAudit				27) RainbowCrack
    10) findmyhash				28) rcracki-mt
    11) gpp-decrypt				29) RSMangler
    12) hash-identifier			30) SQLdict
    13) HexorBase				31) Statsprocessor
    14) THC-Hydra				32) THC-pptp-bruter
    15) John the Ripper			33) TrueCrack
    16) Johnny				34) WebScarab 
    17) keimpx				35) wordlists 
    18) Maltego Teeth			36) zaproxy 

    0) Install all Password Attacks tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryReverse(self):
        print ('''
    \033[1;36m=+[ Reverse Engineering\033[1;m

    1) apktool
    2) dex2jar
    --) NO.diStorm3
    4) edb-debugger
    5) jad	
    6) javasnoop
    --) NO.JD-GUI
    --) NO.OllyDbg
    9) smali
    --) NO.Valgrind
    --) NO.YARA

    0) Install all Reverse Engineering tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryHardware(self):
        print ('''
    \033[1;36m=+[ Hardware Hacking\033[1;m

    1) android-sdk
    2) apktool
    3) Arduino
    4) dex2jar
    5) Sakis3G	
    6) smali

    0) Install all Hardware Hacking tools
                    
                            ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

    def printCategoryExtras(self):
        print ('''
    \033[1;36m=+[ Extra\033[1;m

    1) Wifresti
    2) Squid3
    -----
    R) REMOVE all tools (ATTENTION script doesn't check for dependencies outside of katoolin)
                    ''')
        print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

