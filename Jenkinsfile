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
                sh 'cd /home/docker/TodoApiTests;ls -la;dotnet vstest out/TodoApiTests.dll --logger:"trx;LogFileName=TestReport.html"'
                sh 'cd /home/docker/TodoApiTests/TestResults; ls'
                sh "cp -R /home/docker/TodoApiTests/TestResults reports"
            }
        }
    }
    post {
        always {
                sh 'docker-compose down'
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: false,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'TestReport.html',
                    reportName: 'TestReport'
                ])
                cleanWs()
        }
    }
}