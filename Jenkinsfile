
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -la'
                sh 'cat requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-cicd-app:latest .'
            }
        }

        stage('Load Image into Minikube') {
            steps {
                sh 'docker exec minikube crictl images'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl rollout restart deployment/flask-deployment'
                sh 'kubectl rollout status deployment/flask-deployment --timeout=120s'
            }
        }
    }
}
