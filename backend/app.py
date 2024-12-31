from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue dans le système de gestion des notes !"

if __name__ == "__main__":
    app.run(debug=True)