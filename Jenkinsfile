pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/KaloyanNikolov2021/VOT-Jenkins-Project'
            }
        }

        stage('Check python and pip') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('Install dependencies') {
            steps {
                bat '"C:\\Users\\kaloy\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run app') {
            steps {
                bat '"C:\\Users\\kaloy\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
            }
        }
    }
}
