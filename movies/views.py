from django.shortcuts import render, redirect, get_object_or_404
#from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate 
from django.core.paginator import Paginator
from .models import Project
from .form import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.


	
def home(request):
	projects = Project.objects.all()[::-1]
	paginator = Paginator(projects, 3)
	pageNumber = request.GET.get('page')
	pageObj = paginator.get_page(pageNumber)
	return render(request, 'movies/home.html',  {'pageObj': pageObj})
    
def detailMovie(request, movieId):
	projects = get_object_or_404(Project, pk = movieId)
	return render(request, 'movies/detailMovie.html', {'projects': projects})
    
@login_required	
def index(request):
	projects = Project.objects.filter(user = request.user)[::-1]
	paginator = Paginator(projects, 3)
	pageNumber = request.GET.get('page')
	pageObj = paginator.get_page(pageNumber)
	return render(request, 'movies/index.html',  {'pageObj': pageObj})
	
	 
@login_required	
def viewProject(request, moviePk):	
	projects = get_object_or_404(Project, pk = moviePk, user = request.user)
	if request.method == 'GET':
		form = ProjectForm(instance = projects)
		return render (request, 'movies/viewProject.html', {'projects':projects, 'form':form})
	else:
		try:
			form = ProjectForm(request.POST, instance = projects)
			form.save()
			return redirect('index')
		except ValueError:
			return render(request, 'movies/viewProject.html',{'projects':projects, 'form':form, 'error':'Wrong Information Passed'})


@login_required	
def deleteProject(request, moviePk):
	projects = get_object_or_404(Project, pk = moviePk, user = request.user)
	if request.method == 'POST':
		projects.delete()
		return redirect('index')
	   
def signupuser(request):
	if request.method == 'GET':
		return render(request, 'movies/signupuser.html', {'form': UserCreationForm})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('index')
			except IntegrityError:
				return render(request, 'movies/signupuser.html', {'form': UserCreationForm(), 'error': 'Username already taken Plese choose different username'})
		else:
			return render(request, 'movies/signupuser.html', {'form': UserCreationForm(), 'error': 'Password did not match.'})
			
			
def loginUser(request):
	if request.method == 'GET':
		return render(request, 'movies/loginUser.html', {'form': AuthenticationForm()})
	else:
		user = authenticate(request, username =request.POST['username'] , password = request.POST['password'])
		if user is None:
			return render(request, 'movies/loginUser.html', {'form': AuthenticationForm(), 'error': 'username and password are not matching.'})
		else:
			login(request, user)
			return redirect('index')
			
			

@login_required			
def createProject(request):
	if request.method == 'GET':
		return render (request, 'movies/createProject.html', {'form': ProjectForm()})
	else:
		try:
			form = ProjectForm(request.POST)
			newProject = form.save(commit = False)
			newProject.user = request.user
			newProject.save()
			return redirect('index')
		except ValueError:
			return render (request, 'movies/createProject.html', {'error': 'Something Goes Wrong...'})



@login_required	
def logoutUser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')
