pipeline {
  agent any

  environment {
    IMAGE_NAME = "annie237/flask-capstone"
  }

  stages {
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $ annie capstone .'
      }
    }
  }
}