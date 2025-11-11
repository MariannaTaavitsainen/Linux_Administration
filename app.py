from flask import Flask, render_template, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

def get_utc_time():
    # Yhdistetään MySQL:ään
    conn = mysql.connector.connect(
        host="localhost",
        user="mataavit24",
        password="mataavit24",
        database="kello"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT utc_time FROM timeUCT ORDER BY id DESC LIMIT 1;")
    result = cursor.fetchone()
    conn.close()
    return result["utc_time"] if result else None  # palauta None jos ei dataa

@app.route('/')
def home():
    return render_template("index.html", uct_time=get_utc_time())

@app.route('/api/uct-time')
def api_utc_time():
    utc = get_utc_time()
    
    # Muutetaan datetime merkkijonoksi (ISO-formaatti) ennen jsonifya
    if isinstance(utc, datetime):
        utc = utc.isoformat()
    
    return jsonify({"uct_time": utc})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
