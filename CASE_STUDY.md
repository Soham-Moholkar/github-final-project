# IBM DevOps Engineering: An End-to-End Learning Case Study

**Soham Prasanna Moholkar**  
IBM on Coursera · Learning portfolio: 31 October–18 November 2026  
Evidence reviewed: 19 November 2026

> **The project:** connect Agile planning, Git collaboration, Python application development, automated testing, security, containers and deployment automation through a customer Accounts microservice, supported by earlier IBM course assignments.
>
> **Verified capstone CI result:** 33 tests passed · 98% reported coverage · 0 Flake8 findings. These results describe one recorded CI execution, not production performance.

**Jump to** [Assignment deep dives](#assignment-deep-dives) · [All 15 courses](#3-all-15-courses-in-the-case-study) · [Accounts API](#4-main-implementation-customer-accounts-service) · [Delivery pipeline](#delivery-flow) · [Verified results](#6-results-and-evidence) · [Evidence index](#9-evidence-index-and-provenance)

## Executive summary

The IBM learning programme covered 15 courses. The engineering challenge was to connect their individual practices into a delivery process that another developer could inspect and reproduce. A working API alone would not demonstrate that process. The portfolio also needed traceable requirements, repeatable tests, a defined runtime, security controls and a clear deployment path.

The strongest implementation sits in [github-final-project](https://github.com/Soham-Moholkar/github-final-project). Although its name comes from the GitHub assignment, it now contains the Accounts service, CI workflow, Dockerfile, Kubernetes manifests and Tekton CD pipeline. This case study uses that repository as its central implementation and connects it to the calculator, emotion detection and counter-service assignments.

The result is a learning portfolio with verifiable source code and CI outcomes. The reviewed GitHub Actions execution tests the Accounts service against PostgreSQL and passes its configured 95% coverage requirement. Kubernetes and Tekton definitions describe the deployment process. A live cluster rollout, public production endpoint, availability target and operational improvement measurements are outside the evidence reviewed here.

## 1. Context, objective and role

**Context.** The supplied presentation reports completion of all 15 courses, an unweighted mean grade of 97.13%, four perfect scores and a capstone grade of 96.08%. These are portfolio-reported course results. They are separate from the engineering measures obtained from GitHub Actions.

**Objective.** Build a coherent delivery story around a REST microservice: define work as user stories, implement customer-account operations, test expected and failure behaviours, automate checks, package the application and define deployment to Kubernetes.

**Role and attribution.** Soham's portfolio contains individual course exercises and adaptations of IBM teaching repositories. The Accounts application builds on the IBM DevOps capstone starter by John Rofrano. The emotion detection application builds on IBM Developer Skills Network material. This is a student engineering case study rather than a claim of an IBM employment engagement or a commercial customer delivery. Existing licenses and authorship notices remain applicable.

**Success criteria.** The Accounts API should implement create, list, read, update and delete operations with consistent HTTP responses. Automated checks should lint the service and tests, run against a database, and enforce at least 95% coverage. Packaging and deployment configuration should be versioned alongside the application.

## 2. Project map

| Project | Purpose in the learning journey | Evidence and outcome |
| --- | --- | --- |
| [GitHub assignment and Accounts capstone](https://github.com/Soham-Moholkar/github-final-project) | Main delivery case: account lifecycle, planning, tests, security, CI, containers and CD definitions | CRUD implementation, ten closed user stories, passing CI, deployment manifests and Tekton pipeline |
| [Git and GitHub exercises](https://github.com/Soham-Moholkar/mcino-Introduction-to-Git-and-GitHub) | Practice repository structure and contribution conventions | Simple-interest Bash script, compound-interest Python script, contribution guide, code of conduct and issue templates |
| [Flask and Watson emotion detection](https://github.com/Soham-Moholkar/oaqjp-final-project-emb-ai) | Turn an external AI capability into a web application | Python package, Flask routes, browser form, five-emotion tests and invalid-input handling |
| [Module 8 application repository](https://github.com/Soham-Moholkar/ibm-devops-module-8-) | Related emotion detection assignment artifact | Matching application package, server, browser assets and tests. Treated as related evidence, not a second independent AI system |
| [CI/CD counter service](https://github.com/Soham-Moholkar/ibm-ci-cd-practice) | Isolate automation around a small REST service | GitHub Actions lint/test/image-build jobs, Tekton tasks and OpenShift deployment script. Recorded CI succeeded |
| [DevOps capstone workspace](https://github.com/Soham-Moholkar/devops-capstone-project) | Retain the capstone starter and related work | Accounts model/service layout, tests and Tekton artifacts. The more complete reviewed delivery implementation is in `github-final-project` |
| [Agile planning lab](https://github.com/Soham-Moholkar/lab-agile-planning) | Planning exercise repository | A README is present. The reviewed issue endpoint returned no issues, so the concrete planning evidence below comes from the Accounts repository |

### Assignment deep dives

#### Bash calculator and GitHub collaboration

The simple-interest assignment gives the repository a small, predictable executable to document and share. The Bash script reads principal, time and annual rate interactively. It passes the calculation to `bc`, requests two decimal places and prints the interest amount. For example, a principal of 1,000 at 5% annually for two years yields 100. The related Python exercise uses compounding and returns the final amount, which is 1,102.50 for the same inputs. That difference illustrates why a project README should define the meaning of the output as well as give an example.

The GitHub artifacts add the collaboration layer around those scripts. The README documents usage and assumptions, the license establishes reuse terms, and the contributing guide and issue templates give contributors a way to report and discuss changes. These files document a repository workflow. Individual review activity would require pull request records. [Bash assignment](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/simple-interest.sh), [Git/GitHub exercise files](https://github.com/Soham-Moholkar/mcino-Introduction-to-Git-and-GitHub/tree/5cfed37446575ca6dd764e7a27b63a114dc379b3)

#### Flask application with Watson NLP

The Flask assignment separates three responsibilities. The browser captures text and displays the response. The Flask route reads `textToAnalyze` and builds the user-facing result. The Python adapter sends the text to the Skills Network Watson NLP service and maps the response to five emotion scores and a dominant emotion. An HTTP 400 from Watson takes the invalid-input path, and the Flask route displays a prompt to try again. Other upstream HTTP errors propagate through the adapter's error handling, so a service timeout or upstream outage remains a candidate for clearer user messaging.

The included suite has one example for each of joy, anger, disgust, sadness and fear. These tests call the external service, so their outcome depends on network reachability and the lab endpoint. A practical next step would be to add local tests with recorded response fixtures for score extraction, invalid input and unexpected upstream responses, then keep a smaller live test for the integration. The reviewed files establish the app and its test cases. The portfolio does not claim that its live endpoint was exercised for this case study. [Browser code](https://github.com/Soham-Moholkar/oaqjp-final-project-emb-ai/blob/d947e795f4fa6e16c8ec849e249e93975a8ec96a/static/mywebscript.js), [Python adapter](https://github.com/Soham-Moholkar/oaqjp-final-project-emb-ai/blob/d947e795f4fa6e16c8ec849e249e93975a8ec96a/EmotionDetection/emotion_detection.py), [Five test cases](https://github.com/Soham-Moholkar/oaqjp-final-project-emb-ai/blob/d947e795f4fa6e16c8ec849e249e93975a8ec96a/test_emotion_detection.py)

#### Counter microservice and CI/CD practice

The counter lab keeps application state in a Python dictionary. A client creates a named counter at zero, increments it with `PUT`, reads its value or deletes it. The service returns 409 when a client reuses an existing name and 404 when a client reads or increments an unknown counter. Deletion returns 204 even if the counter is already absent. The in-memory design keeps the lab focused on delivery automation. State belongs to the process and disappears on restart.

In the recorded Actions run, the lint and test job completed before the container-build job. The test log shows **9 passing tests and 99% reported coverage**, and the image job completed successfully. The workflow builds a commit-tagged image in the runner. Separately, the OpenShift Tekton definition orders workspace cleanup, clone, lint, tests, Buildah and deployment. Its shell entry point supplies the branch, image reference, workspace and service account, while the deployment task waits for rollout. Those cluster steps are defined in source. The recorded Actions image job establishes the build outcome. [Counter routes](https://github.com/Soham-Moholkar/ibm-ci-cd-practice/blob/d0e9be94bcc9423d07453a998222e078ba859890/service/routes.py), [Counter test log](https://github.com/Soham-Moholkar/ibm-ci-cd-practice/actions/runs/44327056109/job/134881065023), [Image build job](https://github.com/Soham-Moholkar/ibm-ci-cd-practice/actions/runs/44327056109/job/134881303094), [Tekton definition](https://github.com/Soham-Moholkar/ibm-ci-cd-practice/blob/d0e9be94bcc9423d07453a998222e078ba859890/.tekton/pipeline.yml)

## 3. All 15 courses in the case study

The course names below follow the supplied portfolio. Each entry states its contribution to the case and the boundary of the available evidence.

### 01 · Introduction to DevOps

**Problem:** code, testing and deployment can become disconnected activities. **Application:** the Accounts repository keeps application code, quality checks and deployment definitions together. Its issue backlog connects functional work with technical work such as CI and containerization. **Learning:** delivery quality depends on the whole change process. A passing test stage is useful evidence, while deployment still needs its own execution record.

### 02 · Introduction to Cloud Computing

**Problem:** developers need to understand which responsibilities remain with an application team when using managed infrastructure. **Application:** the service separates application configuration from the runtime through environment variables and provides Kubernetes manifests. **Learning:** a managed cluster does not remove responsibility for persistent data, access, configuration and recovery. The reviewed material demonstrates a cloud-oriented deployment design, not a verified cloud availability outcome.

### 03 · Agile Development and Scrum

**Problem:** a broad instruction to “complete the service” is difficult to implement and assess. **Application:** ten Accounts issues split the work into environment setup, account operations, CI, security, Docker, Kubernetes and CD automation. Issue descriptions include roles, needs, acceptance criteria, sprint assignments and estimates. All ten are closed in the reviewed snapshot. **Learning:** acceptance criteria create a bridge between a requirement and a test. Closed issues record project state but do not independently prove a successful cluster rollout. [Planning evidence](https://github.com/Soham-Moholkar/github-final-project/issues?q=is%3Aissue)

### 04 · Introduction to Software Engineering

**Problem:** mixing storage, HTTP handling and configuration makes a service harder to change. **Application:** the Accounts implementation separates its persistent model in `service/models.py`, routes in `service/routes.py`, configuration and shared error/logging handlers. Tests mirror these responsibilities. **Learning:** clear boundaries make changes easier to verify and explain. The structure extends IBM's provided starter architecture rather than representing a framework built from scratch.

### 05 · Getting Started with Git and GitHub

**Problem:** assignments need inspectable history and contribution conventions. **Application:** the calculator repositories contain source files, licenses, contribution instructions and issue templates. The Accounts repository adds user stories and a CI badge. Recent commits document API/security work, a runner compatibility change and a complete Tekton pipeline. **Learning:** a repository communicates both the implementation and how to work on it. This case does not infer a peer-review process solely from the presence of GitHub files.

### 06 · Hands-on Introduction to Linux Commands and Shell Scripting

**Problem:** repeated environment and deployment steps are easy to perform inconsistently. **Application:** the portfolio contains Bash calculator and setup scripts. The counter-service deployment script applies Tekton resources and starts a pipeline with repository, branch, application and image parameters. **Learning:** shell scripts make operational steps explicit. The script's existence documents automation intent, while runtime logs would be required to demonstrate execution in OpenShift. [Deployment script](https://github.com/Soham-Moholkar/ibm-ci-cd-practice/blob/main/bin/deploy.sh)

### 07 · Python for Data Science, AI and Development

**Problem:** application logic needs dependable data handling, functions and error behaviour. **Application:** Python supports the compound-interest exercise, the emotion detection package and the Accounts service. The emotion detector constructs a request, extracts five scores and calculates the dominant emotion. **Learning:** foundational Python skills transfer into API integration and service development. The reviewed repositories do not establish a separate NumPy/pandas analysis project, so none is claimed here.

### 08 · Developing AI Applications with Python and Flask

**Problem:** users need a simple interface to an external NLP service. **Application:** a browser form sends text to Flask's `/emotionDetector` route, which calls the Skills Network Watson NLP emotion endpoint. The package returns anger, disgust, fear, joy and sadness scores plus the dominant emotion. HTTP 400 responses produce empty results that the server turns into an invalid-text message. The request has a 30-second timeout. **Learning:** model access is only one part of an application. Input handling, response formatting and service availability affect its usability. The five dominant-emotion tests depend on the lab service, and no fresh successful execution is claimed here. [Application source](https://github.com/Soham-Moholkar/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/emotion_detection.py)

### 09 · Introduction to Containers with Docker, Kubernetes and OpenShift

**Problem:** an application needs a defined runtime and a reproducible deployment description. **Application:** the Accounts Dockerfile uses Python 3.9, installs dependencies, runs Gunicorn on port 8080 and switches to UID 1001. The Kubernetes deployment defines one replica, resource requests/limits, readiness and liveness probes, and a non-root security context. A ClusterIP Service exposes port 8080 inside the cluster. **Learning:** image packaging, readiness and networking solve different problems. The supplied demo uses SQLite under `/tmp`; pod replacement can lose its data. [Dockerfile](https://github.com/Soham-Moholkar/github-final-project/blob/main/Dockerfile), [Deployment](https://github.com/Soham-Moholkar/github-final-project/blob/main/deploy/deployment.yaml)

### 10 · Application Development using Microservices and Serverless

**Problem:** a service should expose a focused capability through a stable interface. **Application:** the Accounts API owns customer-account lifecycle operations. The counter service and the emotion application provide separate learning examples with different responsibilities. **Learning:** a useful boundary follows the capability and its data. These repositories demonstrate small services and API contracts. A deployed function, event bus or serverless workload was not present in the reviewed artifacts, so serverless remains course learning rather than a claimed deployment result.

### 11 · Introduction to Test and Behavior Driven Development

**Problem:** CRUD code needs protection against regressions and invalid requests. **Application:** the Accounts suite covers persistence, serialization, missing records, invalid payloads, unsupported media types, idempotent deletion, security headers and CORS. User-story acceptance criteria use Given/When/Then language. **Outcome:** the inspected CI execution ran 33 tests successfully and reported 98% combined statement/branch coverage. Configuration enforces a 95% minimum. **Learning:** tests should demonstrate behaviour and failure handling. Final code and logs establish the suite's behaviour; they do not prove the chronological red/green/refactor sequence or a separate automated BDD runner. [Coverage configuration](https://github.com/Soham-Moholkar/github-final-project/blob/main/setup.cfg)

### 12 · Continuous Integration and Continuous Delivery

**Problem:** quality checks should run consistently on changes, and deployment steps should be repeatable. **Application:** Accounts CI triggers on pushes and pull requests to `main`, with a manual trigger available. It starts PostgreSQL 15, installs Python 3.9 dependencies, runs Flake8 and executes nosetests. The separate Tekton definition clones, lints, tests, builds/pushes an image, applies manifests, updates the image and waits for rollout. The counter project provides another Actions/Tekton/OpenShift exercise. **Outcome:** the inspected Accounts and counter CI runs succeeded. **Learning:** a successful CI run proves the stages it executed. It does not prove the separately defined Tekton pipeline ran. [Accounts CI](https://github.com/Soham-Moholkar/github-final-project/blob/main/.github/workflows/ci-build.yaml), [Tekton CD](https://github.com/Soham-Moholkar/github-final-project/blob/main/tekton/pipeline.yaml)

### 13 · Application Security and Monitoring / DevSecOps

**Problem:** web service behaviour and runtime permissions need deliberate controls. **Application:** Accounts initializes Flask-Talisman and Flask-CORS, and tests response headers and preflight behaviour. Its container uses a non-root user, while Kubernetes drops Linux capabilities and prevents privilege escalation. **Learning:** these are implemented controls with a defined scope. The lab disables forced HTTPS and allows broad CORS defaults. Authentication, authorization, strict origin policy and automated SAST/SCA/DAST gates would require further work and evidence. No completed scan programme is claimed. [Application initialization](https://github.com/Soham-Moholkar/github-final-project/blob/main/service/__init__.py)

### 14 · Monitoring and Observability for Development and DevOps

**Problem:** deployment configuration needs a way to tell whether the process is responding. **Application:** the service has `/health`, application logging, Gunicorn access logging and Kubernetes probes. Tekton includes rollout status verification. **Learning:** these provide a starting point for operation. `/health` returns a process-level status and does not actively verify database readiness. Reviewed artifacts do not establish a metrics dashboard, distributed tracing, SLO alerts or measured recovery time. These are the next operational extensions rather than completed outcomes.

### 15 · DevOps Capstone Project

**Problem:** integrate the preceding skills into an assessable delivery system. **Application:** extend the Accounts starter into a complete CRUD service, describe work through user stories, add security behaviour and tests, automate PostgreSQL-backed CI, and version Docker/Kubernetes/Tekton configuration. **Outcome:** the portfolio reports a 96.08% capstone course grade, and the reviewed engineering evidence independently shows successful CI with 33 tests and 98% coverage. **Learning:** a strong capstone explains which stages ran and which stages are represented by configuration, then makes both easy to inspect.

## 4. Main implementation: customer Accounts service

### User need and API contract

A customer-service representative needs to manage account details without changing application code or accessing database tables directly. The service exposes an HTTP interface over a model containing account ID, name, email, address, optional phone number and join date.

| Operation | Endpoint | Expected behaviour |
| --- | --- | --- |
| Create | `POST /accounts` | Return 201 and a Location header |
| List | `GET /accounts` | Return 200 and a JSON array |
| Read | `GET /accounts/{id}` | Return 200, or 404 if absent |
| Update | `PUT /accounts/{id}` | Return 200 with saved details, or 404 if absent |
| Delete | `DELETE /accounts/{id}` | Return 204, including repeated deletion |
| Health | `GET /health` | Return 200 with process-level status |

### Sprint plan and acceptance evidence

| Sprint | What the backlog aimed to deliver | Acceptance examples | What a reviewer can inspect |
| --- | --- | --- | --- |
| 1 · Service | A reproducible environment and account read, list, update and delete operations | Read by ID returns the right account. Updating it persists changes. A deleted account can no longer be retrieved. | [Environment story](https://github.com/Soham-Moholkar/github-final-project/issues/1), [Account deletion story](https://github.com/Soham-Moholkar/github-final-project/issues/5), [API tests](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/tests/test_routes.py) |
| 2 · Quality and security | Consistent automated checks, security headers and CORS behaviour | A pushed commit runs lint and tests. An allowed preflight response permits JSON `PUT`. Response headers include the configured browser controls. | [CI story](https://github.com/Soham-Moholkar/github-final-project/issues/6), [Security story](https://github.com/Soham-Moholkar/github-final-project/issues/7), [Recorded CI](https://github.com/Soham-Moholkar/github-final-project/actions/runs/44360229468) |
| 3 · Delivery | A Docker image, Kubernetes resources and cluster automation | The container is configured to run on port 8080 as a non-root user. Tekton can hand off a built image to Kubernetes and wait for rollout. | [Container story](https://github.com/Soham-Moholkar/github-final-project/issues/8), [Kubernetes story](https://github.com/Soham-Moholkar/github-final-project/issues/9), [CD story](https://github.com/Soham-Moholkar/github-final-project/issues/10), [Versioned deployment assets](https://github.com/Soham-Moholkar/github-final-project/tree/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/deploy) |

### Example: follow one account through the service

1. Send a JSON body with a synthetic name, email and address to `POST /accounts`. The client may omit `phone_number` and `date_joined`. The model supplies an empty phone value and defaults the join date to the current date.
2. The route checks the request media type and calls the model's deserializer. SQLAlchemy persists the new record and assigns its integer ID. The route returns 201, the serialized account and a `Location` header for the new resource.
3. Read that location and use `PUT /accounts/{id}` to send the full account representation with a revised address. A subsequent GET should return the new address with the original ID. A client updating another field should retain any original join date it wants to preserve, because the deserializer defaults an omitted date during update as well.
4. Delete the resource. The first DELETE returns 204, a GET for the deleted ID returns 404, and repeating the DELETE still returns 204. This gives a client a stable response when retrying a deletion.

| Input or condition | How the service responds | Coverage in the reviewed suite |
| --- | --- | --- |
| Request omits a required account field | Model validation leads to a structured 400 response | Invalid create and update cases |
| `date_joined` is not a valid date | Model validation rejects the value | Invalid date model test |
| Write uses an unsupported media type | Route returns 415 | Separate create and update cases |
| Read or update targets an absent ID | Route returns 404 | Separate read and update cases |
| Browser sends a preflight for a JSON PUT | Response exposes allowed methods and headers | CORS preflight regression case |
| Unsupported HTTP method | Shared error handler returns a JSON 405 response | Unsupported method regression case |

The model stores the join date as a database date and exposes it in the API as an ISO-formatted string. The route layer handles HTTP semantics and the model owns database operations. Shared error handlers keep the shape of error responses consistent. [Accounts model](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/service/models.py), [Routes](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/service/routes.py), [Error handlers](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/service/common/error_handlers.py)

### Architecture and data flow

1. A client sends an HTTP request to the Flask application.
2. Route handlers validate the media type and deserialize account data.
3. The SQLAlchemy Account model performs persistence operations.
4. The service serializes a JSON response and returns an appropriate HTTP status.
5. Shared handlers format errors and logs. Talisman and CORS affect HTTP response behaviour.

PostgreSQL is the database used by GitHub Actions. The checked-in Kubernetes demo uses SQLite instead. That distinction matters: the CI run verifies PostgreSQL-backed behaviour, while the demo manifest prioritizes a self-contained lab setup over durable storage.

### Delivery flow

```mermaid
flowchart LR
    subgraph CI["GitHub Actions · verified run"]
        direction LR
        A["Checkout"] --> B["Python and PostgreSQL"] --> C["Flake8"] --> D["Tests and coverage"]
    end
    subgraph CD["Tekton · deployment defined in source"]
        direction LR
        E["Clone"] --> F["Lint and test"] --> G["Build and push image"] --> H["Apply manifests"] --> I["Verify rollout"]
    end
    classDef ci fill:#e8effb,stroke:#1957ca,color:#0e2140
    classDef cd fill:#e2f1f2,stroke:#007f81,color:#0e2140
    class A,B,C,D ci
    class E,F,G,H,I cd
```

**Continuous integration, executed:** GitHub push/PR → checkout → Python setup → PostgreSQL-backed dependency/test environment → Flake8 → nosetests and coverage gate.

**Continuous delivery, defined:** Tekton clone → lint → tests using in-memory SQLite → Kaniko image build/push → apply Kubernetes manifests → set the image → wait for rollout → print deployment resources.

The pipeline definition has an explicit 180-second rollout timeout. Its sample image reference uses a local registry and a mutable `latest` tag. Its Kaniko task permits an insecure registry, reflecting a lab configuration. A stronger release process would use a trusted registry, an immutable image digest, durable PostgreSQL configuration and a retained deployment record.

### Environments and deployment handoffs

| Environment | Database and runtime | Evidence or intended use |
| --- | --- | --- |
| Developer walkthrough | Python and Flask with a file-based SQLite database when following the local README | Quick review of the REST contract without provisioning PostgreSQL |
| GitHub Actions | Python 3.9 and a PostgreSQL 15 service container on an Ubuntu 22.04 runner | Recorded lint, tests and coverage for the reviewed Accounts revision |
| Tekton test task | Python 3.9 and in-memory SQLite | Defined pre-build check in the pipeline |
| Kubernetes demonstration | Gunicorn on port 8080 with SQLite at `/tmp/accounts.db` | Defined lab runtime. The single replica uses process-level readiness and liveness checks. |

The example PipelineRun selects the repository and branch, supplies an image destination and requests a 1 GiB shared workspace. That workspace carries the checkout into lint, test, build and deploy tasks. Kaniko uses the repository Dockerfile and pushes to the configured registry. The deploy task first applies the checked-in manifests, then selects the built image for the Accounts Deployment and waits for its rollout. The pipeline service account is bound to a namespace Role covering Deployments, ReplicaSets, Services and Pods. The application container has its own restrictions, including a non-root UID and dropped Linux capabilities. [Pipeline run configuration](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/tekton/pipelinerun.yaml), [Namespace permissions](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/tekton/rbac.yaml), [Deployment and probes](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/deploy/deployment.yaml)

A subsequent lab verification could capture the following evidence under one source revision:

| Checkpoint | Expected signal |
| --- | --- |
| Source and build | The PipelineRun logs the checked-out commit, and the registry reports a digest for the image that was pushed |
| Rollout | Kubernetes reports the Deployment available and the Pod ready, and the running image matches the built digest |
| Service routing | The ClusterIP Service resolves an endpoint for the Accounts Pod, and `GET /health` returns 200 through that Service |
| Application behaviour | A smoke test creates, reads and deletes a synthetic record, checks the expected HTTP status codes, and saves the results with the PipelineRun |
| Data durability | A future PostgreSQL deployment preserves a synthetic record through Pod replacement. The checked-in SQLite demo does not provide that guarantee. |

### Decisions and tradeoffs

| Decision | Benefit in this project | Tradeoff or follow-up |
| --- | --- | --- |
| Retain the IBM Python 3.9/nosetests toolchain | Matches course dependencies and recorded CI | Modernize and revalidate the toolchain as a separate change |
| Use PostgreSQL in CI | Exercise the service with the intended relational database family | Keep database configuration consistent across later deployment tests |
| Keep a SQLite demo deployment | Make a small lab deployment self-contained | Replace ephemeral storage before using persistent customer data |
| Run the app as a non-root user | Reduce application runtime privileges | Review pipeline and cluster privileges separately |
| Check probes and rollout status | Add process health and deployment feedback | Add dependency-aware readiness and application smoke tests |
| Keep CI and Tekton definitions in Git | Make delivery steps reviewable | Record execution provenance before claiming a deployed release |

## 5. A concrete iteration: CI compatibility

The first reviewed Accounts workflow failed during **Set up Python**. The job log reports that the setup action could not find Python 3.9 for x64 Ubuntu 26.04. The job had already checked out the repository, but it skipped dependency installation, lint and tests. The failure therefore identified an environment issue before any application checks ran.

The next commit pinned the runner to Ubuntu 22.04 while retaining the course's Python 3.9 toolchain. The following recorded run succeeded. The later run reviewed in this study reached both Flake8 and the PostgreSQL-backed test suite, with zero lint findings and 33 passing tests. This sequence shows why the runner, application runtime and dependencies all belong in the reproducibility record. [Failed setup job](https://github.com/Soham-Moholkar/github-final-project/actions/runs/44353810897/job/134976363624), [Runner change](https://github.com/Soham-Moholkar/github-final-project/commit/ff3d8b1e193cee773f6ea0f0c1eb6eff59f97904), [First successful run after the fix](https://github.com/Soham-Moholkar/github-final-project/actions/runs/44354205606)

## 6. Results and evidence

| Measure | Observed result | Interpretation |
| --- | --- | --- |
| Accounts tests | 33 passed | Historical CI job executed successfully |
| Accounts coverage | 98% reported | Combined statement/branch report, rounded by the tool; exceeds the configured 95% gate |
| Flake8 | 0 findings | Lint check for `service` and `tests` passed in the inspected job |
| Planning backlog | 10 of 10 reviewed issues closed | Repository planning state, not independent runtime proof |
| Account operations | Create, list, read, update, delete | Present in source and covered by the recorded tests |
| Counter CI | 9 tests passed, 99% reported coverage and a successful image build | Historical Actions run for the independent counter assignment |
| Container/deployment assets | Dockerfile, Deployment, Service and Tekton pipeline | Versioned implementation and deployment configuration |
| Course completion | 15 courses, 97.13% mean grade | Reported by the supplied learning portfolio, separate from software test coverage |

**Primary engineering record:** [Accounts CI run 44360229468](https://github.com/Soham-Moholkar/github-final-project/actions/runs/44360229468), source commit [`6cbfc82`](https://github.com/Soham-Moholkar/github-final-project/tree/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3), executed on 18 November 2026. The reviewed build job reports `TOTAL 249 statements, 5 missed, 26 branches, 1 partial branch, 98%` and `Ran 33 tests ... OK`.

**Supporting automation record:** [Counter CI run 44327056109](https://github.com/Soham-Moholkar/ibm-ci-cd-practice/actions/runs/44327056109), source commit [`d0e9be9`](https://github.com/Soham-Moholkar/ibm-ci-cd-practice/tree/d0e9be94bcc9423d07453a998222e078ba859890), executed on 18 November 2026.

No deployment-frequency, lead-time, change-failure-rate, recovery-time, cost-saving or user-adoption result is available in the reviewed evidence. The portfolio demonstrates implementation and learning outcomes without assigning invented business impact.

## 7. Reproduction and deployment review path

Use the recorded Accounts commit for comparison with the historical CI results. The following commands are a review path from the repository's documented setup, not a claim that this case-study preparation reran the service or deployed a cluster.

```bash
git clone https://github.com/Soham-Moholkar/github-final-project.git
cd github-final-project
git checkout 6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3

# In Bash with Python 3.9 available:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Local demonstration database; CI uses PostgreSQL instead.
export DATABASE_URI=sqlite:////tmp/accounts.db
flake8 service tests --count --show-source --statistics
nosetests -vv -s tests/test_cli_commands.py tests/test_common.py tests/test_models.py tests/test_routes.py
flask run --host 0.0.0.0 --port 8080
```

Container and cluster review requires a compatible Docker/Kubernetes environment and an image accessible to the cluster. Review `Dockerfile`, `deploy/` and `tekton/` before applying them. A local `docker build` alone does not make the image available to a remote cluster. Review the repository README for the demonstration workflow and the pipeline's registry, storage and service-account settings for the intended lab environment.

## 8. Next engineering iteration

1. **Retain deployment proof.** Capture a Tekton PipelineRun result, image digest, rollout status, resource snapshot and API smoke-test output for the same source revision.
2. **Make data durable.** Configure external PostgreSQL, secret references, migrations and a tested backup/restore process.
3. **Tighten the service boundary.** Add authentication/authorization, restrict browser origins and validate HTTPS configuration at ingress.
4. **Extend release checks.** Add dependency and image scanning, retain results, and define release acceptance criteria.
5. **Operate against explicit targets.** Add request/error/latency metrics, dependency-aware readiness, traces where useful, alert rules and an exercised rollback procedure.

These are proposed improvements. They are not represented as completed project features.

### What an operator would check first

The repository already provides a process health endpoint, request logging and rollout checks. These answer different questions. If a new Pod never becomes ready, start with rollout status, Pod events, image pull status and application startup logs. If the Pod is ready but account requests fail, inspect routing and the application's database connection, then run a small synthetic Accounts transaction. The current `/health` response alone cannot establish that database operations work.

A first monitoring baseline would track request count, server-error rate and latency by route pattern and status class. That would help distinguish a slow dependency from a deployment that simply lost traffic. Request IDs would let an operator correlate a failed request with its application log. Account names, emails and addresses should stay out of routine telemetry. Once there is usage data, use it to choose objectives and alert thresholds. During a release, record the pre-release baseline, compare the same indicators after rollout, and use the image digest to identify the version an operator could roll back to.

## 9. Evidence index and provenance

| Evidence | Link |
| --- | --- |
| Accounts source snapshot | [Commit 6cbfc82](https://github.com/Soham-Moholkar/github-final-project/tree/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3) |
| REST routes | [service/routes.py at reviewed commit](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/service/routes.py) |
| Security initialization | [service/__init__.py at reviewed commit](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/service/__init__.py) |
| Coverage gate | [setup.cfg at reviewed commit](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/setup.cfg) |
| PostgreSQL CI | [ci-build.yaml at reviewed commit](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/.github/workflows/ci-build.yaml) |
| Test execution and coverage | [Successful CI run and job logs](https://github.com/Soham-Moholkar/github-final-project/actions/runs/44360229468/job/134999244053) |
| Container runtime | [Dockerfile at reviewed commit](https://github.com/Soham-Moholkar/github-final-project/blob/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/Dockerfile) |
| Kubernetes configuration | [deploy directory at reviewed commit](https://github.com/Soham-Moholkar/github-final-project/tree/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/deploy) |
| CD configuration | [tekton directory at reviewed commit](https://github.com/Soham-Moholkar/github-final-project/tree/6cbfc82e8bbc9d1d37f9efa39db8526c758c3ae3/tekton) |
| User stories | [Accounts issues](https://github.com/Soham-Moholkar/github-final-project/issues?q=is%3Aissue), [Kanban project linked by the README](https://github.com/users/Soham-Moholkar/projects/3) |
| Earlier CI/CD assignment | [Counter source snapshot](https://github.com/Soham-Moholkar/ibm-ci-cd-practice/tree/d0e9be94bcc9423d07453a998222e078ba859890) |
| AI/Flask assignment | [Emotion detection source snapshot](https://github.com/Soham-Moholkar/oaqjp-final-project-emb-ai/tree/d947e795f4fa6e16c8ec849e249e93975a8ec96a) |
| Git assignment | [Git/GitHub exercises](https://github.com/Soham-Moholkar/mcino-Introduction-to-Git-and-GitHub) |
| Course grades and curriculum | Supplied `IBM_DevOps_15_Course_Learning_Portfolio.pptx`, slides 1–3 and 12. The presentation's certificate links were not independently revalidated for this case study |

Repository files and issue/run metadata were inspected on 19 November 2026. The Kanban link is included as the README's navigation reference; its live board state was not independently inspected. Runtime results in this case refer to existing recorded GitHub Actions executions. No new cluster deployment or production benchmark formed part of preparing this document.

---

**Portfolio conclusion.** This work connects course foundations to a concrete, testable service and a versioned delivery process. Its strongest demonstrated outcome is a reproducible quality check backed by real CI logs. The next step is to extend that same evidence discipline through deployment and operation.
