pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/KaloyanNikolov2021/VOT-Jenkins-Project.git'
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
