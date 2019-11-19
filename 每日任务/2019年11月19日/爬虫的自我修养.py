#-----如何访问互联网
import urllib.request
import urllib.parse

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
data = {}
data["i"] = " qqqq"
data["from"] = " AUTO"
data["to"] = " AUTO"
data["smartresult"] = " dict"
data["client"] = " fanyideskweb"
data["salt"] = " 15741583189621"
data["sign"] = " 89cab6a9c9eb11051942344d323c2cfb"
data["ts"] = " 1574158318962"
data["bv"] = " 140f03b6cc43b5b1fabe089d78dc366f"
data["doctype"] = " json"
data["version"] = " 2.1"
data["keyfrom"] = " fanyi.web"
data["action"] = " FY_BY_CLICKBUTTION"
data = urllib.parse.urlencode(data).encode("utf-8")




##
##i: 姜枫是帅哥
##from: AUTO
##to: AUTO
##smartresult: dict
##client: fanyideskweb
##salt: 15741583189621
##sign: 89cab6a9c9eb11051942344d323c2cfb
##ts: 1574158318962
##bv: 140f03b6cc43b5b1fabe089d78dc366f
##doctype: json
##version: 2.1
##keyfrom: fanyi.web
##action: FY_BY_CLICKBUTTION

response = urllib.request.urlopen(url,data)
html = response.read().decode("utf-8")


print(html)
