pipeline {
    agent {
        docker {
            image 'docker' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'docker stop flask'
                sh 'docker swarm leave -f'
                sh 'docker rmi colingibbons/flask'
                sh 'docker build -t colingibbons/flask .'
                sh 'docker swarm init'
                sh 'docker stack deploy -c docker-compose.yml flask'
            }
        }
        stage('Test'){
            steps{
                sh 'apt-get install python3'
                sh 'python3 ./test.py'
            }
        }
        stage('Deploy'){
            steps{
                sh 'docker push colingibbons/flask'
            }
        }

    }
}
