from django.shortcuts import render
from django.http import HttpResponse

from .models import Grades,Students,Scores

from django.db.models import F,Q 

# Create your views here.

def index(request):
    return HttpResponse(" This is my_app view !!")

def grades(request):
    
    # 去模板里取数据
    gradesList = Grades.objects.all()

    # grade = Grades.objects.filter(students__scontend__contains='try')
    # print(grade)
    #可以使用模型的A属性与B属性进行比较 
    g = Grades.objects.filter(ggirlnum__gt=F('gboynum')) #F对象
    print(g)

    # 将数据传递给模板,模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'my_app/grades.html', {"grades": gradesList})

def students(request):
    # studentsList = Students.objects.all()
    studentsList = Students.stuObj.all()
    studentsList2 = Students.stuObj2.all()

    # studentsList3 = Students.stuObj2.all()[0:2]
    # studentsList3 = Students.stuObj2.filter(sname__contains="z")
    #条件为And模式 可以取反~Q
    # studentsList3 = Students.stuObj2.filter(Q(pk__lte=1) | Q(sage__gt=20))
    studentsList3 = Students.stuObj2.filter(~Q(pk__lte=1))

    return render(request, 'my_app/students.html', {"students": studentsList,'students2':studentsList3})

def geturl1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + " " + b + " " + c)

def showregist(request):
    return render(request, 'my_app/register.html',)

def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("register")


from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def redirect1(request):
    # return HttpResponseRedirect('/redirect2')
    return redirect('/redirect2')
def redirect2(request):
    return HttpResponse("to redirect2 ")


def main(request):
    username = request.session.get("name","guest")
    return render(request,"my_app/main.html",{'username':username})


def login(request):
    return render(request, 'my_app/login.html', {})

def showmain(request):
    # print("ssssssssssssssss")
    username = request.POST.get("username")
    request.session['name'] = username

    # request.session.set_expiry(10) #设置session 过期时间
    return redirect('/main')

from django.contrib.auth import logout
def quit(request):

    logout(request)
    return redirect('/main')





