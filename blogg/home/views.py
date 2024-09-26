from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from home.models import Contact
from blog.models import Post

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 5 or len(phone) < 8 or len(content) < 2:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name = name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(title__icontains=query)
    params = {'allPosts' : allPosts}
    return render(request, 'home/search.html', params)
