## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/MariamKipshidze/fastapi-learning-series.git
````

### 2. Create and Activate a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist yet, install FastAPI and Uvicorn manually:

```bash
pip install fastapi[all] uvicorn
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

This will start the development server at `http://127.0.0.1:8000/`
Interactive API docs - `http://127.0.0.1:8000/docs`
Alternative API docs - `http://127.0.0.1:8000/redoc`
