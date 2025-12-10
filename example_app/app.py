from flask import Flask, request, jsonify
from llm_guard.guard import LLMGuard
from .llm_client import ask_llm

app = Flask(__name__)

# Initialize security layer
guard = LLMGuard(policy="balanced")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    # Pass through LLM Guard
    result = guard.process(prompt)

    if not result["allowed"]:
        return jsonify({
            "status": "blocked",
            "reason": result["reason"]
        }), 403

    # Call LLM safely
    response = ask_llm(result["sanitized_prompt"])

    return jsonify({
        "status": "allowed",
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)
