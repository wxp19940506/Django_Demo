from django.shortcuts import render
from djpager.form import ContactForm
from django.http import HttpResponse
from djpager.models import UserInfo
# Create your views here.

def index(request):
    if request.method == "POST":
        user = ContactForm(request.POST)
        if user.is_valid():
            try:
                user_name = user.data.get("name")
                print(user_name)
                # username = UserInfo.objects.get(user_name)
                u = UserInfo().objects.get(name="12")
                print(u+"-----")
                if user_name == u.name:
                    u.age = user.age
                    u.save()
                    return HttpResponse("修改成功")
            except AttributeError:
                print("AttributeError")
                user.save()
                return HttpResponse("保存成功")
        else:
            return HttpResponse("保存失败:"+str(user.errors))
    else:
        return render(request, "index.html")

