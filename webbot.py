# Web controlled robot by PiCymru (@picymru / http://picymru.org.uk)

import subprocess
import time
import os

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
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(WebControl(), '/', conf)