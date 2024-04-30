pipeline {
    agent any
    stages {
         stage("Build") {
            steps {
                sh "dir"
                sh "pwd"
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip install -U pip"
                sh "pip install --target ./dependencies -r fastapi_smoothgpt/requirements.txt --upgrade --no-user"
                sh "dir"
                }
          } 
          stage("Package"){
            steps {
                dir ('dependencies'){
                // sh "cd dependencies"
                sh "pwd"
                sh "dir"
                sh "zip -r ../aws_function.zip ." 
                // sh "cd .."
                sh "pwd"
                sh "dir"
                sh "zip -g ../aws_function.zip -r ../fastapi_smoothgpt"
                sh "dir"
                // archiveArtifacts artifacts: 'aws_function.zip', fingerprint: true
                }
            }
          }

        stage("Deploy") {
             steps {
                sh "pwd"
                sh "dir"
                archiveArtifacts artifacts: 'aws_function.zip', fingerprint: true
                deployLambda([alias: '', artifactLocation: 'aws_function.zip', awsAccessKeyId: 'AKIAVPFFP273OQQXHNHA', awsRegion: 'us-east-1', awsSecretKey: '{AQAAABAAAAAwAmY8Z9Z1/Q9CeJRNRZ084cBP+Zz8a+RYHJhd0GpVdvy4w5eBZD8Fo5ovqCGPmKQlmK6w5S9Q0hIL0ZBasXIKXw==}', deadLetterQueueArn: '', environmentConfiguration: [kmsArn: ''], functionName: 'smoothgpt-api', handler: 'fastapi_smoothgpt.main.handler', memorySize: '512', role: 'arn:aws:iam::376156706806:role/service-role/smoothgpt-api-role-t775jdav', runtime: 'python3.11', securityGroups: '', subnets: '', timeout: '30', updateMode: 'code', publish: 'true', description: 'managed by jenkins'])
             }
        }
        

    }
    post {
        always {
            cleanWs()
        }
    }
}

