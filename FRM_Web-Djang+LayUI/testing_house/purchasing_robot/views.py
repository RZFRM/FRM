import time

from django.shortcuts import render

# Create your views here.


# Create your views here.
import os

from django.http import JsonResponse, response, HttpResponse
from django.shortcuts import render, redirect
import pandas as pd
import xlrd
import uuid
from system_config.models import User, Job_list_summary, Application_info, JobList ,EmpSalary ,CorpsInfo
from IsearchAPI.ISAPI import rpa_rest
from . import  models

detail_job_no  = ''


#  TODO  采购机器人基础配置页
def pruchasing_robot_base(request):

    return render(request, 'purchasing_robot_base_manager.html')


#  TODO  采购机器人业务管理页
def pruchasing_robot_business(request):

    return render(request, 'purchasing_robot_business_manager.html', locals())



#  TODO  采购机器人任务管理页
def pruchasing_robot_jobs(request):

    return render(request, 'purchasing_robot_jobs_manager.html')



#  TODO  任务列表信息

#  TODO  任务 任务  大致 信息
def set_purchase_robot_jobs_info(request):
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
        {"id": 10010, "job_no": "6x54asd", "job_name": "10月采购请购机器人", "job_type": "采购机器人", "job_start_time": "20191111", "job_status": '待执行',},
        {"id": 10010, "job_no": "78asdx5", "job_name": "10月采购合同机器人", "job_type": "采购机器人", "job_start_time": "20191112", "job_status": '待执行',},
        {"id": 10010, "job_no": "54687xd", "job_name": "10月采购报账机器人", "job_type": "采购机器人", "job_start_time": "20191113", "job_status": '待执行',},
        {"id": 10010, "job_no": "adsx456", "job_name": "10月采购到货入库机器人", "job_type": "采购机器人", "job_start_time": "20191114", "job_status": '待执行',},
        {"id": 10010, "job_no": "asd12345", "job_name": "10月采购付款机器人", "job_type": "采购机器人", "job_start_time": "20191114", "job_status": '待执行',},
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
        {"id": 10010, "job_name": "2020年10月采购材料A", "job_type": "采购机器人", "job_start_time": "20191111", "job_status": '待执行',},
        # {"id": 10010, "job_no": "78asdx5", "job_name": "10月采购合同机器人", "job_type": "采购机器人", "job_start_time": "20191112", "job_status": '待执行',},
        # {"id": 10010, "job_no": "54687xd", "job_name": "10月采购报账机器人", "job_type": "采购机器人", "job_start_time": "20191113", "job_status": '待执行',},
        # {"id": 10010, "job_no": "adsx456", "job_name": "10月采购到货入库机器人", "job_type": "采购机器人", "job_start_time": "20191114", "job_status": '待执行',},
        # {"id": 10010, "job_no": "adsx456", "job_name": "10月采购付款机器人", "job_type": "采购机器人", "job_start_time": "20191114", "job_status": '待执行',},
        ]}



    return  HttpResponse(data)

    return JsonResponse(data)








#  TODO  任务列表 启动采购机器人
def set_purchase_startjobs_info(request):
    job_no = request.POST.get('job_no')
    job_type = request.POST.get('job_type')

    username = request.COOKIES.get('username')
    client_id = User.objects.get(user_name=username)
    robot_client_id = client_id.user_agent_no
    print("=======================", job_no, job_type)
    if job_no == '6x54asd':
        #  TODO  请购机器人
        start_robot(jobs='purchase_requisition_RPA_2', rpa_client_id=robot_client_id, job_no=job_no)
        return HttpResponse('success')

    elif  job_no  == '78asdx5':
        #  TODO   采购机器人  采购合同机器人
        start_robot(jobs='purchase_order_RPA', rpa_client_id=robot_client_id, job_no=job_no)
        return HttpResponse('success')

    elif  job_no  == '54687xd':
        #  TODO   采购机器人  采购入库机器人
        start_robot(jobs='purchase_warehousing', rpa_client_id=robot_client_id, job_no=job_no)
        return HttpResponse('success')

    elif  job_no  == 'adsx456':
        #  TODO   采购机器人  采购发票记账机器人
        start_robot(jobs='purchase_to_account', rpa_client_id=robot_client_id, job_no=job_no)
        return HttpResponse('success')

    elif  job_no  == 'asd12345':
        #  TODO   采购机器人  采购报账机器人
        start_robot(jobs='purchase_payment_RPA', rpa_client_id=robot_client_id, job_no=job_no)
        return HttpResponse('success')

    # print(robot_flow, robot_client_id)

    # username = request.COOKIES.get('username')
    # print(username)
    # try:
    #     online_jon = User.objects.filter(user_name_id=username).first()
    #     print(online_jon)
    #     if online_jon:
    #
    #     # Job_list_summary.save()
    #         print('加入队列成功！')
    #
    #     #  TODO  启动客户端
    #         start_robot(jobs='GeShui', rpa_client_id=robot_client_id, job_no=job_no)
    #         return HttpResponse('sucess')
    #     else:
    #     # Job_list_summary.objects.filter(Q(job_no=job_no) & Q(user_name_id=username)).update(job_status='1110')
    #     # print(Job_list_summary.objects.filter(Q(job_no=job_no) & Q(user_name_id=username)).first())
    #     # print(111111111111111111111111111111111111111111111111)
    #     # Job_list_summary.save()
    #         start_robot(jobs='purchase_requisition_RPA_2', rpa_client_id=robot_client_id, job_no=job_no)
    #         return HttpResponse('success')
    # except:
    #     print('开始功能失败！')
    # return HttpResponse('success')
    # except:
    #     start_robot(jobs='purchase_requisition_RPA_2', rpa_client_id=robot_client_id, job_no=job_no)
    #     return HttpResponse('success')

# TODO  任务列表删除 采购机器人
def set_purchase_deletjobs_info(request):
    job_no = request.POST.get('job_no')
    job_type = request.POST.get('job_type')

    username = request.COOKIES.get('username')
    client_id = User.objects.get(user_name=username)
    robot_client_id = client_id.user_agent_no
    print("=======================", job_no, job_type)
    # print(robot_flow, robot_client_id)




# TODO  任务列表停止 采购机器人
def set_purchase_stopjobs_info(request):
    job_no = request.POST.get('job_no')
    job_type = request.POST.get('job_type')

    username = request.COOKIES.get('username')
    client_id = User.objects.get(user_name=username)
    robot_client_id = client_id.user_agent_no
    print("=======================", job_no, job_type)
    # print(robot_flow, robot_client_id)














#  TODO  采购机器人 创建请购单
def pruchasing_robot_create(request):
    return  render(request, 'purchasing_project_info.html', locals())



#  TODO  启动  机器人
def start_robot(jobs, rpa_client_id, job_no):
    print('开始下发机器人执行')

    isa_no = rpa_rest(host='http://rpa.chinaive.com', rest_type='start-job',
                      data_json={"proc_code": jobs, "robot_no": rpa_client_id},
                      add_pr='/rapi/rcall.action?', token='9f9d7e7a928a4873ae6191f5386b4288')

    print('isa_no =====================', isa_no['result']['job_no'])

    #  TODO  获取此机器人在 服务器的任务编号写入数据库
    # rpa_rest(host='http://rpa.chinaive.com', rest_type='get-jobs', data_json={"proc_code": jobs},
    #      add_pr='/rapi/rcall.action?', token='59e078f284f440f49e36076eb07efbc3')
    try:
        time.sleep(0.5)
        # Job_list_summary.objects.filter(job_no=job_no).update(isa_job_no=isa_no['result']['job_no'])
        # Job_list_summary.objects.filter(job_no = job_no).update(isa_job_no=isa_no['result']['START_TIME'])
        # Job_list_summary.isa_job_no = isa_no['result']['job_no']
        # Job_list_summary.save()
    except:
        print('艺赛琪编号写入失败')

