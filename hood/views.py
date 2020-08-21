from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Profile,Neighbourhood,User,Businesses,Post
from .forms import NeighbourhoodForm,BusinessForm,PostForm

# Create your views here.


def index(request):

    neighbourhoods = Neighbourhood.objects.all()
    user = User.objects.all()
    business = Businesses.objects.all()
    
    context= {
        ""
    }
    
    return render(request,'index.html',{'neighbourhoods':neighbourhoods,'user':user,'business':business})


def display_profile(request,username):
    profile = Profile.objects.get(user__username= username)
    # user_projects = Projects.objects.filter(author_profile =profile).order_by('created_date')
    context={
        "profile":profile,
        # "user_projects":user_projects
    }
    return render(request,'profile_details.html',context)




def neighbourhoods(request):
    current_user = request.user
    posts = Post.objects.all()
    business = Businesses.objects.all()
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            location = form.cleaned_data['location']
            occupants = form.cleaned_data['occupants']
            saveHood = Neighbourhood(name=name,location=location,occupants=occupants)
            saveHood.save()
            return redirect(index)
    else:
        form = NeighbourhoodForm()
    return render(request,'myhood/upload.html',{'form':form,'business':business,'posts':posts})




def business(request):
    if request.method == 'POST':
        form2 = BusinessForm(request.POST,request.FILES)
        if form2.is_valid():
            saveBusiness = form2.save(commit=False)
            saveBusiness.save()
            return redirect(neighbourhoods)
    else:
        form2 = BusinessForm()
    return render(request,'business.html',{'form2':form2})


def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Businesses.search_by_business_name(search_term)
        message = f"{search_term}"

        return render(request, 'myhood/search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'myhood/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request,'myhood/post.html',{'form':form})