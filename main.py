import os
import datetime
from send_email import email_tool

#NOTE 
#    ktoolbox sync-creator https://kemono.su/fanbox/user/16034374 --start-time= 
#    datetime.data.today()

os.system('mkdir ./Downlaods')

require_files = os.listdir('./sync_require')
for file in require_files:
    with open('./sync_require/' + file, 'r') as file_open:
        text = file_open.read()
    file_open.close()
    text = text.split('\n')
    i = 0
    name = text[i].replace('#', '').replace(' ', '')
    i += 1
    email_adress = text[i].replace('#', '').replace(' ', '')
    i += 1
    url = []
    url_email = ''
    while i <= len(text)-1:
        if text[i] != '':
            url += [text[i]]
            url_email += text[i] + '\n'
        i += 1
    #NOTE name --> 需求中填写的昵称
    #     email_adress --> 邮箱地址
    #     url --> type: list 更新地址列表
    #     url_email --> 纯文本地址集，仅用添加至正文

    email_tool(receiver = email_adress, URL = url_email, upload_name = name, status_num = '1', name = name, user_update = '')

    os.system('''mkdir "./Downlaods/''' + name + '''"''')
    os.chdir('./Downlaods/' + name)

    #NOTE ktoolbox sync-creator https://kemono.su/fanbox/user/16034374 --start-time= 
    for url_download in url:
        start_time = str(datetime.date.today() - datetime.timedelta(days=1))
        end_time = str(datetime.date.today())
        os.system('ktoolbox sync-creator ' + url_download + ' --start-time=' + start_time + ' --end-time=' + end_time)

    #email_tool(receiver = email_adress, URL = url_email, upload_name = name, status_num = '2', name = name, user_update = '')

    os.system('rm -r ./logs')
    down_user = os.listdir('./')
    user_update = []
    for user in down_user:
        user_num = os.listdir('./' + user)
        if len(user_num) != 1:
            user_update += [user]
            os.system('rm ./' + user + '/creator-indices.ktoolbox')
        else:
            os.system('rm -r ./' + user)
    down_user = os.listdir('./')
    if down_user == []:
        os.system('echo "empty" > empty.empty')
        
    #NOTE 现在所处目录:Downlaods/name/
    #     user_update --> list 包含所更新画师的昵称
    
    user_update = str(user_update).replace('[', '').replace(']', '').replace("'", '')

    if user_update == '':
        user_update = '!!!NO USER NEED TO UPDATE!!!'

    email_tool(receiver = email_adress, URL = url_email, upload_name = name, status_num = '2', name = name, user_update = '')

    os.chdir('../..')

    with open('./sync_require/' + file, 'w') as file_open:
        file_open.write(email_adress + '\n' + url_email + '\n' + name + '\n' + '3' + '\n' + name + '\n' + user_update)
    file_open.close()
