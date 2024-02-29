
import requests
import re
import pandas as pd
import time

import json

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

#%E6%97%A0%E6%B6%82%E8%A3%85  无涂装
#%E5%85%A8%E6%81%AF 全息

def sendEmail(context):
    my_sender='762674784@qq.com'    # 发件人邮箱账号
    my_pass = 'wesirzzfibapbdhh'              # 发件人邮箱密码
    my_user='762674784@qq.com'      # 收件人邮箱账号，我这边发送给自己

    msg=MIMEText(context,'plain','utf-8')
    msg['From']=formataddr(["小旺助手",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["南波万",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="小旺助手提醒您该梭哈了"                # 邮件的主题，也可以说是标题

    server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件

def main():
    try:
        #请求
        #请求头参数
        headers = {
            'cookie': 'Device-Id=iG9P2xyditYu0kPBM6mX; remember_me=U1103958728|HDsN8zFOkJECNcIDi1R6cGVn43ruvcaO; session=1-xRg3_oUho46brZwAOVjI5ERMCODw5EoilROla19pZ3cV2030275984; Locale-Supported=zh-Hans; game=csgo; csrf_token=IjQ4MTA2YjFlYWU0MzBiYWUxYWVkNTJlNTRhMmUxMjZkMGNkYTY0MjEi.GMBx_A.T31wz74TyCJh1rsU8C1USPjiWuY',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

        #初始化
        #查询列表
        jewelrys_gun_list=[{'AK-47 | 血腥运动 (崭新出厂)':690},{'AK-47 | 黄金藤蔓 (崭新出厂)':24600},{'AK-47 | 火神 (崭新出厂)':4576},{'AK-47 | 燃料喷射器 (崭新出厂)':2650},{'AK-47 | X 射线 (崭新出厂)':9918},{'AWP | 迷人眼 (崭新出厂)':109},{'M4A1 消音型 | 印花集 (崭新出厂)':2487},{'M4A1 消音型 | 澜磷 (崭新出厂)':3797},{'M4A4 | 喧嚣杀戮 (崭新出厂)':165},{'沙漠之鹰 | 印花集 (崭新出厂)':498},{'沙漠之鹰 | 黄金锦鲤 (崭新出厂)':500}]
        jewelrys_knife_list=[{'短剑（★）':2458},{'蝴蝶刀（★）':10840},{'爪子刀（★）':6898},{'骷髅匕首（★）':4948},{'流浪者匕首（★）':2819}]
        jewelrys_sticker_list=[{'印花 | Copenhagen Flames （全息） | 2021年斯德哥尔摩锦标赛':59},{'印花 | Team Liquid （全息） | 2021年斯德哥尔摩锦标赛':29},{'印花 | Movistar Riders （全息） | 2021年斯德哥尔摩锦标赛':71.4},{'印花 | Copenhagen Flames(全息)| 2022年安特卫普锦标赛':31.55},{'印花 | Cloud9(全息)| 2022年安特卫普锦标赛':170}]
        #武器
        category_gun_list=['weapon_ak47','weapon_awp','weapon_m4a1_silencer','weapon_m4a1','weapon_deagle']
        #category_knife_list=['weapon_knife_butterfly','weapon_knife_karambit','weapon_knife_skeleton','weapon_knife_outdoor','weapon_knife_stiletto']
        category_sticker_list=['sticker_tournament18','sticker_tournament19']
        #武器类别
        quality_list=['normal']
        #武器外观
        exterior_list=['wearcategory0']
        #武器品质
        rarity_list=['ancient_weapon','legendary_weapon']
        #邮件内容
        context=''

        #遍历获取信息
        #遍历步枪类型
        for gun in category_gun_list:
            #遍历武器品质
            for rarity in rarity_list:
                #get请求url接口
                #路径前面加一个‘r',是为了保持路径在读取时不被漏读，错读
                buff_gun_request_url="https://buff.163.com/api/market/goods?game=csgo&page_num=1&category="+gun+"&rarity="+rarity+"&quality=normal&exterior=wearcategory0&tab=selling&use_suggestion=0&_=1709106198618"
                buff_gun_text = requests.get(url=buff_gun_request_url, headers=headers).text
                #print(buff_gun_text)
                #json转为字典
                items_gun_dict=json.loads(buff_gun_text)
                #print(type(item_dict))
                #print(item_dict)
                items_gun_list=items_gun_dict['data']['items']
                #print(type(item_list))
                #遍历所有武器
                for item_gun in items_gun_list:
                    #print(type(item))
                    item_gun_name=item_gun['name']
                    #遍历查询的饰品
                    for jewelry_gun in jewelrys_gun_list:
                        #比较是否为所要查询饰品
                        #print(type(jewelry))
                        #print(list(jewelry.keys())[0])
                        jewelry_gun_name=list(jewelry_gun.keys())[0]
                        if item_gun_name==jewelry_gun_name:
                            #keys方法在python3返回dict_keys类型，要其中的key值，需要list()方法，再通过列表下标获得
                            #查询饰品价格是否在购买价格范围内，若在则发送邮件通知
                            item_gun_price=float(item_gun['sell_min_price'])
                            jewelry_gun_price=list(jewelry_gun.values())[0]
                            ##values方法在python3返回dict_values类型，要其中的value值，需要list()方法，再通过列表下标获得
                            if item_gun_price<jewelry_gun_price+jewelry_gun_price*0.05:
                                if item_gun_price>jewelry_gun_price-jewelry_gun_price*0.05:
                                    #编辑邮件内容
                                    context+='您关注的饰品'+jewelry_gun_name+'的价格已在'+str(jewelry_gun_price)+'范围内'+',目前的价格为'+str(item_gun_price)+'\r\n'
                                    print(context)
                                    break
                        else:    
                            continue
                time.sleep(1)
        #获取刀信息                
        #遍历页数
        for i in range(2):
            buff_knife_request_url="https://buff.163.com/api/market/goods?game=csgo&page_num="+str(i+1)+"&category_group=knife&search=%E6%97%A0%E6%B6%82%E8%A3%85&sort_by=price.desc&tab=selling&use_suggestion=0&_=1709106198721"
            buff_knife_text = requests.get(url=buff_knife_request_url, headers=headers).text
            #print(buff_knife_text)
            #json转为字典
            items_knife_dict=json.loads(buff_knife_text)
            #print(type(item_dict))
            #print(item_dict)
            items_knife_list=items_knife_dict['data']['items']
            #print(type(item_list))
            #遍历所有武器
            for item_knife in items_knife_list:
                #print(type(item))
                item_knife_name=item_knife['name']
                #遍历查询的饰品
                for jewelry_knife in jewelrys_knife_list:
                    #比较是否为所要查询饰品
                    #print(type(jewelry))
                    #print(list(jewelry.keys())[0])
                    jewelry_knife_name=list(jewelry_knife.keys())[0]
                    if item_knife_name==jewelry_knife_name:
                        #keys方法在python3返回dict_keys类型，要其中的key值，需要list()方法，再通过列表下标获得
                        #查询饰品价格是否在购买价格范围内，若在则发送邮件通知
                        item_knife_price=float(item_knife['sell_min_price'])
                        jewelry_knife_price=list(jewelry_knife.values())[0]
                        ##values方法在python3返回dict_values类型，要其中的value值，需要list()方法，再通过列表下标获得
                        if item_knife_price<jewelry_knife_price+jewelry_knife_price*0.05:
                            if item_knife_price>jewelry_knife_price-jewelry_knife_price*0.05:
                                #编辑邮件内容
                                context+='您关注的饰品'+jewelry_knife_name+'的价格已在'+str(jewelry_knife_price)+'范围内'+',目前的价格为'+str(item_knife_price)+'\r\n'
                                print(context)
                                break
                    else:    
                        continue
            time.sleep(1)
        #遍历全息贴纸类型
        for sticker in category_sticker_list:
            #遍历武器品质
            for i in range(2):
                #get请求url接口
                #路径前面加一个‘r',是为了保持路径在读取时不被漏读，错读
                buff_sticker_request_url="https://buff.163.com/api/market/goods?game=csgo&page_num="+str(i+1)+"&category="+sticker+"&search=%E5%85%A8%E6%81%AF&sort_by=price.desc&tab=selling&use_suggestion=0&_=1709129998682"
                buff_sticker_text = requests.get(url=buff_sticker_request_url, headers=headers).text
                #print()
                #json转为字典
                items_sticker_dict=json.loads(buff_sticker_text)
                #print(type(item_dict))
                #print(items_sticker_dict)
                items_sticker_list=items_sticker_dict['data']['items']
                #print(type(item_list))
                #遍历所有贴纸
                for item_sticker in items_sticker_list:
                    #print(type(item))
                    item_sticker_name=item_sticker['name']
                    #遍历查询的饰品
                    for jewelry_sticker in jewelrys_sticker_list:
                        #比较是否为所要查询饰品
                        #print(type(jewelry))
                        #print(list(jewelry.keys())[0])
                        jewelry_sticker_name=list(jewelry_sticker.keys())[0]
                        if item_sticker_name==jewelry_sticker_name:
                            #keys方法在python3返回dict_keys类型，要其中的key值，需要list()方法，再通过列表下标获得
                            #查询饰品价格是否在购买价格范围内，若在则发送邮件通知
                            item_sticker_price=float(item_sticker['sell_min_price'])
                            jewelry_sticker_price=list(jewelry_sticker.values())[0]
                            ##values方法在python3返回dict_values类型，要其中的value值，需要list()方法，再通过列表下标获得
                            if item_sticker_price<jewelry_sticker_price+jewelry_sticker_price*0.05:
                                if item_sticker_price>jewelry_sticker_price-jewelry_sticker_price*0.05:
                                    #编辑邮件内容
                                    context+='您关注的饰品'+jewelry_sticker_name+'的价格已在'+str(jewelry_sticker_price)+'范围内'+',目前的价格为'+str(item_sticker_price)+'\r\n'
                                    print(context)
                                    break
                        else:    
                            continue
                time.sleep(1)

        #发送邮件
        if len(context)!=0:
            sendEmail(context)
    
    # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    except Exception:  
        main()

    


if __name__ == "__main__":
    # 当程序被调用执行时，调用函数
    main()
          
