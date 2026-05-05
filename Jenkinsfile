pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-capstone"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/annienankeu/pcl-devops-capstone.git'
            }
        }

        stage('SonarQube Analysis') {
    steps {
        script {
            def scannerHome = tool 'SonarScanner'
            withSonarQubeEnv('SonarQube') {
                sh """
                ${scannerHome}/bin/sonar-scanner \
                -Dsonar.projectKey=flask-capstone \
                -Dsonar.sources=.
                """
            }
        }
    }
}
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline executed successfully 🎉'
        }
        failure {
            echo 'CI Pipeline failed ❌ Check logs'
        }
    }
}