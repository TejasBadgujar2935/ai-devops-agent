pipeline {


agent any

stages {

    stage('Checkout Code') {

        steps {

            echo 'Checking Out Source Code'

        }

    }

    stage('Verify Workspace') {

        steps {

            sh 'pwd'
            sh 'ls -la'

        }

    }

    stage('Check Python') {

        steps {

            sh 'python3 --version || python --version'

        }

    }

    stage('Check Docker') {

        steps {

            sh 'docker --version'

        }

    }

    stage('Build Docker Image') {

        steps {

            sh 'docker build -t ai-devops-agent:latest .'

        }

    }

    stage('Verify Image') {

        steps {

            sh 'docker images'

        }

    }

}

post {

    success {

        echo 'Pipeline Completed Successfully'

    }

    failure {

        echo 'Pipeline Failed'

    }

}


}
