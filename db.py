from flask import Flask, render_template, g
import sqlite3
from sqlite3 import Error 

application = Flask(__name__)

app = application

connection = sqlite3.connect(r"C:\Users\Chithra-Laptop\Desktop\FYP\MQTT (2)\MQTT\db\mqtt1.db", check_same_thread=False) 

def connect_to_database():
    return connection


def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def execute_query(query, args=()):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

@app.route("/")
def point1():

  rows = execute_query("""SELECT * FROM sensorPoint""")
  return '<br>'.join(str(row) for row in rows)

#return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)