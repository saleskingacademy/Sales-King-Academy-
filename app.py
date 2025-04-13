from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Sales King Academy AI System is now live and operational!"

if __name__ == '__main__':
    app.run()
