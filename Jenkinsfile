pipeline {
  agent any

  stages {
    stage('Install test runner') {
      steps {
        sh 'python3 -m pip install --user pytest'
      }
    }
    stage('Syntax check') {
      steps {
        sh 'python3 -m compileall -q src tests'
      }
    }
    stage('Fixture tests') {
      steps {
        sh 'python3 -m pytest -q'
      }
    }
  }
}
