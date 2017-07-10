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

import os, logging, subprocess, time
from bottle import route, request, response, redirect, hook, error, default_app, view, static_file, template, HTTPError
from gpiozero import Robot, DistanceSensor

@route('/left')
def action_left():
	robot.left()
	time.sleep(0.2)
	robot.stop()
	return "LEFT TURN"

@route('/right')
def action_right():
	robot.right()
	time.sleep(0.2)
	robot.stop()
	return "RIGHT TURN"

@route('/forward')
def action_forward():
	robot.forward()
	time.sleep(0.2)
	robot.stop()
	return "FORWARDS"

@route('/back')
def action_back():
	robot.backward()
	time.sleep(0.2)
	robot.stop()
	return "BACKWARDS"

@route('/ultrasonic')
def ultrasonic():
	return "{:.2f}".format(sensor.distance)

@route('/cheese')
def cheese():
	response.content_type = 'image/jpeg'
	response.cache_control = 'no-store'
	with subprocess.Popen(["raspistill", "-vf", "-w", "400", "-h", "300", "-o", "-"], stdout=subprocess.PIPE) as proc:
		return proc.stdout.read()
	return run_output.stdout

@route('/')
def index():
	return static_file('index.html', root='public')

@route('/style.css')
def index():
	return static_file('style.css', root='public')

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	# Save to file
	parser.add_argument("-i", "--host", default=os.getenv('IP', '127.0.0.1'), help="IP Address")
	parser.add_argument("-p", "--port", default=os.getenv('PORT', 5000), help="Port")

	# Verbose mode
	parser.add_argument("--verbose", "-v", help="increase output verbosity", action="store_true")
	args = parser.parse_args()

	if args.verbose:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.INFO)
	log = logging.getLogger(__name__)

	try:
		robot = Robot(left=(10, 9), right=(8, 7))
		sensor = DistanceSensor(18, 17)
		robot.stop()
	except Exception as e:
		log.error(e)
		exit()

	try:
		app = default_app()
		app.run(host=args.host, port=args.port, server='tornado')
	except:
		log.error("Unable to start server on {}:{}".format(args.host, args.port))