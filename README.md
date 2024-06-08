# recipe-repo
This is a Recipe Sharing Platform

Follow below steps to  install and run
1. clone the repo.
2. run `pip install -r requirements.txt`.
3. run `python3 manage.py migrate`.
4. run `python3 manage.py createsuperuser`, #follow the commands after this
5. run `python3 manage.py runserver 8000`.

# APIS
Below are the apis

1. Create User: `http://127.0.0.1:8000/api/account/user-create/` method=POST. #only mobile and password are required to create user.
2. Login: `http://127.0.0.1:8000/api/login-user/`  method=POST.
3. Create Recipe: `http://127.0.0.1:8000/api/recipes/` method=POST.
4. Get Recipe: `http://127.0.0.1:8000/api/recipes/` method=GET.
4. Update Recipe: `http://127.0.0.1:8000/api/recipes/<int:pk>` method=PUT/PATCH.
4. Delete Recipe: `http://127.0.0.1:8000/api/recipes/<int:pk>` method=DELETE.
5. Create Category: `http://127.0.0.1:8000/api/categories/`  method=POST.
6. Get Category:`http://127.0.0.1:8000/api/categories/` method=GET
7. Get Review:`http://127.0.0.1:8000/api/reviews/` method=GET.
8. Create Review:`http://127.0.0.1:8000/api/reviews/` method=POST.
8. Update Review:`http://127.0.0.1:8000/api/reviews/<int:pk>` method=PUT/PATCH.
8. Delete Review:`http://127.0.0.1:8000/api/reviews/<int:pk>` method=DELETE.

for any information, feel free to contact at 'vandanaiec3093@gmail.com'

For DEMO:
url: http://vandanap.pythonanywhere.com/admin
username: 9988665544
password: 9988665544


