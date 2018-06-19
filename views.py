from django.shortcuts import render

# Create your views here.
def indexs(request):
    return render(request,'index.html')
def showData(request):
    if request.method=='POST':
        outing=request.POST['outi']
        triping=request.POST['trip']
        dinner=request.POST['dinn']
        person=request.POST['pers']
        a =float(outing) /float(person)
        b =float(triping) /float(person)
        c =float(dinner) /float(person)
        d=float(outing)+ float(triping)+ float(dinner)
        e=a+b+c
        data={'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'person':person}
    return render(request,'display.html',data)