# BamChat
Full-stack Angular + FastAPI + MySQL 3D Design Generator with Role-Based Admin Panel

3d-design-generator/
├── backend/
├── frontend/
├── README.md
└── .gitignore



cd backend
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install fastapi uvicorn sqlalchemy mysqlclient alembic python-dotenv passlib bcrypt PyJWT
touch main.py

echo "__pycache__/" >> .gitignore
echo ".env" >> .gitignore
