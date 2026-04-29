pipeline {
  agent any

  environment {
    IMAGE_NAME = "annie237/flask-capstone"
  }

  stages {
    stage('Clone') {
      steps {
        git 'https://github.com/annienankeu/pcl-devops-capstone.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $ capstone/flask'
      }
    }
  }
}