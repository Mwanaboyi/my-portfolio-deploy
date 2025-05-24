from flask import Flask, render_template, request, jsonify
import pyodbc

app = Flask(__name__)

# SQL Server connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=PANIASUS\\SQLEXPRESS02;"
    "DATABASE=PortfolioMessages;"
    "Trusted_Connection=yes;"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Use JSON since fetch() sends JSON    
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ContactMessages (Name, Email, Message) VALUES (?, ?, ?)",
        (name, email, message)
    )
    conn.commit()
    return jsonify({"status": "success", "message": "Message saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
