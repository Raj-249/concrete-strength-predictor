# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy ONLY the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies (disabling pip cache keeps the image small)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your backend code (main.py and the .joblib files)
COPY . .

# Expose the application port
EXPOSE 8000

# Execute the backend server when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]