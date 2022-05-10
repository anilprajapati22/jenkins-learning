pipeline {
    agent any
    environment { 
        sgnenv = "Hello this is the value of env variable"
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }

    stages {
            stage('Code-Fetch') {
            steps {
                echo "code fetching from git"
                git 'https://github.com/anilprajapati22/jenkins_docker.git'
            }
        }
        stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
        
        stage('Build') {
            steps {
                echo "Building the image"
                sh "pwd"
                sh "ls"
                sh 'docker build -t anilprajapati18/flask-sgn .'
            }
        }
        stage('Push-on-Dockerhub') {
            steps {
                echo "pushing on docker hub"
                sh 'docker push anilprajapati18/flask-sgn'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f flask-server || true'
                sh 'docker run -d -p 80:5000 --name flask-server anilprajapati18/flask-sgn'
                sh 'docker logs flask-server'
            }
        }


        // stage('cleanup') {
        //     steps {
        //         echo "Clear docker container"
        //         sh 'docker rm -f flask-server'
        //     }
        // }        
    }
}
