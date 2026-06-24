pipeline {

agent any

stages {

    stage('Checkout') {

        steps {
            git 'https://github.com/TejasBadgujar2935/ai-devops-agent.git'
        }
    }

    stage('Verify') {

        steps {
            bat 'python --version'
        }
    }

}


}
