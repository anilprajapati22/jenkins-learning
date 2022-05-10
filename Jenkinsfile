pipeline {
    agent any
    environment { 
        sgnenv = "Hello this is the value of env variable"
    }

    stages {
            stage('Code-Fetch') {
            steps {
                echo "code fetching from git"
                git 'https://github.com/anilprajapati22/jenkins_docker.git'
            }
        }
        
        stage('Build') {
            steps {
                echo "Building the image"
                sh "pwd"
                sh "ls"
                sh 'docker build -t flask-sgn .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run -d --name flask-server flask-sgn'
                sh 'docker logs flask-server'
            }
        }
        stage('cleanup') {
            steps {
                echo "Clear docker container"
                sh 'docker rm -f flask-server'
            }
        }        
    }
}
