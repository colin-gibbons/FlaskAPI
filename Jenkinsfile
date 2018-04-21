pipeline {
    agent {
        docker {
            image 'docker' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'docker stack deploy -c docker-compose.yml flask' 
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest --verbose --junit-xml test-reports/results.xml app.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
