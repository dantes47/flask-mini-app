from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return '''<html style="background: grey;">
                <h1 style="text-align: center; color: teal;">{}</h1>
              </html>'''.format(app.config['SECRET_KEY']).upper()

if __name__ == '__main__':
    app.run()