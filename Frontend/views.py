from django.shortcuts import render,redirect
from .models import Save_Details as Save_Details
from Frontend.models import Save_Details
from Backend.models import DestinationDB,FlightBookingDb,PlaceDB,singleDestinationBd,Hotels,Restaurants
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.views.generic import View, FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRECT))



def Frontend_page(request):
    pro = DestinationDB.objects.all()
    return render(request,"Frontend_page.html",{'pro':pro})



def Category_Destinations(request,id):
    pro = DestinationDB.objects.filter(id=id)
    places = PlaceDB.objects.filter(modeName__id=id)

    destinations = singleDestinationBd.objects.filter(modeName__id=id)


    return render(request,"Category_Destinations.html", {'places':places,'pro':pro,'destinations':destinations})



def filter_destinations(request,pk):
    single_destinations = singleDestinationBd.objects.filter(state=pk)

    return render(request,"Single_Destinations.html",{'destinations':single_destinations})

# ******************************************************************************************************************


def Single_places(request,Singlid):
    single = singleDestinationBd.objects.get(id=Singlid)
    Hotel = Hotels.objects.filter(destination__id=Singlid)
    Restaurant = Restaurants.objects.filter(destination__id=Singlid)
    fling = FlightBookingDb.objects.all()
    return render(request,"Single_places.html", {'single':single,'Hotel':Hotel,'Restaurant':Restaurant,'fling':fling})


# *******************************************************************************************************


def FlightBooking(request, id):
    fling = FlightBookingDb.objects.filter(destination__id=id)
    ticket = singleDestinationBd.objects.all()
    return render(request, "FlightBook.html", {'fling': fling,'ticket':ticket})


def TicketBook(request,id):
    ticket = Hotels.objects.filter(destination=id)
    Hotel = Hotels.objects.all()
    destination = singleDestinationBd.objects.get(id=id)
    total=destination.Price

    payment = client.order.create({
        "amount": total * 100,
        "currency": "INR",
        "payment_capture":"1"
         })
    order_id = payment['id']
    context = {
        'order_id':order_id,
        'payment':payment,


    }
    return render(request,"Ticket_Book.html",{'ticket':ticket,'Hotel':Hotel,'destination':destination,"total":total,"context":context})

def Place_order(request, pk):
    if request.method == "POST":
        Name = request.POST.get('Name')
        State = request.POST.get('State')
        Phone = request.POST.get('Phone')
        Email = request.POST.get('Email')
        Date = request.POST.get('Date')
        Quantity = request.POST.get('Quantity')

        price = request.POST.get('Price')
        sn = singleDestinationBd.objects.get(id=pk)
        Save_Details.objects.create(user=request.user, Name=Name, State=State, Phone=Phone, Email=Email,Date=Date,Quantity=Quantity, single_destination=sn, price=price)
        messages.success(request, 'Details saved successfully.')
        return redirect('TicketBook', id=pk)


    return render(request, "Ticket_Book.html", {'messages': messages.get_messages(request)})




@csrf_exempt
def success(request):
    if request.user.is_authenticated:
        save_details = Save_Details.objects.filter(user=request.user).latest('created_at')
        return render(request, "success.html", {"detail": save_details})
    else:
        return render(request, "userlogin.html") 





# **********************************************************Loging/logout************************************************



def userlogin_page(request):
    return render(request,"userlogin.html")



class RegistrationView(FormView):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'Signup.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration successfully")
            return redirect('login')
        messages.error(request,"Please enter correct details")
        return render(request, 'Signup.html', {"form": form})


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'userlogin.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            psw = form.cleaned_data.get('password')
            usr = authenticate(request, username=uname, password=psw)
            if usr:
                login(request, user=usr)
                messages.success(request,"login successfully")
                return redirect('Frontend_page')
        messages.error(request,"Invalid Userlogin")
        return render(request, 'userlogin.html', {"form": form, "messages": messages.get_messages(request)})

def signout_view(request, *args, **kwargs):
    logout(request)
    return redirect("Frontend_page")



# ********************************************************************************************************




def About(request):
    return render(request,"About.html")