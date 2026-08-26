# Concrete Compressive Strength Predictor

A full-stack machine learning application that predicts the 28-day compressive strength of concrete based on mixture proportions (cement, water, aggregates, admixtures) and curing age.

The application models the non-linear physical interactions between concrete ingredients, offering an analytical alternative to traditional 28-day physical curing tests. It is built as a modular microservice featuring a FastAPI backend, an interactive web UI, and is deployed on cloud platforms for easy accessibility.

## Live Application

**Access the live application here:** [https://concrete-compressive-strength-predictions.streamlit.app/](https://concrete-compressive-strength-predictions.streamlit.app/)

## Features

- **Interactive Web Dashboard:** Clean user interface to enter mix design parameters and view real-time strength predictions.
- **FastAPI Backend:** High-performance backend with automated data validation via Pydantic.
- **Microservices Architecture:** Fully decoupled frontend and backend services.
- **Cloud Deployment:** Deployed on Streamlit Cloud (frontend) and FastAPI Cloud (backend) for easy accessibility without infrastructure overhead.
- **Production Ready:** Containerization with Docker for reproducible local development and testing.

## Tech Stack

- **Machine Learning:** Scikit-Learn (Polynomial Regression, GridSearchCV, StandardScaler), Joblib
- **Backend:** Python, FastAPI, Pydantic, Uvicorn
- **Frontend:** Streamlit, Requests
- **Cloud Deployment:** Streamlit Cloud, FastAPI Cloud
- **Containerization:** Docker, Docker Compose (for local development)
- **Data Processing:** Pandas, NumPy, Matplotlib, Seaborn

## Model Performance

- R-squared (R2): 0.90
- Root Mean Squared Error (RMSE): 5.21 MPa

## Project Structure

```text
Concrete Strength/
│
├── backend/
│   ├── Dockerfile                 # Backend container configuration
│   ├── main.py                    # FastAPI application
│   ├── concrete_model.joblib      # Trained machine learning model
│   ├── scaler.joblib              # Data preprocessing scaler
│   └── requirements.txt           # Backend dependencies
│
├── frontend/
│   ├── Dockerfile                 # Frontend container configuration
│   ├── app.py                     # Streamlit dashboard application
│   └── requirements.txt           # Frontend dependencies
│
├── data/
│   ├── Concrete Compressive Strength.csv   # Original raw dataset
│   ├── concrete.csv                        # Cleaned dataset
│   └── concrete_to_raw.py                  # Data cleaning script
│
├── notebooks/
│   ├── concrete.ipynb             # EDA and model training notebook
│   └── requirements.txt           # Jupyter dependencies
│
├── docker-compose.yml             # Docker Compose configuration
└── README.md                      # Project documentation
```
## Cloud Deployment

The application is currently deployed on free cloud platforms:

- **Frontend:** Hosted on [Streamlit Cloud](https://streamlit.io/cloud) - automatically deploys from the GitHub repository
- **Backend API:** Hosted on [FastAPI Cloud](https://fastapicloud.com) - automatically deploys from the GitHub repository

No credit card required for deployment on these platforms. The services communicate seamlessly for real-time predictions.

## Running Locally for Development

### Option 1: Docker Compose (Recommended for Local Development)

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

### Option 2: Manual Setup (Without Docker)

1. **Backend:**

    ```Bash
    cd backend
    pip install -r requirements.txt
    fastapi dev main.py
    ```

    Backend will be available at `http://localhost:8000`

2. **Frontend (in a new terminal):**

    ```Bash
    cd frontend
    pip install -r requirements.txt
    streamlit run app.py
    ```

    Frontend will be available at `http://localhost:8501`

## API Endpoints

The backend FastAPI application provides the following endpoints:

- **`GET /`** - Root endpoint returning API status
- **`POST /predict`** - Submit concrete mix parameters and receive strength prediction
  - Expected input: JSON with 8 concrete mix parameters
  - Returns: Predicted compressive strength in MPa

**Example API Request:**

```json
{
  "cement": 540,
  "slag": 0,
  "ash": 0,
  "water": 162,
  "superplastic": 40,
  "coarseagg": 1040,
  "fineagg": 676,
  "age": 28
}
```

Visit the API docs at `/docs` for interactive Swagger documentation.

## Model Details

- **Algorithm:** Polynomial Regression (degree 2)
- **Training Data:** 1,030 concrete mixture samples
- **Features:** 8 input parameters
- **Performance Metrics:**
  - R² Score: 0.90 (explains 90% of variance)
  - RMSE: 5.21 MPa
- **Data Scaling:** StandardScaler for feature normalization

## Deploying to Cloud

### Deploy Frontend to Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository and main file (`frontend/app.py`)
5. Configure the app and deploy

### Deploy Backend to FastAPI Cloud

1. Navigate to the `backend` directory in your terminal.
2. Install the CLI: `pip install "fastapi[standard]"`
3. Run `fastapi login` to authenticate.
4. Run `fastapi deploy` to build and deploy to the cloud.
5. Update the frontend `app.py` with the new API endpoint URL.

## Usage

1. **Visit the live app:** [https://concrete-compressive-strength-predictions.streamlit.app/](https://concrete-compressive-strength-predictions.streamlit.app/)
2. **Enter concrete mix parameters:**
   - Cement (kg/m³)
   - Blast furnace slag (kg/m³)
   - Fly ash (kg/m³)
   - Water (kg/m³)
   - Superplasticizer (kg/m³)
   - Coarse Aggregate (kg/m³)
   - Fine Aggregate (kg/m³)
   - Curing Age (Days)
3. **View the predicted 28-day compressive strength in MPa**

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

Please ensure your code follows best practices and includes appropriate documentation.

## Author

**Raj Varshney** | B.Tech Civil Engineering, IIT Bhubaneswar