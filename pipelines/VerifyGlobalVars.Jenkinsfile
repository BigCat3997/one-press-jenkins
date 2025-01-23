pipeline {
    agent any

    environment {
        // Define initial environment variables
        GLOBAL_VAR1 = 'initial_value1'
        GLOBAL_VAR2 = 'initial_value2'
    }

    stages {
        stage('Initialize') {
            steps {
                script {
                    // Print initial values
                    echo "Initial GLOBAL_VAR1: ${env.GLOBAL_VAR1}"
                    echo "Initial GLOBAL_VAR2: ${env.GLOBAL_VAR2}"
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Run the Python script and capture the output
                    def output = sh(script: 'python3 pipelines/modify_env.py', returnStdout: true).trim()
                    echo "Python script output:\n${output}"

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
                    echo "Modified GLOBAL_VAR1: ${env.GLOBAL_VAR1}"
                    echo "Modified GLOBAL_VAR2: ${env.GLOBAL_VAR2}"
                }
            }
        }
    }
}
