from django.shortcuts import render,redirect
from Backend.models import DestinationDB,PlaceDB,FlightBookingDb,singleDestinationBd
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def Tourism_page(request):
    return render(request,"Tourism_page.html")

def Destination_page(request):
    return render(request,"Add_Destinations.html")

def Destination_save(request):
    if request.method =="POST":
        Na = request.POST.get("Name")
        Des = request.POST.get("Description")
        img = request.FILES['image']
        obj = DestinationDB(Name=Na, Description=Des, Image=img)
        obj.save()
        return redirect(Destination_page)


def Display_Destinations(request):
    Data = DestinationDB.objects.all()
    return render(request,"Display_Destinations.html",{'Data':Data})

def Edit_Destinations(request,c_id):
    y = DestinationDB.objects.get(id=c_id)
    return render(request,"edit_Destinations.html",{'y':y})

def update_Destinations(request,p_id):
    if request.method == "POST":
        x = request.POST.get('Name')
        y = request.POST.get('Description')
        try:
            f = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(f.name, f)
        except MultiValueDictKeyError:
            file = DestinationDB.objects.get(id=p_id).Image
        DestinationDB.objects.filter(id=p_id).update(Name=x, Description=y, Image=file)
        return redirect(Display_Destinations)


# *********************************************************************************************



def Place_page(request):
    return render(request,"Add_places.html")

def Place_save(request):
    if request.method =="POST":
        D_na = request.POST.get("modeName")
        P_Na = request.POST.get("state")
        P_pr = request.POST.get("P_Price")
        P_Des = request.POST.get("P_Description")
        P_img = request.FILES['images']
        obj = PlaceDB,DestinationDB(modeName=D_na ,state=P_Na, P_Price=P_pr, P_Description=P_Des,P_Image=P_img)
        obj.save()
        return redirect(Place_page)

def Display_Places(request):
    place = PlaceDB.objects.all()
    return render(request,"Display_Places.html",{'place':place})

def Edit_Places(request,e_id):
    edit = PlaceDB.objects.get(id=e_id)
    return render(request,"Edit_places.html",{'edit':edit})

def update_Places(request,u_id):
    if request.method == "POST":
        D_na = request.POST.get("Name")
        P_Na = request.POST.get("P_Name")
        P_pr = request.POST.get("P_Price")
        P_Des = request.POST.get("P_Description")
        try:
            f = request.FILES['images']
            fs = FileSystemStorage()
            file = fs.save(f.name, f)
        except MultiValueDictKeyError:
            file = PlaceDB.objects.get(id=u_id).P_Image
        PlaceDB.objects.filter(id=u_id).update(Name=D_na, P_Name=P_Na, P_Price=P_pr, P_Description=P_Des,P_Image=file)
        return redirect(Display_Places)


# ************************************************************************************************************


def Add_Flight(request):
    return render(request,"Add_FlightBooking.html")

def Flight_save(request):
    if request.method =="POST":
        x = request.POST.get("Flight_Name")
        y = request.POST.get("Depart")
        z = request.POST.get("Arrive")
        m = request.POST.get("Price")
        f_img = request.FILES['image']
        obj = FlightBookingDb(Flight_Name=x, Depart=y, Arrive=z,Price=m, Flight_Image=f_img)
        obj.save()
        return redirect(Add_Flight)

def Display_Flight(request):
    fly = FlightBookingDb.objects.all()
    return render(request,"Display_Flight.html",{'fly':fly})

def Edit_Flight(request,f_id):
    Book = FlightBookingDb.objects.get(id=f_id)
    return render(request,"Edit_Flight.html",{'Book':Book})

def update_Flight(request,g_id):
    if request.method == "POST":
        x = request.POST.get("Flight_Name")
        y = request.POST.get("Depart")
        z = request.POST.get("Arrive")
        m = request.POST.get("Price")
        try:
            f = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(f.name, f)
        except MultiValueDictKeyError:
            file = FlightBookingDb.objects.get(id=g_id).Flight_Image
        FlightBookingDb.objects.filter(id=g_id).update(Flight_Name=x, Depart=y, Arrive=z,Price=m, Flight_Image=file)
        return redirect(Display_Flight)



# *****************************************************************************************************************************



def single_page(request):
    return render(request,"Add_single.html")

def Single_save(request):
    if request.method =="POST":
        S_na = request.POST.get("modeName")
        S_sa = request.POST.get("state")
        S_Na = request.POST.get("From_To")
        S_pr = request.POST.get("Duration")
        S_ps = request.POST.get("Price")
        S_img = request.FILES['images']
        obj = singleDestinationBd(state=S_sa, modeName=S_na, From_To=S_Na, Duration=S_pr, Price=S_ps, Place_image=S_img)
        obj.save()
        return redirect(single_page)

def Display_Single(request):
    Single = singleDestinationBd.objects.all()
    return render(request,"Display_Single.html",{'Single':Single})

def Edit_Single(request,a_id):
    sin = singleDestinationBd.objects.get(id=a_id)
    return render(request,"Edit_Single.html",{'sin':sin})

def update_Single(request,b_id):
    if request.method == "POST":
        S_na = request.POST.get("category")
        S_Na = request.POST.get("From_To")
        S_pr = request.POST.get("Duration")
        S_ps = request.POST.get("Price")
        try:
            f = request.FILES['images']
            fs = FileSystemStorage()
            file = fs.save(f.name, f)
        except MultiValueDictKeyError:
            file = singleDestinationBd.objects.get(id=b_id).Place_image
        singleDestinationBd.objects.filter(id=b_id).update(category=S_na, From_To=S_Na, Duration=S_pr, Price=S_ps, Place_image=file)
        return redirect(Display_Single)


# *********************************************************************************************************************************************


