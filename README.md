# AMR Risk Surveillance & Multi-Factor Crop Advisory System

A comprehensive AI-powered agricultural decision support system that combines machine learning, geospatial intelligence, and market analysis to provide sustainable farming recommendations.

## Features

### 🔬 Machine Learning Core
- **Random Forest Classifier** trained on 1,500+ synthetic agricultural records
- **AMR Risk Prediction** based on manure usage, pesticide frequency, animal density, soil pH, and moisture
- **High Accuracy** classification with detailed probability outputs

### 🌍 Location-Based Intelligence
- **Geospatial Input** accepts village/city names or PIN codes
- **Weather API Integration** (currently mocked, easily replaceable with real APIs)
- **Market Price Simulation** based on location-specific mandi prices

### 🌱 Three-Tier Recommendation Engine

#### Tier 1: AMR Safety Override
- Activates when AMR Risk is High
- Recommends only Industrial Crops: Cotton, Jute
- Displays strict public health warnings against raw-consumption crops

#### Tier 2: pH-Based Recommendations
- Activates when AMR Risk is Low
- **4.5-5.5 pH**: Tea, Coffee, Cashew, Rubber
- **5.5-6.5 pH**: Ragi, Tur Dal, Groundnut, Grapes
- **6.5-7.5 pH**: Basmati Rice, Wheat, Sugarcane, Mango
- **7.5-8.5 pH**: Cotton, Soybeans, Chickpeas, Oranges

#### Intercropping Layer
- Simple companion planting suggestions (e.g., Wheat + Mustard)
- One companion crop per recommended crop

#### Profit Advisor
- Identifies the crop with highest current market price among recommendations
- Mock integration with Agmarknet INR prices

## Technology Stack

- **Backend**: Python Flask
- **Machine Learning**: Scikit-learn (Random Forest)
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Data Processing**: Pandas, NumPy
- **Model Persistence**: Joblib

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Installation Steps

1. **Clone/Download the project**
   ```bash
   cd path/to/project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model (optional - runs automatically on first app start)**
   ```bash
   python train_model.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
├── app.py                 # Main Flask application
├── train_model.py         # Dataset generation and model training
├── requirements.txt       # Python dependencies
├── amr_dataset.csv        # Generated synthetic dataset (created automatically)
├── amr_risk_model.pkl     # Trained ML model (created automatically)
└── templates/
    ├── index.html         # Main dashboard interface
    └── result.html        # Analysis results page
```

## API Endpoints

- `GET /` - Main dashboard
- `POST /analyze` - Process agricultural parameters and return recommendations
- `GET /api/health` - Health check endpoint

## Usage

1. **Enter Location**: Input village/city name or PIN code
2. **Input Parameters**:
   - Manure Usage (0-50 Tons/Acre)
   - Pesticide Frequency (0-12 times/month)
   - Animal Density (0-600 livestock count)
   - Soil pH (4.0-9.0)
   - Soil Moisture (10-90%)
3. **Get Results**: View AMR risk assessment, crop recommendations, and profit analysis

## Future Enhancements

### 🚀 IoT Sensor Fusion
- Real-time soil moisture sensors
- Automated weather station integration
- Livestock monitoring systems
- Drone-based field surveillance

### 🧠 Deep Learning (CNNs)
- Computer vision for crop disease detection
- Satellite imagery analysis for yield prediction
- Automated weed identification
- Quality assessment of harvested crops

### ⛓️ Blockchain-Based Data Auditing
- Immutable supply chain tracking
- Quality assurance certificates
- Transparent pricing mechanisms
- Farmer-to-consumer traceability

## Model Performance

The Random Forest classifier achieves high accuracy in predicting AMR risk levels based on agricultural parameters. The model is trained on synthetically generated data that follows realistic agricultural patterns and risk correlations.

## Data Privacy & Security

- All processing happens locally
- No user data is stored or transmitted
- Model predictions are computed in real-time
- Weather and market data can be easily replaced with real APIs

## Contributing

This system serves as a foundation for advanced agricultural technology. Contributions are welcome in:
- Improving ML model accuracy
- Adding real API integrations
- Enhancing UI/UX
- Implementing additional recommendation algorithms

## License

This project is developed for educational and research purposes in agricultural technology and AMR surveillance.

---

**Built with ❤️ for sustainable agriculture and public health**