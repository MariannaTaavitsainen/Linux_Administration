from flask import Flask 
import mysql.connector 
app = Flask(__name__) 
@app.route('/') 
def home(): 
# Connect to MySQL/MariaDB 
    conn = mysql.connector.connect( 
        host="localhost", 
        user="mataavit24", 
        password="mataavit24", 
        database="kello" 
    ) 
    cursor = conn.cursor() 
    cursor.execute("SELECT NOW()")
    result = cursor.fetchone() 
    # Clean up 
    cursor.close() 
    conn.close() 
    return f"""
    <html>
    	<head><title>LEMP Example</title></head>
      	<body>
            <h1>Hello from MySQL!</h1>
            <p>Current SQL server time: {result[0]}</p>
        </body>
    </html>
    """
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
