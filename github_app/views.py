from django.shortcuts import render
import requests
import json

def index(request):
    if request.method == 'POST':
        username = request.POST.get('screen_name')
        count = request.POST.get('count')
        repos_response = requests.get('https://api.github.com/users/'+username+'/repos?per_page='+count)        
        repos = repos_response.json()
        return render(request, 'github_app/index.html', {'repos':repos, 'user':username})
    else:
        return render(request, 'github_app/index.html', {})

