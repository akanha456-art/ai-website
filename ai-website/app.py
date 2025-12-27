from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()  # Reads OPENAI_API_KEY automatically

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_msg
    )
    return jsonify({"reply": response.output_text})

if __name__ == "__main__":
    app.run()
