# ML Inference Serving Application

![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-1.24.1-green)
![Docker](https://img.shields.io/badge/Docker-blue)

Demo showing how to serve a Hugging Face Transformers sentiment analysis model via FastAPI and Docker.

## Features
- FastAPI REST API for inference (`/predict`)
- Pre-trained **DistilBERT** sentiment analysis model using **Hugging Face**
- Dockerized environment for reproducible deployment


## Installation and Docker

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/marcolacagnina/ml-inference-serving.git
    cd ml-inference-serving/
    ```

2.  **Docker building**
    ```bash
    docker build -t transformer-api .
    ```
    
3. **Docker run**
   ```bash
   docker run -p 8000:8000 transformer-api
   ```

## Usage
Send a POST request to `/predict` with JSON:
 ```bash
 {
  "text": "Nice to meet you!"
 }
 ```

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


