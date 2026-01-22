from flask import Flask, render_template, request

app = Flask(__name__)

# --- KONFIGURASI ---
JAWABAN_RAHASIA = "singa"  # Jawaban kuis

# --- RUTE 1: HALAMAN DEPAN & LOGIC KUIS ---
@app.route('/', methods=['GET', 'POST'])
def index():
    error_mode = False 
    
    if request.method == 'POST':
        jawaban_user = request.form.get('jawaban', '').lower().strip()
        
        if jawaban_user == JAWABAN_RAHASIA:
            # Jawaban BENAR -> Masuk ke halaman special (Page 2)
            foto_clara = "image/mbkC.jpg" 
            return render_template('special.html', foto=foto_clara)
        else:
            # Jawaban SALAH -> Mode error aktif
            error_mode = True

    return render_template('index.html', error=error_mode)

# --- RUTE 2: HALAMAN KETIGA (MOMENT) ---
# 👇 PENTING: Ditaruh DI SINI (Sebelum app.run) 👇
@app.route('/spesial_2')
def moment():
    # Pastikan file foto 'mbkc2.jpg' ada di folder static/image/
    foto_clara_2 = "image/mbkc2.jpg" 
    return render_template('spesial_2.html', foto=foto_clara_2)


# --- RUTE TERAKHIR: LAST PAGE ---
@app.route('/lastpage')
def lastpage():
    foto_clara = "image/pramukamode.jpg"
    
    return render_template('lastpage.html', foto=foto_clara)

# --- START SERVER (WAJIB PALING BAWAH) ---
if __name__ == '__main__':
    app.run(debug=True)
