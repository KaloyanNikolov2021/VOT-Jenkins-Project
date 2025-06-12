from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "this is my project for virtualization of cloud technologies using jensking and flash"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
