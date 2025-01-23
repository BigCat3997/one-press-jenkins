pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/BigCat3997/one-press-ado-templates.git'
        BRANCH = 'main'
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Clone the GitHub repository
                    sh "git clone -b ${BRANCH} ${REPO_URL} repo"
                }
            }
        }

        stage('Retrieve Commit IDs') {
            steps {
                script {
                    // Change directory to the cloned repository
                    dir('repo') {
                        // Retrieve the Git commit ID and short commit ID
                        def commitId = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                        def shortCommitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()

                        // Write the commit IDs to a file named environment.sh
                        writeFile file: 'environment.sh', text: """
                        #!/bin/bash
                        export GIT_COMMIT_ID=${commitId}
                        export GIT_SHORT_COMMIT_ID=${shortCommitId}
                        """

                        // Print the commit IDs
                        echo "Git Commit ID: ${commitId}"
                        echo "Git Short Commit ID: ${shortCommitId}"
                    }
                }
            }
        }

        stage('Verify Environment File') {
            steps {
                script {
                    // Print the contents of the environment.sh file
                    sh '. ./repo/environment.sh'
                    echo "Git Commit ID: ${GIT_COMMIT_ID}"
                    echo "Git Short Commit ID: ${GIT_SHORT_COMMIT_ID}"
                }
            }
        }
    }
}
