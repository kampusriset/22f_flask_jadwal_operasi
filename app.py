from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
import re

app = Flask(__name__)


app.secret_key = 'your-secret-key'
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'surgery_scheduling'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        cursor.close()
        db.close()
        
        if account:
            session['loggedin'] = True
            session['username'] = account['username']
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect username/password!')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        
        if account:
            flash('Account already exists!')
        else:
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password,))
            db.commit()
        
        cursor.close()
        db.close()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        username = request.form['username']
        old_password = request.form['password']
        new_password = request.form['new_password']
        
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, old_password,))
        account = cursor.fetchone()
        
        if account:
            cursor.execute('UPDATE users SET password = %s WHERE username = %s', (new_password, username,))
            db.commit()
        
        cursor.close()
        db.close()
        
        if account:
            return redirect(url_for('login'))
        else:
            flash('Incorrect username/password!')
    
    return render_template('change_password.html')

@app.route('/dashboard')
def dashboard():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM surgeries')
    surgeries = cursor.fetchall()
    cursor.close()
    db.close()
    
    return render_template('dashboard.html', surgeries=surgeries)

@app.route('/add_surgery', methods=['POST'])
def add_surgery():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nama_pasien = request.form['nama_pasien']
        level_urgensi = request.form['level_urgensi']
        alamat = request.form['alamat']
        tanggal_operasi = request.form['tanggal_operasi']
        
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute('INSERT INTO surgeries (nama_pasien, level_urgensi, alamat, tanggal_operasi) VALUES (%s, %s, %s, %s)', 
                      (nama_pasien, level_urgensi, alamat, tanggal_operasi,))
        db.commit()
        cursor.close()
        db.close()
    
    return redirect(url_for('dashboard'))

@app.route('/edit_surgery', methods=['POST'])
def edit_surgery():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        id = request.form['id']
        nama_pasien = request.form['nama_pasien']
        level_urgensi = request.form['level_urgensi']
        alamat = request.form['alamat']
        tanggal_operasi = request.form['tanggal_operasi']
        
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute('UPDATE surgeries SET nama_pasien = %s, level_urgensi = %s, alamat = %s, tanggal_operasi = %s WHERE id = %s', 
                      (nama_pasien, level_urgensi, alamat, tanggal_operasi, id,))
        db.commit()
        cursor.close()
        db.close()
    
    return redirect(url_for('dashboard'))

@app.route('/delete_surgery/<int:id>')
def delete_surgery(id):
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute('DELETE FROM surgeries WHERE id = %s', (id,))
    db.commit()
    cursor.close()
    db.close()
    
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
