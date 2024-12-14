def setGlobalEnvVars(filePath) {
    def envVars = readFile(filePath).split('\n')
    def newEnvVars = []
    envVars.each { envVar ->
        if (envVar) {
            def (key, value) = envVar.split('=')
            newEnvVars.add("${key}=${value.replaceAll('"', '')}")
        }
    }
    return newEnvVars
}

return this