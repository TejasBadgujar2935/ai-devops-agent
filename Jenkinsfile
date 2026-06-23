pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ai-devops-agent .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 ai-devops-agent'
            }
        }
    }
}
