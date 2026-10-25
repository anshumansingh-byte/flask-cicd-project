
pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        ECR_REPOSITORY = '554663574752.dkr.ecr.ap-south-1.amazonaws.com/flask-cicd-app'
    }

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

        stage('Login to AWS ECR') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'aws-ecr-credentials',
                    usernameVariable: 'AWS_ACCESS_KEY_ID',
                    passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                )]) {
                    sh '''
                        export AWS_DEFAULT_REGION="$AWS_REGION"
                        aws ecr get-login-password --region "$AWS_REGION" |
                        docker login --username AWS --password-stdin "$ECR_REPOSITORY"
                    '''
                }
            }
        }

        stage('Push Image to ECR') {
            steps {
                sh '''
                    docker tag flask-cicd-app:latest "$ECR_REPOSITORY:latest"
                    docker push "$ECR_REPOSITORY:latest"
                '''
            }
        }

        stage('Load Image into Minikube') {
            steps {
                sh 'docker save flask-cicd-app:latest | docker exec -i minikube ctr -n k8s.io images import -'
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
