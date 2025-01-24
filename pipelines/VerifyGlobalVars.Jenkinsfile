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
// conda init bash
                    sh """
                        env
                        git clone ${FUNCTIONS_REPO_URL} -b features/enhance-structure
                        ls -la
                        
                        conda create -n one-press-functions python=3.10 -y
                        source activate base
                        conda activate one-press-functions
                        pip install -r ./one-press-functions/requirements.txt
                    """

                    sh """
                        export STAGE_NAME=${stageName}
                        export BOOTSTRAP_BASE_DIR=${WORKSPACE}
                        source activate one-press-functions
                        python one-press-functions/app/main.py INITIALIZE_WORKSPACE
                    """
                }
            }
        }


        stage('Build') {
            steps {
                script {
                    def stageName = "BUILD"

                    sh """
                        export STAGE_NAME=${stageName}
                        export BOOTSTRAP_BASE_DIR=${WORKSPACE}

                        source activate one-press-functions
                        python one-press-functions/app/main.py INITIALIZE_WORKSPACE
                    """
                }
            }
        }
    }
}
