## installation

``` pip install -r requirements.txt ```

``` python manage.py makemigrations ```

``` python manage.py migrate ```

``` python manage.py runserver ```

Open browser for front end views on 
127.0.0.1:8000

for auth API end points use the indicated endpoints 

## Djoser end points for authentication

|**Endpoint** | **Description**|
|---|---|
|/auth/users/| Register a new user |
| /auth/users/me/ | retrieve/update the currently logged in user |
| /auth/jwt/create/| create a JWT by passing a valid user in the post request to this endpoint|
|/auth/jwt/refresh/ | get a new JWT once the lifetime of the previously generated one expires |