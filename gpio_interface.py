from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

led = 17

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route("/")
def index():
    # Generate a chache buster based on the current time
    cache_buster = int(time.time())
    # Render the index file and pass the cache buster to it
    return render_template("index.html", cache_buster=cache_buster)

@app.route("/on")
def turn_on():
    GPIO.output(led,GPIO.HIGH)
    
    # Generate a chache buster based on the current time
    cache_buster = int(time.time())
    # Render the index file and pass the cache buster to it
    return render_template("index.html", cache_buster=cache_buster)

@app.route("/off")
def turn_off():
    GPIO.output(led,GPIO.LOW)
    
    # Generate a chache buster based on the current time
    cache_buster = int(time.time())
    # Render the index file and pass the cache buster to it
    return render_template("index.html", cache_buster=cache_buster)


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0",port=8080,debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()