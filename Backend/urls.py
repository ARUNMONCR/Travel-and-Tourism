from django.urls import path
from Backend import views

urlpatterns = [
    path('Tourism_page/', views.Tourism_page, name="Tourism_page"),
    path('Destination_page/', views.Destination_page, name="Destination_page"),
    path('Destination_save/', views.Destination_save, name="Destination_save"),
    path('Display_Destinations/', views.Display_Destinations, name="Display_Destinations"),
    path('Edit_Destinations/<int:c_id>/', views.Edit_Destinations, name="Edit_Destinations"),
    path('update_Destinations/<int:p_id>/', views.update_Destinations, name="update_Destinations"),

# ************************************************************************************************************


    path('Place_page/', views.Place_page, name="Place_page"),
    path('Place_save/', views.Place_save, name="Place_save"),
    path('Display_Places/', views.Display_Places, name="Display_Places"),
    path('Edit_Places/<int:e_id>/', views.Edit_Places, name="Edit_Places"),
    path('update_Places/<int:u_id>/', views.update_Places, name="update_Places"),

# ******************************************************************************************************************

    path('Add_Flight/', views.Add_Flight, name="Add_Flight"),
    path('Flight_save/', views.Flight_save, name="Flight_save"),
    path('Display_Flight/', views.Display_Flight, name="Display_Flight"),
    path('Edit_Flight/<int:f_id>/', views.Edit_Flight, name="Edit_Flight"),
    path('update_Flight/<int:g_id>/', views.update_Flight, name="update_Flight"),

# *********************************************************************************************************************


    path('single_page/', views.single_page, name="single_page"),
    path('Single_save/', views.Single_save, name="Single_save"),
    path('Display_Single/', views.Display_Single, name="Display_Single"),
    path('Edit_Single/<int:a_id>/', views.Edit_Single, name="Edit_Single"),
    path('update_Single/<int:b_id>/', views.update_Single, name="update_Single"),


]