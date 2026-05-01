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
       stage('SonarQube Analysis') {
          steps {
             withSonarQubeEnv('SonarQube') {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                  sh '''
                  sonar-scanner \
                 -Dsonar.projectKey=flask-capstone \
                 -Dsonar.sources=. \
                 -Dsonar.host.url=http://host.docker.internal:9000 \
                 -Dsonar.login=$SONAR_TOKEN
                 '''
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