FROM python:3.9-slim

# Create a non-root user (Hugging Face requirement)
RUN useradd -m -u 1000 user
USER user

# Set environment variables for the user
ENV HOME=/home/user
ENV PATH="${HOME}/.local/bin:${PATH}"

WORKDIR ${HOME}/app

# Copy requirements first to leverage Docker cache
COPY --chown=user:user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY --chown=user:user . .

# Hugging Face exposes port 7860
EXPOSE 7860

# Run the FastAPI application on port 7860
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]