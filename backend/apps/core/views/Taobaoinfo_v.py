#coding:utf-8
import base64, copy, logging, os, sys, time, xlrd, json, datetime, configparser
from django.http import JsonResponse
from django.apps import apps
import numbers
from collections import defaultdict
from django.db.models.aggregates import Count,Sum
from django.db.models import Case, When, IntegerField, F
from .models import storeup
from django.forms import model_to_dict
import requests
from util.CustomJSONEncoder import CustomJsonEncoder
from .models import taobaoinfo
from util.codes import *
from urllib.parse import unquote
from util.auth import Auth
from util.common import Common
import util.message as mes
from django.db import connection
import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Q
from util.baidubce_api import BaiDuBce
from .config_model import config
import pandas as pd


def taobaoinfo_default(request):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        req_dict.update({"isdefault":"是"})
        data=taobaoinfo.getbyparams(taobaoinfo, taobaoinfo, req_dict)
        if len(data)>0:
            msg['data']  = data[0]
        else:
            msg['data']  = {}
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_page(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        global taobaoinfo
        #当前登录用户信息
        tablename = Auth().getTokenInfo(request).get('tablename')

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  =taobaoinfo.page(taobaoinfo, taobaoinfo,req_dict, request)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_autoSort(request):
    '''
    ．智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
主要信息列表（如商品列表，新闻列表）中使用，显示最近点击的或最新添加的5条记录就行
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if "clicknum"  in taobaoinfo.getallcolumn(taobaoinfo,taobaoinfo):
            req_dict['sort']='clicknum'
        elif "browseduration"  in taobaoinfo.getallcolumn(taobaoinfo,taobaoinfo):
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        req_dict['order']='desc'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = taobaoinfo.page(taobaoinfo,taobaoinfo, req_dict)

        return JsonResponse(msg, encoder=CustomJsonEncoder)

#分类列表
def taobaoinfo_lists(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":[]}
        msg['data'],_,_,_,_  = taobaoinfo.page(taobaoinfo, taobaoinfo, {})
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_query(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        try:
            query_result = taobaoinfo.objects.filter(**request.session.get("req_dict")).values()
            msg['data'] = query_result[0]
        except Exception as e:

            msg['code'] = crud_error_code
            msg['msg'] = f"发生错误：{e}"
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_list(request):
    '''
    前台分页
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        #获取全部列名
        columns=  taobaoinfo.getallcolumn( taobaoinfo, taobaoinfo)
        if "vipread" in req_dict and "vipread" not in columns:
          del req_dict["vipread"]
        #表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
        try:
            __foreEndList__=taobaoinfo.__foreEndList__
        except:
            __foreEndList__=None
        try:
            __foreEndListAuth__=taobaoinfo.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        #authSeparate
        try:
            __authSeparate__=taobaoinfo.__authSeparate__
        except:
            __authSeparate__=None

        if __foreEndListAuth__ =="是" and __authSeparate__=="是":
            tablename=Auth().getTokenInfo(request).get('tablename')
            if tablename!="users" and Auth().getTokenInfo(request).get('params') is not None:
                req_dict['userid']=Auth().getTokenInfo(request).get('params').get("id")

        tablename = Auth().getTokenInfo(request).get('tablename')
        if tablename == "users" and req_dict.get("userid") != None:#判断是否存在userid列名
            del req_dict["userid"]
        else:
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            if __isAdmin__ == "是":
                if req_dict.get("userid"):
        # del req_dict["userid"]
                    pass
            else:
    #非管理员权限的表,判断当前表字段名是否有userid
                if "userid" in columns:
                    try:
                        pass
                    except:
                        pass
        #当列属性authTable有值(某个用户表)[该列的列名必须和该用户表的登陆字段名一致]，则对应的表有个隐藏属性authTable为”是”，那么该用户查看该表信息时，只能查看自己的
        try:
            __authTables__=taobaoinfo.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __foreEndListAuth__=="是":
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    try:
                        del req_dict['userid']
                    except:
                        pass
                    params = Auth().getTokenInfo(request).get('params')
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break
        
        if taobaoinfo.__tablename__[:7]=="discuss":
            try:
                del req_dict['userid']
            except:
                pass

        q = Q()
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = taobaoinfo.page(taobaoinfo, taobaoinfo, req_dict, request, q)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_save(request):
    '''
    后台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys():
            del req_dict['clicktime']
        tablename=Auth().getTokenInfo(request).get('tablename')
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        #获取全部列名
        columns=  taobaoinfo.getallcolumn( taobaoinfo, taobaoinfo)
        if tablename!='users' and req_dict.get("userid")==None and 'userid' in columns  and __isAdmin__!='是':
            params=Auth().getTokenInfo(request).get('params')
            req_dict['userid']=params.get('id')


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']

        idOrErr= taobaoinfo.createbyreq(taobaoinfo,taobaoinfo, req_dict)
        if idOrErr is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = idOrErr
        else:
            msg['data'] = idOrErr

        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_add(request):
    '''
    前台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        tablename=Auth().getTokenInfo(request).get('tablename')

        #获取全部列名
        columns=  taobaoinfo.getallcolumn( taobaoinfo, taobaoinfo)
        try:
            __authSeparate__=taobaoinfo.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="是":
            tablename=Auth().getTokenInfo(request).get('tablename')
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=Auth().getTokenInfo(request).get('params').get("id")
                except:
                    pass

        try:
            __foreEndListAuth__=taobaoinfo.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=Auth().getTokenInfo(request).get('tablename')
            if tablename!="users":
                req_dict['userid']=Auth().getTokenInfo(request).get('params').get("id")


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']
        error= taobaoinfo.createbyreq(taobaoinfo,taobaoinfo, req_dict)
        if error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_thumbsup(request,id_):
    '''
     点赞：表属性thumbsUp[是/否]，刷表新增thumbsupnum赞和crazilynum踩字段，
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=taobaoinfo.getbyid(taobaoinfo,taobaoinfo,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = taobaoinfo.updatebyparams(taobaoinfo,taobaoinfo, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)


def taobaoinfo_info(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data = taobaoinfo.getbyid(taobaoinfo,taobaoinfo, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= taobaoinfo.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"  and  "clicknum"  in taobaoinfo.getallcolumn(taobaoinfo,taobaoinfo):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}
            ret=taobaoinfo.updatebyparams(taobaoinfo,taobaoinfo,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_detail(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data =taobaoinfo.getbyid(taobaoinfo,taobaoinfo, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= taobaoinfo.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"   and  "clicknum"  in taobaoinfo.getallcolumn(taobaoinfo,taobaoinfo):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}

            ret=taobaoinfo.updatebyparams(taobaoinfo,taobaoinfo,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_update(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys() and req_dict['clicktime']=="None":
            del req_dict['clicktime']
        if req_dict.get("mima") and "mima" not in taobaoinfo.getallcolumn(taobaoinfo,taobaoinfo) :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in taobaoinfo.getallcolumn(taobaoinfo,taobaoinfo) :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = taobaoinfo.updatebyparams(taobaoinfo, taobaoinfo, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def taobaoinfo_delete(request):
    '''
    批量删除
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        error=taobaoinfo.deletes(taobaoinfo,
            taobaoinfo,
             req_dict.get("ids")
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def taobaoinfo_vote(request,id_):
    '''
    浏览点击次数（表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1）
统计商品或新闻的点击次数；提供新闻的投票功能
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}


        data= taobaoinfo.getbyid(taobaoinfo, taobaoinfo, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=taobaoinfo.updatebyparams(taobaoinfo,taobaoinfo,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return JsonResponse(msg)

def taobaoinfo_importExcel(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}

        excel_file = request.FILES.get("file", "")
        if excel_file.size > 100 * 1024 * 1024:  # 限制为 100MB
            msg['code'] = 400
            msg["msg"] = '文件大小不能超过100MB'
            return JsonResponse(msg)

        file_type = excel_file.name.split('.')[1]
        
        if file_type in ['xlsx', 'xls']:
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            table = data.sheets()[0]
            rows = table.nrows
            
            try:
                for row in range(1, rows):
                    row_values = table.row_values(row)
                    req_dict = {}
                    taobaoinfo.createbyreq(taobaoinfo, taobaoinfo, req_dict)
                    
            except:
                pass
                
        else:
            msg = {
                "msg": "文件类型错误",
                "code": 500
            }
                
        return JsonResponse(msg)

import math

#查找相似用户
def cosine_similarity(a, b):
    numerator = sum([a[key] * b[key] for key in a if key in b])
    denominator = math.sqrt(sum([a[key]**2 for key in a])) * math.sqrt(sum([b[key]**2 for key in b]))
    return numerator / denominator

#协同算法
def taobaoinfo_autoSort2(request):
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")
        cursor = connection.cursor()
        sorted_recommended_goods=[]
        user_ratings={}
        token = request.META.get('HTTP_TOKEN')
        decode_str = eval(base64.b64decode(token).decode("utf8"))
        user_id = decode_str['params']["id"]

        try:
            user_items = defaultdict(list)
            #用户 -> 收藏/关注过的物品列表（去重）
            for rec in storeup.objects.filter(tablename="taobaoinfo",type=  1 ).values('userid', 'refid').distinct():
                user_items[rec['userid']].append(rec['refid'])
            # 用户 -> 点赞过的物品列表（去重）
            for rec in storeup.objects.filter(tablename="taobaoinfo", type=21).values('userid', 'refid').distinct():
                user_items[rec['userid']].append(rec['refid'])
            # 封装userid、goodid的矩阵
            for user, items in user_items.items():
                ratings_dict = {}
                if user_ratings.__contains__(user):
                    ratings_dict = user_ratings[user]
                else:
                    for item in items:
                        if ratings_dict.__contains__(str(item)):
                            ratings_dict[str(item)] += 1
                        else:
                            ratings_dict[str(item)] = 1
                user_ratings[user] = ratings_dict
            try:
                # 计算目标用户与其他用户的相似度
                similarities = {other_user: cosine_similarity(user_ratings[user_id], user_ratings[other_user])
                                for other_user in user_ratings if other_user != user_id}
                # 找到与目标用户最相似的用户
                most_similar_user = sorted(similarities, key=similarities.get, reverse=True)[0]
                # 找到最相似但目标用户未购买过的商品
                recommended_goods = {goods: rating for goods, rating in user_ratings[most_similar_user].items() if
                                     goods not in user_ratings[user_id]}
                # 按评分降序排列推荐
                sorted_recommended_goods = sorted(recommended_goods, key=recommended_goods.get, reverse=True)
            except:
                pass
        except:
            sorted_recommended_goods=[]
        # 获取大模型算法推荐数据
        recommendations = rf_recommendations(request)
        if len(recommendations) > 0:
            rec_itemid = [str(re['itemid']) for re in recommendations]
            new_list = rec_itemid.copy()
            # 结合协同推荐结果
            for item in sorted_recommended_goods:
                if item not in new_list:
                    new_list.append(item)
            sorted_recommended_goods = new_list
        L = []
        where = " AND ".join([f"{key} = '{value}'" for key, value in req_dict.items() if key!="page" and key!="limit" and key!="order"and key!="sort"])
        if where:
            sql = f'''SELECT * FROM (SELECT * FROM taobaoinfo WHERE {where}) AS table1 WHERE id IN ('{"','".join(sorted_recommended_goods)}') union all SELECT * FROM (SELECT * FROM taobaoinfo WHERE {where}) AS table1 WHERE id NOT IN ('{"','".join(sorted_recommended_goods)}')'''
        else:
            sql = f'''select * from taobaoinfo where id in ('{"','".join(sorted_recommended_goods)}') union all select * from taobaoinfo where id not in('{"','".join(sorted_recommended_goods)}')'''
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)

        return JsonResponse({"code": 0, "msg": '',  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":5,"list": L[0:int(req_dict["limit"])]}}, encoder=CustomJsonEncoder)




def taobaoinfo_count(request):
    '''
    总数接口
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        req_dict = request.session.get("req_dict")
        where = ' where 1 = 1 '
        for key in req_dict:
            if req_dict[key] != None:
                where = where + " and key like '{0}'".format(req_dict[key])
        
        sql = "SELECT count(*) AS count FROM taobaoinfo {0}".format(where)
        count = 0
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
        for online_dict in data_dict:
            count = online_dict['count']
        msg['data'] = count

        return JsonResponse(msg, encoder=CustomJsonEncoder)

#对日期进行排序
def order_time(data,type,xColumnName,rev):
    if type=="日":
        result_data = sorted(
            data,
            key=lambda x: (
                int(x[xColumnName].split("-")[0]),
                int(x[xColumnName].split("-")[1]),
                int(x[xColumnName].split("-")[2]),
            ),
            reverse=rev  # 设置排列
        )
    elif type=="月":
        result_data = sorted(
            data,
            key=lambda x: (
                int(x[xColumnName].split("-")[0]),
                int(x[xColumnName].split("-")[1])
            ),
            reverse=rev  # 设置排列
        )
    elif type=="年":
        result_data = sorted(
            data,
            key=lambda x: (
                int(x[xColumnName].split("-")[0]),  # 提取年份并转为整数
            ),
            reverse=rev  # 设置排列
        )
    else:
        result_data = sorted(data, key=lambda x: x[xColumnName], reverse=rev)
    return result_data

# （按值统计）时间统计类型
def taobaoinfo_value(request, xColumnName, yColumnName, timeStatType):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        #获取hadoop分析后的数据文件
        date_type = ""
        if timeStatType == '日':
            date_type = "date"
        if timeStatType == '月':
            date_type = "month"
        if timeStatType == '季':
            date_type = "quarter"
        if timeStatType == '年':
            date_type = "year"
        json_filename = f'taobaoinfo_value{xColumnName}{yColumnName}{date_type}.json'

        if os.path.exists(json_filename) == True:
            with open(json_filename, encoding='utf-8') as f:
                msg['data'] = json.load(f)
        else:
            where = ' where 1 = 1 '
            raw_query_string = request.META.get('QUERY_STRING', '')
            raw_query_string = unquote(raw_query_string)
            conditionColumn = ""
            conditionValue = ""
            if "conditionColumn=" in raw_query_string:
                conditionColumn = raw_query_string.split("conditionColumn=")[1].split("&")[0]
            if "conditionValue=" in raw_query_string:
                conditionValue = raw_query_string.split("conditionValue=")[1].split("&")[0]
            if conditionColumn != "":
                for index, value in enumerate(conditionColumn.split(";")):
                    if ',' in value:
                        where = where + f''' and {value.split(',')[0]} >= \'{conditionValue.split(";")[index].split(",")[0]}\''''
                        where = where + f''' and {value.split(',')[1]} <= \'{conditionValue.split(";")[index].split(",")[1]}\''''
                    else:
                        where = where + f''' and {value} = \'{conditionValue.split(";")[index]}\''''
            req_dict = request.session.get("req_dict")
            statistics_func = "SUM"
            func_params = req_dict.get("func")
            if func_params == "平均":
                statistics_func = "AVG"
            elif func_params == "最大":
                statistics_func = "MAX"
            elif func_params == "最小":
                statistics_func = "MIN"
            elif func_params == "总和":
                statistics_func = "COUNT"
            try:
                del req_dict["func"]
            except:
                pass
            #定义查询统计语句
            for key, value in req_dict.items():
                if key!="limit" and key!="order" and key!="orderType" and key!="conditionColumn"and key!="conditionValue":
                    where = where + " and {0} ='{1}' ".format(key,value)
            sql = ''
            if timeStatType == '日':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, ROUND({1}({2}),2) total FROM taobaoinfo {3} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d')".format(xColumnName, statistics_func,yColumnName, where, '%Y-%m-%d')

            if timeStatType == '月':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, ROUND({1}({2}),2) total FROM taobaoinfo {3} GROUP BY DATE_FORMAT({0}, '%Y-%m')".format(xColumnName, statistics_func,yColumnName, where, '%Y-%m')

            if timeStatType == '季':
                sql = "SELECT CONCAT(YEAR(MIN({0})), '-Q', QUARTER(MIN({0}))) AS {0}, {1}({2}) AS total FROM orders {3} GROUP BY YEAR({0}), QUARTER({0})".format(xColumnName,statistics_func, yColumnName, where)

            if timeStatType == '年':
                sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, ROUND({1}({2}),2) total FROM taobaoinfo {3} GROUP BY DATE_FORMAT({0}, '%Y')".format(xColumnName,statistics_func, yColumnName, where, '%Y')
            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime(
                            "%Y-%m-%d %H:%M:%S")
                    else:
                        pass
                L.append(online_dict)
            msg['data'] = L
        req_dict = request.session.get("req_dict")
        #对结果进行排序
        order = req_dict.get('order')
        orderType = req_dict.get('orderType')
        if orderType=='x' :
            if order == "desc":
                msg['data'] = order_time(msg['data'], timeStatType, xColumnName, True)
            else:
                msg['data'] = order_time(msg['data'], timeStatType, xColumnName, False)
        else:
            if order == "desc":
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None), key=lambda x: x['total'],
                                     reverse=True)
            else:
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None), key=lambda x: x['total'])

        if "limit" in req_dict and int(req_dict["limit"]) < len(L):
            msg['data'] = msg['data'][:int(req_dict["limit"])]
        return JsonResponse(msg, encoder=CustomJsonEncoder)

# 按值统计
def taobaoinfo_o_value(request, xColumnName, yColumnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        #获取hadoop分析后的数据文件
        json_filename = f'taobaoinfo_value{xColumnName}{yColumnName}.json'

        if os.path.exists(json_filename) == True:
            with open(json_filename, encoding='utf-8') as f:
                msg['data'] = json.load(f)
        else:
            where = ' where 1 = 1 '
            raw_query_string = request.META.get('QUERY_STRING', '')
            raw_query_string = unquote(raw_query_string)
            conditionColumn = ""
            conditionValue = ""
            if "conditionColumn=" in raw_query_string:
                conditionColumn = raw_query_string.split("conditionColumn=")[1].split("&")[0]
            if "conditionValue=" in raw_query_string:
                conditionValue = raw_query_string.split("conditionValue=")[1].split("&")[0]
            if conditionColumn != "":
                for index, value in enumerate(conditionColumn.split(";")):
                    if "," in value:
                        where = where + f''' and {value.split(',')[0]} >= \'{conditionValue.split(";")[index].split(",")[0]}\''''
                        where = where + f''' and {value.split(',')[1]} <= \'{conditionValue.split(";")[index].split(",")[1]}\''''
                    else:
                        where = where + f''' and {value} = \'{conditionValue.split(";")[index]}\''''
            req_dict = request.session.get("req_dict")
            statistics_func = "SUM"
            func_params = req_dict.get("func")
            if func_params == "平均":
                statistics_func = "AVG"
            elif func_params == "最大":
                statistics_func = "MAX"
            elif func_params == "最小":
                statistics_func = "MIN"
            elif func_params == "总和":
                statistics_func = "COUNT"
            try:
                del req_dict["func"]
            except:
                pass
            sql = "SELECT {0}, ROUND({1}({2}),2) AS total FROM taobaoinfo {3} GROUP BY {0}".format(xColumnName,statistics_func, yColumnName, where)
            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime(
                            "%Y-%m-%d %H:%M:%S")
                    else:
                        pass
                L.append(online_dict)
            msg['data'] = L
        req_dict = request.session.get("req_dict")
        if "order" in req_dict:
            order = req_dict["order"]
            if order == "desc":
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'],reverse=True)
            else:
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'])

        if "limit" in req_dict and int(req_dict["limit"]) < len(L):
            msg['data'] = msg['data'][:int(req_dict["limit"])]
        return JsonResponse(msg, encoder=CustomJsonEncoder)

# （按值统计）时间统计类型(多)
def taobaoinfo_valueMul(request, xColumnName, timeStatType):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": []}
        req_dict = request.session.get("req_dict")
        #获取hadoop分析后的数据文件
        date_type = ""
        if timeStatType == '日':
            date_type = "date"
        if timeStatType == '月':
            date_type = "month"
        if timeStatType == '季':
            date_type = "quarter"
        if timeStatType == '年':
            date_type = "year"
        #获取hadoop分析后的数据文件
        json_filename = f'''taobaoinfo_value{xColumnName}｛req_dict['yColumnNameMul'].replace(",","")｝{date_type}.json'''

        if os.path.exists(json_filename) == True:
            with open(json_filename, encoding='utf-8') as f:
                msg['data'] = json.load(f)
        else:
            where = ' where 1 = 1 '
            raw_query_string = request.META.get('QUERY_STRING', '')
            raw_query_string = unquote(raw_query_string)
            conditionColumn = ""
            conditionValue = ""
            if "conditionColumn=" in raw_query_string:
                conditionColumn = raw_query_string.split("conditionColumn=")[1].split("&")[0]
            if "conditionValue=" in raw_query_string:
                conditionValue = raw_query_string.split("conditionValue=")[1].split("&")[0]
            if conditionColumn != "":
                for index, value in enumerate(conditionColumn.split(";")):
                    if "," in value:
                        where = where + f''' and {value.split(',')[0]} >= \'{conditionValue.split(";")[index].split(",")[0]}\''''
                        where = where + f''' and {value.split(',')[1]} <= \'{conditionValue.split(";")[index].split(",")[1]}\''''
                    else:
                        where = where + f''' and {value} = \'{conditionValue.split(";")[index]}\''''

            statistics_func = "SUM"
            func_params = req_dict.get("func")
            if func_params == "平均":
                statistics_func = "AVG"
            elif func_params == "最大":
                statistics_func = "MAX"
            elif func_params == "最小":
                statistics_func = "MIN"
            elif func_params == "总和":
                statistics_func = "COUNT"
            try:
                del req_dict["func"]
            except:
                pass
              # 定义查询统计语句
            for key, value in req_dict.items():
                if key != "limit" and key != "order" and key != "orderType" and key != "yColumnNameMul" and key != "conditionColumn" and key != "conditionValue":
                    where = where + " and {0} ='{1}' ".format(key, value)

            for item in req_dict['yColumnNameMul'].split(','):
                sql = ''
                if timeStatType == '日':
                    sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, ROUND({1}({2}),2) total FROM taobaoinfo {3} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d')".format(xColumnName, statistics_func,item, where, '%Y-%m-%d')

                if timeStatType == '月':
                    sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, ROUND({1}({2}),2) total FROM taobaoinfo {3} GROUP BY DATE_FORMAT({0}, '%Y-%m')".format(xColumnName,statistics_func, item, where, '%Y-%m')

                if timeStatType == '季':
                    sql = "SELECT CONCAT(YEAR(MIN({0})), '-Q', QUARTER(MIN({0}))) {0}, {1}({2}) total FROM taobaoinfo {3} GROUP BY YEAR({0}), QUARTER({0})".format(xColumnName, statistics_func,item, where)

                if timeStatType == '年':
                    sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, ROUND({1}({2}),2) total FROM taobaoinfo {3} GROUP BY DATE_FORMAT({0}, '%Y')".format(xColumnName, statistics_func,item, where, '%Y')

                L = []
                cursor = connection.cursor()
                cursor.execute(sql)
                desc = cursor.description
                data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
                for online_dict in data_dict:
                    for key in online_dict:
                        if 'datetime.datetime' in str(type(online_dict[key])):
                            online_dict[key] = online_dict[key].strftime(
                                "%Y-%m-%d %H:%M:%S")
                        else:
                            pass
                    L.append(online_dict)
                    # 结果进行排序
                    order = req_dict.get('order')
                    orderType = req_dict.get('orderType')
                    if orderType == 'x':
                        if order == "desc":
                            L = order_time(L, timeStatType, xColumnName, True)
                        else:
                            L = order_time(L, timeStatType, xColumnName, False)
                    else:
                        if order == "desc":
                            L = sorted((x for x in L if x['total'] is not None),
                                       key=lambda x: x['total'],
                                       reverse=True)
                        else:
                            L = sorted((x for x in L if x['total'] is not None),
                                       key=lambda x: x['total'])
                    # 截取列表个数
                    if "limit" in req_dict and int(req_dict["limit"]) < len(msg['data']):
                        L = L[:int(req_dict["limit"])]
                msg['data'].append(L)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

# （按值统计(多)）
def taobaoinfo_o_valueMul(request, xColumnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": []}

        req_dict = request.session.get("req_dict")
        #获取hadoop分析后的数据文件
        json_filename = f'''taobaoinfo_value{xColumnName}｛req_dict['yColumnNameMul'].replace(",","")｝.json'''

        if os.path.exists(json_filename) == True:
            with open(json_filename, encoding='utf-8') as f:
                msg['data'] = json.load(f)
        else:
            where = ' where 1 = 1 '
            raw_query_string = request.META.get('QUERY_STRING', '')
            raw_query_string = unquote(raw_query_string)
            conditionColumn = ""
            conditionValue = ""
            if "conditionColumn=" in raw_query_string:
                conditionColumn = raw_query_string.split("conditionColumn=")[1].split("&")[0]
            if "conditionValue=" in raw_query_string:
                conditionValue = raw_query_string.split("conditionValue=")[1].split("&")[0]
            if conditionColumn != "":
                for index, value in enumerate(conditionColumn.split(";")):
                    if "," in value:
                        where = where + f''' and {value.split(',')[0]} >= \'{conditionValue.split(";")[index].split(",")[0]}\''''
                        where = where + f''' and {value.split(',')[0]} <= \'{conditionValue.split(";")[index].split(",")[1]}\''''
                    else:
                        where = where + f''' and {value} = \'{conditionValue.split(";")[index]}\''''
            statistics_func = "SUM"
            func_params = req_dict.get("func")
            if func_params == "平均":
                statistics_func = "AVG"
            elif func_params == "最大":
                statistics_func = "MAX"
            elif func_params == "最小":
                statistics_func = "MIN"
            elif func_params == "总和":
                statistics_func = "COUNT"
            try:
                del req_dict["func"]
            except:
                pass
            for item in req_dict['yColumnNameMul'].split(','):
                sql = "SELECT {0}, ROUND({1}({2}),2) AS total FROM taobaoinfo {3} GROUP BY {0}".format(xColumnName, statistics_func,item, where)
                L = []
                cursor = connection.cursor()
                cursor.execute(sql)
                desc = cursor.description
                data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
                for online_dict in data_dict:
                    for key in online_dict:
                        if 'datetime.datetime' in str(type(online_dict[key])):
                            online_dict[key] = online_dict[key].strftime(
                                "%Y-%m-%d %H:%M:%S")
                        else:
                            pass
                    L.append(online_dict)
                msg['data'].append(L)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def taobaoinfo_group(request, columnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}

        #获取hadoop分析后的数据文件
        json_filename = f'taobaoinfo_group{columnName}.json'

        if os.path.exists(json_filename) == True:
            with open(json_filename, encoding='utf-8') as f:
                msg['data'] = json.load(f)
        else:
            where = ' where 1 = 1 '
            raw_query_string = request.META.get('QUERY_STRING', '')
            raw_query_string = unquote(raw_query_string)
            conditionColumn = ""
            conditionValue = ""
            if "conditionColumn=" in raw_query_string:
                conditionColumn = raw_query_string.split("conditionColumn=")[1].split("&")[0]
            if "conditionValue=" in raw_query_string:
                conditionValue = raw_query_string.split("conditionValue=")[1].split("&")[0]
            if conditionColumn != "":
                for index, value in enumerate(conditionColumn.split(";")):
                    if ',' in value:
                        where = where + f''' and {value.split(',')[0]} >= \'{conditionValue.split(";")[index].split(",")[0]}\''''
                        where = where + f''' and {value.split(',')[1]} <= \'{conditionValue.split(";")[index].split(",")[1]}\''''
                    else:
                        where = where + f''' and {value} = \'{conditionValue.split(";")[index]}\''''

            sql = "SELECT COUNT(*) AS total, " + columnName + " FROM taobaoinfo " + where + " GROUP BY " + columnName
            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime("%Y-%m-%d")
                    else:
                        pass
                L.append(online_dict)
            msg['data'] = L
        req_dict = request.session.get("req_dict")
        if "order" in req_dict:
            order = req_dict["order"]
            if order == "desc":
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'],reverse=True)
            else:
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'])

        if "limit" in req_dict and int(req_dict["limit"]) < len(L):
            msg['data'] = msg['data'][:int(req_dict["limit"])]
        return JsonResponse(msg, encoder=CustomJsonEncoder)




import math

def taobaoinfo_cleanse(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        try:
            list, _, _, total,_ = taobaoinfo.page(taobaoinfo, taobaoinfo, {})
            df = pd.DataFrame(list,dtype=object)
#删除重复
            df = df.drop_duplicates(subset=['title'])
#随机填充
            df['shoptag'].replace([None, '' ], pd.NA,inplace = True)
            shoptag_non_na = df['shoptag'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'shoptag']):
                    df.loc[i, 'shoptag'] = shoptag_non_na.sample(n=1,replace=True).values[0]
#随机填充
            df['property1'].replace([None, '' ], pd.NA,inplace = True)
            property1_non_na = df['property1'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'property1']):
                    df.loc[i, 'property1'] = property1_non_na.sample(n=1,replace=True).values[0]
#随机填充
            df['property2'].replace([None, '' ], pd.NA,inplace = True)
            property2_non_na = df['property2'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'property2']):
                    df.loc[i, 'property2'] = property2_non_na.sample(n=1,replace=True).values[0]
#随机填充
            df['property3'].replace([None, '' ], pd.NA,inplace = True)
            property3_non_na = df['property3'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'property3']):
                    df.loc[i, 'property3'] = property3_non_na.sample(n=1,replace=True).values[0]
            data_list = df.to_dict(orient='records')
            taobaoinfo.deletes(taobaoinfo,taobaoinfo,ids=[i["id"] for i in list])
            batchList = []
            for dl in data_list:
                filtered_data = {k: v for k, v in dl.items() if v not in [None, '', float('nan')] and (not isinstance(v, float) or not math.isnan(v))}
                batchList.append(taobaoinfo(**filtered_data))
            taobaoinfo.objects.bulk_create(batchList)
        except Exception as e:
            msg["code"] = other_code
            msg["msg"] = e.__str__()

        return JsonResponse(msg)


from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import pickle
from .models import yonghu
def taobaoinfo_trainRecommend(request):
    """
    训练随机森林模型并保存到文件
    该函数负责：
    1. 从数据库获取用户、物品和购买记录数据
    2. 数据预处理和特征工程
    3. 训练随机森林模型
    4. 保存模型和预处理对象到文件
    """
    if request.method == 'GET' or request.method == 'POST':
        msg = {'code': normal_code, 'msg': '训练完成', 'data': {}}
        try:
            #用户表
            query_all = yonghu.objects.all()
            #用户特征
            users_data = {
                'userid': [i.id for i in query_all],
                'nianling': [i.nianling for i in query_all],
                'xingbie': [i.xingbie for i in query_all],
            }
            #物品表
            sp_all = taobaoinfo.objects.all()
            #物品特征
            items_data = {
                'itemid': [i.id for i in sp_all],
                'title': [i.title for i in sp_all],
                'shoptag': [i.shoptag for i in sp_all],
                'baoyounew': [i.baoyounew for i in sp_all],
                'prosheng': [i.prosheng for i in sp_all],
            }

            #收藏关注记录
            storeup_all = storeup.objects.filter(tablename = "taobaoinfo",type =   1 ).all()
            purchases_data = {
                'userid': [i.userid for i in storeup_all],
                'itemid': [i.refid for i in storeup_all]
            }
            """创建特征矩阵"""
            #购买记录与用户、物品信息
            users_df = pd.DataFrame(users_data)
            items_df = pd.DataFrame(items_data)
            purchases_df = pd.DataFrame(purchases_data)
            """准备训练数据"""
            #创建用户-物品交互矩阵（1表示购买/收藏/点击过，0表示未购买/未收藏/未点击过）
            all_user_item_pairs = []
            #获取所有用户和物品
            all_users = users_df['userid'].unique()
            all_items = items_df['itemid'].unique()
            # 进行特征工程处理
            user_nianling_encoder = LabelEncoder().fit(users_df['nianling'])
            user_xingbie_encoder = LabelEncoder().fit(users_df['xingbie'])
            item_title_encoder = LabelEncoder().fit(items_df['title'])
            item_shoptag_encoder = LabelEncoder().fit(items_df['shoptag'])
            item_baoyounew_encoder = LabelEncoder().fit(items_df['baoyounew'])
            item_prosheng_encoder = LabelEncoder().fit(items_df['prosheng'])
            # 为每个用户创建与所有物品的组合
            for user in all_users:
                #获取用户已购买的物品
                purchased_items = purchases_df[purchases_df['userid'] == user]['itemid'].values
                # 为每个物品创建记录
                for item in all_items:
                    # 标签：1表示购买/收藏/点击过，0表示未购买/未收藏/未点击
                    label = 1 if item in purchased_items else 0
                    # 获取用户特征和物品特征
                    user_features = users_df[users_df['userid'] == user].iloc[0]
                    item_features = items_df[items_df['itemid'] == item].iloc[0]
                    # 创建特征向量，使用编码器将分类特征转换为数值
                    features = [
                        user_nianling_encoder.transform([user_features['nianling']])[0],  # nianling编码
                        user_xingbie_encoder.transform([user_features['xingbie']])[0],  # xingbie编码
                        item_title_encoder.transform([item_features['title']])[0],  # title编码
                        item_shoptag_encoder.transform([item_features['shoptag']])[0],  # shoptag编码
                        item_baoyounew_encoder.transform([item_features['baoyounew']])[0],  # baoyounew编码
                        item_prosheng_encoder.transform([item_features['prosheng']])[0],  # prosheng编码
                    ]
                    #将用户-物品对添加到列表中
                    all_user_item_pairs.append({
                        'userid': user,
                        'itemid': item,
                        'features': features,
                        'label': label
                    })
            # 创建包含所有用户-物品对的DataFrame
            data_df = pd.DataFrame(all_user_item_pairs)
            # 提取特征和标签
            X = np.array([x for x in data_df['features']]) # 特征矩阵
            y = data_df['label'].values # 标签向量
            # 分割训练集和测试集
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            print("训练集特征形状:", X_train)
            print("测试集特征形状:", X_test)
            print("训练集标签形状:", y_train)
            print("测试集标签形状:", y_test)
            #训练随机森林模型
            model = RandomForestClassifier(
                n_estimators=50,  # 减少树的数量以加快训练
                max_depth=10,  # 树的最大深度
                random_state=42 # 随机种子，确保结果可重现
            )
            # 在训练集上训练模型
            model.fit(X_train, y_train)
            # 计算模型在训练集和测试集上的准确率
            train_score = model.score(X_train, y_train)
            test_score = model.score(X_test, y_test)
            print(f"训练准确率: {train_score:.4f}")
            print(f"测试准确率: {test_score:.4f}")

            # 保存训练好的模型到文件
            with open('rf_model.pkl', 'wb') as f:
                pickle.dump(model, f)
            # 保存预处理对象到文件，用于后续预测
            preprocessing_objects = {
                'user_nianling_encoder': user_nianling_encoder,
                'user_xingbie_encoder': user_xingbie_encoder,
                'item_title_encoder': item_title_encoder,
                'item_shoptag_encoder': item_shoptag_encoder,
                'item_baoyounew_encoder': item_baoyounew_encoder,
                'item_prosheng_encoder': item_prosheng_encoder,
                'users_df': users_df,
                'items_df': items_df,
                'purchases_df': purchases_df
            }
            with open('rf_preprocessing.pkl', 'wb') as f:
                pickle.dump(preprocessing_objects, f)

        except Exception as e:
            msg["code"] = other_code
            msg["msg"] = e.__str__()
        return JsonResponse(msg)

def merge_and_deduplicate(list1, list2):
    """
    合并两个列表并去除id重复的字典元素
    保留第一个出现的元素
    """
    seen_ids = set()
    result = []
    # 遍历第一个列表
    for item in list1:
        item_id = item['id']
        if item_id not in seen_ids:
            seen_ids.add(item_id)
            result.append(item)
    # 遍历第二个列表
    for item in list2:
        item_id = item['id']
        if item_id not in seen_ids:
            seen_ids.add(item_id)
            result.append(item)
    return result

#随机森林模型训练、输出推荐结果
def rf_recommendations(request):
    """
    使用训练好的随机森林模型进行推荐
    该函数负责：
    1. 加载已训练的模型和预处理对象
    2. 获取当前用户信息和已购买物品
    3. 对未购买物品进行预测
    4. 返回按预测概率排序的推荐列表
    """
    #判断当前登录用户
    tablename = Auth().getTokenInfo(request).get('tablename')
    if tablename !='yonghu':
        return []
    # 检查模型文件是否存在
    if not os.path.exists('rf_model.pkl') or not os.path.exists('rf_preprocessing.pkl'):
        print("模型文件不存在，请先调用 train_rf_model() 训练模型")
        return []

        # 加载训练好的模型
    with open('rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
        # 加载预处理对象
    with open('rf_preprocessing.pkl', 'rb') as f:
        preprocessing_objects = pickle.load(f)

    # 从预处理对象中提取各个组件
    user_nianling_encoder = preprocessing_objects['user_nianling_encoder']
    user_xingbie_encoder = preprocessing_objects['user_xingbie_encoder']
    item_title_encoder = preprocessing_objects['item_title_encoder']
    item_shoptag_encoder = preprocessing_objects['item_shoptag_encoder']
    item_baoyounew_encoder = preprocessing_objects['item_baoyounew_encoder']
    item_prosheng_encoder = preprocessing_objects['item_prosheng_encoder']
    users_df = preprocessing_objects['users_df']
    items_df = preprocessing_objects['items_df']
    purchases_df = preprocessing_objects['purchases_df']

    #获取当前用户id
    user_id = Auth().getTokenInfo(request).get('params').get("id")
    #获取用户已购买的物品
    purchased_items = purchases_df[purchases_df['userid'] == user_id]['itemid'].values
    #获取用户信息
    user_info = users_df[users_df['userid'] == user_id].iloc[0]
    #为每个未购买的物品计算购买概率
    recommendations = []
    for _, item in items_df.iterrows():
        if item['itemid'] in purchased_items:
            continue  #跳过已购买的物品
        # 创建特征向量，使用与训练时相同的编码器
        features = [
            user_nianling_encoder.transform([user_info['nianling']])[0],  # nianling编码
            user_xingbie_encoder.transform([user_info['xingbie']])[0],  # xingbie编码
            item_title_encoder.transform([item['title']])[0],  # title编码
            item_shoptag_encoder.transform([item['shoptag']])[0],  # shoptag编码
            item_baoyounew_encoder.transform([item['baoyounew']])[0],  # baoyounew编码
            item_prosheng_encoder.transform([item['prosheng']])[0],  # prosheng编码
        ]
        # 使用模型预测购买概率
        proba = model.predict_proba([features])[0]
        if len(proba) == 1:
            # 如果只有一个类别，则如果模型类别是1，则概率为proba[0]，否则为0
            if model.classes_[0] == 1:
                probability = proba[0]
            else:
                probability = 0
        else:
            probability = proba[1]
        recommendations.append({
            'itemid': item['itemid'],
            'title':item['title'],  #title编码
            'shoptag':item['shoptag'],  #shoptag编码
            'baoyounew':item['baoyounew'],  #baoyounew编码
            'prosheng':item['prosheng'],  #prosheng编码
            'probability': probability
        })
        # 按概率排序并返回前top_n个
        recommendations.sort(key=lambda x: x['probability'], reverse=True)
    print(f"\n为用户 {user_id} 的推荐结果:")
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. 物品ID: {rec['itemid']},购买概率: {rec['probability']:.4f}")
    return recommendations



