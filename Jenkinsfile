pipeline {
    agent any
       triggers {
        pollSCM "* * * * *"
       }
    stages {
        stage('Build Application') { 
            steps {
                echo '=== Building app_django_flask_react_microservices Application ==='
            }
        }
        stage('Test Application') {
            steps {
                echo '=== Testing app_django_flask_react_microservices Application ==='
            }
        }
        stage('Build Docker Image') {
            when {
                branch 'master'
            }
            steps {
                echo '=== Building app_django_flask_react_microservices Docker Image ==='
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'master'
            }
            steps {
                echo '=== Pushing app_django_flask_react_microservices Docker Image ==='
            }
        }
        
        stage('Clean') {
            steps {
                echo '=== Delete the local docker images ==='
            }
        }
    }
}

