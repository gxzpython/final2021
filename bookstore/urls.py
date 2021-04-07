from django.urls import path

from . import views

app_name="bookstore"

urlpatterns=[
    # http://127.0.0.1:8000/book-store/

    path('',views.index,name='index'),
    # http://127.0.0.1:8000/book-store/signin/

    path('signin/',views.signin,name='signin'),
    # http://127.0.0.1:8000/book-store/register/

    path('register/',views.register,name='register')
]