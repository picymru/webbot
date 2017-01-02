#!/usr/bin/env python3

##
# webbot - A browser controlled robot! Your little frIEnd.
##
# Copyright (c) 2016 PiCymru
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess
import time
import os
import socket

import cherrypy
from gpiozero import Robot, DistanceSensor

robot = Robot(left=(10, 9), right=(8, 7))
sensor = DistanceSensor(18, 17)

class WebControl(object):
    @cherrypy.expose
    def left(self):
        robot.left()
        time.sleep(0.2)
        robot.stop()
        return "LEFT TURN"

    @cherrypy.expose
    def right(self):
        robot.right()
        time.sleep(0.2)
        robot.stop()
        return "RIGHT TURN"

    @cherrypy.expose
    def forwards(self):
        robot.forward()
        time.sleep(0.2)
        robot.stop()
        return "FORWARDS"
 
    @cherrypy.expose
    def backwards(self):
        robot.backward()
        time.sleep(0.2)
        robot.stop()
        return "BACKWARDS"

    @cherrypy.expose
    def ultrasonic(self):
        return "{:.2f}".format(sensor.distance)

    @cherrypy.expose
    def cheese(self):
        cherrypy.response.headers['Content-Type'] = 'image/jpeg'
        cherrypy.response.headers['Cache-Control'] = 'no-store'
        with subprocess.Popen(["raspistill", "-vf", "-w", "400", "-h", "300", "-o", "-"], stdout=subprocess.PIPE) as proc:
            return proc.stdout.read()
        return run_output.stdout

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    robot.stop()
    cherrypy.config.update({'server.socket_host': os.getenv('IP', '0.0.0.0')})
    
    # We'll make life easy, and detect the LAN IP to show you where to visit!
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))

    print("Web controlled robot by PiCymru")
    print("Want to control me? In your browser, visit http://{}:8080/static/index.html".format(s.getsockname()[0]))
    
    cherrypy.quickstart(WebControl(), '/', conf)