# DevOps Capstone: Customer Accounts Service

## IBM DevOps case study

[Read the complete 15-course case study](CASE_STUDY.md), covering the Accounts capstone, Git/GitHub assignments, Flask and Watson NLP, CI/CD, security, containerization and deployment definitions. Includes verified CI results, architecture, decisions, limitations and links to source evidence.

[![CI Build](https://github.com/Soham-Moholkar/github-final-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Soham-Moholkar/github-final-project/actions/workflows/ci-build.yaml)

An Accounts REST microservice based on the official IBM DevOps capstone starter. It supports CREATE, LIST, READ, UPDATE and DELETE, includes Talisman security headers and CORS, and runs on port 8080.

## Run and test

Use Python 3.9 for compatibility with the course's nosetests toolchain.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export DATABASE_URI=sqlite:////tmp/accounts.db
flask run --host 0.0.0.0 --port 8080
```

For PostgreSQL set `DATABASE_URI=postgresql://USER:PASSWORD@HOST:5432/accounts`. GitHub Actions tests against PostgreSQL.

```bash
flake8 service tests --count --statistics
nosetests -vv -s tests/test_cli_commands.py tests/test_common.py tests/test_models.py tests/test_routes.py
```

Coverage must remain at least 95%. Tests cover CRUD persistence, invalid requests, missing accounts, idempotent deletion, security headers and CORS preflight.

## API

| Method | Path | Success |
| --- | --- | --- |
| GET | / | 200 service metadata |
| GET | /health | 200 health status |
| POST | /accounts | 201 account with Location header |
| GET | /accounts | 200 JSON list |
| GET | /accounts/{id} | 200 account |
| PUT | /accounts/{id} | 200 updated account |
| DELETE | /accounts/{id} | 204 empty response |

## Container and Kubernetes

```bash
docker build -t accounts:1.0 .
docker run --rm -p 8080:8080 -e DATABASE_URI=sqlite:////tmp/accounts.db accounts:1.0
kubectl apply -f deploy/
kubectl rollout status deployment/accounts
kubectl port-forward service/accounts 8080:8080
```

The provided Kubernetes deployment uses a single replica and SQLite for a self-contained lab demonstration. Pod replacement resets that demonstration database. Use an external PostgreSQL database for durable deployment. The container runs as a non-root user with readiness and liveness probes.

## Planning and automation

[Kanban project](https://github.com/users/Soham-Moholkar/projects/3) · [User story template](.github/ISSUE_TEMPLATE/user-story.md) · [CI workflow](.github/workflows/ci-build.yaml)

Sprint 1 implements the environment and REST endpoints; Sprint 2 adds CI and security; Sprint 3 covers Docker, Kubernetes and Tekton deployment automation.

The `tekton/` directory contains CD pipeline and task definitions. Build and deployment evidence is collected from actual executions.

## Attribution

Accounts starter code: John Rofrano and IBM, licensed under Apache 2.0. The existing calculator, contribution guide, code of conduct and license are retained below and in the repository.

---

# This is the README.md file for the **github-final-project**

A calculator that calculates simple interest given principal, annual rate of interest and time period in years.

```text
Input:
   p, principal amount
   t, time period in years
   r, annual rate of interest (percentage)
Output:
   simple interest = p*t*r/100
```

## Run the calculator

Use Bash with the `bc` calculator installed:

```bash
bash simple-interest.sh
```

Enter the principal, time period in years, and annual percentage rate when prompted.
For example, principal `1000`, time `2`, and rate `5` produce simple interest of `100.00`.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
