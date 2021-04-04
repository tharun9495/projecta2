from django.http import HttpResponse
import os
file_path=os.path.abspath(__file__)
pro2_dir_path=os.path.dirname(file_path)
dir_path=os.path.dirname(pro2_dir_path)
def func1(request):
    return HttpResponse("<h1>Hi How are you</h1>")
def func12(request):
    file_addr=os.path.join(dir_path,"sample11.html")
    fp=open(file_addr,"r")
    data=fp.read()
    return HttpResponse(data)    
