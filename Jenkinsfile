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
    }
}
