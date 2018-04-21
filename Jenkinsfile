pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'docker' 
                }
            }
            steps {
                sh 'docker stack deploy -c docker-compose.yml flask' 
            }
        }
    }
}
