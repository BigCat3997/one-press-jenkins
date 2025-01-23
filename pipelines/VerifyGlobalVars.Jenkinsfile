pipeline {
    agent any

    environment {
        // Define initial environment variables
        VAR1 = 'initial_value1'
        VAR2 = 'initial_value2'
        VAR3 = 'initial_value3'
    }

    stages {
        stage('Initialize') {
            steps {
                script {
                    // Print initial values
                    echo "Initial VAR1: ${env.VAR1}"
                    echo "Initial VAR2: ${env.VAR2}"
                    echo "Initial VAR3: ${env.VAR3}"
                }
            }
        }

        stage('Run Script and Capture Output') {
            steps {
                script {
                    // Run the script and capture the output
                    def output = sh(script: 'bash generate_vars.sh', returnStdout: true).trim()
                    echo "Script output:\n${output}"

                    // Parse the output and set the environment variables
                    output.split('\n').each { line ->
                        def (key, value) = line.split('=')
                        env."${key}" = value
                    }
                }
            }
        }

        stage('Use Modified Variables') {
            steps {
                script {
                    // Print modified values
                    sh '. ./generate_vars.sh'
                    echo "Modified VAR1: ${env.VAR1}"
                    echo "Modified VAR2: ${env.VAR2}"
                    echo "Modified VAR3: ${env.VAR3}"
                }
            }
        }
    }
}
