from fastapi import FastAPI, Form
import joblib


app= FastAPI()

pipeline = joblib.load("modelos/pipelines/pipelines1.joblib")
modelo = joblib.load("modelos/estimators/modelo01.joblib")

@app.post("/predict")
def predict(sexo: str=Form(...),
			edad: int=Form(...), 
			monto: int=Form(...), 
			tipo_vivienda: str=Form(...)):

	x = pipeline.transform([[sexo, edad, monto, tipo_vivienda]])
	#print("resultado pipeline",x)
	#prediction = modelo.predict(x)
	#print("resultado prediction",prediction)
	prob_bad_client= modelo.predict_proba(x)[0][1]
	
	
	return {"prob_bad_client": prob_bad_client}