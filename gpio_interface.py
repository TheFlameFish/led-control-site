from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

led = 17


led_status = False

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route("/")
def index():
    global led_status
    
    # Generate a chache buster based on the current time
    cache_buster = int(time.time())
    # Check the LED status
    print(led_status)
    if led_status:
        status_string = "on"
    else:
        status_string = "off"
    print(status_string)

    # Render the index file and pass the cache buster and LED status to it
    return render_template("index.html", cache_buster=cache_buster, status=status_string)

@app.route("/on")
def turn_on():
    global led_status

    GPIO.output(led,GPIO.HIGH)
    led_status = True
    # Generate a chache buster based on the current time
    cache_buster = int(time.time())
    # Render the index file and pass the cache buster to it
    return index()

@app.route("/off")
def turn_off():
    global led_status

    GPIO.output(led,GPIO.LOW)
    led_status = False
    # Generate a chache buster based on the current time
    cache_buster = int(time.time())
    # Render the index file and pass the cache buster to it
    return index()


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0",port=8080,debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()