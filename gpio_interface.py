from flask import Flask, render_template
import RPi.GPIO as GPIO

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
    return render_template("index.html")

@app.route("/on")
def turn_on():
    GPIO.output(led,GPIO.HIGH)
    return render_template("index.html")

@app.route("/off")
def turn_off():
    GPIO.output(led,GPIO.LOW)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)