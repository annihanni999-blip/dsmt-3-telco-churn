from fastapi import FastAPI
from pydantic import BaseModel

from prediction import make_prediction

app = FastAPI()


class Customer(BaseModel):
    tenure: float
    monthly: float
    techsupport: int


@app.post("/predict")
def predict(customer: Customer):
    probability = make_prediction(
        tenure=customer.tenure,
        MonthlyCharges=customer.monthly,
        TechSupport_yes=customer.techsupport,
    )
    return {"prediction": probability}
