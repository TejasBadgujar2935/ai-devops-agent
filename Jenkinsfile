pipeline {


agent any

stages {

    stage('Verify Jenkins') {

        steps {

            echo '================================='
            echo 'AI DevOps Agent Pipeline Started'
            echo 'Jenkins Connected Successfully'
            echo '================================='

        }
    }

    stage('Git Info') {

        steps {

            sh 'pwd'
            sh 'ls -la'

        }
    }

}

post {

    success {

        echo 'Build Successful'
    }

    failure {

        echo 'Build Failed'
    }

}


}
