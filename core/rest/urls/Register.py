from django.urls import path


from ..views import Register


urlpatterns = [
    path('',
         Register.RegisterView.as_view(),
         name='auth_register'),
]