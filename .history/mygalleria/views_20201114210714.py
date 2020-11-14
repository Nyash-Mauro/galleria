from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse, Http404
import datetime as dt
from cloudinary.forms import cl_init_js_callbacks
from .models import Photo, Category, Image, Location
from .forms import PhotoForm


def index(request):
    photo = Image.display_photo()
    return render(request, '.html', {"photo": photo})


def photo_today(request):
    date = dt.date.today()
    photo = Image.display_photo()
    return render(request, 'gallery/todays_photos.html', {"date": date, "photo": photo})


def upload(request):
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'upload.html', context)


def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', "Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

# View Function to present news from the past days


def past_days_photos(request, past_date):

    try:
        # Convert data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photo_today)

    photo = Image.days_photo(date)
    return render(request, 'gallery/past_photos.html', {"date": date, "photo": photo})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'gallery/search.html', {"message": message, "category": searched_category})

    else:
        message = "You haven't searched for any category"
        return render(request, 'gallery/search.html', {"message": message})


def category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "gallery/category.html", {"category": category})
