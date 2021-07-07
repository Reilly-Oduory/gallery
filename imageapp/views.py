from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Image, CATEGORY_CHOICES, Comment
from .forms import CommentForm

choices = CATEGORY_CHOICES


# Create your views here.
def index(request):
    title = "Reilly's Photo Gallery"
    posts = Image.all_images()

    return render(request, 'index.html', {"title": title, "posts": posts, "choices": choices})


def category(request, category_name):
    images = Image.search_image(category_name)
    message = f"{category_name}"

    return render(request, 'sort.html', {"images": images, "message": message, "choices": choices})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        filter_location = request.GET.get("image")
        filtered_images = Image.filter_by_location(filter_location)
        message = f"{filter_location}"
        return render(request, 'search.html', {"message": message, "filtered_images": filtered_images, "choices": choices})
    else:
        message = "You haven't searched for any term yet"
        return render(request, 'search.html', {"message": message, "choices": choices})


def individual_image(request, image_id):
    try:
        image = Image.get_image_by_id(image_id)
        comments = Comment.all_comments(image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'image.html', {"image": image, "choices": choices, "comments":comments})


def comment(request, image_id):
    image = Image.get_image_by_id(image_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.image = image
        obj.save()
        return redirect(f'/image/{image_id}')

    return render(request, 'comment.html', {"image": image, "form": form, "choices": choices})