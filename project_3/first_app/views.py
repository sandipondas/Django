from django.shortcuts import render

# Create your views here.
def home(request):
    d = { 'author' : 'sandipon', 'age' : 20, 'list' : ["Django", "is", "best"], 'courses' : [
        {
            'id' : 1,
            'name' : "phitron",
            'fee' : 2000
        },
        {
            'id' : 2,
            'name' : "Math",
            'fee' : 1500
        },
        {
            'id' : 1,
            'name' : "C",
            'fee' : 5000
        }

    ]}
    return render(request, 'home.html', d)