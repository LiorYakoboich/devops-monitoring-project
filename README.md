# 🚀 DevOps Monitoring Project

[![CI](https://github.com/LiorYakoboich/devops-monitoring-project/actions/workflows/ci.yml/badge.svg)](https://github.com/LiorYakoboich/devops-monitoring-project/actions)

A production-style DevOps monitoring project demonstrating a full observability stack using **FastAPI, Prometheus, and Grafana**.

---

## 📌 Overview

This project simulates a real-world microservice environment with monitoring capabilities.

It includes:

* A FastAPI application exposing metrics
* Prometheus for metrics scraping
* Grafana for visualization dashboards
* Docker Compose for orchestration

---

## 🧱 Tech Stack

* **Backend:** FastAPI (Python)
* **Monitoring:** Prometheus
* **Visualization:** Grafana
* **Containerization:** Docker & Docker Compose
* **CI/CD:** GitHub Actions

---

## ⚙️ Features

* ✅ FastAPI web service
* ✅ Health check endpoint (`/health`)
* ✅ Prometheus metrics endpoint (`/metrics`)
* ✅ Request counting and latency tracking
* ✅ Grafana dashboards for visualization
* ✅ Dockerized environment
* ✅ CI pipeline with GitHub Actions

---

## 📊 Monitoring & Observability

The application exposes metrics using Prometheus, including:

* Total requests
* Request rate (req/sec)
* Request latency

Grafana is used to visualize these metrics via dashboards.

---

## 📸 Dashboard Preview

*Add your screenshot here*

```md
![Grafana Dashboard](docs/dashboard.png)
```

---

## 📁 Project Structure

```
devops-monitoring-project/
├── app/                      # FastAPI application
├── prometheus/              # Prometheus configuration
│   └── prometheus.yml
├── grafana/
│   └── dashboards/
│       └── fastapi-dashboard.json   # Exported Grafana dashboard
├── tests/                   # Unit tests
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
```

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/LiorYakoboich/devops-monitoring-project.git
cd devops-monitoring-project
```

### 2. Run with Docker

```bash
docker compose up --build
```

---

## 🌐 Access the Services

| Service    | URL                           |
| ---------- | ----------------------------- |
| FastAPI    | http://localhost:8000         |
| Metrics    | http://localhost:8000/metrics |
| Prometheus | http://localhost:9090         |
| Grafana    | http://localhost:3000         |

---

## 🔐 Grafana Login

* **Username:** admin
* **Password:** admin

---

## 📈 Grafana Dashboard

The project includes a pre-built Grafana dashboard:

📄 `grafana/dashboards/fastapi-dashboard.json`

This dashboard visualizes:

* Request Rate
* Total Requests
* Request Latency

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🔄 CI Pipeline

The project includes a GitHub Actions workflow that:

* Installs dependencies
* Runs tests
* Validates code

---

## 💡 Future Improvements

* Grafana dashboard auto-provisioning
* Kubernetes deployment
* Alerting (Grafana / Prometheus alerts)
* Load testing integration

---

## 👩‍💻 Author

**Lior Yakobovich**

---

## ⭐ Why This Project?

This project demonstrates real DevOps skills:

* Monitoring and observability setup
* Working with metrics and dashboards
* Containerized environments
* CI/CD integration

---

## 🚀 Next Step

👉 Automate Grafana dashboard provisioning (coming next!)
