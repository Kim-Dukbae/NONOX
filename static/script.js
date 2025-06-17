async function send() {
    const inputEl = document.getElementById('input');
    const chatBox = document.getElementById('chatBox');
    const msg = inputEl.value.trim();
    if (!msg) return;

    const userMsg = document.createElement('div');
    userMsg.className = 'message user';
    userMsg.textContent = msg;
    chatBox.appendChild(userMsg);
    chatBox.scrollTop = chatBox.scrollHeight;

    inputEl.value = '';

    const res = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
    });
    const data = await res.json();

    const botMsg = document.createElement('div');
    botMsg.className = 'message bot';
    botMsg.innerHTML = data.response;
    chatBox.appendChild(botMsg);
    chatBox.scrollTop = chatBox.scrollHeight;

    loadHistory();
    loadStats();  // ✅ 통계 갱신
}

async function loadHistory() {
    const res = await fetch('/history');
    const messages = await res.json();
    let text = "";
    for (const msg of messages) {
        text += `[${msg.role}] ${msg.content}\n`;
    }
    document.getElementById("history").innerText = text;
}

async function loadStats() {
    const res = await fetch('/stats');
    const stats = await res.json();
    const statBox = document.getElementById("stats");
    statBox.innerHTML = `
    • 질문 수: ${stats.questions}<br>
    • 총 토큰 수: ${stats.total_tokens}<br>
    • 평균 질문 길이: ${stats.avg_question_length}자
  `;
}

document.getElementById("input").addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        send();
    }
});

window.onload = () => {
    loadHistory();
    loadStats();
};
