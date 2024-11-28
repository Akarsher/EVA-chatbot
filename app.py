from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import markdown2
# Configure the API key
genai.configure(api_key="AIzaSyAg2Q5vhu-4KaIMXzOP8Aq79JWrDQED1NU")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    creator_questions = [
        "who created you",
        "who created EVA",
        "who created EVA chatbot",
        "who made this chatbot",
        "who is your creator",
        "who developed this chatbot",
        "who developed you",
        "who built you"
    ]
    if any(q in user_input.lower() for q in creator_questions):
        return jsonify({"response": "Iam a LLM Chatbot created by Akarsh E.R and Navya Vijayakumar ,trained by google's gemini api."})    

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
