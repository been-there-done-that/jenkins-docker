pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'ls -lrth'
                sh "docker build -t myapp ."
                sh "docker run -ridt -p 5000:5000 myapp"
                // sh "docker kill $(docker ps -q)"
                // sh "docker rm $(docker ps -a -q)"
                // sh "docker rmi $(docker images -q)"
            }
        }
    }
}