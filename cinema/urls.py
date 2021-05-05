"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from movies import views
from django.conf.urls.static import static
from django.conf import settings
from movies.api import ProjectCreateApi, ProjectApi, ProjectUpdateApi,  ProjectDeleteApi

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name = 'home'),
	path('<int:movieId>/',views.detailMovie, name = 'detailMovie'),
	path('index/', views.index, name = 'index'),
	path('movies/<int:moviePk>/',views.viewProject, name = 'viewProject'),
	path('movies/<int:moviePk>/delete/', views.deleteProject, name = 'deleteProject'),
	path('signup/', views.signupuser, name = 'signupuser'),
	path('logout/', views.logoutUser, name = 'logoutUser'),
	path('login/', views.loginUser, name = 'loginUser'),
	path('createProject/', views.createProject, name = 'createProject'),
	path('api',ProjectApi.as_view()),
	path('api/create',ProjectCreateApi.as_view()),
	path('api/<int:pk>',ProjectUpdateApi.as_view()),
	path('api/<int:pk>/delete',ProjectDeleteApi.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
