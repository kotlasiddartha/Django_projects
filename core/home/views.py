from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("""<h1>Hey I am a Django server.</h1>
    #                     <p>Hey this is coming from Django server</p>
    #                     <hr>
    #                     <h3>Hope you are doing great :)</h3>
    #                     """)
    peoples = [
        {"name":"siddartha kotla", "age":15},
        {"name":"muvva kotla", "age":23},
        {"name":"chait kotla", "age":50}
    ]

    text = """Hello this is siddartha and he is learning django"""
    return render(request, "home/index.html",context = {"page" : "Django 2023 tutorial","peoples" : peoples, "text" : text})

def about(request):
    context = {"page":"about"}
    return render(request, "home/about.html",context)

def contact(request):
    context = {"page":"contact"}
    return render(request, "home/contact.html",context)


def success_page(request):
    context = {"page":"success_page"}
    return HttpResponse("<h1>Hey this is a Success page</h1>")

