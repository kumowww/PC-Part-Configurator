from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/components', methods=['GET'])
def get_components():
    conn = get_db_connection()
    
    cpus = conn.execute('SELECT * FROM components WHERE category = "cpu"').fetchall()
    mobos = conn.execute('SELECT * FROM components WHERE category = "mobo"').fetchall()
    psus = conn.execute('SELECT * FROM components WHERE category = "psu"').fetchall()
    
    conn.close()

    return jsonify({
        "cpus": [dict(row) for row in cpus],
        "motherboards": [dict(row) for row in mobos],
        "psus": [dict(row) for row in psus]
    })

@app.route('/api/validate', methods=['POST'])
def validate_build():
    data = request.json
    conn = get_db_connection()
    
    cpu = conn.execute('SELECT * FROM components WHERE id = ?', (data['cpu_id'],)).fetchone()
    mobo = conn.execute('SELECT * FROM components WHERE id = ?', (data['mobo_id'],)).fetchone()
    psu = conn.execute('SELECT * FROM components WHERE id = ?', (data['psu_id'],)).fetchone()
    conn.close()

    if not cpu or not mobo or not psu:
        return jsonify({"status": "error", "messages": ["Invalid components selected"]}), 400

    errors = []
    if cpu['socket'] != mobo['socket']:
        errors.append(f"Incompatible: CPU uses {cpu['socket']} but Motherboard is {mobo['socket']}.")

    total_wattage = cpu['wattage'] + 150 
    if total_wattage > psu['wattage']:
        errors.append(f"Incompatible: System needs ~{total_wattage}W, but PSU is only {psu['wattage']}W.")

    if errors:
        return jsonify({"status": "error", "messages": errors})
    
    total_price = cpu['price'] + mobo['price'] + psu['price']
    return jsonify({"status": "ok", "total_price": total_price, "wattage": total_wattage})

if __name__ == '__main__':
    app.run(debug=True, port=5000)