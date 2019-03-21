![katoolinv2](https://user-images.githubusercontent.com/10264942/53847666-deb9f180-3fb1-11e9-82fc-b7cba2fe6d4c.png)
# katoolin 
Command line interface (CLI) to install Kali Linux Tools in your desired distribution.

# Quickstart
## Python
The installer will try to setup python if not found, you should ensure it succeeds.
Ensure you have Python 2.x installed as this tool is written in Python. ([python.org/downloads](https://www.python.org/downloads/))

## Install
Execute this in CLI/Terminal to install and run katoolin in few lines
```bash
mkdir ~/_katemp && cd ~/_katemp && \
wget https://git.io/fjf6m -O katoolin.zip && unzip katoolin.zip && sudo ./install.sh && \
cd ~/ && rm -rf ~/_katemp && katoolin
```

# Features
- Install script
- Uninstall script
- Bulk install packages
- Bulk remove packages

# HowTo
## Operating System
Pick your preferred linux operating system you want to deal with.
The katoolin toolset and setup-helper are versatile and try to fit all your needs.

## Tested
- Ubuntu 18.04 (native and vbox)
- Debian Stretch (native and vbox)
- Linux Mint (vbox)
- Raspbian (vbox created from PiDesktop release:2018-11-26 kernel:4.9)

# Execution tasks
## Install
The following tasks will be executed during install:
- Os/Platform detection
- Setting up required Python (stick to 2.7) if necessary
- Adding/Overwriting katoolin as binary

## Setup
The following tasks can be executed in setup menu: 
- Initialising trusted keys for Kalis repositories
- Add Kali (rolling) repositories
- Installs as global command 'katoolin'

# Installation
## Python
Ensure you have Python 2.x installed as this tool is written in Python. ([python.org/downloads](https://www.python.org/downloads/))
The installer will try to setup python if not found, you should ensure it succeeds.
## Bash
```bash
wget https://git.io/fjf6m -O katoolin.zip
unzip katoolin.zip
sudo ./install.sh
```

# Usage

| Target | Command | Note |
|:-:|:-:|:-:|
| Start | `sudo katoolin` |Installing software requires root |
| Choose a listed category | (int) `1-14` |  |
| Choose a listed tool | (int) `1-99` | Actual max number depends on category |
| Install all tools @mainmenu | (int) `0` | Downloading and installing 300+ tools probably cost some time depending on your connection, hardware and os|
| Install all tools @category | (int) `0` | Adding multiple tools probably cost some time depending on your connection, hardware and os |
| Go back | `back` | Step back to the parent menu |
| Go home | `gohome` | Enter the main menu |

# Hint
Some scripts, apps and software elements need interactive decisions, so this install is not totally automisable at the moment.

## Warning
<span style="color:red">
Before updating your base system, ensure to remove all Kali Linux repositories if you want to avoid any kind of update problem.</span>

# Problems? Questions? Improvements?
There are two types of issues available at the github repository site.
## Mandatory
There are mandatory fields you have to fill. If not all mandatory fields are filled, the issue will not be handled.
## Bug Report
Start here:
- [github.com/mko-x/katoolin/newBugReport](https://s.m-ko.de/katoolin-new-bug)
## Feature request
Start here:
- [github.com/mko-x/katoolin/newFeatureRequest](https://s.m-ko.de/kat-new-feat)
