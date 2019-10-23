from django.shortcuts import render

# Create your views here.


# Create your views here.
import os

from django.http import JsonResponse, response
from django.shortcuts import render, redirect
import pandas as pd
import xlrd
import uuid
from system_config.models import CorpsInfo, MakeTaxMidPerson, User, EmpBaseInfo, EmpTaxInfo, EmpSalary, JobList, \
    CorpsInfo
from IsearchAPI.ISAPI import rpa_rest


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

    return JsonResponse({"result":200})


#  TODO  采购机器人 弹框第二步
def purchaes_requisitions_create(request):
    return render(request, 'purchaes_requisitions_2.html')


# TODO  采购机器人第二步数据
def purchaes_requisitions_create_data(request):
    return render(request, '200')


#  TODO  采购机器人 弹框第三步
def purchaes_requisitions_determine(request):
    user_name = request.COOKIES.get('username')
    data = request.POST.get('data')
    print( user_name,'-----------------------' ,data)


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
    # print('detail =====================', user_jobs)
    # data_list = []
    #
    # print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
    # jobs_company_count  = JobList.objects.filter(job_no=detail_job_no).count()
    # # jobs_company_count2 = jobs_company_count1.count()
    # print('jobs_company_count =========================', jobs_company_count)
    # job_emp_str = EmpSalary.objects.filter(job_no=detail_job_no).count()
    #
    # job_crops_faile_count =JobList.objects.filter(job_no=detail_job_no, job_result='1115').count()
    # job_crops_scurss_count = JobList.objects.filter(job_no=detail_job_no, job_result='1118').count()
    # print('jobs_emp_count =========================', job_emp_str, job_crops_faile_count, job_crops_scurss_count)
    #
    # for i in user_jobs:
    #     # print('row : user_jobs', i)
    #     data_dic = {
    #                    "jobs_id": i.job_no
    #                    , "jobs_type": "个税机器人"
    #                    , "jobs_start_time":str(i.job_start_time)
    #                    ,"jobs_stop_time": str(i.job_end_time)
    #                    ,"jobs_summary_time": str(i.job_use_time)
    #                     # ,"jobs_resutl": run_status[i.job_status]
    #                     ,"jobs_company_count": jobs_company_count
    #                     ,"jobs_person_summary_count":job_emp_str
    #                     ,'jobs_company_scues':job_crops_scurss_count
    #                     ,'jobs_company_fail':job_crops_faile_count
    #     }
    #     data_list.append(data_dic)
    # print('data_list =================',data_list)
    # data = {
    #     "code": 0
    #     , "msg": ""
    #     , "count": 1
    #     , "data": data_list
    # }
    # print('deatil =========data================',data)

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
    # user_name = request.COOKIES.get('username')
    # print(111111111111111111111111111111)
    # print(detail_job_no)
    #
    # user_jobs = JobList.objects.filter(user_name = user_name)
    #
    # # jobs_list = Job_list_summary.objects.get(user_name=user_name)
    #
    # print('detail =====================', user_jobs)
    # data_list = []
    #
    # print(' 已完成：：：：：：：：：：：：：：：：：', user_jobs)
    # jobs_company_count  = JobList.objects.filter(job_no=detail_job_no).count()
    # # jobs_company_count2 = jobs_company_count1.count()
    # print('jobs_company_count =========================', jobs_company_count)
    # job_emp_str = EmpSalary.objects.filter(job_no=detail_job_no).count()
    #
    # job_crops_faile_count =JobList.objects.filter(job_no=detail_job_no, job_result='1115').count()
    # job_crops_scurss_count = JobList.objects.filter(job_no=detail_job_no, job_result='1118').count()
    # print('jobs_emp_count =========================', job_emp_str, job_crops_faile_count, job_crops_scurss_count)
    #
    # for i in user_jobs:
    #     # print('row : user_jobs', i)
    #     data_dic = {
    #                    "jobs_id": i.job_no
    #                    , "jobs_type": "个税机器人"
    #                    , "jobs_start_time":str(i.job_start_time)
    #                    ,"jobs_stop_time": str(i.job_end_time)
    #                    ,"jobs_summary_time": str(i.job_use_time)
    #                     # ,"jobs_resutl": run_status[i.job_status]
    #                     ,"jobs_company_count": jobs_company_count
    #                     ,"jobs_person_summary_count":job_emp_str
    #                     ,'jobs_company_scues':job_crops_scurss_count
    #                     ,'jobs_company_fail':job_crops_faile_count
    #     }
    #     data_list.append(data_dic)
    # print('data_list =================',data_list)
    # data = {
    #     "code": 0
    #     , "msg": ""
    #     , "count": 1
    #     , "data": data_list
    # }
    # print('deatil =========data================',data)

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
        # {"id": 10016, "job_no": "采购包装箱", "job_name": "2020/11/16 10:33:06", "job_type": "封边打孔车间（二车间）", "job_start_time": "纪晶", "job_status": '未完成',"job_time": '2020/10/27 19:53:46',},
        # {"id": 10017, "job_no": "采购A配件", "job_name": "2020/10/20 10:33:06", "job_type": "封边打孔车间（二车间）", "job_start_time": "纪晶", "job_status": '未完成',"job_time": '2020/10/30 09:50:32',},
        # {"id": 10018, "job_no": "采购B配件", "job_name": "2020/10/20 10:33:06", "job_type": "封边打孔车间（二车间）", "job_start_time": "纪晶", "job_status": '已完成',"job_time": '2020/10/26 14:08:02',},
        # {"id": 10019, "job_no": "采购工具", "job_name": "2020/10/20 10:33:06", "job_type": "封边打孔车间（二车间）", "job_start_time": "纪晶", "job_status": '待执行',"job_time": '2020/10/31 20:46:21',},
        # {"id": 10020, "job_no": "采购工作服", "job_name": "2020/10/20 10:33:06", "job_type": "封边打孔车间（二车间）", "job_start_time": "纪晶", "job_status": '已完成',"job_time": '2020/11/20 15:01:23',},
        # {"id": 10021, "job_no": "采购电脑", "job_name": "2020/10/20 10:33:06", "job_type": "封边打孔车间（二车间）", "job_start_time": "纪晶", "job_status": '已完成',"job_time": '2020/10/23 18:41:56',},
        # {"id": 10010, "job_no": "78asdx5", "job_name": "10月采购合同机器人", "job_type": "采购机器人", "job_start_time": "20191112", "job_status": '待执行',},
        # {"id": 10010, "job_no": "54687xd", "job_name": "10月采购报账机器人", "job_type": "采购机器人", "job_start_time": "20191113", "job_status": '待执行',},
        # {"id": 10010, "job_no": "adsx456", "job_name": "10月采购到货入库机器人", "job_type": "采购机器人", "job_start_time": "20191114", "job_status": '待执行',},
        # {"id": 10010, "job_no": "adsx456", "job_name": "10月采购付款机器人", "job_type": "采购机器人", "job_start_time": "20191114", "job_status": '待执行',},
    ]}

    return JsonResponse(data)




def create_purchase_number():
    # TODO  判断 数据库是否有 CG000001
    
    pruchase_number = 'CG'




'''

DROP TABLE IF EXISTS `purchase_change_data`;
CREATE TABLE `purchase_apply_table` (
  `id` int (10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `gmt_create` datetime NOT NULL COMMENT '创建时间',
  `gmt_modified` datetime NOT NULL COMMENT '最后修改时间',
  `purchase_number` varchar(20)  DEFAULT NULL COMMENT '采购编号',
  `purchase_usesing` varchar(20)  DEFAULT NULL COMMENT '采购用途',
  `goods_number` varchar(20)  DEFAULT NULL COMMENT '货物名称',
  `recommended_unite_price_` varchar(20)  DEFAULT NULL COMMENT '建议单价',
  `specification`  varchar(20) default  NULL  COMMENT '单位',
  `goods_count` varchar(20)  DEFAULT NULL COMMENT '货物数量',
  `recommended_price` varchar(20)  DEFAULT NULL COMMENT '建议金额',
  `applicant` varchar(20)  DEFAULT NULL COMMENT '申请人',
   `user_name`  varchar(20)  DEFAULT  NULL COMMENT  '用户名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

'''