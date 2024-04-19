from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.inicio, name="inicio"),
    path('new', v.alumno_new, name="alumno_new"),
    path('edit/<int:id>', v.alumno_update, name="alumno_update"),
    path('delete/<int:id>', v.alumno_delete, name="alumno_delete"),
    path('view/<int:id>', v.alumno_view, name="alumno_view"),
]