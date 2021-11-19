from flask import Flask, render_template, request

app = Flask(__name__)

app.config["SECRET_KEY"] = '571ebf8e13ca209536c29be68d435c00'

from app import views