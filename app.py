from flask import Flask, request, jsonify, render_template, session
import requests
import os
import markdown

app = Flask(__name__, template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY", "default_fallback")

@app.route("/")
def index():
    session['messages'] = []
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_prompt = request.json["message"]
    messages = session.get("messages", [])
    messages.append({"role": "user", "content": user_prompt})

    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "gemma3:4b",
        # "model": "jinbora/deepseek-r1-Bllossom:8b",
        # "model": "dolphin-mistral:latest",
        "messages": messages,
        "stream": False
    })

    result = response.json()
    assistant_reply_raw = result.get("message", {}).get("content", "")
    assistant_reply = markdown.markdown(assistant_reply_raw, extensions=["extra", "nl2br"])

    if not assistant_reply:
        return jsonify({"response": "⚠️ 응답 없음 또는 형식 오류"})

    # 세션에는 마크다운 원문 저장
    messages.append({"role": "assistant", "content": assistant_reply_raw})
    session['messages'] = messages

    return jsonify({"response": assistant_reply})

@app.route("/history", methods=["GET"])
def history():
    return jsonify(session.get("messages", []))

@app.route("/stats", methods=["GET"])
def stats():
    import re
    from statistics import mean

    messages = session.get("messages", [])
    user_msgs = [m["content"] for m in messages if m["role"] == "user"]
    total_tokens = sum(len(re.findall(r"\S+", m["content"])) for m in messages)
    avg_length = round(mean(len(m) for m in user_msgs), 1) if user_msgs else 0

    return jsonify({
        "questions": len(user_msgs),
        "total_tokens": total_tokens,
        "avg_question_length": avg_length
    })

if __name__ == "__main__":
    app.run(port=5000)
