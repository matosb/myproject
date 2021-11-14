pipeline {
  agent { label 'linux' }
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('matos-dockerhub')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t matos007/titanic:latest .'
      }
    }
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push matos007/titanic:latest'
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}