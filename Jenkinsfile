pipeline {
  agent any

  stages {
    stage('Install test runner') {
      steps {
        script {
          if (isUnix()) {
            sh 'python3 -m pip install --user pytest'
          } else {
            bat 'py -3 -m pip install --user pytest'
          }
        }
      }
    }
    stage('Syntax check') {
      steps {
        script {
          if (isUnix()) {
            sh 'python3 -m compileall -q src tests'
          } else {
            bat 'py -3 -m compileall -q src tests'
          }
        }
      }
    }
    stage('Fixture tests') {
      steps {
        script {
          if (isUnix()) {
            sh 'python3 -m pytest -q'
          } else {
            bat 'py -3 -m pytest -q'
          }
        }
      }
    }
  }
}
