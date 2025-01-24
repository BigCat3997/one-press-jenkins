pipeline {
    agent any

    environment {
        REPO_URL = "https://github.com/BigCat3997/one-press-ado-templates.git"
        FUNCTIONS_REPO_URL = "https://github.com/BigCat3997/one-press-functions.git"
        BRANCH = "main"
        CONDA_BIN_PATH = "/opt/miniconda3/bin"
        FUNCTIONS_WORK_DIR = "${env.WORKSPACE}/one-press-functions"
        PATH="${env.CONDA_BIN_PATH}:${env.PATH}"
        PYTHONPATH="${env.FUNCTIONS_WORK_DIR}:${env.PYTHONPATH}"
    }

    stages {
        stage('Bootstrap') {
            steps {
                script {
                    def stageName = "BOOTSTRAP"

                    echo "========== STARTING STAGE: ${stageName} =========="

                    sh """
                        env
                        git clone ${FUNCTIONS_REPO_URL} -b features/enhance-for-jenkins
                        ls -la
                        conda create -n one-press-functions python=3.10 -y
                        source activate one-press-functions
                        pip install -r ./one-press-functions/requirements.txt
                    """


                    // sh """
                    //     source generate_vars.sh

                    //     # Print the variables to verify
                    //     echo "VAR1=\$VAR1"
                    //     echo "VAR2=\$VAR2"
                    //     echo "VAR3=\$VAR3"
                    // """

                    sh """
                        export STAGE_NAME=${stageName}
                        export BOOTSTRAP_BASE_DIR=${WORKSPACE}

                        source activate one-press-functions  > /dev/null 2>&1
                        python one-press-functions/app/main.py INITIALIZE_WORKSPACE
                        ls -la /home/jenkins/agent/workspace/weather-forecast/bootstrap_section
                        cat /home/jenkins/agent/workspace/weather-forecast/bootstrap_section/env_vars.sh
                    """

                    sh(label: 'Clone source', script: '''
                        export STAGE_NAME=${stageName}
                        export BOOTSTRAP_BASE_DIR=${WORKSPACE}

                        source /home/jenkins/agent/workspace/weather-forecast/bootstrap_section/env_vars.sh
                        export APP_SOURCE_PREFIX_PATH=$FLOW_BOOTSTRAP_SECTION_DIR
                        export APP_SOURCE="app_source"
                        export GIT_URL="https://github.com/BigCat3997/one-press-mock-projects.git"
                        export GIT_BRANCH="main"
                        export IS_PRIVATE_REPO="False"
                        export GIT_USERNAME="abc"
                        export GIT_TOKEN="abc"

                        source activate one-press-functions  > /dev/null 2>&1
                        python one-press-functions/app/main.py GIT_CLONE_ADO
                    ''')

        //   - bash: |
        //       source activate $FUNCTIONS_VENV
        //       python $EXECUTE_COMMAND
        //     env:
        //       FUNCTIONS_VENV: ${{ parameters.functionsVenv }}
        //       EXECUTE_COMMAND: ${{ parameters.functionsWorkDir }}/app/main.py GIT_CLONE_ADO
        //       APP_SOURCE_PREFIX_PATH: $(FLOW_BOOTSTRAP_SECTION_DIR)
        //       APP_SOURCE: ${{ parameters.appFolder }}
        //       GIT_URL: ${{ parameters.gitUrl }}
        //       GIT_BRANCH: ${{ parameters.gitBranch }}
        //       IS_PRIVATE_REPO: ${{ parameters.isPrivateRepo }}
        //       GIT_USERNAME: ${{ parameters.gitUsername }}
        //       GIT_TOKEN: ${{ parameters.gitToken }}
        //       ARCHIVE_PATH: $(Build.ArtifactStagingDirectory)
        //     displayName: "Bootstrap: Clone source"
                    echo "========== COMPLETED STAGE: ${stageName} =========="
                }
            }
        }


        // stage('Build') {
        //     steps {
        //         script {
        //             def stageName = "BUILD"

        //             sh """
        //                 export STAGE_NAME=${stageName}
        //                 export BOOTSTRAP_BASE_DIR=${WORKSPACE}

        //                 source activate one-press-functions
        //                 python one-press-functions/app/main.py INITIALIZE_WORKSPACE
        //             """
        //         }
        //     }
        // }

        // stage('Unit Test') {
        //     steps {
        //         script {
        //             def stageName = "UNIT_TEST"

        //             sh """
        //                 export STAGE_NAME=${stageName}
        //                 export BOOTSTRAP_BASE_DIR=${WORKSPACE}

        //                 source activate one-press-functions
        //                 python one-press-functions/app/main.py INITIALIZE_WORKSPACE
        //             """
        //         }
        //     }
        // }
    }
}
