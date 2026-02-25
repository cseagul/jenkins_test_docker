pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "chaimsiegel"
        IMAGE_NAME = 'playwright-app'
        DOCKER_TAG = "${env.GIT_COMMIT[0..6]}"
        FULL_IMAGE_NAME = "${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${DOCKER_TAG}"
    }
    stages {

        stage('Build Docker Image') {
            steps {
                script {
                     sh "docker build -t ${FULL_IMAGE_NAME} ."
                }
            }
        }

        // stage('Run Container') {
        //     steps {
        //         sh '''
        //             docker rm -f ${IMAGE_NAME} || true
        //             docker run -d -p 8080:8080 ${IMAGE_NAME}
        //         '''
        //     }
        // }
        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'a7b55340-e2da-4977-8adc-fe0a94db95d9',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh "docker push ${FULL_IMAGE_NAME}"
            }
        }

        stage('Tag Latest') {
            steps {
                sh """
                    docker tag ${FULL_IMAGE_NAME} ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest
                    docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest
                """
            }
        }
    }
    post {
        failure {
            echo "Build failed."
        }
    }
}