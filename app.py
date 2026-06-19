from flask import Flask, render_template, request
from train_model import predict_amr_risk

app = Flask(__name__)

MARKET_PRICES = {
    "Cotton": 8110,
    "Jute": 5650,
    "Rice": 2450,
    "Wheat": 2585,
    "Maize": 2400,
    "Tea": 18500,
    "Coffee": 35000,
    "Barley": 1980,
    "Potatoes": 2200
}

PRICE_UNIT = "₹/quintal"


def get_crop_recommendations(risk_level, soil_ph):
    # Critical / High risk → industrial crops only
    if risk_level in ["Critical", "High"]:
        return {
            "tier": f"{risk_level} AMR Risk - Industrial Safety Override",
            "crops": ["Cotton", "Jute"],
            "warning": "Food crops are blocked due to high AMR risk."
        }

    # Medium risk → safer limited crops
    if risk_level == "Medium":
        return {
            "tier": "Medium Risk Advisory",
            "crops": ["Wheat", "Maize"],
            "warning": "Moderate AMR risk detected. Safer crops are recommended."
        }

    # Low risk → pH-based crop advisory
    if soil_ph < 5.5:
        return {
            "tier": "Acidic Soil Advisory",
            "crops": ["Tea", "Coffee", "Potatoes"],
            "warning": None
        }
    elif 6.0 <= soil_ph <= 7.5:
        return {
            "tier": "Neutral Soil Advisory",
            "crops": ["Rice", "Wheat", "Maize"],
            "warning": None
        }
    elif soil_ph > 8.0:
        return {
            "tier": "Alkaline Soil Advisory",
            "crops": ["Barley", "Cotton"],
            "warning": None
        }
    else:
        return {
            "tier": "General Soil Advisory",
            "crops": ["Wheat", "Maize"],
            "warning": None
        }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        location = request.form.get("location", "").strip()
        manure = float(request.form.get("manure_usage", 0))
        pesticide = float(request.form.get("pesticide_freq", 0))
        density = float(request.form.get("animal_density", 0))
        soil_ph = float(request.form.get("soil_ph", 0))
        moisture = float(request.form.get("soil_moisture", 0))

        # ML prediction
        risk_level, probs = predict_amr_risk(manure, pesticide, density, soil_ph, moisture)

        # Recommendation logic
        recommendation_data = get_crop_recommendations(risk_level, soil_ph)
        crops = recommendation_data["crops"]

        # Keep only crops present in market price dictionary
        valid_crops = [crop for crop in crops if crop in MARKET_PRICES]

        if not valid_crops:
            return "System Error: No valid crops found in market price database."

        # Best crop by highest price
        best_crop = max(valid_crops, key=lambda crop: MARKET_PRICES[crop])

        result = {
            "location": location,
            "inputs": {
                "manure_usage": manure,
                "pesticide_freq": pesticide,
                "animal_density": density,
                "soil_ph": soil_ph,
                "soil_moisture": moisture
            },
            "amr_risk": {
                "level": risk_level,
                "probability_low": probs.get("Low", 0.0),
                "probability_medium": probs.get("Medium", 0.0),
                "probability_high": probs.get("High", 0.0),
                "probability_critical": probs.get("Critical", 0.0)
            },
            "recommendations": {
                "tier": recommendation_data["tier"],
                "crops": valid_crops,
                "warning": recommendation_data["warning"]
            },
            "market_prices": {
                crop: MARKET_PRICES[crop] for crop in valid_crops
            },
            "profit_advisor": {
                "recommended_crop": best_crop,
                "price": MARKET_PRICES[best_crop],
                "unit": PRICE_UNIT
            }
        }

        return render_template("result.html", result=result)

    except ValueError:
        return "Invalid input. Please enter valid numeric values."
    except Exception as e:
        return f"System Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)