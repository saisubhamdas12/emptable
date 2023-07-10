from django.shortcuts import render
from app1.models import*
from django.http import HttpResponse
# Create your views here.
def display_db(request):
    ldo=Dept.objects.all()
    leo=Emp.objects.all()
    d={'ldo':ldo,'leo':leo}
    return render(request,'display_db.html',d)

def display_dept(request):
    if request.method=="POST":
        deptno=request.POST['dept']
        dname=request.POST['dept1']
        loc=request.POST['dept2']
        do=Dept.objects.get_or_create(deptno=deptno,dname=dname,loc=loc)[0]
        do.save()
        return display_db(request)

    return render(request,'display_dept.html')

def display_emp(request):
    ldo=Dept.objects.all()
    d1={'ldo':ldo}
    if request.method=="POST":
        empno=request.POST['emp']
        ename=request.POST['emp1']
        job=request.POST['emp2']
        hiredate=request.POST['emp3']
        sal=request.POST['emp4']
        comm=request.POST['emp5']
        deptno=request.POST['deptno']
        print(deptno)
        do=Dept.objects.get(deptno=deptno)

        eo=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,hiredate=hiredate,
                                        sal=sal,comm=comm,deptno=do)[0]
        eo.save()
        # return HttpResponse('data insertion done')
        return display_db(request)

    return render(request,'display_emp.html',d1)

