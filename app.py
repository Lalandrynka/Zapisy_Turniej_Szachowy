from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# połączenie z bazą danych
db = mysql.connector.connect(
    host="localhost",
    user="Admin_szachy",
    password="SZACHY",
    database="zapisy_turniej_szachowy"
)

cursor = db.cursor()

# strona główna - wyświetlanie użytkowników
@app.route("/")
def index():
    cursor.execute("SELECT imie, nazwisko, wiek, kategoria, ranking FROM zapisy")
    users = cursor.fetchall()
    return render_template("zapisy_na_turniej.html", users=users)

# dodawanie użytkownika
@app.route("/add", methods=["POST"])
def add_user():
    imie     = request.form["imie"]
    nazwisko = request.form["nazwisko"]
    email    = request.form["email"]
    numer    = request.form["numer"]
    wiek     = request.form["wiek"]
    ranking  = request.form["ranking"]
    numer_konta_bankowego = request.form["numer_konta_bankowego"]

    # Radio buttony mają name="kategoria" w HTML
    kategoria = request.form.get("kategoria")

    sql = """INSERT INTO zapisy
        (imie, nazwisko, `e-mail`, numer, wiek, kategoria, ranking, numer_konta_bankowego)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (imie, nazwisko, email, numer, wiek, kategoria, ranking, numer_konta_bankowego)

    cursor.execute(sql, values)
    db.commit()
    return "Użytkownik dodany! <a href='/'>Powrót</a>"

app.run(debug=True)