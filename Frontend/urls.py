from django.urls import path
from Frontend import views

urlpatterns = [
    path('Frontend_page/', views.Frontend_page, name="Frontend_page"),
    path('Category_Destinations/<int:id>/', views.Category_Destinations, name="Category_Destinations"),
    path('filter_destinations/<int:pk>/', views.filter_destinations, name="filter_destinations"),




# ************************************Lgin page URL********************************************************************

    path('signup',views.RegistrationView.as_view(),name="Signup"),
    path('login/', views.SignInView.as_view(), name="login"),
    path('logout/',views.signout_view,name="logout"),

# ************************************Flight Booking URL*************************************************************

    path('FlightBooking/<int:id>/', views.FlightBooking, name="FlightBooking"),
    path('TicketBook/<int:id>/', views.TicketBook, name="TicketBook"),
    # path('Save_details/', views.Save_detail, name='Save_details'),
    path('Place_order/<int:pk>/', views.Place_order, name='Place_order'),
    path('success/', views.success, name='success'),
    path('About/', views.About, name='About'),


# ***************************************Single_Place URL***********************************************************************

    path('Single_places/<int:Singlid>/', views.Single_places, name="Single_places"),

]
