from flask import Flask, render_template_string
from datetime import datetime
import pytz

app = Flask(__name__)

# София timezone
SOFIA_TZ = pytz.timezone('Europe/Sofia')

@app.route('/')
def home():
    sofia_time = datetime.now(SOFIA_TZ).strftime('%H:%M:%S')
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="bg">
    <head>
        <meta charset="UTF-8">
        <title>🚀 VOT Project with Jenkins</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #1f1c2c, #928dab);
                color: #f2f2f2;
                text-align: center;
                padding-top: 50px;
                animation: fadeIn 1s ease-in;
            }

            h1 {
                font-size: 2.8em;
                margin-bottom: 10px;
                color: #ffcc00;
            }

            p {
                font-size: 1.2em;
                margin-bottom: 30px;
            }

            .timer, .clock {
                font-size: 2em;
                margin: 20px auto;
                background: rgba(255, 255, 255, 0.1);
                padding: 15px 30px;
                border-radius: 12px;
                width: fit-content;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            }

            span {
                font-weight: bold;
                color: #00ffcc;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <h1>🌐 Проект по Виртуализация с Jenkins</h1>
        <p>Добре дошли! Вижте колко време сте тук и колко е часът в София ⏰</p>

        <div class="timer">
            ⏳ Прекарано време в сайта: <span id="timer">0</span> сек.
        </div>

        <div class="clock">
            🕒 Текущ час в София: <span id="sofiaClock">{{ sofia_time }}</span>
        </div>

        <script>
            let seconds = 0;
            setInterval(() => {
                seconds++;
                document.getElementById('timer').textContent = seconds;
            }, 1000);

            function updateSofiaClock() {
                fetch('/sofia-time')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('sofiaClock').textContent = data.time;
                    });
            }
            setInterval(updateSofiaClock, 1000);
        </script>
    </body>
    </html>
    ''', sofia_time=sofia_time)

@app.route('/sofia-time')
def sofia_time():
    sofia_time = datetime.now(SOFIA_TZ).strftime('%H:%M:%S')
    return {'time': sofia_time}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
