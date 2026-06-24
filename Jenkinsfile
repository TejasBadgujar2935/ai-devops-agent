pipeline {

```
agent any

stages {

    stage('Check Tools') {

        steps {

            bat 'python --version'
            bat 'docker --version'
            bat 'kubectl version --client'
            bat 'git --version'

        }

    }

}
```

}
