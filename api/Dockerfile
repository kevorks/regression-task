FROM python:3.10

WORKDIR  /app/api

# Copy only the necessary files for the API service
COPY main.py .
COPY best_model.pkl .
COPY requirements-api.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements-api.txt

# Expose the port on which the FastAPI server will run
EXPOSE 8000

# Run the FastAPI server when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
