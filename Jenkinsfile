pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-capstone"
    }

    stages {

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {

                    sh '''
                    /opt/sonar-scanner/bin/sonar-scanner \
                      -Dsonar.projectKey=flask-capstone \
                      -Dsonar.sources=app \
                      -Dsonar.exclusions=**/venv/**,**/__pycache__/**,**/*.pyc \
                      -Dsonar.python.version=3.10 \
                      -Dsonar.host.url=http://sonarqube:9000 \
                      -Dsonar.token=$SONAR_TOKEN
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }
stage('Push Docker Image') {
    steps {

        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
        )]) {

            sh '''
            docker login -u $DOCKER_USER -p $DOCKER_PASS

            docker tag flask-capstone:latest $DOCKER_USER/flask-capstone:latest

            docker push $DOCKER_USER/flask-capstone:latest
            '''
        }
    }
}

        stage('Trivy Security Scan') {
            steps {
                sh "trivy image ${IMAGE_NAME}:latest"
            }
        }

        stage('Run Container') {
            steps {
                sh """
                docker stop flask-app || true
                docker rm flask-app || true

                docker run -d \
                  --name flask-app \
                  -p 5000:5000 \
                  ${IMAGE_NAME}:latest
                """
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