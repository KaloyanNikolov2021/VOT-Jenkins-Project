from flask import Flask, render_template_string
from datetime import datetime
import pytz

app = Flask(__name__)

# София timezone
SOFIA_TZ = pytz.timezone('Europe/Sofia')

@app.route('/')
def home():
    # Вземаме текущо време в София, форматираме като string (часове:минути:секунди)
    sofia_time = datetime.now(SOFIA_TZ).strftime('%H:%M:%S')
    # Връщаме HTML с динамичното време
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Virtualization Project</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            .timer, .clock { font-size: 2em; margin: 20px; }
        </style>
    </head>
    <body>
        <h1>Tova e moq proekt po VOT s Jenkins</h1>
        <p>Welcome. Tuk mojete da vidite kolko vreme izpolzvate tozi site i kolko e chasa</p>

        <div class="timer">
            Izgubeno vreme na tozi site: <span id="timer">0</span> sec
        </div>

        <div class="clock">
            Chasa v Sofia: <span id="sofiaClock">{{ sofia_time }}</span>
        </div>

        <script>
            // Таймер за време на сайта (секунди)
            let seconds = 0;
            setInterval(() => {
                seconds++;
                document.getElementById('timer').textContent = seconds;
            }, 1000);

            // Обновяване на локалното време на София всяка секунда
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
    app.run(host='0.0.0.0', port=5000)
