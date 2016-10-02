Browser controlled robot
========================

This is a very simple Python based robot project for the Raspberry Pi designed for use with the Cam Jam 3 robotics kit. Using gpiozero and CherryPy the program will host it's own web page which can be used to control the robot.

Hardware required:
 - Raspberry Pi
 - CamJam EduKit 3 robotics kit
 - Official Raspberry Pi camera (optional but recommended)
 - Wi-Fi connection

Software required:
 - CherryPy Python module
 - gpiozero Python module

Cherry Py can be installed with the following command:
pip3 install cherrypy

The gpiozero module comes pre-installed on recent Raspbian releases but can be installed manually if not available with the following command:
sudo apt-get install python3-gpiozero

You can run the project from the command line simply by typing:
python webbot.py

Once running you can connect to the robot from any web browser on the same network as the robot. If your Raspberry Pi has the default network settings you can access it at the following URL:

http://raspberrypi.lan/static/

Once connected you can use the following keys on your keyboard to control the robot:

- Arrow keys for forwards, backwards, left turn and right turn
- 'c' key to capture and display an image from the camera if connected
- 'u' key to turn on/off an ultrasonic distance measurement every 2 seconds

This project has been developed by PiCymru as part of our education and learning programme. We are happy for you to use and adapt this project to your needs but please provide attribution as required.

If you do use this project or have any feedback we would love to hear from you, tweet us at @PiCymru or e-mail us at hello@picymru.org.uk

A big thanks to Tim Richardson & Mike Horne for the fantastic CamJam 3 and Ben Nuttall and the gpiozero team for such a simple library.

Visit us at http://picymru.org.uk/