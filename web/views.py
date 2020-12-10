from django.shortcuts import render,HttpResponse
from io import BytesIO
from utils.check_code import create_validate_code

# Create your views here.

def check_code(request):
    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def longin(request):
    if request.method=='GET':
        return render(request,"login.html")
    else:
        request.
        return HttpResponse("FULIHUA")


