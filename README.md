![katoolinv2](https://user-images.githubusercontent.com/10264942/51780243-46586380-210d-11e9-9bc1-1c6bf66f8e5d.png)
# katoolin 
Command line interface (CLI) to install Kali Linux Tools in your desired distribution.

# Why?
Provide Kali Linux Tools to other distributions than Kali itself.

# HowTo
## Operating System
Pick your preferred operating system you want to deal with.
The katoolin toolset and setup-helper is versatile and tries to fit all your needs.

## Tested
- Ubuntu 18.04 (native and vbox)
- Debian Stretch (native and vbox)
- Linux Mint (vbox)
- Raspbian (vbox created from PiDesktop release:2018-11-26 kernel:4.9)

## Built-In-Preparation
- Setup required Python (stick to 2.7)
- Initialising trusted keys for Kali's repositories
- Add Kali (rolling) repositories
- Setup apt-fast for accelerated bulk installations
- Installs as command 'katoolin'

# Installation
$ wget https://github.com/mko-x/katoolin/releases/download/support-raspbian/katoolin.zip

$ unzip katoolin.zip

$ sudo ./install.sh

# Usage
- start/run: $ sudo katoolin
- 1-99: Choose a listed category
- 1-99: Choose a listed tool
- 0 in Category installs all of its tools
- 0 at home installs all tools of all categories at once (Be careful with size, traffic and time)
- back : Go back
- gohome : Go to the main menu

# Features
- bulk imnstall via zero (0) code (may last some time depending on your connection)
- bulk remove

# Hint
- some scripts, apps, software elements need interactive decisions, so at the moment this install is not totally automisable

## Warning
Before updating your base system, ensure to remove all Kali Linux repositories if you want to avoid any kind of update problem.

# Problems? Questions? Improvements?
- https://github.com/mko-x/katoolin/issues
