# 💬 LLM Chat with Ollama (Flask 기반)

> Ollama와 연동되는 미니멀한 웹 챗봇  
> Python + Flask + HTML/CSS/JS 기반

---

## 🚀 소개

이 프로젝트는 로컬에서 실행되는 LLM 엔진인 **Ollama**와 연동하여  
간단한 챗봇 인터페이스를 제공하는 웹 앱입니다.  

모든 처리가 로컬 PC 내에서 이루어지기 때문에 개인정보 보호가 필수적인 환경에 적합하며,
프라이빗 데이터나 민감한 연구 정보를 다루는 연구자에게는 필수적인 선택입니다.

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
1. 모델 다운로드  
👉 [https://ollama.com/library/gemma3](https://ollama.com/library/gemma3)

2. Ollama 모델 실행
```bash
ollama run gemma3


```

```text
project_root/
├── run_chat.bat       # 실행 web 서버 (더블클릭)
├── app.py             # Flask 서버 코드
├── templates/
│   └── index.html     # 메인 HTML 템플릿
├── static/
│   ├── style.css      # CSS 스타일
│   └── script.js      # 클라이언트 로직

