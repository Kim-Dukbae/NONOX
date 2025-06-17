# 💬 LLM Chat with Ollama (Flask 기반)

> Ollama와 연동되는 미니멀한 웹 챗봇  
> Python + Flask + HTML/CSS/JS 기반

---

## 🚀 소개

이 프로젝트는 로컬에서 실행되는 LLM 엔진인 **Ollama**와 연동하여  
간단한 챗봇 인터페이스를 제공하는 웹 앱입니다.  
세션을 활용해 대화 히스토리를 유지하고, 통계 패널도 함께 표시됩니다.

---

## 🖥️ 데모 화면

![demo 사진](https://github.com/user-attachments/assets/affeb86d-8e14-4144-9e3e-f50aed5b7ee6)

---

## 🔧 필요 라이브러리

- ✅ flask
- ✅ requests
- ✅ markdown

---

## 📂 사용 방법

```text
project_root/
├── run_chat.bat       # 실행 web 서버 (더블클릭)
├── app.py             # Flask 서버 코드
├── templates/
│   └── index.html     # 메인 HTML 템플릿
├── static/
│   ├── style.css      # CSS 스타일
│   └── script.js      # 클라이언트 로직

