from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.environ.get("API_KEY"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    
    prompt = f"You are a young woman speaking to her best friend. You're girly, bubbly, and fun. You type in lowercase and use lots of slang:\nUser: {user_input}\nBot:"
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    output = response.text if response.text else "Sorry, I couldn't process that. Please try again."
    
    return jsonify({"response": output})

if __name__ == "__main__":
    app.run(debug=True)
