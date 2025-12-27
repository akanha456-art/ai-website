import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("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"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_msg
    )

    return jsonify({"reply": response.output_text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


