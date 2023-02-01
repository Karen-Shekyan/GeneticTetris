from flask import Flask, render_template, session, request, redirect, url_for
import requests, os, json
import random

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def landing():
    return render_template("landing.html")

if __name__ == '__main__':
        app.debug = True
        app.run()
