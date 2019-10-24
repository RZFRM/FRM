from django.shortcuts import render

# Create your views here.


# Create your views here.
import os

from django.http import JsonResponse, response, HttpResponse
from django.shortcuts import render, redirect
import pandas as pd
import xlrd
import uuid
from system_config.models import CorpsInfo, MakeTaxMidPerson, User, EmpBaseInfo, EmpTaxInfo, EmpSalary, JobList, \
    CorpsInfo
from IsearchAPI.ISAPI import rpa_rest
from system_config.models import User, Job_list_summary, Application_info
import time
from sql_operating.mysql_class import *


# TODO 生成8位唯一任务编号
def create_uuid():

    a = uuid.uuid1()
    job_no = str(a)
    return job_no[0:8]

# TODO  货物信息
goods_numbers ={'002':'封边条','003':'A产品配件',
               '004':'B产品配件','007':'包装箱',
               '008':'工具','009':'手套',
               '010':'工作服'}







DB = Mysql_client_FRM()

#  TODO  采购机器人基础配置页
def pruchasing_robot_base(request):
    return render(request, 'purchasing_robot_base_manager.html')


#  TODO  采购机器人业务管理页
def pruchasing_robot_business(request):
    return render(request, 'purchasing_robot_business_manager.html', locals())


#  TODO  采购机器人任务管理页
def pruchasing_robot_jobs(request):
    return render(request, 'purchasing_robot_jobs_manager.html')


#  TODO  采购机器人 弹框第一步
def purchasing_created(request):

    return render(request, 'purchasing_created_1.html')


# TODO 第一步数据确认
def purchasing_created_data(request):
    #  TODO  入库添加 新的数据

    return render(request,'200')


#  TODO  采购机器人 弹框第二步
def purchaes_requisitions_create(request):
    # user_name = request.COOKIES.get('username')
    # modules = request.POST.get("modules")
    #
    # price = request.POST.get("price")
    # unit  = request.POST.get("unit")
    # quantity = request.POST.get("quantity")
    # print( user_name,'-----------------------' ,modules, price , unit , quantity)
    #
    # purchase_number = 'CG0000007'
    # print(locals())
    return render(request, 'purchaes_requisitions_2.html', locals())



# TODO  采购机器人第二步数据

def purchaes_requisitions_create_data(request):
    user_name = request.COOKIES.get('username')

    # TODO 请购单编号
    purchase_number_1 = request.POST.get('purchase_number')
    # TODO 直接采购
    procurement_type_1 =request.POST.get('procurement_type')
    # TODO 采购用途
    purchase_usesing_1 =request.POST.get('purchase_usesing')
    # TODO  货物编码
    goods_number_1 =request.POST.get('goods_number')
    # TODO 建议单价
    recommended_unite_price_1 =request.POST.get('unit_price')
    # TODO 单位规格
    specification_1 =request.POST.get('specification')


    # TODO 数量
    goods_count_1 =request.POST.get('goods_count')

    # TODO 建议金额
    recommended_price_1 =request.POST.get('recommended_price')
    # TODO  申请人
    applicant_1 =request.POST.get('applicant')

    # TODO 申请部门
    application_depart_1 =request.POST.get('application_depart')

    # TODO 申请日期
    purchase_time_1 =request.POST.get('purchase_time')

    # TODO 部门负责人
    department_head_1 =request.POST.get('department_head')

    # TODO 公司负责人
    company_head_1 =request.POST.get('company_head')
    #
    # print(purchase_number,procurement_type,purchase_usesing, goods_number,
    #       recommended_unite_price_, specification, goods_count,
    #       recommended_price,applicant, application_depart, purchase_time, department_head
    #       ,company_head)

    #  TODO  插入数据库
    #  TODO  1.获取机器人名字, 2,获取请购信息

    business_name_1 = str(goods_numbers[goods_number_1])+'采购申请与审批'
    gmt_create_1 = (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    gmt_modified_1 = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    purchase_apply_status  ='1116'
    recommended_date = '2020-12-09'
    # print(gmt_modified, gmt_create, purchase_apply_status, business_name)
    try:
        DB.get_insert(table='purchase_apply_table',
                      values=(gmt_create_1, gmt_modified_1,purchase_number_1,procurement_type_1,purchase_usesing_1,
                              goods_number_1,recommended_unite_price_1, specification_1, goods_count_1,
                              recommended_price_1,applicant_1, application_depart_1,user_name
                              ,purchase_time_1,recommended_date,
                              purchase_apply_status,department_head_1,company_head_1,business_name_1),
                    fields ="(gmt_create, gmt_modified,purchase_number,procurement_type,purchase_usesing,"
                            "goods_number,recommended_unite_price_ ,specification,goods_count,"
                            "recommended_price,applicant,application_depart,user_name,"
                            "purchase_time,recommended_date,"
                            "purchase_apply_status,department_head,company_head,business_name)")
    except Exception as e:
        print('插入失败！')
        return  False





    #  TODO  创建任务信息

    job_no = create_uuid()
    jobs_name = '采购'+goods_numbers[goods_number_1]+'请购单填制'
    print('job_no ============================',job_no)
    print('jobbbbbbbbbbbbbbb:', job_no)
    # TODO  获取开始时间写入数据库  用户名  写入数据库
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localTime)

    # TODO  写入数据库
    try:
        job_list_summary = Job_list_summary()
        job_list_summary.job_type = request.POST.get('robot_name')
        job_list_summary.job_no = job_no
        job_list_summary.job_name = jobs_name
        job_list_summary.user_name_id = user_name
        job_list_summary.job_start_time = localTime
        job_list_summary.job_status = '1110'
        job_list_summary.save()
    except:
        print('写入数据库失败！')
    #  TODO  启动RPA  --

    # TODO 添加任务信息
    # print( user_name,'-----------------------' ,modules, price , unit , quantity)


    return HttpResponse(200)


#  TODO  采购机器人 弹框第三步
def purchaes_requisitions_determine(request):

    return render(request, 'purchaes_requisitions_determine_3.html')


#  TODO  采购机器人 弹框第四步
def purchaes_order_create(request):
    return render(request, 'purchaes_order_4.html')


#  TODO  采购机器人 弹框第五步
def purchaes_order_determine(request):
    return render(request, 'purchaes_order_determine_5.html')


#  TODO  采购机器人 弹框第六步
def purchaes_storage_create(request):
    return render(request, 'purchaes_storage_6.html')


#  TODO  采购机器人 弹框第七步
def purchaes_storage_determine(request):
    return render(request, 'purchaes_storage_determine_7.html')


#  TODO  采购机器人 弹框第八步
def purchaes_reimburse_create(request):
    return render(request, 'purchaes_reimburse_8.html')


#  TODO  采购机器人 弹框第九步
def purchaes_reimburse_determine(request):
    return render(request, 'purchaes_reimburse_determine_9.html')


#  TODO  采购机器人 弹框第十步
def purchaes_payment_create(request):
    return render(request, 'purchaes_payment_10.html')


#  TODO  采购机器人 弹框第十一步
def purchaes_payment_determine(request):
    return render(request, 'purchaes_payment_determine_11.html')


#  TODO  采购机器人 弹框第十二步
def purchaes_business_data_display(request):
    return render(request, 'purchaes_business_data_display_12.html')


#  TODO  任务列表信息

#  TODO  任务 任务  大致 信息
def set_purchase_robot_jobs_info(request):
     #

    data = {"code": 0, "msg": "", "count": 1000, "data": [
        {"id": 10010, "job_no": "6A55V4AD", "job_name": "2020年12月6日采购封边条-付款单录入及核销", "job_type": "  采购付款机器人",
         "job_start_time": "2020/12/17 23:03:26", "job_status": '正在执行', },
        {"id": 10010, "job_no": "SDR55X75", "job_name": "2020年12月6日采购封边条-发票关联及核算", "job_type": "  采购报账机器人",
         "job_start_time": "2020/12/17 20:44:47", "job_status": '正在执行', },
        {"id": 10010, "job_no": "C5SV582X", "job_name": "2020年12月6日采购封边条-到货单及入库单填写", "job_type": "  采购入库机器人",
         "job_start_time": "2020/12/10 10:27:18", "job_status": '正在执行', },
        {"id": 10010, "job_no": "5ZCD6CZ6", "job_name": "2020年12月6日采购封边条-采购订单填写", "job_type": "  采购订货机器人",
         "job_start_time": "2020/12/6 11:29:34", "job_status": '正在执行', },
        {"id": 10010, "job_no": "62AGC86X", "job_name": "2020年12月6日采购封边条-请购单填写", "job_type": "  采购申请机器人",
         "job_start_time": "2020/12/6 08:54:34", "job_status": '正在执行', },
        {"id": 10010, "job_no": "DR65V3E9", "job_name": "2020年11月1日采购X型板-付款单录入及核销", "job_type": "采购付款机器人",
         "job_start_time": "2020/11/11 12:26:02", "job_status": '待执行', },
        {"id": 10010, "job_no": "3FTB3C55", "job_name": "2020年11月1日采购X型板-发票关联及核算", "job_type": "采购报账机器人",
         "job_start_time": "2020/11/09 14:48:21", "job_status": '待执行', },
        {"id": 10010, "job_no": "ADHJ8121", "job_name": "2020年11月1日采购X型板-到货单及入库单填写", "job_type": "采购入库机器人",
         "job_start_time": "2020/11/05 07:30:24", "job_status": '待执行', },
        {"id": 10010, "job_no": "25G8C6EC", "job_name": "2020年11月1日采购X型板-采购订单填写", "job_type": "采购订货机器人",
         "job_start_time": "2020/11/01 17:22:02", "job_status": '待执行', },
        {"id": 10010, "job_no": "63Z8GXa5", "job_name": "2020年11月1日采购X型板-请购单填写", "job_type": "采购申请机器人",
         "job_start_time": "2020/10/30 14:04:47", "job_status": '待执行', },
        # {"id": 10010, "job_no": "A5AFX58F", "job_name": "2020年11月1日采购X型板-付款单录入及核销", "job_type": "采购机器人", "job_start_time": "2020/10/27 09:45:31", "job_status": '未完成',},
    ]}

    return JsonResponse(data)


def set_purchase_robot_buession_info(request):


    data = {"code": 0, "msg": "", "count": 1000, "data": [
        {"id": 10010, "job_no": "采购封边条", "job_name": "2020/12/6 18:03:26", "job_type": "封边打孔车间（二车间）",
         "job_start_time": "纪晶", "job_status": '未处理', "job_time": '2020/12/17 23:03:26', },
        {"id": 10011, "job_no": "采购X型板", "job_name": "2020/11/27 16:13:06", "job_type": "封边打孔车间（二车间）",
         "job_start_time": "纪晶", "job_status": '已处理', "job_time": '2020/11/29 23:03:26', },
        {"id": 10012, "job_no": "采购手套", "job_name": "2020/11/17 17:43:45", "job_type": "封边打孔车间（二车间）",
         "job_start_time": "纪晶", "job_status": '未处理', "job_time": '2020/11/17 23:03:26', },
        {"id": 10013, "job_no": "采购1CM板材", "job_name": "2020/11/09 05:48:49", "job_type": "封边打孔车间（二车间）",
         "job_start_time": "纪晶", "job_status": '已处理', "job_time": '2020/11/09 23:03:26', },
        {"id": 10014, "job_no": "采购3cm板材", "job_name": "2020/10/28 10:33:18", "job_type": "封边打孔车间（二车间）",
         "job_start_time": "纪晶", "job_status": '已处理', "job_time": '2020/10/28 23:03:26', },
        {"id": 10015, "job_no": "采购6CM板材", "job_name": "2020/10/20 15:47:21", "job_type": "封边打孔车间（二车间）",
         "job_start_time": "纪晶", "job_status": '未处理', "job_time": '2020/10/20 23:03:26', },
    # {"id": 10010, "job_no": "adsx456", "job_name": "10月采购付款机器人", "job_type": "采购机器人", "job_start_time": "20191114", "job_status": '待执行',},
    ]}

    return JsonResponse(data)




def set_create_purchase_number(request):
    # TODO  判断 数据库是否有 CG000001

    try:
        buessines_info = DB.get_select('purchase_apply_table','id','id')
        print(buessines_info)
        if buessines_info  == False:
            id = 1
            purchase_number = "CG0000" + str(id)
            return HttpResponse(purchase_number)
        else:
            id = int(buessines_info) +1
            purchase_number = "CG0000" + str(id)
            return HttpResponse(purchase_number)
    except Exception as e:
        print('调取数据库失败!',e)
        return HttpResponse(False)









