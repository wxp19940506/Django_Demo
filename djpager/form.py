from django.forms import ModelForm,ValidationError
from djpager.models import UserInfo
class ContactForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'

    def clean(self):
        clean_data = super(ContactForm, self).clean()
        age = clean_data.get("age")
        if age is None:
            raise ValidationError("请输入age的值")
        elif age > 100:
            raise ValidationError("你有100岁！？是不是傻")
        return clean_data