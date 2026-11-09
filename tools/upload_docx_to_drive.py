# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.parse
import os

token_file = r"C:\Users\c\.gemini\antigravity\plugin_data\gdocs\token.json"
with open(token_file, "r", encoding="utf-8") as f:
    tdata = json.load(f)

access_token = tdata["token"]["access_token"]
doc_id = "14guwdS-lEtpr9ttd4Mmyh4wVF-AaNklY"
docx_path = r"docs\requerimientos\informe-unificado-acuerdos-por-semana-erp-almahue.docx"

if not os.path.exists(docx_path):
    raise FileNotFoundError(f"No existe {docx_path}")

with open(docx_path, "rb") as f:
    docx_bytes = f.read()

print(f"Subiendo {len(docx_bytes)} bytes de {docx_path} a Drive ID {doc_id}...")

url = f"https://www.googleapis.com/upload/drive/v3/files/{doc_id}?uploadType=media"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}

req = urllib.request.Request(url, data=docx_bytes, headers=headers, method="PATCH")
try:
    with urllib.request.urlopen(req) as resp:
        res_data = resp.read()
        print("Respuesta exitosa de Drive API:")
        print(res_data.decode("utf-8"))
except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8")
    print(f"HTTPError {e.code}: {e.reason}")
    print(err_body)
