from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render



def homepage(request):
    data = {"header": "Homepage", "message": "Welcome to my site!"}
    return render (request, 'homepage.html', context=data)

    # return HttpResponse('<h1>Home</h1>')
def about(request):
    header = "About us"
    staff = ['John Nichols', 'John Rogers', 'Timothy Smith']
    director= {"name": "David Lee", "img": '/director.jpg'}
    address = ('20 W 34th St.', 'New York', 'NY 10001', 'USA')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)
    # return HttpResponse(f"""<h1>About</h1>
    # <div> Company Name: {company_name} </div>
    # <div> Company Phone: {company_phone} </div>
    # """)
