from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()

    return render(
        request,
        "review_system/index.html",
        context={"reviews": reviews}
    )

@login_required
def create_review(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = request.user
        pub_date = request.POST.get("pub_date")

        Review.objects.create(
            title=title,
            content=content,
            author=user,
            pub_date=pub_date
        )

        return redirect("review-list")
    
    return render(
        request,
        "review_system/review_form.html"
    )