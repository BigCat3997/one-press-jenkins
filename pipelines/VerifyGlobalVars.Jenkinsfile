pipeline {
    agent any

    environment {
        REPO_URL = "https://github.com/BigCat3997/one-press-ado-templates.git"
        FUNCTIONS_REPO_URL = "https://github.com/BigCat3997/one-press-functions.git"
        BRANCH = "main"
        CONDA_BIN_PATH = "/opt/miniconda3/bin"
        FUNCTIONS_WORK_DIR = "abc"
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
                        env
                        git clone ${FUNCTIONS_REPO_URL} -b features/enhance-structure
                        ls -la
                        conda init bash
                        conda create -n one-press-functions python=3.10 -y
                        echo 'PATH: $PATH'
                        echo 'PYTHONPATH: $PYTHONPATH'
                        source activate base
                        conda activate one-press-functions
                        pip install -r ./one-press-functions/requirements.txt
                    """
// conda activate one-press-functions
                    sh """
                        source activate one-press-functions
                        python one-press-functions/app/main.py INITIALIZE_WORKSPACE
                    """

        //   - bash: |
        //       source activate $FUNCTIONS_VENV
        //       python $EXECUTE_COMMAND
        //     env:
        //       FUNCTIONS_VENV: ${{ parameters.functionsVenv }}
        //       EXECUTE_COMMAND: ${{ parameters.functionsWorkDir }}/app/main.py INITIALIZE_WORKSPACE
        //       STAGE_NAME: BOOTSTRAP
        //       BOOTSTRAP_BASE_DIR: "${{ parameters.workspaceWorkDir }}"
        //     displayName: "Bootstrap: Initialize workspace"
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
