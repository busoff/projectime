# Note


## User login

Reference: https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/

### Use django authentication APP

- toplevel setting.py

```py
INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    ...
]

urlpatterns = [
    ...
    path('accounts/', include('django.contrib.auth.urls')),
    ...
]

# add template folder which stores login.html
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },

]

# redirect after login or logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

- create a user with /admin

- create login.html in <project>/template/registration

in login.html we not only provide the login form but also error handling 
```html
???
```

- Use django builtin user instead our own??
- if user doesn't login then redirect user to login page

```py
# <your-app>/views.py

from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...
```

```py
# <your-app>/settings.py
settings.LOGIN_URL = '/accounts/login'
```



