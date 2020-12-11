<<<<<<< HEAD
from django.shortcuts import render
from django.shortcuts import HttpResponse
from io import BytesIO
from utils.check_code import create_validate_code
# Create your views here.


def check_code(request):
    """
    验证码
    :param request:
    :return:
    """
=======
from django.shortcuts import render,HttpResponse
from io import BytesIO
from utils.check_code import create_validate_code

# Create your views here.

def check_code(request):
>>>>>>> origin/master
    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def longin(request):
<<<<<<< HEAD
     if request.method=='GET':
          return render(request,"login.html")
     return HttpResponse("FULIHUA")
=======
    if request.method=='GET':
        return render(request,"login.html")
    else:

        return HttpResponse("FULIHUA")


>>>>>>> origin/master
