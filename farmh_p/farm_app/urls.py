from django.urls import path
from . import views
import farm_app

urlpatterns = [
    path("",views.Main,name="main"),
    # path("123/",views.Insert,name="create"),
    path("drone/",views.drone,name="drone"),
    
    path("history/",views.history,name="history"),
    path("analysis/",views.analysis,name="analysis"),
    path("result/",views.result,name="result"),
    path('farm_app/upload/',views.upload,name="upload"),
    path('farm_app/upload_create/',views.upload_create,name="upload_create"),
    #path('farm_app/profile/',views.profile,name="profile"),
]


