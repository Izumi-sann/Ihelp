from flask import Flask, render_template, request, redirect, url_for, jsonify
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
            colore VARCHAR(1000) NOT NULL,
            descrizione VARCHAR(255) NOT NULL
        );
    ''')
    conn.commit()

@app.route('/')
def index():
    return render_template('prova.html')

@app.route('/invia', methods=['POST'])
def controllo():
    if request.method == 'POST':
        dati = request.get_json()
        longitudine = dati.get('lng')
        latitudine = dati.get('lat')
        Td = dati.get('di')   # Tempo di (stringa totale)
        #Td = Td.split()
        colore = dati.get('col')
        tipo = dati.get('desc')

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO marker(latitudine, longitudine, data, colore, descrizione)
                VALUES (?, ?, ?, ?, ?)
            ''', (latitudine, longitudine, Td, colore, tipo))
            conn.commit()
        
        return redirect(url_for('prova'))
    
@app.route('/')
def lista():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT latitudine, longitudine, data, colore, descrizione FROM marker")
        latitudine, longitudine, data, colore, descrizione = cursor.fetchall()
    return render_template('prova.html', lat = latitudine, long = longitudine, dat = data, color = colore, descr = descrizione)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)