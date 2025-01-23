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

        stage('Read Environment Variables from File') {
            steps {
                script {
                    // Read the environment variables from the file
                    def envVars = readFile('env_vars.txt').trim()
                    echo "Environment variables from file:\n${envVars}"

                    // Parse the file and set the environment variables
                    envVars.split('\n').each { line ->
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
