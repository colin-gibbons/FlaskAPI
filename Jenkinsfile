pipeline {
    agent {
        docker {
            image 'docker' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                try {
                sh 'docker stop flask'
                sh 'docker rmi colingibbons/flask'
                sh 'docker build -t colingibbons/flask .'
                } catch (Exception ex){
                    
                }
                sh 'sudo docker stack deploy -c docker-compose.yml flask'
            }
        }
        stage('Test'){
            steps{
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
