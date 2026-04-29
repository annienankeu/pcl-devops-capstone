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