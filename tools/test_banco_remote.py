import urllib.request, json

req = urllib.request.Request("http://127.0.0.1:4010/api/v1/auth/login", data=json.dumps({"email":"admin@almahue.local","password":"Admin123!"}).encode(), headers={"Content-Type":"application/json"})
res = json.loads(urllib.request.urlopen(req).read().decode())
token = res["token"]
empresa = res["user"]["empresaId"]

payload = {"codigo":"001","nombre":"Banco de Chile","rut":"97.004.000-5","activo":True}
req2 = urllib.request.Request("http://127.0.0.1:4010/api/v1/bancos", data=json.dumps(payload).encode(), headers={"Content-Type":"application/json", "Authorization": f"Bearer {token}", "x-empresa-id": str(empresa)})
try:
    res2 = json.loads(urllib.request.urlopen(req2).read().decode())
    print("SUCCESS_CREATE_BANCO:", res2)
except urllib.error.HTTPError as e:
    print("HTTP_ERROR:", e.code, e.read().decode())
