from flask import Flask

# Inisialisasi Flask
app = Flask(__name__)

# Konfigurasi secret key (penting buat session/form)
app.config['SECRET_KEY'] = 'kunci_rahasia' 

# Import routes di akhir biar ga circular import
from app import routes