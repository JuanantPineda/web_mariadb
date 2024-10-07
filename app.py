from flask import Flask, render_template, abort, redirect,request
import os, MySQLdb


app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()