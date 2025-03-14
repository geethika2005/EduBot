from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/feestructure')
def fee_structure():
    return render_template('feestructure.html')

@app.route('/seats')
def seats():
    return render_template('seats.html')

@app.route('/placements')
def placements():
    return render_template('placements.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/message', methods=['POST'])
def message():
    user_input = request.json.get('message')
    response = requests.post(RASA_API_URL, json={"sender": "user", "message": user_input})
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to get response from Rasa server"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=3003)
