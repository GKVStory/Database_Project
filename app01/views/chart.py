from django.http import JsonResponse
from django.shortcuts import render

from app01 import models


def chart_list(request):
    """ 数据统计页面 """
    return render(request, 'chart_list.html')


def chart_bar(request):
    """ 构造柱状图的数据 ，看看各部门人员年龄段分布"""
    legend = []
    series_list = []
    depart = models.Department.objects.all()
    for obj in depart:
        legend.append(str(obj))
        data_list = []
        type_1 = models.UserInfo.objects.filter(depart_id=obj.pk, age__lte=20).count()
        type_2 = models.UserInfo.objects.filter(depart_id=obj.pk, age__gt=20, age__lte=25).count()
        type_3 = models.UserInfo.objects.filter(depart_id=obj.pk, age__gt=25, age__lte=30).count()
        type_4 = models.UserInfo.objects.filter(depart_id=obj.pk, age__gt=30).count()
        data_list.append(type_1)
        data_list.append(type_2)
        data_list.append(type_3)
        data_list.append(type_4)
        series_list.append({
            "name": str(obj),
            "type": 'bar',
            "data": data_list
        })
    x_axis = ['20岁以下', '20岁至25岁', '25岁至30岁', '30岁以上']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def chart_pie(request):
    """ 构造饼图的数据，看看各种级别号码的比例 """
    count = models.PrettyNum.objects.all().count()
    db_data_list = []
    for i in range(count):
        value = models.PrettyNum.objects.filter(level=i).count()
        if value != 0:
            db_data_list.append({
                "value": value,
                "name": str(i) + "级号码"
            })
        i += 1
    result = {
        "status": True,
        "data": db_data_list
    }
    return JsonResponse(result)


def chart_line(request):
    """
    构造折线图的数据，按顺序看看年龄越大账户余额分布如何
    """
    temp_legend = []
    series_list = []
    temp_axis = []
    user = models.UserInfo.objects.all()
    for item in user:
        temp_legend.append(str(item.depart))
        temp_axis.append(item.age)
    legend = list(set(temp_legend))
    x_axis = list(set(temp_axis))
    x_axis.sort()

    for first_item in legend:
        temp_data_list = []
        for second_item in user:
            if str(second_item.depart) == str(first_item):
                for third_item in x_axis:
                    if second_item.age == third_item:
                        temp_data_list.append(int(second_item.account))
                data_list = list(set(temp_data_list))
                data_list.sort()
        series_list.append({
            "name": first_item,
            "type": 'line',
            "stack": 'Total',
            "data": temp_data_list
        })
    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)
