# 🩺 Kidney Disease Classification – End-to-End MLOps Project

An end-to-end Deep Learning and MLOps project that automates the **Kidney Disease Classification pipeline** using modern tools like **DVC**, **MLflow**, **AWS**, and **GitHub Actions**. The model leverages **VGG16** architecture and includes full CI/CD automation from training to deployment inside Docker containers.

---

<img src="./assets/Screenshot 2025-06-28 014237.png" alt="Kidney Disease Classification App UI" style="width:100%; border:1px solid #ccc; border-radius:6px;" />

## 🚀 Project Overview

- ✅ Classify kidney scans using **VGG16** deep learning model
- 📁 Pipeline orchestration using **DVC**
- 📊 Experiment tracking with **MLflow**
- ☁️ Cloud storage with **AWS S3**
- 🐳 Dockerized workflow pushed to **AWS ECR**
- 🖥️ Model served on **AWS EC2** via Docker container
- 🔁 CI/CD setup with **GitHub Actions** + **Self-Hosted Runner**

---

## 📂 Dataset Used

- **Dataset:** CT Kidney Dataset (Normal, Tumor)
- 📥 Source: [Kaggle - CT Kidney Dataset](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone)
- 💡 Images categorized into 2 classes: `normal` and `tumor`

---

## 🧠 Deep Learning Pipeline

1. **Data Ingestion** – Load & prepare datasets
2. **Base Model Preparation** – Load the base model **VGG16** from Keras API
3. **Model Training** – Image resizing, preprocessing, and training on dataset
4. **Model Evaluation** – Evaluate model with metrics
5. **Prediction Interface** – Web app using Flask


---

## 🔧 MLOps Stack Used

| Tool           | Purpose                                      |
|----------------|----------------------------------------------|
| **DVC**        | Pipeline orchestration & version control     |
| **MLflow**     | Model tracking, metrics, experiments         |
| **AWS S3**     | Artifact & model storage                     |
| **AWS ECR**    | Docker container registry                    |
| **AWS EC2**    | Hosting prediction API using Docker          |
| **Docker**     | Containerize and run Flask app               |
| **GitHub Actions** | CI/CD for training, testing & deployment |

---

## 🧪 Model Architecture

- Base Model: **VGG16** (pre-trained on ImageNet)
- Fine-tuned on custom kidney disease dataset
- Input Size: `224x224` RGB images
- Final activation: `softmax`

---

---

## 🛠️ Setup & Installation

```bash
# 1. Clone the repository
https://github.com/keshav1017/kidney-disease-classification

# 2. Create conda environment
conda create -n kidney python=3.8 -y
conda activate kidney

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the pipeline
python main.py
```

---

## 🔁 Run Flask App (Locally)

```bash
python flask_app/app.py
```

Open `http://localhost:8080` to access the app.

---

## 📦 MLflow Tracking

- Track experiment results using MLflow
- Hosted on [dagshub.com](https://dagshub.com/)

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/your-user/kidney-disease-project.mlflow
export MLFLOW_TRACKING_USERNAME=your_user
export MLFLOW_TRACKING_PASSWORD=your_token
python main.py
```

---

## 📡 DVC Commands

```bash
dvc init       # Initialize DVC
dvc repro      # Run entire pipeline
dvc dag        # View pipeline as DAG
```

---

## 🐳 Docker Setup

### Build and Push Image to AWS ECR
```bash
docker build -t kidney-classifier .
aws ecr get-login-password | docker login --username AWS --password-stdin <your-repo>
docker tag kidney-classifier:latest <your-ecr-url>
docker push <your-ecr-url>
```

### Run on AWS EC2
```bash
sudo docker run -p 8080:8080 kidney-classifier
```

---

## 🔄 GitHub Actions CI/CD

- Automatically trains model on every push to `main`
- Pushes trained model and Docker image
- Deploys to AWS EC2 via self-hosted runner

---

## ✅ Final Outputs

- 🧠 Trained VGG16 model for kidney classification
- 🔁 Fully automated pipeline with MLflow + DVC
- 📦 Dockerized app deployed via AWS EC2
- 📊 Metrics logged & visualized via Dagshub MLflow

---

## 👨‍💻 Author

**Keshav Prasad**  
🔗 [LinkedIn](https://linkedin.com/in/keshavprasad1017) 

---

⭐ If you found this project helpful, don't forget to give it a star!
