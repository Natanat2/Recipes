backend:

cd recipes 

python -m venv venv

source venv/bin/activate  # 

(или venv\Scripts\activate для Windows)

pip install -r requirements.txt

py manage.py runserver

----

frontend:

cd recipes/frontend/recipes

npm start
