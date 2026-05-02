from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/components', methods=['GET'])
def get_components():
    conn = get_db_connection()
    cpus = conn.execute('SELECT * FROM components WHERE category = "cpu"').fetchall()
    mobos = conn.execute('SELECT * FROM components WHERE category = "mobo"').fetchall()
    psus = conn.execute('SELECT * FROM components WHERE category = "psu"').fetchall()
    conn.close()

    cpu_groups = {}
    for cpu in cpus:
        cpu_dict = dict(cpu)
        model = cpu_dict['model']
        cpu_groups.setdefault(model, []).append(cpu_dict)

    return jsonify({
        "cpuModels": cpu_groups,
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

if __name__ == "__main__":
    app.run(debug=True)