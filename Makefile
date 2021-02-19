NAME := webbot

.PHONY: install
install:
	sudo apt-get install python3 python3-pip
	sudo pip3 install -r requirements.txt
