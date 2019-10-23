from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
import datetime

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .models import User, School as SCHOOL
from sql_operating.mysql_class import SqlModel
from .common import province_city



class Index(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        admin_user = request.POST.get('username')
        admin_pass = request.POST.get('pwd')
        try:
            mysql_username = User.objects.filter(admin_user=admin_user).first()
            mysql_password = User.objects.filter(admin_pass=admin_pass)
        except:
            return JsonResponse({'result': 'fail'})
        if mysql_username:
            if mysql_password:
                return JsonResponse({'result': 'success','username':admin_user})
            return JsonResponse({'result': 'fail'})
        else:
            return JsonResponse({'result': 'fail'})


class Task(View):
    def get(self,request):
        admin_user = request.COOKIES.get('username')
        sql = "select admin_type from admin_user where admin_user='%s'" % admin_user
        try:
            admin_type = SqlModel().select_one(sql)
        except:
            return JsonResponse({"result": "fail", "msg": "数据库查询错误"})

        if admin_type:
            task_root = ["实训任务", "教学资源", "学生管理", "教师管理", "班级管理", "专业管理", "教务管理", "学校管理", "课程管理","案例管理"]
            task_edu = ["实训任务", "教学资源", "学生管理", "教师管理", "班级管理", "专业管理", "教务管理"]
            task_teach = ["实训任务", "教学资源", "学生管理"]
            task_student = ["实训任务", "教学资源"]
            if admin_type[0] == '1':
                return JsonResponse({"result": task_root})
            elif admin_type[0] == '2':
                return JsonResponse({"result": task_edu})
            elif admin_type[0] == '3':
                return JsonResponse({"result": task_teach})
            elif admin_type[0] == '4':
                return JsonResponse({"result": task_student})
            else:
                return JsonResponse({"result": "fail", "msg": "请重新登入"})
        else:
            return JsonResponse({"result": "fail", "msg": "请重新登入"})


# 学校管理页面
class School(View):
    """学校管理页面展示，学校新增/修改逻辑"""
    def get(self,request):
        """GET请求，学校管理页面展示"""
        sql = "select school_code,school_name,school_rank,school_type,school_province,school_city,admin_name,create_name,create_time from school"
        try:
            school_info = SqlModel().select_all(sql)
        except:
            return JsonResponse({"result": "数据库查询错误，请重试"})

        if school_info:
            for i in school_info:
                i[8] = str(i[8])[:10]
            return JsonResponse({"result": school_info})
        else:
            return JsonResponse({"result": ""})

    def post(self,request):
        """POST请求，新增、修改逻辑"""
        school_name = request.POST.get('school_name')
        school_code = request.POST.get('school_code')
        school_rank = request.POST.get('school_rank')
        school_type = request.POST.get('school_type')
        school_province = request.POST.get('school_province')
        school_city = request.POST.get('school_city')
        admin_name = request.POST.get('admin_name')
        admin_user = request.COOKIES.get('username')    # cookies中获取登入者帐号
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        try:
            result1 = SCHOOL.objects.filter(school_code=int(school_code))
            if result1:
                sql = "update school set school_code='%s',school_name='%s',school_rank='%s',school_type='%s',school_province='%s', school_city='%s',admin_name='%s',create_name='%s',create_time='%s' where school_code='%s'" % (int(school_code), school_name, school_rank, school_type, school_province, school_city, admin_name,admin_user, now_time,school_code)
                res = SqlModel().insert_or_update(sql)
                if res:
                    return JsonResponse({"result": "修改成功"})
                else:
                    return JsonResponse({"result": "修改失败"})
            else:
                sql = "insert into school (school_code,school_name,school_rank,school_type,school_province,school_city,admin_name,create_name,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                int(school_code), school_name, school_rank, school_type, school_province, school_city, admin_name,
                admin_user, now_time)
                res = SqlModel().insert_or_update(sql)
                if res:
                    return JsonResponse({"result": "新增成功"})
                else:
                    return JsonResponse({"result": "新增失败"})
        except:
            return JsonResponse({"result": "fail", "msg": "数据库错误,请重试"})


class School_delete_search(View):
    """get请求，学校删除接口，post请求，学校搜索接口"""
    def get(self,request):
        """学校修改功能"""
        school_code = request.GET.get("school_code")

        sql = "delete from school where school_code='%s'" % int(school_code)
        try:
            res = SqlModel().insert_or_update(sql)
            if res:
                return JsonResponse({"result": "删除成功"})
            else:
                return JsonResponse({"result": "删除失败", "msg": "该学校信息不存在"})
        except:
            return JsonResponse({"result": "fail", "msg": "数据库错误,请重试"})

    def post(self,request):
        school_name = request.POST.get('school_name')
        sql = "select school_code,school_name,school_rank,school_type,school_province,school_city,admin_name,create_name,create_time from school where school_name like '%%%s%%'" % school_name
        try:
            school_info = SqlModel().select_all(sql)
            if school_info:
                return JsonResponse({"result": school_info})
            else:
                return JsonResponse({"result": ""})
        except:
            return JsonResponse({"result": "fail", "msg": "数据库错误,请重试"})


def province(request):
    """学校页面，所在省份下拉接口"""
    province_list = []
    for i in province_city:
        province_list.append(i["name"])

    return JsonResponse({"result":province_list})

def city(request):
    """学校页面，城市下拉接口"""
    city_list=[]
    province_name = request.GET.get('province_name')
    for i in province_city:
        if i["name"] == province_name:
            city_list = i["city"]
    if city_list:
        return JsonResponse({"result": city_list})
    else:
        return JsonResponse({"result": ""})

def edu(request):
    """学校页面，教务管理员下拉接口"""
    school_code = request.GET.get('school_code')
    sql = "select admin_name from admin_user where school_code='%s'" % school_code
    admin_name = SqlModel().select_all(sql)
    admin_name_list = []
    if admin_name:
        for i in admin_name:
            admin_name_list.append(i[0])
        return JsonResponse({"result":admin_name_list})
    else:
        return JsonResponse({"result":""})


class Edu(View):
    """教务管理"""
    def get(self,request):
        """教务页面展示"""
        admin_user = request.COOKIES.get('username')
        sql = "select school_code from admin_user where admin_user='%s'" % admin_user
        try:
            school_code = SqlModel().select_one(sql)
            if school_code:
                school_code = school_code[0]
                sql = "select admin_name,admin_user,admin_pass,phone,admin_state,create_name,create_time from admin_user where school_code='%s'" % int(school_code)
                edu_list = SqlModel().select_all(sql)
                if edu_list:
                    return JsonResponse({"resutlt": edu_list})
                else:
                    return JsonResponse({"result": ""})
            else:
                return JsonResponse({"result": "该登入帐号没有对应学校，请重新登入"})
        except:
            return JsonResponse({"result": "数据库错误，请重试"})

    def post(self,request):
        """教务新增、修改接口"""
        admin_name = request.POST.get('admin_name')
        admin_user = request.POST.get('admin_user')
        admin_pass = request.POST.get('admin_pass')
        phone = request.POST.get('phone')
        admin_state = request.POST.get('admin_state')
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        admin_type = "2"
        log_accounts = request.COOKIES.get('username')   # 登入者帐号，创建人

        sql = "select admin_name,school_code from admin_user where admin_user='%s'" % log_accounts
        sql2 = "select school_code from admin_user where admin_user='%s'" % admin_user   # 该语句判断数据是否存在，是新增还是修改
        try:
            admin_list = SqlModel().select_one(sql)   # admin_list[0] = admin_name = create_name , admin_list[1] = school_code
            res = SqlModel().select_one(sql2)
        except:
            return JsonResponse({"result": "fail", "msg": "数据库错误，请重试"})

        if res:
            """修改接口"""
            sql_revise = "update admin_user set admin_name='%s',admin_user='%s',admin_pass='%s',admin_type='%s',phone='%s',school_code='%s',admin_state='%s',create_name='%s',create_time='%s' where admin_user='%s'" % (admin_name,admin_user,admin_pass,admin_type,phone,admin_list[1],admin_state,admin_list[0],now_time,admin_user)
            resu = SqlModel().insert_or_update(sql_revise)
            if resu:
                return JsonResponse({"result": "修改成功"})
            else:
                return JsonResponse({"result": "修改失败"})
        else:
            """新增接口"""  # TODO 这里继续
            sql_add = "insert into admin_user "


            return JsonResponse({"result": ""})











