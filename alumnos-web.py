import MySQLdb as mariadb
from flask import Flask
from flask import render_template

app = Flask(__name__)

def connect():
    mariadb_connection = mariadb.connect(user='root', passwd = '', db = '')
    return mariadb_connection

@app.route("/")
def hello():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, ap_paterno, ap_materno from alumnos")
    conn.close()
    return render_template('alumnos-web.html', cursor=cursor)

if __name__ == "__main__":
    app.run()
