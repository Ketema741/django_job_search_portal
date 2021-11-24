from django.shortcuts import render
from django.http import HttpResponse, request
from  django.contrib import messages

# Create your views here.
def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')


def about_view(request, *args, **kwargs):
    my_contex = {
        "my_text":"this is our number: ",
         "my_number":'+251912323811',
         "contact_us": "contact us",
         "our_products": ['Apple','Mango','Bananna'],
    }
    return render(request,'about.html', my_contex)


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>social page</h1>")
