from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="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")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_msg}]
    )

    bot_reply = response.choices[0].message.content
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
