pipeline {
    agent {
        docker {
            image 'docker' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'docker stop colingibbons/flask'
                sh 'docker rmi colingibbons/flask'
                sh 'docker build -t colingibbons/flask .'
                sh 'docker run -d -p 80:5000 --name flask colingibbons/flask'
            }
        }

    }
}
