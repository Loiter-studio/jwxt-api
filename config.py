class Config:
    """Configure for JWXT"""
    def __init__(self):
        self.scoreUrl   = "http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getKccjList"
        self.loginUrl   = "http://uems.sysu.edu.cn/jwxt/j_unieap_security_check.do"
        self.courseUrl  = "http://uems.sysu.edu.cn/jwxt/sysu/xk/xskbcx/xskbcx.jsp"
    def score(self, xnd, xq):
        query = """{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{kccjStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"kccjStore",pageNumber:1,pageSize:200,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.xscj.xscjcx.model.KccjModel",order:"t.xn, t.xq, t.kch, t.bzw"}},parameters:{"kccjStore-params": [{"name": "Filter_t.pylbm_0.31229493138756364", "type": "String", "value": "'01'", "condition": " = ", "property": "t.pylbm"}, {"name": "Filter_t.xn_0.32465981964936424", "type": "String", "value": "'"""+xnd+"""'", "condition": " = ", "property": "t.xn"}, {"name": "Filter_t.xq_0.9852216962896978", "type": "String", "value": "'"""+xq+"""'", "condition": " = ", "property": "t.xq"}], "args": ["student"]}}}"""
        return query


if __name__ == "__main__":
    c = Config()
    print c.score("2012-2013", "2")
