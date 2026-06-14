# Dockerized-App-Stack
## Project Overview
This repository contains a fully containerized, multi-service application stack engineered for safe, reproducible deployments. The architecture decouples application logic from configuration management, ensures zero credential leaks via rigorous layer separation, and establishes resilient inter-service communication over an isolated network fabric.
## Architectural Highlights & Grading Checklist
### 1. Security & Containment
Non-Root Execution: The application container rejects elevated privileges by running under an explicit non-root runtime environment user account.

Hermetic Image Builds: Uses a lightweight Python footprint to minimize attack surface vectors, compiled with targeted build-stage pipeline layers.

Perfect .dockerignore Implementation: High-risk variables (.env), system states (.git), and structural garbage cache arrays (__pycache__, .venv) are systematically blacklisted from entering the container context registry.

### 2. Orchestration & Networking
Named Service Resolution: Services drop legacy hardcoded loops (127.0.0.1) in favor of dynamic DNS mapping. The app container identifies and queries database and caching layers strictly by their internal service nicknames over the Docker bridge network.

Environment-Driven State Configuration: Configuration profiles are strictly decoupled from source text arrays. System variables utilize external environment scopes via host orchestration pipelines.

Persistence & Synchronization: Active database mutations are mapped safely out of transient memory and written directly into persistent storage spaces using a dedicated, isolated named engine volume (pgdata).

Active Readiness Probes: Includes structural automated loops ensuring containers remain completely gate-checked until underlying data layers declare a functional, healthy status condition.
# Repository Structure
```
.
├── Dockerfile
├── .env.example
├── .dockerignore
├── README.md
├── app.py
├── assets
└── compose.yaml
```
# Quickstart Deployment Guide
Follow these sequential execution paths to build and launch the environment stack:

## 1. Initialize Configuration Profile
Clone this repository workspace onto your system environment. Before executing a build, generate your local runtime parameters file from the template schema:

```
cp .env.example .env
```
Open the freshly generated .env file on your host workspace and populate your designated connection variables and credentials safely.

## 2. Launch the Orchestration Stack
Compile your local application context and bring up the system nodes securely in detached background mode:

```
docker compose up -d --build
```
## 3. Verify Active Stack Status
Inspect the status monitors to ensure every operational unit registers a functional, healthy uptime condition flag:

```
docker compose ps
```
## 4. Review Runtime Logging Pipelines
To follow the internal output telemetry from your services mapping out to standard output (stdout/stderr), execute the live tracking stream:

```
docker compose logs -f app
```
# System Verification Gallery
Here is the active container group confirming healthy operation and runtime isolation checks matching target layout criteria:

## Status Healthy On running Docker Compose
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/1.png)

### More detailed screenshot
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/1.1.png)
## Docker status
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/compose%20ps.png)
## Validating correct connection between app.py and database
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/connection%20app%20db.png)
## Endpoint Testing & Validation
1.
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/curl%201.png)
2.
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/curl%20health.png)
3.
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/curl%20app.png)
4.
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/curl%20api.png)
## Logs Checks and Validation
1.
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/logs%20app%20db.png)
2.
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/logs%20redis.png)

## Docker compose volumes OUTPUT
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/volumes.png)
## Check on Database maintained even after stopping the container AND Successful stopping the container
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/down.png)
## Successful Stopping All and Exiting the containers with deleting volumes
![image alt](https://github.com/NoFallback/Dockerized-App-Stack/blob/66488c7840470caeda7b80fb2fbef88b084a35ef/assets/down%20v.png)


