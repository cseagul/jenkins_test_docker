pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'playwright-app:latest'
        SHORT_SHA = "${env.GIT_COMMIT[0..6]}"
        DOCKER_TAG = "${DOCKER_IMAGE}-${SHORT_SHA}"
    }
    stages {

        stage('Build Docker Image') {
            steps {
                script {
                     sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d -p 8080:8080 ${IMAGE_NAME}
                '''
            }
        }
    }
    post {
        failure {
            echo "Build failed."
        }
    }
}