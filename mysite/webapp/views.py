from django.shortcuts import render
def home(request):
    print(request)
    return render(request,'home.html',{'text':'TEST'})
#static to dynamic content is rendering
#response----render it is  a file
#need to render the template
def add(request):
    value1=int(request.POST['num1'])
    value2 = int(request.POST['num2'])
    res=value1 + value2
    return render(request,'result.html',{'result':res})