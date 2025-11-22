# **House Price Prediction — End-to-End Production-Grade MLOps Pipeline**

## **Why This Project? (The Problem)**

Most ML projects never make it to production because they lack:

* automated training,
* reproducibility,
* observability,
* and reliable deployments.

The goal of this project was to **build a real production-ready MLOps system**, not just train a model.

---

## **What I Built (The Solution)**

A **complete, automated MLOps pipeline** that takes a raw CSV → trains a model → tracks experiments → versions data → packages the model → deploys on Kubernetes → monitors it → detects drift → supports canary releases → and runs fully via GitHub Actions.

This is a **DevOps → MLOps upgrade project**, built with the tools an actual production team uses.

---

## **Core Architecture**

<img width="1471" height="927" alt="c1276ae6-6c78-4f56-a5b2-7cb7777ea04b" src="https://github.com/user-attachments/assets/ec90c12d-d315-440a-b9c9-90cb71b3ca12" />

---

## **Key Features (What Makes This Project Production-Grade)**

### **1. Data Versioning & Reproducible Training**

* DVC + DagsHub remote
* Every dataset and model version is tracked
* `dvc repro` rebuilds the entire pipeline deterministically

### **2. Experiment Tracking & Model Registry**

* MLflow for tracking metrics, parameters, artifacts
* Centralized registry to promote models to production
* Auto-logging of every training run via GitHub Actions
  <img width="1878" height="1024" alt="image" src="https://github.com/user-attachments/assets/b3abe86c-f69c-450b-b6b3-74083f5acc21" />

### **3. Automated Pipelines: CI / CT / CD**

* **CT**: Re-train on every data/code change
* **CI**: Docker build & push
* **CD**: Auto-update Kubernetes manifests with the new model image tag
* **Drift-Check Stage**: Placeholder for EvidentlyAI integration
<img width="1869" height="1031" alt="image" src="https://github.com/user-attachments/assets/5abbff34-966b-47e6-8e08-5a359ef7a86e" />

### **4. Model Serving (FastAPI + Docker + Distroless)**

* Lightweight & secure inference server
* Prometheus metrics auto-exposed
* Docker image pushed to ECR

### **5. Kubernetes Deployment + Scaling**

* Deployments, Services, HPA
* Metrics exposed to Prometheus using ServiceMonitor
* Real-time dashboards in Grafana
  <img width="1887" height="987" alt="429179c7-81bb-4001-bf86-c6c8b6c884c0" src="https://github.com/user-attachments/assets/bcf1af4a-611d-4226-b7be-65df544301ed" />


### **6. Canary Deployment (v1 + v2 Rollout)**

* Two deployments running simultaneously
* Traffic split controlled via Kubernetes selector rules
* Foundation for progressive rollouts & A/B testing
<img width="1887" height="987" alt="429179c7-81bb-4001-bf86-c6c8b6c884c0" src="https://github.com/user-attachments/assets/8b8dcd2d-d58a-4bb4-abb5-bd2ae909db15" />

### **7. Observability**

* **Prometheus**: request count, latency, CPU, memory
* **Grafana**: custom dashboards for model SLIs
* Model-level metrics exposed via FastAPI instrumentator
<img width="1880" height="1030" alt="38964e63-9e6c-40a8-8f3b-2737d07f2540" src="https://github.com/user-attachments/assets/7df722db-08f8-40bb-81d9-e3b4df15a462" />

---

## **Tech Stack**

* **MLOps:** MLflow, DVC, EvidentlyAI (planned)
* **CI/CD:** GitHub Actions
* **Serving:** FastAPI, Uvicorn, Docker, Distroless
* **Orchestration:** Kubernetes (Kind cluster)
* **Observability:** Prometheus, Grafana, ServiceMonitor
* **Model:** Linear Regression (simple by design)

---

## **Pipeline Flow (High Level)**

1. Data added → DVC tracks it → pushed to DagsHub
2. GitHub Actions triggers Continuous Training
3. MLflow logs experiment + registers new model
4. CI builds and pushes container image
5. CD updates K8s deployment with new image
6. Canary release deployed (v1 + v2)
7. Prometheus/Grafana monitor model behavior
8. Drift detection pipeline checks incoming data

---

## **How to Run Locally**

```bash
dvc repro
docker build -t house-price-serving -f docker/Dockerfile.fastapi .
kind load docker-image house-price-serving
kubectl apply -f k8s_manifests/
```

---

## **Why This Project Matters**

This project demonstrates the **full skillset required for an MLOps/DevOps/SRE engineer**:

* automation
* scalability
* observability
* reproducibility
* production-grade deployments

Not just training a model — **running ML as a real system**.

---

Just say **“Generate LinkedIn post”**.
