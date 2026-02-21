from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
from fastapi.responses import FileResponse
import schemas
import uvicorn

app = FastAPI(title="Stock Price Prediction API")

# Load trained model
model = joblib.load("model/stock_model.pkl")

@app.post("/predict")
def predict_price(data: schemas.StockInput):

    X = np.array([[ 
        data.open,
        data.high,
        data.low,
        data.close,
        data.traded_quantity,
        data.ma_5,
        data.ma_10,
        data.vol_ma_5,
        data.close_lag1,
        data.momentum_3,
        data.volatility_5,
        data.price_change
    ]])

    prediction = model.predict(X)

    return {
        "predicted_price": float(prediction[0])
    }

@app.get("/results")
def get_results_plot():
    return FileResponse("assets/results.png")

# Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)