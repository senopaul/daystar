"""
URL configuration for DayStar_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from schoolApp.views import *

urlpatterns = [
    path('', landingView, name='landing'),
    path('dashboard/', indexView, name='index'),
    path('admin/', admin.site.urls),


    #Sitter Urls
    path('addsitter/', addSitter, name='add_sitter'),
    path('listSitters/', listSitters, name='list_sitters'),
    path('sitters/<int:id>/', viewSitter, name='view_sitter'),
    path('viewSitter/<int:id>', viewSitter, name='view_sitter'),
    path('editSitter/<int:id>', editSitter, name='edit_sitter'),
    # path('deleteSitter/<int:id>', deleteSitter, name='delete_sitter'),



    #Baby urls
    path('addBaby/', addBaby, name='add_baby'),
    path('listBabies/', listBabies, name='list_babies'),
    path('viewBaby/<int:id>', viewBaby, name='view_baby'),
    path('editBaby/<int:id>', editBaby, name='edit_baby'),
    # path('deleteBaby/<int:id>', deleteBaby, name='delete_baby'),


    #Product urls
    path('addProduct/', addProduct, name='add_product'),
    path('listProducts/', listProducts, name='list_products'),
    path('deleteProduct/<int:id>', deleteProduct, name='delete_product'),


    #Registration URLS
    path('register/', registerView, name='register'),
    path('logon', loginView, name='logon'),
    path('logout/', logoutView, name='logout'),


    #Attendance URLS
    path('addAttendance/', addAttendance, name='add_attendance'),
    path('listAttendance/', listAttendances, name='list_attendance'),
    path('deleteAttendance/<int:id>', deleteAttendance, name='delete_attendance'),

    

    #Procurement URLS


    #Report URL

    path('reports/', reports, name='reports'),

    # path('search/', search, name='search'),
    # path('searchResults/', searchResults, name='search_results'),

    # path('settings/', settingsview, name='settings'),

]
