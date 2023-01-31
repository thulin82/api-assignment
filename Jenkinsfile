pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo "Building....."
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying...."
                sh 'docker-compose up -d'
            }
        }
        stage('Verify') {
            agent {
                docker { image 'localhost:5000/my-python2' }
            }
            steps {
                echo "Verifying...."
                sh 'fab verifyUrl:http://host.docker.internal:8080'
            }
        }
        stage('Test') {
            agent {
                docker { image 'localhost:5000/todoapitests' }
            }
            steps {
                sh 'cd /tmp/TodoApiTests/out;pwd;ls;dotnet vstest TodoApiTests.dll --logger:trx'
            }
        }
    }
    post {
        always {
                sh 'docker-compose down'
                cleanWs()
        }
    }
}