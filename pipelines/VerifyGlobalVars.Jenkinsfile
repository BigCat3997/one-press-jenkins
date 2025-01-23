pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/BigCat3997/one-press-ado-templates.git'
        BRANCH = 'main'
        // CONDA_BIN_PATH = 'abc'
        // FUNCTIONS_WORK_DIR = 'abc'
        PATH="${env.CONDA_BIN_PATH}:${env.PATH}"
        PYTHONPATH="${env.FUNCTIONS_WORK_DIR}:${env.PYTHONPATH}"
    }

    stages {
        stage('Bootstrap') {
            steps {
                script {
                    // sh """
                    //     echo '#!/bin/bash' > environment.sh
                    //     echo 'export PATH=\$PATH:${CONDA_BIN_PATH}' >> environment.sh
                    //     echo 'export PYTHONPATH=\$PYTHONPATH:${FUNCTIONS_WORK_DIR}' >> environment.sh
                    // """

                    sh """
                        // . environment.sh
                        echo 'PATH: $PATH'
                        echo 'PYTHONPATH: $PYTHONPATH'
                    """
                }
            }
        }

        // stage('Retrieve Commit IDs') {
        //     steps {
        //         script {
        //             // Change directory to the cloned repository
        //             dir('repo') {
        //                 // Retrieve the Git commit ID and short commit ID
        //                 def commitId = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
        //                 def shortCommitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()

        //                 // Write the commit IDs to a file named environment.sh
        //                 writeFile file: 'environment.sh', text: """
        //                 #!/bin/bash
        //                 export GIT_COMMIT_ID=${commitId}
        //                 export GIT_SHORT_COMMIT_ID=${shortCommitId}
        //                 """

        //                 // Print the commit IDs
        //                 echo "Git Commit ID: ${commitId}"
        //                 echo "Git Short Commit ID: ${shortCommitId}"
        //             }
        //         }
        //     }
        // }

        // stage('Verify Environment File') {
        //     steps {
        //         script {
        //             // Print the contents of the environment.sh file
        //             sh '''
        //                 . ./repo/environment.sh
        //                 echo "GIT_COMMIT_ID: $GIT_COMMIT_ID"
        //                 echo "GIT_SHORT_COMMIT_ID: $GIT_SHORT_COMMIT_ID"
        //             '''
        //         }
        //     }
        // }
    }
}
