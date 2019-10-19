import os
import re



# ========================================客户端标识===================================
def get_agent_no():
    '''
    本函数只有通过服务器下发流程才能正常执行，因为本地与服务器当前路径不一样
    '''
    current_path = os.getcwd()

    print('服务器下发方式当前文件路径：', current_path)  # C:\iS-RPA\plugin\Com.Isearch.Func.AI

    up_up_path = os.path.abspath(os.path.join(os.getcwd(), "../."))
    print('当前路径上上级目录：', up_up_path)  # C:\iS-RPA\
    # logdir_path = up_up_path + '\\' + 'Logs'
    # print('日志文件夹路径：', logdir_path)
    # lst = os.listdir(logdir_path)
    #
    # print('日志文件夹logs下的所有文件：',lst)  # ['1', '2019-08-13', '2019-08-14', '2019-08-15', '2019-08-16', '2019-08-17', '2019-08-19', '2019-08-20', '2019-08-21', '2019-08-22', '2019-08-23', '2019-08-24', '2019-08-26', '2019-08-27', '2019-08-28', '2019-08-29', '2019-08-30']
    #
    # print('logs文件夹下最新日志文件夹名称：', lst[0])
    # target_logdir_path = logdir_path + '\\' + lst[0]
    # print('最新日志文件夹如2019-08-30的全路径：', target_logdir_path)
    # target_latest_log_file = target_logdir_path + '\\' + 'RPARobot.log'
    # print('agent_no所在文件全路径：', target_latest_log_file)  # C:\iS-RPA\logs\2019-08-30\ClientManHelper.log
    # target_latest_log_file = target_latest_log_file.replace('\\', '/')
    # print('修改路径符后的路径：', target_latest_log_file)
    #
    # with open(target_latest_log_file, "r", encoding="gbk", errors="ignore") as f:
    #     rfile = f.read()
    #     agent_no = re.findall(r'''"agent_no":"(.*?)".*?"agent_version"''', rfile, re.S)[0]
    #     user_name = re.findall(r'''"user_name":"(.*?)".*?}''', rfile, re.S)[0]
    #     agent_id = user_name + '@' + agent_no
    #     print('最终目的的agent_id：', agent_id)

    # return agent_id


get_agent_no()