pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the Flask CI/CD project'
                checkout scm
            }
        }

        stage('Verify Files') {
            steps {
                echo 'Checking project files'
                sh 'ls -la'
                sh 'cat requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building the Flask Docker image'
                sh 'docker build -t flask-cicd-app .'
            }
        }
    }
}