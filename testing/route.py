from testing import app,db
from flask import request,render_template,flash
from datetime import datetime
from werkzeug.utils import secure_filename
from moviepy.editor import VideoFileClip
from testing.models import VideoMetadata
import os

@app.route('/')
def index():
    return render_template('index.html')

ALLOWED_EXTENSIONS = ['mp4']
def allowed(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload',methods = ['POST'])
def upload():
    if 'video' not in request.files:
        return ('No video has been found')
    video = request.files['video']
    if video.filename == "":
        return ("No video file has been selected")
    if video and allowed(video.filename):
        video.save(os.path.join('testing/Static/Videos/', video.filename))
        filename = secure_filename(video.filename)
        filepath = os.path.join('testing/Static/Videos/', video.filename)
        video_clip = VideoFileClip(filepath)
        file_size = os.path.getsize(filepath)
        duration = video_clip.duration
        metadata = VideoMetadata(
            filename=filename,
            file_size=file_size,
            duration=duration,
            upload_date=datetime.now()
        )
        db.session.add(metadata)
        db.session.commit()
        return ("Thank you for uploading and metadata stored")
    return ('Invalid file type')

@app.route('/delete_video/<int:video_id>', methods=["POST","GET"])
def delete(video_id):
    video = VideoMetadata.query.filter_by(id = video_id).first()
    if video:
        filepath = os.path.join('testing/Static/Videos/', video.filename)
        if os.path.exists(filepath):
            os.remove(filepath)
        
        db.session.delete(video)
        db.session.commit()
        return("Metadata has been removed from the table, as well as from the physical folder")
    else:
        return("Id doesn't exist")
        

