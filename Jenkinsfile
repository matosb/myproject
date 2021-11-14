pipeline {
    agent { docker { image 'matos007/titanic' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}