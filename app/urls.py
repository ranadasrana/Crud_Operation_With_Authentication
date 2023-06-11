from django.urls import path

from .views import (
    home,
    login,
    registration,
    create,
    allProf,
    singleProf,
    delete,
    updateProfile,
)

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('allProf/', allProf, name='allProf'),
    path('singleProf/<int:id>/', singleProf, name='singleProf'),
    path('delete/<int:id>/', delete, name='delete'),
    path('updateProfile/<int:id>/', updateProfile, name='updateProfile'),
]
