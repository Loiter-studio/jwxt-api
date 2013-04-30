import json
import requests


user = {'j_username':"09388267", 'j_password':'12124398'}
r = requests.get("http://uems.sysu.edu.cn/jwxt/j_unieap_security_check.do", params=user)
cookies = r.cookies

# kecheng
#query = {'xnd':"2009-2010", "xq":"2"}
#result = requests.get("http://uems.sysu.edu.cn/jwxt/sysu/xk/xskbcx/xskbcx.jsp", params=query, cookies=cookies)

# score
scoreUrl = "http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getKccjList"
xnd = "2009-2010"
xq = "2"
sid = "09388267"

#query = """{"header": {"code": -100, "message": {"title": "", "detail": ""}}, "body": {"dataStores" : {"kccjStore" :{"rowSet": {"primary":[], "filter": [],"delete": []}, "name": "kccjStore", "pageNumber" :1, "pageSize": 100,"recordCount":0, "rowSetName": "pojo_com.neusoft.education.sysu.xscj.xscjcx.model.KccjModel", "order": "t.xn, t.xq, t.kch, t.bzw"}}, "parameters": {"kccjStore-params": [{"name": "Filter_t.pylbm_0.14250923241738405", "type": "String", "value": "'01'", "condition": " = ", "property": "t.pylbm"}, {"name": "Filter_t.xn_0.9157393842453891", "type": "String", "value": "2009-2010", "condition": " = ", "property": "t.xn"}, {"name": "Filter_t.xq_0.5502242433637169", "type": "String", "value": "2", "condition": " = ", "property": "t.xq"}, {"name": "xh", "type": "String", "value": "09388267", "condition": " = ", "property": "t.xh"}], "args": ["student"]}}}"""

query = """{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{kccjStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"kccjStore",pageNumber:1,pageSize:200,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.xscj.xscjcx.model.KccjModel",order:"t.xn, t.xq, t.kch, t.bzw"}},parameters:{"kccjStore-params": [{"name": "Filter_t.pylbm_0.31229493138756364", "type": "String", "value": "'01'", "condition": " = ", "property": "t.pylbm"}, {"name": "Filter_t.xn_0.32465981964936424", "type": "String", "value": "'2010-2011'", "condition": " = ", "property": "t.xn"}, {"name": "Filter_t.xq_0.9852216962896978", "type": "String", "value": "'1'", "condition": " = ", "property": "t.xq"}], "args": ["student"]}}}"""

headers = {"Accept": "text/plain", "render":"unieap", "content-type": "mulitpart/form-data"}
#headers = {"content-type": "mulitpart/form-data" }
#score = requests.post("http://httpbin.org/post", headers=headers, cookies=cookies, data=query)
score = requests.post(scoreUrl, headers=headers,  cookies=cookies, data=query)

print score.content
