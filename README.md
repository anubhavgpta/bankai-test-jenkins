# Bankai Jenkins Demo Repository

A deliberately vulnerable, synthetic repository for trying Bankai's repository connection, security scanning, finding triage, remediation pull requests, and Jenkins multibranch verification. All embedded credentials are fake. Do not deploy this project or reuse its vulnerable patterns.

## Try it with Bankai

1. Connect this GitHub repository to a Bankai project.
2. Run a repository scan. The fixtures include SQL injection, command injection, path traversal, weak authentication, debug settings, fake hardcoded credentials, permissive CORS, and outdated dependencies.
3. Connect Jenkins from the project. Bankai creates a multibranch pipeline for this repository; branch and pull request discovery are enabled.
4. Open a pull request to exercise Jenkins verification. The `Jenkinsfile` runs safe syntax and fixture tests. It intentionally does not install the outdated vulnerable runtime dependencies.

Jenkins needs the Pipeline: Multibranch and GitHub Branch Source plugins. For a private GitHub repository, configure suitable GitHub credentials in Jenkins before its first indexing/build.

## Fixture inventory

| File | Intended finding |
| --- | --- |
| `src/auth.py` | SQL injection, weak password verification, source-controlled signing key |
| `src/commands.py` | OS command injection |
| `src/files.py` | Path traversal |
| `src/config.py` | Debug mode and fake credentials |
| `src/web.py` | Permissive CORS and detailed errors |
| `requirements.txt` | Intentionally outdated dependencies for SCA scanning |

The tests inspect inert behavior and do not run exploit payloads. The vulnerable functions are included only for isolated security testing.
