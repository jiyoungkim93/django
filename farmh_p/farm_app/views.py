# 작성자 : 김지영

from django.shortcuts import render
# from django.http import HttpResponse

from .models import  Users, Comments, Crops, Deeplearnings, Dronerunnings,Farmdiaries, Pestinfos, Ptcinfos   # 모델 불러오기
from django.http import HttpResponse
# Create your views here.

# 메인페이지 출력 / css폴더에 있는 html연결
#def home(request):
#    return HttpResponse('login.html')
    
def Main(request):
    return render(request, 'Main.html')

# 데이터확인하기
# 디비연동이 성공적으로 되었는지 데이터를 출력

# 사용자
def users_view(request):
    users = Users.objects.all()
    #post테이블의 모든  객체 불러와서 posts변수에 저장
    return render(request, 'Main.html',{"users": users})


#
def comments_view(request):
    comments = Comments.objects.all() 
    return render(request, 'Main.html',{"comments": comments})

#딥러닝
def deeplearnings_view(request):
    deeplearnings = Deeplearnings.objects.all()  
    return render(request, 'Main.html',{"deeplearnings": deeplearnings})

#드론
def dronerunnings_view(request):
    dronerunnings = Dronerunnings.objects.all()   
    return render(request, 'Main.html',{"dronerunnings": dronerunnings})

#이력관리
def farmdiaries_view(request):
    farmdiaries = Farmdiaries.objects.all()  
    return render(request, 'Main.html',{"farmdiaries": farmdiaries})

#
def pestinfos_view(request):
    pestinfos = Pestinfos.objects.all()    
    return render(request, 'login.html',{"pestinfos": pestinfos})

#
def ptcinfos_view(request):
    ptcinfos = Ptcinfos.objects.all()  
    return render(request, 'login.html',{"ptcinfos": ptcinfos})

#
def crops_view(request):
    crops = Crops.objects.all()    
    return render(request, 'login.html',{"crops": crops})

# 드론 
def drone(req):
    
    return render(req,"drone_control.html")

def history(req):
    
    return render(req,"history.html")


def analysis(req):
   
    return render(req,"analysis.html")