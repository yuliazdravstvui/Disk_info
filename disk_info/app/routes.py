from app import app
from app.disk_utils import get_disk_info
from flask import render_template

@app.route('/')
def index():
    disks = get_disk_info()
    return render_template('index.html', disks=disks)