from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Contact
from blog.models import Post

# HTML PAGES
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
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning  (request, "No search results found. Check again ")
    params = {'allPosts' : allPosts, 'query': query}
    return render(request, 'home/search.html', params)

# Authenticate APIs
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check error inputs
        if len(username) > 12:
            messages.success(request, "Your username must be under 12 characters.")  
            return redirect('home')    
        if not username.isalnum():
            messages.success(request, "Username should only contain letters and numbers")  
            return redirect('home')  
        if pass1 != pass2:
            messages.success(request, "Passwords do not match")  
            return redirect('home')    

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "Your Blogger account has been successfully created.")  
        return redirect('home')     
    else:
        return HttpResponse("404 - Not Found")
    
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username = loginusername, password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('home')
    return HttpResponse("404 - Not Found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
