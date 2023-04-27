from flask import Flask, render_template, url_for

app = Flask(__name__)

data_mahasiswa = [
    {
        "Nama":"Usman Kene",
        "Kelas":"Ips II",
        "Alamat":"Dokiri"
    },
    {
        "Nama":"Fajrin S",
        "Kelas":"Ips II",
        "Alamat":"AffairS"
    }
]

@app.route("/")
def home():
    return render_template("base.html")
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/artikel/<info>")
def artikel(info):
    return " ini ada pada bagian  artikel " + info

@app.route("/data_mahasiswa")
def data_m():
    return render_template("data_mahasiswa.html", data_mahasiswa=data_mahasiswa)

if __name__ == "__main__":
    app.run(debug=True)