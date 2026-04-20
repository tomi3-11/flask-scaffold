FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key #use "openssl rand -hex 30" to generate a random key
DATABASE_URL=sqlite:///instance/{{project_name}}.db
