from django.urls import path
from . import views

urlpatterns = [
    path("",views.Main,name="main"),
    # path("123/",views.Insert,name="create"),
    path("drone/",views.drone,name="drone"),
    
    path("history/",views.history,name="history"),
    path("analysis/",views.analysis,name="analysis"),
]


