# Concrete Compressive Strength Predictor

A full-stack machine learning application that predicts the 28-day compressive strength of concrete based on mixture proportions (cement, water, aggregates, admixtures) and curing age.

The application models the non-linear physical interactions between concrete ingredients, offering an analytical alternative to traditional 28-day physical curing tests. It is built as a modular microservice featuring a RESTful API backend, an interactive web UI, and Docker containerization for reproducible deployments.

## Features

- Interactive Web Dashboard: Clean user interface to enter mix design parameters and view real-time strength predictions.
- REST API: FastAPI backend with automated data validation via Pydantic.
- Microservices Architecture: Fully decoupled frontend and backend services.
- Containerization: Docker and Docker Compose setup for consistent local and production deployment.

## Tech Stack

- Machine Learning: Scikit-Learn (Polynomial Regression, GridSearchCV, StandardScaler), Joblib
- Backend: Python, FastAPI, Pydantic, Uvicorn
- Frontend: Streamlit, Requests
- Containerization: Docker, Docker Compose
- Data Processing: Pandas, NumPy, Matplotlib, Seaborn

## Model Performance

- R-squared (R2): 0.90
- Root Mean Squared Error (RMSE): 5.21 MPa

## Project Structure

```text
concrete-strength-predictor/
│
├── backend/
│   ├── Dockerfile                 # Backend container configuration
│   ├── main.py                    # FastAPI application
│   ├── concrete_model.joblib      # Serialized Scikit-Learn Model
│   ├── scaler.joblib              # Serialized Data Scaler
│   └── requirements.txt           # Backend dependencies
│
├── frontend/
│   ├── Dockerfile                 # Frontend container configuration
│   ├── app.py                     # Streamlit dashboard
│   └── requirements.txt           # Frontend dependencies
│
├── data/
│   ├── Concrete Compressive Strength.csv   # Original dataset
│   └── concrete.csv                        # Cleaned dataset
│
├── notebooks/
│   ├── concrete.ipynb             # EDA and model training pipeline
│   └── requirements.txt           # Data science dependencies
│
├── scripts/
│   └── concrete_to_raw.py         # Data cleaning utility script
│
├── docker-compose.yml             # Docker orchestration
└── README.md                      # Project documentation
```
## Running Locally

### Option 1: Docker Compose (Recommended)

1. **Clone the repository:**

    ```Bash
    git clone https://github.com/Raj-249/concrete-strength-predictor.git
    cd concrete-strength-predictor
    ```

2. **Build and start the containers:**

    ```Bash
    docker compose up --build
    ```

3. **Access the services:**

    - **Frontend UI:** [http://localhost:8501](http://localhost:8501/)
    - **API Documentation (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)

### Option 2: Manual Setup

1. **Backend:**

    ```Bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```

2. **Frontend:**

    ```Bash
    cd frontend
    pip install -r requirements.txt
    streamlit run app.py
    ```

## Author

**Raj Varshney** | B.Tech Civil Engineering, IIT Bhubaneswar