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
                sh 'docker build -t colingibbons/flask .'
                sh 'docker run -d -p 80:5000 --name flask colingibbons/flask'
            }
        }

    }
}
