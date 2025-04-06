from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "memoria/IHELP.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

with get_db_connection() as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS marker(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            latitudine DECIMAL(300,200) NOT NULL,
            longitudine DECIMAL(300,200) NOT NULL,
            data VARCHAR(1000) NOT NULL,
            colore VARCHAR(7) NOT NULL,
            tipologia VARCHAR(255) NOT NULL
        );
    ''')
    conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invia', methods=['POST'])
def controllo():
    if(request.method == 'POST'):
        longitudine = request.form.get('')
        latitudine = request.form.get('')
        Td = request.form.get('')   #Tempo di (stringa totale)
        Td = Td.split()
        colore = request.form.get('')
        tipo = request.form.get('')

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO marker(latitudine, longitudine, data, colore, tipologia)
                VALUES (?, ?, ?, ?, ?)
            ''', (latitudine, longitudine, Td[0:6], colore, tipo))
            conn.commit()
        return redirect(url_for('index'))
    
@app.route('/')
def lista():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT latitudine, longitudine, data, colore, tipologia FROM marker")
        latitudine, longitudine, data, colore, tipologia = cursor.fetchall()
    return render_template('index.html', lat = latitudine, long = longitudine, dat = data, color = colore, tipol = tipologia)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)