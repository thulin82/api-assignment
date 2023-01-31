pipeline {
    agent any
    // Enable section to set up scheduled job 
    //triggers {
    //    cron('H 6 * * *')
    //}
    stages {
        stage('Deploy SUT') {
            steps {
                echo "Deploying...."
                sh 'docker-compose up -d'
            }
        }
        stage('Verify SUT') {
            agent {
                docker { image 'localhost:5000/my-python2' }
            }
            steps {
                echo "Verifying...."
                sh 'fab verifyUrl:http://host.docker.internal:8080'
            }
        }
        stage('Test SUT') {
            agent {
                docker {
                    image 'localhost:5000/todoapitests'
                    reuseNode true
                }
            }
            steps {
                sh 'cd /home/docker/TodoApiTests;ls -la;dotnet vstest out/TodoApiTests.dll --logger:trx'
                sh 'cp -R /home/docker/TodoApiTests/TestResults results'
            }
        }
    }
    post {
        always {
                sh 'docker-compose down'
                step([$class: 'MSTestPublisher', testResultsFile:"results/*.trx", failOnError: false, keepLongStdio: true])
                cleanWs()
        }
    }
}
