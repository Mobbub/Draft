from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import uuid, os, time, random

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'default_secret_key'
user_data = {}

def generate_session_id():
    return str(uuid.uuid4())

@app.route('/')
@app.route('/main')
def main():
    session_id = session.get('session_id', None)
    if session_id is None:
        session['session_id'] = generate_session_id()
        user_data[session['session_id']] = {    
            "status": False,
        }
        
@app.route('/my_zap')
def my_zap():
    pass