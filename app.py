from flask import Flask, render_template

app = Flask("__name__")


my_hobby="Surfing"

@app.route("/")
def home():
    return render_template("repress.html", dfe=my_hobby)


if __name__ == "__main__":
    app.run(debug=True)