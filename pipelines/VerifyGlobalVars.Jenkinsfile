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
                    // Define Groovy variables at the top level of the script block
                    def newEnvVars = [:]

                    // Run the Python script and capture the output
                    def output = sh(script: 'python3 pipelines/modify_env.py', returnStdout: true).trim()
                    echo "Python script output:\n${output}"

                    // Parse the output and set the Groovy variables
                    output.split('\n').each { line ->
                        def (key, value) = line.split('=')
                        newEnvVars[key] = value
                    }

                    // Update the Groovy variables
                    GLOBAL_VAR1 = newEnvVars['GLOBAL_VAR1']
                    GLOBAL_VAR2 = newEnvVars['GLOBAL_VAR2']
                }
            }
        }

        stage('Use Modified Variables') {
            steps {
                script {
                    // Print modified values using Groovy variables
                    echo "Modified GLOBAL_VAR1: ${GLOBAL_VAR1}"
                    echo "Modified GLOBAL_VAR2: ${GLOBAL_VAR2}"
                }
            }
        }
    }
}
