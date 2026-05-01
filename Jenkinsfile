pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/annienankeu/pcl-devops-capstone.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-capstone:latest .'
            }
        }

        stage('SonarQube Analysis') {
    steps {
        withSonarQubeEnv('SonarQube') {

            def scannerHome = tool 'SonarScanner'

            withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                sh """
                ${scannerHome}/bin/sonar-scanner \
                -Dsonar.projectKey=flask-capstone \
                -Dsonar.sources=. \
                -Dsonar.host.url=http://sonarqube:9000 \
                -Dsonar.token=$SONAR_TOKEN
                """
            }
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
