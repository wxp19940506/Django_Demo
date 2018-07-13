from django.shortcuts import render
from djpager.form import ContactForm
from django.http import HttpResponse
from djpager.models import UserInfo
# Create your views here.
# 保存提交的数据
def index(request):
    if request.method == "POST":
        user = ContactForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponse("保存成功")
        else:
            return HttpResponse("保存失败:")
    else:
        return render(request, "index.html")

def base(request):
    if request.method == "POST":
        user = ContactForm(request.POST)
        if user.is_valid():
            data_name = user.data.get("name")
            data_age = user.data.get("age")
            a =UserInfo.objects.filter(name=data_name).update(age=data_age)
            if a == 0:
                isSave = UserInfo.objects.create(name=data_name,age=data_age)
                print(str(isSave)+"---")
                if isSave:
                    return HttpResponse("新增成功")
                else:
                    return HttpResponse("新增失败")
            else:
                return HttpResponse("修改成功")

            # user.save()
            return HttpResponse("保存成功")
        else:
            return HttpResponse("保存失败")
    else:
        return render(request, "base.html")