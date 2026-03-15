# DevOps Monitoring Project

A simple FastAPI service designed for DevOps monitoring demonstrations.

## Features

* FastAPI web service
* Health check endpoint
* Dependency management with requirements.txt
* Git version control
* Ready for containerization and monitoring integration

## Run locally

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open in browser:

```
http://localhost:8000/health
```

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Git
* GitHub

## Future Improvements

* Docker container
* Prometheus metrics
* Grafana dashboard
* CI/CD pipeline
