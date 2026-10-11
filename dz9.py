from datetime import datetime
import json
import sqlite3
import urllib.request

url = "https://api.open-meteo.com/v1/forecast?latitude=51.52&longitude=30.75&current=temperature_2m"

req = urllib.request.urlopen(url)
data = json.loads(req.read().decode("utf-8"))

temp_val = data["current"]["temperature_2m"]
temperature = f"{temp_val}°C"
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

connection = sqlite3.connect("itstep_DB.sl3", timeout=5)
cur = connection.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_time TEXT,
        temperature TEXT
    )
""")
cur.execute(
    "INSERT INTO weather (date_time, temperature) VALUES (?, ?)",
    (current_time, temperature),
)
connection.commit()
connection.close()

print(f"Успішно збережено: [{current_time}] {temperature}")