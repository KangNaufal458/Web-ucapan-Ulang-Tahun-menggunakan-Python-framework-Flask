from flask import render_template, request, redirect, url_for
from app import app

JAWABAN_RAHASIA = "singa"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        jawaban = request.form.get('jawaban', '').lower().strip()
        if jawaban == JAWABAN_RAHASIA:
            return redirect(url_for('surprise')) # Redirect biar URL-nya bersih
        else:
            return render_template('index.html', error="Salah wleee!")
            
    return render_template('index.html')

@app.route('/happy-birthday')
def surprise():
    # Di sini lo bisa oper data dinamis
    wish = "Semoga panjang umur dan sehat selalu!"
    return render_template('surprise.html', ucapan=wish)
