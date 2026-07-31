# Cloud-Native CI/CD Platform using Docker, GitHub Actions & AWS

A production-inspired CI/CD project demonstrating containerized application deployment, automated build pipelines, and cloud deployment practices using Docker, GitHub Actions, and AWS.

This project showcases DevOps fundamentals by automating the build and deployment lifecycle of a FastAPI application while following industry best practices for containerization, reverse proxy configuration, and deployment automation.

---

## Features

- Dockerized FastAPI application
- Multi-stage Docker build for optimized images
- Nginx reverse proxy configuration
- Docker Compose for local development
- GitHub Actions CI/CD workflow
- Automated application deployment
- Container health checks
- Non-root Docker containers
- Production-ready project structure
- Infrastructure ready for AWS deployment

---

## Tech Stack

- Docker
- Docker Compose
- GitHub Actions
- FastAPI
- Python
- Nginx
- AWS EC2
- Linux
- Git

---

## Project Structure

```
cloud-native-cicd-platform/
│
├── .github/
│   └── workflows/
├── app/
│   ├── src/
│   └── tests/
├── docker/
├── docs/
├── nginx/
├── scripts/
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Architecture

```
Developer
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
(Build → Test → Deploy)
     │
     ▼
AWS EC2
     │
     ▼
Docker Compose
     │
     ├── FastAPI Application
     └── Nginx Reverse Proxy
```

---

## Getting Started

### Clone Repository

```bash
git clone https://github.com/<your-username>/cloud-native-cicd-platform.git
cd cloud-native-cicd-platform
```

### Start the Application

```bash
docker compose up --build
```

Application:

```
http://localhost
```

Health Check:

```
http://localhost/health
```

---

## CI/CD Workflow

The project is designed to support a CI/CD pipeline using GitHub Actions.

Typical workflow:

- Source Code Push
- Build Docker Image
- Run Tests
- Build Validation
- Deploy to AWS EC2
- Verify Health Check

---

## Security Practices

- Non-root Docker container
- Multi-stage Docker build
- Reverse proxy using Nginx
- Basic rate limiting
- Security response headers
- Container health checks



