from django.urls import path
from . import views

from main_app.views import editor, delete_document


urlpatterns = [
    path('', editor, name='editor'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
    path('accounts/signup/', views.signup, name='signup'),
]