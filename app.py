from flask import Flask, jsonify, request
from app.services.fusion import MultimodalFusion

app = Flask(__name__)
fusion_engine = MultimodalFusion()

@app.route('/')
def home():
    return jsonify({
        "project": "CrimeVision AI - Multimodal Forensic Analysis",
        "status": "Backend is running successfully on CPU!"
    })

@app.route('/analyze-fusion', methods=['POST'])
def analyze_fusion():
    """
    Activity 6.1 & 6.3: Integrated API endpoint for multimodal evidence fusion and reporting.
    """
    data = request.json or {}
    image_data = data.get("image_detections", [])
    audio_data = data.get("audio_events", [])
    video_data = data.get("video_timeline", [])
    
    report = fusion_engine.fuse_evidence(image_data, audio_data, video_data)
    return jsonify({
        "status": "success",
        "forensic_report": report
    })

if __name__ == '__main__':
    app.run(debug=False, port=5000)