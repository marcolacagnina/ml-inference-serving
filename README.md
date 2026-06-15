# ML Inference Serving Application

![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green)
![Docker](https://img.shields.io/badge/Docker-blue)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces/marcolac/ml-inference-serving)

Demo showing how to serve a Hugging Face Transformers sentiment analysis model via FastAPI and Docker, deployed on a Serverless Cloud infrastructure.

## Features
- FastAPI REST API for inference (`/predict`)
- Pre-trained **DistilBERT** sentiment analysis model using **Hugging Face**
- **Cloud-Native Docker Environment:** Hardened container running as a non-root user (UID 1000) for security compliance.
- Serverless deployment via **Hugging Face Spaces**.


## Local Installation (Docker)

If you want to run this locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/marcolacagnina/ml-inference-serving.git](https://github.com/marcolacagnina/ml-inference-serving.git)
    cd ml-inference-serving/
    ```

2.  **Docker building:**
    ```bash
    docker build -t transformer-api .
    ```
    
3.  **Docker run:**
    *(Note: Port is mapped to 7860 to match Cloud deployment standards)*
    ```bash
    docker run -p 7860:7860 transformer-api
    ```

## Usage (cURL)
Send a POST request to `/predict` with JSON:
```bash
curl -X POST "[https://marcolac-ml-inference-serving.hf.space/predict](https://marcolac-ml-inference-serving.hf.space/predict)" \
     -H "Content-Type: application/json" \
     -d '{"text": "Nice to meet you!"}'

Example response:
 ```bash
 {
  "label": "POSITIVE",
  "score": 0.9998
 }
 ```

## Tech Stack
* Python 3.11+
* **FastAPI** + Pydantic
* Hugging Face Transformers
* PyTorch
* Docker


