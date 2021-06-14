pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'ls -lrth'
                sh "docker build -t myapp ."
                sh "sudo docker run --rm -dit -p 5000:5000 --name=myappcontainer myapp"
                sleep time: 2500, unit: 'MILLISECONDS'
                sh "sudo docker stop myappcontainer"
                sh "echo ${env}"
            }
        }
    }
}
