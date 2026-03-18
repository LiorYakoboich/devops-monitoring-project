# 🚀 DevOps Monitoring Project

## 📌 Overview

This project demonstrates a complete monitoring stack built using a FastAPI application, Prometheus, and Grafana.

The goal of this project is to showcase DevOps skills by implementing real-time monitoring, metrics collection, and visualization in a containerized environment.

---

## 🧰 Tech Stack

* **FastAPI** – Backend service
* **Prometheus** – Metrics collection
* **Grafana** – Visualization & dashboards
* **Docker & Docker Compose** – Containerization
* **Python** – Application logic
* **GitHub Actions** – CI pipeline

---

## ⚙️ Features

* 📊 Real-time request monitoring
* ⏱ Request latency tracking
* 🔍 Custom Prometheus metrics
* ❤️ Health check endpoint (`/health`)
* 📈 Grafana dashboards with multiple panels:

  * Request Rate (req/sec)
  * Total Requests
  * Request Latency
* 🐳 Fully containerized environment using Docker Compose

---

## 🏗 Architecture

```
Client → FastAPI App → Prometheus → Grafana Dashboard
```

* The FastAPI app exposes metrics via `/metrics`
* Prometheus scrapes metrics from the app
* Grafana visualizes the data in dashboards

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/LiorYakoboich/devops-monitoring-project.git
cd devops-monitoring-project
```

---

### 2. Run with Docker Compose

```bash
docker compose up --build
```

---

### 3. Access the services

| Service     | URL                   |
| ----------- | --------------------- |
| FastAPI App | http://localhost:8000 |
| Prometheus  | http://localhost:9090 |
| Grafana     | http://localhost:3000 |

---

## 🔐 Grafana Login

```text
Username: admin
Password: admin
```

---

## 📊 Example Metrics

* `app_requests_total`
* `app_request_duration_seconds`

---

## 📈 Dashboard Overview

The Grafana dashboard includes:

* **Request Rate** – number of requests per second
* **Total Requests** – cumulative requests
* **Request Latency** – response time tracking

---

## 🧠 What I Learned

* Building a monitoring system end-to-end
* Working with Prometheus metrics
* Designing Grafana dashboards
* Containerizing applications with Docker
* Connecting services using Docker Compose

---

## 🔮 Future Improvements

* Add alerting (Grafana Alerts / Alertmanager)
* Deploy to cloud (AWS / GCP / Azure)
* Add Kubernetes deployment
* Improve CI/CD pipeline (build & push Docker images)

---

## 👩‍💻 Author

**Lior Yakobovich**

---

⭐ If you found this project helpful, feel free to star the repo!
