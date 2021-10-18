from flask import Flask
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
