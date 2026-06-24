pipeline {


agent any

stages {

    stage('Check Tools') {

        steps {

          sh 'python3 --version'
          sh 'docker --version'
          sh 'kubectl version --client'

        }

    }

}


}
