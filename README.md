<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=3000&pause=1000&color=A855F7&center=true&vCenter=true&width=700&lines=AI-Powered+Online+Interview+Analyzer;Real-Time+Facial+Emotion+Detection;Lie+Detection+%7C+WebRTC+Video+Call" alt="Typing SVG" />

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/DeepFace-AI-A855F7?style=for-the-badge&logo=tensorflow&logoColor=white" alt="DeepFace"/>
  <img src="https://img.shields.io/badge/WebRTC-P2P_Video-333333?style=for-the-badge&logo=webrtc&logoColor=white" alt="WebRTC"/>
  <img src="https://img.shields.io/badge/Socket.IO-Real--Time-010101?style=for-the-badge&logo=socketdotio&logoColor=white" alt="Socket.IO"/>
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/OpenCV-Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
</p>

<p>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" alt="Status"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue?style=flat-square" alt="Platform"/>
</p>

</div>

---

## 📌 Project Overview

**AI-Powered Online Interview Analyzer** is a full-stack, real-time interview intelligence platform that leverages **Artificial Intelligence**, **WebRTC peer-to-peer video calling**, and **facial emotion recognition** to analyze a candidate's behavioral patterns during a live online interview — providing the interviewer with actionable insights on **confidence**, **stress**, and a computed **deception probability score**.

> The system operates through two role-based portals — the **Interviewer Dashboard** (Admin) and the **Candidate Interview Interface** — connected via a secure, shareable room link. All analysis happens live, in-browser, with no third-party video service.

### 🎯 How It Works

```
Interviewer creates a Room → shares the join link with the Candidate
         ↓
Both connect via WebRTC (peer-to-peer video + audio call)
         ↓
Every 3 seconds: Candidate's webcam frame is sent to the AI backend
         ↓
DeepFace analyzes the frame → returns dominant emotion
         ↓
Frontend computes Confidence Score, Stress Level, Deception Probability
         ↓
Interviewer sees a live analysis dashboard with real-time charts
         ↓
Session ends → Report saved to SQLite → Both parties see final results
```

---

## ✨ Features

### 🔴 Live AI Emotion Detection
- Captures the candidate's webcam frame every **3 seconds** and sends it to the DeepFace AI engine
- Detects 7 core emotions: `happy`, `sad`, `angry`, `fear`, `surprise`, `disgust`, `neutral`
- Overlays a **bounding box** around the detected face on the candidate's video feed

### 📊 Real-Time Behavioral Metrics
- **Confidence Score** — rises with positive/neutral emotions, tracked across the entire session
- **Stress Level** — escalates with negative emotions (anger, fear, disgust, sadness)
- **Deception Probability** — weighted formula: `50% Stress + 30% Inverse Confidence + 20% Voice Nervousness`

### 📹 WebRTC Peer-to-Peer Video Call
- Fully functional **live video + audio** call between interviewer and candidate
- No third-party video service — all communication is browser-to-browser
- Signaling handled via **Socket.IO** (offer / answer / ICE candidates exchange)
- Google STUN server used for NAT traversal

### 🎙️ Voice Stress Analysis
- Analyzes audio from the candidate's microphone
- Returns a **"Nervous" or "Stable"** voice status on a per-sample basis

### 🗂️ Session Report Generation
- End-of-session report for both interviewer and candidate
- Displays average confidence, stress rating, deception probability
- Results persisted to **SQLite database** (`interviews.db`)
- **Downloadable PDF report** for record-keeping

### 🎨 Premium Dark-Theme UI
- Fully custom CSS with neon glassmorphism aesthetic
- Animated background orbs, scanning line effects, and micro-animations
- Custom cursor, live waveform bars, and smooth page transitions
- Fully responsive three-screen layout (Start → Interview → Report)

### 🔒 Role-Based Access
| Feature | Interviewer | Candidate |
|---|---|---|
| Create Room | ✅ | ❌ |
| View Live Emotion Telemetry | ✅ | ❌ |
| Mute/Unmute Controls | ✅ | ❌ |
| End Session | ✅ | ❌ |
| Deception Probability Report | ✅ | ✅ |
| View Own Behavioral Summary | ✅ | ✅ |
| Download PDF Report | ✅ | ✅ |

---

## 🛠️ Technologies Used

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python 3.10+, Flask | REST API server, page routing |
| **Real-Time** | Flask-SocketIO, Socket.IO | WebRTC signaling, room management |
| **AI / ML** | DeepFace (TensorFlow) | Facial emotion recognition |
| **Computer Vision** | OpenCV (`cv2`), NumPy | Image decoding and frame processing |
| **Video Call** | WebRTC | Peer-to-peer audio/video streaming |
| **Database** | SQLite3 | Persistent session report storage |
| **Frontend** | HTML5, Vanilla CSS, JavaScript | UI, animations, API calls |
| **Browser APIs** | Canvas API, Fetch API, MediaDevices API | Frame capture, HTTP requests, camera access |
| **Templating** | Jinja2 | Server-side variable injection into HTML |
| **Network** | Ngrok (optional) | Public URL tunneling for remote testing |

---

## 📁 Folder Structure

```
AI-Powered_Online_interview_Analyzer/
│
├── 📂 Backend/
│   └── app.py                  ← Flask server (routes, AI analysis, SocketIO, DB)
│
├── 📂 Frontend/
│   ├── index.html              ← Landing page (room creation entry point)
│   ├── interviewer.html        ← Interviewer dashboard (live emotion telemetry)
│   └── candidate.html         ← Candidate interview page (video feed + report)
│
├── 📂 Ai_lie_Detector/         ← Legacy/alternate build artifacts
├── 📂 diagram_images/          ← System design diagrams
├── 📂 ngrok-v3-stable-windows-amd64/  ← Ngrok binary for tunneling
├── 📂 venv/                    ← Python virtual environment
│
├── interviews.db               ← SQLite database (auto-created on first run)
├── generate_report.py          ← PDF report generation script
├── landing.html                ← Standalone landing page (alternate entry)
├── System_Design_Document.md   ← ER diagrams, DFDs, UML use case diagrams
├── project_explanation.md      ← Full line-by-line code walkthrough
└── README.md                   ← You are here 📍
```

---

## 🚀 Installation

### Prerequisites
- Python **3.10+**
- `pip` package manager
- A modern browser (Chrome / Edge recommended for WebRTC)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/md-farman/AI-Powered_Online_interview_Analyzer.git
cd AI-Powered_Online_interview_Analyzer
```

### 2️⃣ Create & Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install flask flask-cors flask-socketio deepface opencv-python numpy
```

> ⚠️ **Note:** DeepFace will automatically download the required AI model weights (~500MB) on first run. Ensure you have a stable internet connection.

### 4️⃣ Run the Server

```bash
cd Backend
python app.py
```

The server starts at: **`http://localhost:5000`**

### 5️⃣ Open the Application

| Role | URL |
|---|---|
| 🎤 **Interviewer** | `http://localhost:5000` → Click **"Create New Interview Room"** |
| 👤 **Candidate** | Open the shareable link: `http://localhost:5000/join/<room_id>` |

> 💡 For remote testing across different machines, use **Ngrok** (included in the repo):
> ```bash
> ngrok-v3-stable-windows-amd64\ngrok.exe http 5000
> ```
> Share the generated public URL with the candidate.

---

## 📸 Screenshots


### 🖥️ Interviewer Dashboard
![alt text](image.png)


### 📊 Interviewer Analysis Dashboard

<!-- SCREENSHOT: INTERVIEWER ANALYSIS DASHBOARD -->
<!-- Paste your screenshot here -->

```
[ INTERVIEWER ANALYSIS DASHBOARD SCREENSHOT ]
```

---

### 📋 Candidate Interview Result Page

<!-- SCREENSHOT: CANDIDATE INTERVIEW RESULT PAGE -->
<!-- Paste your screenshot here -->

```
[ CANDIDATE INTERVIEW RESULT PAGE SCREENSHOT ]
```

---

### 📥 Download Result Page

<!-- SCREENSHOT: DOWNLOAD RESULT PAGE -->
<!-- Paste your screenshot here -->

```
[ DOWNLOAD RESULT PAGE SCREENSHOT ]
```

---

### 🧑‍💼 Candidate Dashboard

<!-- SCREENSHOT: CANDIDATE DASHBOARD -->
<!-- Paste your screenshot here -->

```
[ CANDIDATE DASHBOARD SCREENSHOT ]
```

---

### 🎥 Candidate Online Interview — Video Call Interface

<!-- SCREENSHOT: CANDIDATE ONLINE INTERVIEW VIDEOCALL INTERFACE -->
<!-- Paste your screenshot here -->

```
[ CANDIDATE ONLINE INTERVIEW VIDEOCALL INTERFACE SCREENSHOT ]
```

---

### 🏁 Candidate Interview End Page

<!-- SCREENSHOT: CANDIDATE INTERVIEW END PAGE -->
<!-- Paste your screenshot here -->

```
[ CANDIDATE INTERVIEW END PAGE SCREENSHOT ]
```

---

## 🔮 Future Improvements

| # | Enhancement | Description |
|---|---|---|
| 1 | 🎙️ **Real Voice Stress Analysis** | Replace simulated audio analysis with `librosa` + `pyAudioAnalysis` for actual pitch, tremor, and speech-rate-based stress detection |
| 2 | 🔐 **User Authentication** | Add login/register system with JWT tokens so interviewers can maintain a history of all sessions |
| 3 | 📈 **Session History Dashboard** | A dedicated admin panel to browse, filter, and compare all past interview reports from the database |
| 4 | 📄 **Auto-Generated PDF Reports** | Automatically generate and email downloadable PDF reports with charts and analysis summaries post-interview |
| 5 | 🌐 **Cloud Deployment** | Deploy the backend to **Render** / **Railway** and configure persistent cloud storage (PostgreSQL) instead of SQLite |
| 6 | 📱 **Mobile-Responsive UI** | Optimize the candidate and interviewer views for mobile and tablet browsers |
| 7 | 🧠 **Multi-Face Detection** | Extend the AI pipeline to handle multiple faces in a frame (e.g., panel interviews) |
| 8 | 🗣️ **Speech-to-Text Transcription** | Integrate Whisper (OpenAI) to transcribe and keyword-analyze candidate answers in real time |
| 9 | 📊 **Emotion Timeline Charts** | Display an interactive timeline graph of emotion fluctuations over the session duration |
| 10 | 🔗 **ATS / HR Integration** | Provide a REST API for integration with popular Applicant Tracking Systems (ATS) like Workday or Greenhouse |

---

## 👨‍💻 Author

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=2DD4BF&center=true&vCenter=true&width=500&lines=Built+with+%E2%9D%A4%EF%B8%8F+by+Mohammed+Farman;Full-Stack+%7C+AI+%7C+Computer+Vision" alt="Author Typing" />

**Mohammed Farman**
*B.C.A. Computer Science & Engineering *

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YOUR_GITHUB_USERNAME)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_LINKEDIN)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:YOUR_EMAIL@gmail.com)

</div>

---

<div align="center">

**⭐ If you found this project useful, please star the repository!**

<img src="https://img.shields.io/github/stars/YOUR_USERNAME/AI-Powered_Online_interview_Analyzer?style=social" alt="Stars"/>

*Made with 🔮 AI, ☕ Coffee, and late-night debugging sessions.*

</div>
