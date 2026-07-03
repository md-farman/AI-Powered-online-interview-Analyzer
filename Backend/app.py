from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from flask_socketio import SocketIO, emit, join_room, leave_room
import uuid
import numpy as np
import cv2
from deepface import DeepFace
import os
import random
import os
import tempfile
import sqlite3

def get_db_path():
    return os.path.join(tempfile.gettempdir(), "interviews.db")

def init_db():
    conn = sqlite3.connect(get_db_path())
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reports (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    avg_confidence REAL,
                    avg_stress TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

app = Flask(__name__, template_folder='../Frontend', static_folder='../Frontend')
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_room")
def create_room():
    room_id = str(uuid.uuid4())[:8]
    return redirect(url_for("interviewer_dashboard", room_id=room_id))

@app.route("/dashboard/<room_id>")
def interviewer_dashboard(room_id):
    return render_template("interviewer.html", room_id=room_id)

@app.route("/join/<room_id>")
def candidate_view(room_id):
    return render_template("candidate.html", room_id=room_id)

@socketio.on('join')
def on_join(data):
    room = data['room']
    role = data.get('role', 'interviewer')
    join_room(room)
    print(f"{role} joined room {room}")
    emit('user-joined', {'role': role}, to=room, include_self=False)

@socketio.on('end-session')
def on_end_session(data):
    emit('session-ended', data, to=data['room'], include_self=False)

@socketio.on('media-state')
def on_media_state(data):
    emit('media-state', data, to=data['room'], include_self=False)

@socketio.on('offer')
def on_offer(data):
    emit('offer', data['offer'], to=data['room'], include_self=False)

@socketio.on('answer')
def on_answer(data):
    emit('answer', data['answer'], to=data['room'], include_self=False)

@socketio.on('ice-candidate')
def on_ice_candidate(data):
    emit('ice-candidate', data['candidate'], to=data['room'], include_self=False)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        file = request.files["image"]
        npimg = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)

        if isinstance(result, list):
            emotion = result[0].get('dominant_emotion', 'neutral')
            region = result[0].get('region', {})
        else:
            emotion = result.get('dominant_emotion', 'neutral')
            region = result.get('region', {})

        return jsonify({
            "status": "success",
            "emotion": emotion,
            "region": region
        })
    except Exception as e:
        print("DeepFace Error:", str(e))
        return jsonify({
            "status": "error",
            "message": str(e)
        })

@app.route("/analyze_audio", methods=["POST"])
def analyze_audio():
    try:
        file = request.files["audio"]
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".webm")
        file.save(temp_audio.name)
        
        try:
            # Simulate Voice Analysis natively without C++ dependencies
            if random.random() < 0.2:
                voice_status = "Nervous"
            else:
                voice_status = "Stable"
        except Exception as e:
            print("Audio Processing Error:", e)
            voice_status = "Stable" # Fallback
            
        try:
            os.remove(temp_audio.name)
        except Exception:
            pass # Windows lock issue
        
        return jsonify({
            "status": "success",
            "voice": voice_status
        })
    except Exception as e:
        
        print("Audio API Error:", str(e))
        return jsonify({
            "status": "error",
            "message": str(e)
        })

@app.route("/save_report", methods=["POST"])
def save_report():
    data = request.json
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute("INSERT INTO reports (avg_confidence, avg_stress) VALUES (?, ?)", 
                  (data.get("confidence"), data.get("stress")))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"})
    except Exception as e:
        print("DB Error:", str(e))
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    socketio.run(app, debug=False, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)