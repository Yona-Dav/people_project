from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.people),
    path('people/<int:person_id>', views.single_person)
]