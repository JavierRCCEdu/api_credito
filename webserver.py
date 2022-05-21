from fastapi import FastAPI, Form, Request
import requests
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app= FastAPI()
url = "http://127.0.0.1:8000/predict"
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

	
@app.post("/consultar")
def consultar(nombre: str=Form(...), sexo: str=Form(...),
              edad: int=Form(...),
              monto: int=Form(...),
              tipo_vivienda: str=Form(...)):
		response = requests.post(url, data={"sexo": sexo, 
	                              "edad":edad, 
								  "monto": monto, 
								  "tipo_vivienda": tipo_vivienda})
								  
		#print(response.json())
		respuesta=response.json()
		if respuesta["prob_bad_client"]>0.5:
			mensaje = f"Apreciado {nombre}, no le podemos prestar dinero"
		else:
			mensaje = f"Apreciado {nombre}, su crédito fue aprobado"
		return mensaje