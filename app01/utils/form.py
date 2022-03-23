from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.bootstrap import BootStrapModelForm


class UserModelForm(BootStrapModelForm):
    name = forms.CharField(
        min_length=3,
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", 'account', 'create_time', "gender", "depart"]


class PrettyModelForm(BootStrapModelForm):

    class Meta:
        model = models.PrettyNum
        fields = ["mobile", 'price', 'level', 'status']

    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def clean_mobile(self):
        # 当前编辑的哪一行的ID
        txt_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")

        # 验证通过，用户输入的值返回
        return txt_mobile
