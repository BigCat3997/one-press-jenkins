pipeline {
    agent any

    environment {
        // Define any environment variables here
        PYTHON_SCRIPT = 'path/to/your_script.py'  // Replace with the path to your Python script
    }

    stages {
        stage('Prepare') {
            steps {
                echo "Hello World"
            }
        }

        stage('Setup Python') {
            steps {
                // Install Python and dependencies if needed
                sh '''
                apk update
                apk add --no-cache python3
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                // Run the Python script
                sh "python3 ${env.PYTHON_SCRIPT}"
            }
        }
    }

    post {
        always {
            // Clean up actions, if any
            echo 'Pipeline finished.'
        }
    }
}
