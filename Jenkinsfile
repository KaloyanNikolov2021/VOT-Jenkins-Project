pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/ТВОЕТО_ПОТРЕБИТЕЛСКО_ИМЕ/ИМЕТО_НА_РЕПОТО.git'
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run app') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
