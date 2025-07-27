from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
cors = CORS(app, origins='*')

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Members API Route
@app.route("/api/users", methods=['POST'])
def users():
    try:
        data = request.get_json()
        input_text = data.get('inputText')
        completion = client.chat.completions.create(
            model="gpt-4.1-nano",  # "gpt-4o-mini" doesn't exist, using gpt-3.5-turbo instead
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": input_text
                }
            ]
        )
        return jsonify({"response": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8080)