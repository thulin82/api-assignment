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
                sh 'cd /home/docker/TodoApiTests;ls -la;dotnet vstest out/TodoApiTests.dll --logger:trx'
                sh 'cd /home/docker/TodoApiTests/TestResults; ls'
                sh "cp -R /home/docker/TodoApiTests/TestResults ${WORKSPACE}"
            }
        }
    }
    post {
        always {
                sh 'docker-compose down'
                sh 'pwd; ls -la'
                step([$class: 'MSTestPublisher', testResultsFile:"reports/*.trx", failOnError: false, keepLongStdio: true])
                cleanWs()
        }
    }
}