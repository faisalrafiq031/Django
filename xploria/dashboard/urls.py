from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tables/', views.tables, name='tables'),
    path('query-editor/', views.query_editor, name='query_editor'),
    path('designer/', views.designer, name='designer'),
    path('analytics/', views.analytics, name='analytics'),
    path('get-columns/', views.get_columns, name='get_columns'),
]