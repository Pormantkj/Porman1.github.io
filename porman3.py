from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Siapa Namamu?</title>
    </head>
    <body>
        <h1>Siapa Namamu?</h1>
        <form action="/nama" method="post">
            <label for="nama">Nama:</label><br>
            <input type="text" id="nama" name="nama"><br><br>
            <input type="submit" value="Kirim">
        </form>
    </body>
    </html>
    '''

@app.route('/nama', methods=['POST'])
def process():
    nama = request.form['nama']
    # Simpan nama ke dalam berkas teks
    with open('jawaban.txt', 'a') as file:
        file.write(nama + '\n')
    return f'<h2>Halo, {nama}!</h2>'

@app.route('/lihat-jawaban')
def lihat_jawaban():
    # Baca isi berkas teks dan tampilkan ke Termux
    with open('jawaban.txt', 'r') as file:
        jawaban = file.read()
    return jawaban

if __name__ == '__main__':
    app.run(debug=True)
