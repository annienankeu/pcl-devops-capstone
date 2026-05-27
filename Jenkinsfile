
pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-capstone"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                git(
                    branch: 'main',
                    url: 'https://github.com/annienankeu/pcl-devops-capstone.git'
                )
            }
        }

        stage('SonarQube Analysis') {
            steps {

                withSonarQubeEnv('SonarQube') {

                    withCredentials([
                        string(
                            credentialsId: 'sonar-token',
                            variable: 'SONAR_TOKEN'
                        )
                    ]) {

                        sh '''
                        /opt/sonar-scanner/bin/sonar-scanner \
                        -Dsonar.projectKey=flask-capstone \
                        -Dsonar.sources=. \
                        -Dsonar.exclusions=**/venv/**,**/__pycache__/**,**/*.pyc \
                        -Dsonar.python.version=3.10 \
                        -Dsonar.host.url=http://sonarqube:9000 \
                        -Dsonar.token=$SONAR_TOKEN
                        '''
                    }
                }
            }
        }

        stage('Quality Gate') {
    steps {
        script {
            timeout(time: 5, unit: 'MINUTES') {
                def qg = waitForQualityGate()
                if (qg.status != 'OK') {
                    error "Pipeline failed due to Quality Gate: ${qg.status}"
                }
            }
        }
    }
}

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-capstone:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {

                    sh '''
                    echo "$DOCKER_PASS" | docker login \
                    -u "$DOCKER_USER" \
                    --password-stdin

                    docker tag flask-capstone:latest \
                    $DOCKER_USER/flask-capstone:latest

                    docker push \
                    $DOCKER_USER/flask-capstone:latest
                    '''
                }
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh 'trivy image flask-capstone:latest'
            }
        }

        stage('Run Container') {
            steps {

                sh '''
                docker stop flask-app || true
                docker rm flask-app || true

                docker run -d \
                --name flask-app \
                -p 5000:5000 \
                flask-capstone:latest
                '''
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