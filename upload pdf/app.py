import os
from flask import Flask,render_template,request
import sqlite3


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload" , methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'pdf/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

@app.route('/download', methods=["GET", "POST"])
def download():

    form = UploadForm()

    if request.method == "POST":

        conn= sqlite3.connect("DataBase.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  tablom """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]
            break

        conn.commit()
        cursor.close()
        conn.close()

        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)


    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target , filename])
        print(destination)
        file.save(destination)
    return render_template("complete.html")



def database(name, data):
    conn= sqlite3.connect("DataBase.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tablom (name TEXT,data BLOP) """)
    cursor.execute("""INSERT INTO tablom (name, data) VALUES (?,?) """,(name,data))

    conn.commit()
    cursor.close()
    conn.close()



def query():
        conn= sqlite3.connect("DataBase.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  tablom """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]
            break

        conn.commit()
        cursor.close()
        conn.close()

        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)


if __name__== "__main__":
    app.run(port=4555, debug=True)
