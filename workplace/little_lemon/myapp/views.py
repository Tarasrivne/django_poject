from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import LogForm
from .models import Menu

# def form_view(request):
#     form = LogForm()
#     if request.method == 'POST':
#         form = LogForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {"form":form}
#     return render(request, "home.html", context)

# def menu(request):
#     newmenu = {'pricechart' : [
#     {'name': "phalaphel", 'price': "11"},
#     {'name': "clecky", 'price': "13"},
#     {'name': "borsch", 'price': "18"}]}
#     return render(request, "menu.html", newmenu)
#
# def menu_id(request):
#     newmenu = Menu.objects.all()
#     item_dict = {'menu': newmenu}
#     return render(request, "menu.html", item_dict)



#
# def about(request):
#     about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant,"
#                               " focused on traditional recipes served with a modern twist."
#                               " The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu"
#                               " of 12–15 items that they rotate seasonally. "
#                               "The restaurant has a rustic and relaxed atmosphere with moderate prices,"
#                               " making it a popular place for a meal any time of the day."}
#     return render(request, "about.html", about_content)





#
# def home(request):
#     return HttpResponse("<h1> Welcome to Little Lemon! </h1>" )
# def about(request):
#     return HttpResponse("<h1> About us </h1>" )
# def Menu(request):
#     return HttpResponse("<h2> Menu for you! </h2>" )
# def book(request):
#     return HttpResponse("<h3> Make a booking Mafaka </h3>" )
#
# def pathview(request, name, id):
#     return HttpResponse("Name:{} UserID:{}".format(name, id))
#
# def qryview(request):
#     name = request.GET['name']
#     id = request.GET['id']
#     return HttpResponse("Name:{} UserID:{}".format(name, id))
#
# def showform(request):
#     return render(request, "form.html")
#
# def drinks(request,drink_name):
#     drink = {
#     'mocha' :'type of coffee',
#     'tea':'type of beverage',
#     'lemonade':'type of refreshment'
#     }
#     choice_of_drink = drink[drink_name]
#     return HttpResponse( f"<h2> {drink_name} </h2>" + choice_of_drink)
#
#


# Create your views here.
def home(request):
    return render(request, "home_ex.html", {})

def register(request):
    return render(request, "register.html", {})

def login(request):
    return render(request, "login.html", {})