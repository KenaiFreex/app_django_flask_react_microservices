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
        }
        stage('Build Docker Image') {
            when {
                branch 'master'
            }
            steps {
                echo '=== Building app_django_flask_react_microservices Docker Image ==='
  /*               script {
                    app = docker.build("awsteamdou/django_microservices_dou")
                } */
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'master'
            }
            steps {
                echo '=== Pushing app_django_flask_react_microservices Docker Image ==='
/*                 script {
                    GIT_COMMIT_HASH = sh (script: "git log -n 1 --pretty=format:'%H'", returnStdout: true)
                    SHORT_COMMIT = "${GIT_COMMIT_HASH[0..7]}"
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerHubCredentials') {
                        app.push("$SHORT_COMMIT")
                        app.push("latest")
                    } */
                }
            }
        }
        stage('Clean') {
            steps {
                echo '=== Delete the local docker images ==='
               /*  sh("docker rmi -f awsteamdou/django_microservices_dou:latest || :")
                   sh("docker rmi -f awsteamdou/django_microservices_dou:$SHORT_COMMIT || :") */
            }
        }
    }
}
