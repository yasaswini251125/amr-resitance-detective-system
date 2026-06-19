import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def assign_risk_level(manure, pesticide, density):
    score = 0

    # Animal density contribution
    if density > 300:
        score += 3
    elif density > 150:
        score += 2
    elif density > 80:
        score += 1

    # Manure contribution
    if manure > 35:
        score += 2
    elif manure > 20:
        score += 1

    # Pesticide contribution
    if pesticide > 8:
        score += 2
    elif pesticide > 4:
        score += 1

    # Final level
    if score >= 6:
        return "Critical"
    elif score >= 4:
        return "High"
    elif score >= 2:
        return "Medium"
    else:
        return "Low"


def generate_synthetic_dataset(n_samples=1500):
    np.random.seed(42)

    manure = np.random.uniform(0, 50, n_samples)
    pesticide = np.random.uniform(0, 12, n_samples)
    density = np.random.uniform(0, 600, n_samples)
    ph = np.random.uniform(4.0, 9.0, n_samples)
    moisture = np.random.uniform(10, 90, n_samples)

    amr_risk = []
    for i in range(n_samples):
        risk_level = assign_risk_level(manure[i], pesticide[i], density[i])
        amr_risk.append(risk_level)

    df = pd.DataFrame({
        'Manure_Usage': manure,
        'Pesticide_Frequency': pesticide,
        'Animal_Density': density,
        'Soil_pH': ph,
        'Soil_Moisture': moisture,
        'AMR_Risk': amr_risk
    })

    df.to_csv('amr_dataset.csv', index=False)
    return df


def train_amr_model():
    df = generate_synthetic_dataset()

    X = df[['Manure_Usage', 'Pesticide_Frequency', 'Animal_Density', 'Soil_pH', 'Soil_Moisture']]
    y = df['AMR_Risk']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, 'amr_risk_model.pkl')
    print("Model trained successfully with multi-class AMR risk levels.")


def predict_amr_risk(m, p, d, ph, moist):
    model = joblib.load('amr_risk_model.pkl')
    features = np.array([[m, p, d, ph, moist]])

    risk = model.predict(features)[0]
    probs = model.predict_proba(features)[0]
    class_names = model.classes_

    prob_dict = {class_names[i]: round(float(probs[i]) * 100, 1) for i in range(len(class_names))}
    return risk, prob_dict


if __name__ == "__main__":
    train_amr_model()