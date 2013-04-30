from flask import Flask, session, redirect, url_for, request, render_template
#from flask.ext.redis import Redis
from config import Config
import requests
import json


#user = {'j_username':"09388267", 'j_password':'12124398'}
#r = requests.get("http://uems.sysu.edu.cn/jwxt/j_unieap_security_check.do", params=user)
#cookies = r.cookies

# kecheng
#query = {'xnd':"2009-2010", "xq":"2"}
#result = requests.get("http://uems.sysu.edu.cn/jwxt/sysu/xk/xskbcx/xskbcx.jsp", params=query, cookies=cookies)

# score
#scoreUrl = "http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getKccjList"
#xnd = "2009-2010"
#xq = "2"
#sid = "09388267"


#headers = {"Accept": "text/plain", "render":"unieap", "content-type": "mulitpart/form-data"}
#score = requests.post(scoreUrl, headers=headers,  cookies=cookies, data=query)

app = Flask(__name__)
app.debug = True
app.config['REDIS_HOST'] = 'localhost'
app.config['REDIS_PORT'] = 6379
app.config['REDIS_DB'] = 0
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#redis = Redis(app)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        sid     = request.form['sid']
        pwd     = request.form['pwd']   # never record user's password
        user    = {'j_username': sid, 'j_password': pwd}
        cookies = requests.get("http://uems.sysu.edu.cn/jwxt/j_unieap_security_check.do", params=user).cookies
        session[sid] = cookies
        return redirect(url_for('index'))
    return '''
        <form action="" method="post" />
            <input type=text name=sid>
            <input type=password name=pwd />
            <input type=submit value=Login />
            </input>
        </form>'''

@app.route("/")
def index():
    return render_template("index.html")

app.run()
