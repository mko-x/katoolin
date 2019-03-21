# NO LONGER MAINTAINED - DEPRECATED/ARCHIVED

##1
Katoolin is based on hardcoded text representation of the different available tools, keeping that up to date by hand is a horrible and boring job.

##2
There are other tools providing installations of kali linux tools like [Tool-X](https://github.com/Rajkumrdusad/Tool-X).

##3
There will never be a situation where you need all of the kali linux tools at once. In the end only a small subset is necessary for penetration testing or analysis etc.

So you can just get the tools from kali itself from [kali.org/tools-listing](https://tools.kali.org/tools-listing

# katoolin 
![katoolinv2](https://user-images.githubusercontent.com/10264942/54731464-a1975700-4b8e-11e9-99f1-547bbf60f16a.png)

# About 
Command line interface (CLI) to install Kali Linux Tools in your desired distribution.

# Quickstart

## Quick install
Execute this in CLI/Terminal to install katoolin:
```bash
mkdir ~/_katemp && cd ~/_katemp && \
wget https://git.io/fjf6m -O katoolin.zip && unzip katoolin.zip && sudo ./install.sh && \
cd ~/ && rm -rf ~/_katemp
```
## Run
Call this in some CLi:
```bash
$ katoolin
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

# Installation
## Steps of katoolin install script
The following tasks will be executed during install:
- Os/Platform detection
- Setting up required Python (stick to 2.7) if necessary
- Installing katoolin as globally available binary
- HINT: Will override existing katoolin

# Menu

## Setup and manage Kali repos
If you didn't use katoolin yet, you need to initialize Kali repos first
- Fetching trusted keys for Kali's repositories
- Add trusted Kali (rolling) repositories to aptitude
and run katoolin in few lines

## Start to install desired Kali tools
The tools are sorted in categories dpending on their purposes.
Choose what you want.
Even install all at once, but be warned: That takes some time.

# Installation
## Python
The installer will try several ways to setup python if not found, you should ensure it succeeds.
Alternative: Install Python 2.x manually. Find it at ([python.org/downloads](https://www.python.org/downloads/))
## Bash
Download, install and run katoolin within four steps:
```bash
wget https://git.io/fjf6m -O katoolin.zip
unzip katoolin.zip
sudo ./install.sh
katoolin
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
