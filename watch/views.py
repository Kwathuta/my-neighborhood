from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from watch.models import *

# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    '''
    user profile
    '''
    current_user = request.user
    user = user_profile.objects.filter(user=current_user.id).first()
    if user is None:
        user = user_profile.objects.filter(user=current_user.id).first()
        posts = Post.objects.filter(user=current_user.id)
        neighborhood = Neighborhood.objects.all()
        business = Business.objects.filter(user=current_user.id)
        return render(request, 'profile.html', {"res": "Please select your neighborhood", "posts": posts, "neigborhood": neighborhood, "businesses": business})
    else:
        neighborhood = user_profile.neighborhood
        posts = Post.objects.filter(
            neighborhood=neighborhood).order_by('-posted_at')
        return render(request, 'index.html', {'posts': posts})


@login_required(login_url="/accounts/login/")
def update_profile(request):
    if request.method == "POST":

        current_user = request.user

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]

        name = request.POST["first_name"] + " " + request.POST["last_name"]

        neighborhood = request.POST["neighbourhood"]

        if neighborhood == "":
            neighborhood = None
        else:
            neighborhood = Neighborhood.objects.get(name=neighborhood)

        avatar = request.FILES["avatar"]

        user = User.objects.get(id=current_user.id)

        if user_profile.objects.filter(user_id=current_user.id).exists():

            profile = user_profile.objects.get(user_id=current_user.id)
            profile.avatar = avatar
            profile.neighborhood = neighborhood
            profile.save()
        else:
            profile = user_profile(
                user_id=current_user.id,
                name=name,
                avatar=avatar,
                neighborhood=neighborhood,
            )

            profile.save_user_profile()

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        user.save()

        return redirect("/profile", {"success": "Profile Updated Successfully"})

    else:
        return render(request, "profile.html", {"failed": "Profile Update Failed"})


@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = user_profile.objects.filter(
        user_id=current_user.id).first()
    posts = Post.objects.filter(user_id=current_user.id)
    neighbourhood = Neighborhood.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    contacts = Contact.objects.filter(user_id=current_user.id)
    return render(request, 'profile.html', {'profile': profile, 'posts': posts, 'neighbourhood': neighbourhood, 'businesses': businesses, 'contacts': contacts})


@login_required(login_url="/accounts/login/")
def posts(request):
    current_user = request.user
    profile = user_profile.objects.filter(user_id=current_user.id).first()
    if profile is None:
        profile = user_profile.objects.filter(user_id=current_user.id).first()
        posts = Post.objects.filter(user_id=current_user.id)
        neighborhood = Neighborhood.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        return render(request, "profile.html", {"res": "Please select your neighborhood to see posts", "neighborhood": neighborhood, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        neighborhood = profile.neighborhood
        posts = Post.objects.filter(
            neighborhood=neighborhood).order_by("-posted_at")
        return render(request, "posts.html", {"posts": posts})


@login_required(login_url="/accounts/login/")
def new_post(request):
    if request.method == "POST":
        current_user = request.user
        title = request.POST["title"]
        description = request.POST["description"]

        profile = user_profile.objects.filter(user_id=current_user.id).first()
        if profile is None:
            profile = user_profile.objects.filter(
                user_id=current_user.id).first()
            posts = Post.objects.filter(user_id=current_user.id)
            neighborhood = Neighborhood.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            return render(request, "profile.html", {"res": "Please update your neighborhood", "neighborhood": neighborhood, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            neighborhood = profile.neighborhood

        if request.FILES:
            image = request.FILES["image"]

            post = Post(
                user_id=current_user.id,
                title=title,
                description=description,
                image=image,
                neighborhood=neighborhood,
            )
            post.create_post()

            return redirect("/profile", {"success": "Post Created Successfully"})
        else:
            post = Post(
                user_id=current_user.id,
                title=title,
                description=description,
                neighborhood=neighborhood,
            )
            post.create_post()

            return redirect("/profile", {"success": "Post Created Successfully"})

    else:
        return render(request, "profile.html", {"res": "Post Creation Failed"})


@login_required(login_url="/accounts/login/")
def new_business(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST["name"]
        email = request.POST["email"]

        profile = user_profile.objects.filter(user_id=current_user.id).first()
        if profile is None:
            profile = user_profile.objects.filter(
                user_id=current_user.id).first()
            posts = Post.objects.filter(user_id=current_user.id)
            neighborhood = Neighborhood.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            return render(request, "profile.html", {"res": "Please update your Neighborhood", "neighborhood": neighborhood, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            neighborhood = profile.neighborhood

        if neighborhood == "":
            neighborhood = None
        else:
            neighborhood = Neighborhood.objects.get(name=neighborhood)

        business = Business(
            user_id=current_user.id,
            name=name,
            email=email,
            neighborhood=neighborhood,
        )
        business.create_business()

        return redirect("/profile", {"success": "Business Created Successfully"})
    else:
        return render(request, "profile.html", {"res": "Business Creation Failed"})


@login_required(login_url="/accounts/login/")
def new_contact(request):
    if request.method == "POST":
        current_user = request.user
        department = request.POST["name"]
        phone = request.POST["phone"]

        profile = user_profile.objects.filter(user_id=current_user.id).first()

        if profile is None:
            profile = user_profile.objects.filter(
                user_id=current_user.id).first()
            posts = Post.objects.filter(user_id=current_user.id)
            neighborhood = Neighborhood.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            return render(request, "profile.html", {"res": "Please update your Neighborhood", "neighborhood": neighborhood, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            neighborhood = profile.neighborhood

        if neighborhood == "":
            neighborhood = None
        else:
            neighborhood = Neighborhood.objects.get(name=neighborhood)

        contact = Contact(
            user_id=current_user.id,
            department=department,
            phone=phone,
            neighborhood=neighborhood,
        )
        contact.create_contact()

        return redirect("/profile", {"success": "Contact Created Successfully"})
    else:
        return render(request, "profile.html", {"res": "Contact Creation Failed"})


@login_required(login_url="/accounts/login/")
def businesses(request):
    current_user = request.user
    profile = user_profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = user_profile.objects.filter(user_id=current_user.id).first()
        posts = Post.objects.filter(user_id=current_user.id)
        neighborhood = Neighborhood.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        return render(request, "profile.html", {"res": "Please update your Neighborhood", "neighborhood": neighborhood, "businesses": businesses, "contacts": contacts, "posts": posts})

    else:
        neighborhood = profile.neighborhood
        businesses = Business.objects.filter(
            neighborhood=profile.neighborhood)
        return render(request, "business.html", {"businesses": businesses})


@login_required(login_url="/accounts/login/")
def contacts(request):
    current_user = request.user

    profile = user_profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = user_profile.objects.filter(
            user_id=current_user.id).first()
        posts = Post.objects.filter(user_id=current_user.id)

        neighborhood = Neighborhood.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)

        return render(request, "profile.html", {"res": "Please update your Neighborhood", "neighborhood": neighborhood, "businesses": businesses, "contacts": contacts, "posts": posts})

    else:
        neighborhood = profile.neighborhood
        contacts = Contact.objects.filter(neighborhood=profile.neighborhood)
        return render(request, "contacts.html", {"contacts": contacts, "neighborhood": profile.neighborhood})
