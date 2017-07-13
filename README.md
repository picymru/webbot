# webbot - A simple browser controlled robot

This is a very simple Python based robot project for the Raspberry Pi designed for use with the Cam Jam 3 robotics kit. Using gpiozero and CherryPy the program will host it's own web page which can be used to control the robot.

## Kit
 - [Raspberry Pi](https://thepihut.com/collections/raspberry-pi/products/raspberry-pi-3-model-b)
 - [CamJam EduKit 3 - Robotics Kit](https://thepihut.com/products/camjam-edukit-3-robotics)
 - [Official Raspberry Pi Camera](https://thepihut.com/collections/raspberry-pi-camera/products/raspberry-pi-camera-module) (optional but recommended)
 - Wi-Fi connection (Built into the Raspberry Pi 3), or Ethernet connection

## Installation
We've made installing everything you need to get started with our browser controlled robot easy!

	git clone https://codedin.wales/picymru/webbot.git
	cd webbot
	make install

## Usage
Running the project is easy. From your Raspberry Pi command line, run the following:

	python3 webbot.py

Once running, the software will display a web address for you to connect to. By default, and for security purposes, the software will only initially allow connections from the web browser running on the Raspberry Pi by visiting http://localhost:5000

If you know what you're doing, and would like to expose the interface to all devices running on your network, then run the software using the following:

	python3 webbot.py -i 0.0.0.0

This will allow you to control the robot from any device on the same network as your Raspberry Pi at http://raspberrypi.lan:5000

### Control
Once connected in your browser, by default, you can use the following keys on your keyboard to control the robot:

- Arrow keys for forwards, backwards, left turn and right turn
- 'c' key to capture and display an image from the camera if connected
- 'u' key to turn on/off an ultrasonic distance measurement every 2 seconds

## License

This project has been developed by PiCymru as part of our education and learning programme. This project is hereby released under the terms of the MIT License, and is included below

	MIT License

	Copyright (c) 2016 PiCymru

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.

## Support

Have a question? Need assistance? Don't stay stuck! If you do use this project or have any feedback we would love to hear from you, tweet us at [@PiCymru](https://twitter.com/PiCymru) or drop us an [e-mail](mailto:hello@picymru.org.uk)

## Thanks
A big thanks to Tim Richardson & Mike Horne for the fantastic CamJam 3 and Ben Nuttall and the gpiozero team for such a simple library.
