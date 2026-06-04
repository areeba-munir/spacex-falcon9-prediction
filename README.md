# 🚀 SpaceX Falcon 9 First Stage Landing Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Plotly Dash](https://img.shields.io/badge/Plotly-Dash-orange)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-red)
![IBM](https://img.shields.io/badge/IBM-Data%20Science%20Capstone-0530ad)

## 📋 Project Overview

This capstone project analyzes **SpaceX Falcon 9 launch data** to predict whether the first stage of a rocket will successfully land and be reused. Since SpaceX advertises Falcon 9 launches at **$62 million** (compared to competitors at $165 million+), the key cost advantage comes from **reusing the first stage**. Accurately predicting landing success helps estimate launch costs and can be useful for companies competing against SpaceX.

---

## 🎯 Business Problem

> **Can we predict if the Falcon 9 first stage will land successfully?**

A successful landing means SpaceX can reuse the booster, significantly reducing costs. This project builds a machine learning pipeline to make that prediction using historical launch data.

---

## 📁 Project Structure

```
spacex-falcon9-prediction/
│
├── 📓 Notebooks
│   ├── jupyter-labs-spacex-data-collection-api-v2.ipynb   # Week 1: API Data Collection
│   ├── jupyter-labs-webscraping.ipynb                      # Week 1: Web Scraping
│   ├── labs-jupyter-spacex-Data_wrangling-v2.ipynb         # Week 2: Data Wrangling
│   ├── jupyter-labs-eda-sql-coursera_sqllite.ipynb         # Week 2: EDA with SQL
│   ├── edadataviz.ipynb                                    # Week 2: EDA with Visualizations
│   ├── lab-jupyter-launch-site-location-v2.ipynb           # Week 3: Folium Maps
│   └── SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb  # Week 4: ML Prediction
│
├── 📊 Dashboard
│   └── spacex_dash_app.py                                  # Plotly Dash Interactive Dashboard
│
├── 🗄️ Data
│   ├── spacex_launch_geo.csv                               # Launch data with coordinates
│   ├── spacex_launch_geo__1_.csv                           # Alternate launch dataset
│   ├── spacex.db                                           # SQLite database (SpaceX data)
│   └── my_data1.db                                         # SQLite database (EDA queries)
│
└── README.md
```

---

## 🗂️ Notebooks — What Each Does

### 1. `jupyter-labs-spacex-data-collection-api-v2.ipynb`
**Data Collection via SpaceX REST API**
- Requests launch data directly from the SpaceX API
- Parses nested JSON responses into a clean Pandas DataFrame
- Extracts booster version, payload mass, launch site, orbit, and landing outcomes
- Saves the processed data for downstream analysis

### 2. `jupyter-labs-webscraping.ipynb`
**Web Scraping with BeautifulSoup**
- Scrapes Falcon 9 launch history from Wikipedia
- Parses HTML tables to extract launch records
- Cleans and structures scraped data into a DataFrame
- Supplements API data with additional historical records

### 3. `labs-jupyter-spacex-Data_wrangling-v2.ipynb`
**Data Wrangling & Feature Engineering**
- Handles missing values in payload mass
- Creates the `class` label column (1 = successful landing, 0 = failure)
- Encodes categorical variables (launch site, orbit, booster version)
- Prepares the final feature matrix for machine learning

### 4. `jupyter-labs-eda-sql-coursera_sqllite.ipynb`
**Exploratory Data Analysis with SQL**
- Loads data into a SQLite database
- Runs SQL queries to explore launch patterns
- Investigates launch sites, booster versions, payload ranges, and success rates
- Answers key business questions using structured queries

### 5. `edadataviz.ipynb`
**Exploratory Data Analysis with Visualizations**
- Creates scatter plots, bar charts, and line charts using Matplotlib & Seaborn
- Analyzes correlations between payload mass, orbit, and landing success
- Visualizes launch success trends over time by flight number
- Identifies which features are most predictive of landing outcome

### 6. `lab-jupyter-launch-site-location-v2.ipynb`
**Interactive Maps with Folium**
- Maps all SpaceX launch sites on an interactive Folium map
- Marks successful and failed landings with color-coded markers
- Calculates distances from launch sites to coastlines, cities, and railroads
- Visualizes geographic clustering of launch outcomes

### 7. `SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb`
**Machine Learning Classification**
- Splits data into training and test sets
- Trains and evaluates four classifiers:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Decision Tree
  - K-Nearest Neighbors (KNN)
- Performs GridSearchCV hyperparameter tuning for each model
- Selects the best model based on test accuracy
- Generates confusion matrices for visual evaluation

---

## 📊 Interactive Dashboard — `spacex_dash_app.py`

An interactive **Plotly Dash** web application for real-time visual analytics.

### Features
| Component | Description |
|-----------|-------------|
| **Dropdown** | Filter by launch site (All Sites or individual site) |
| **Pie Chart** | Shows success launch distribution per site |
| **Range Slider** | Filter by payload mass (0 – 10,000 kg) |
| **Scatter Plot** | Payload vs. Success, color-coded by booster version |

### Running the Dashboard

```bash
# Install dependencies
pip install pandas dash plotly

# Run the app
python spacex_dash_app.py

# Open in browser
http://127.0.0.1:8050/
```

### Dashboard Insights

| Question | Answer |
|----------|--------|
| Which site has the most successful launches? | **KSC LC-39A** |
| Which site has the highest success *rate*? | **KSC LC-39A** (~77%) |
| Best payload range for success? | **2,000 – 5,500 kg** |
| Worst payload range for success? | **6,000 – 9,600 kg** |
| Best booster version? | **FT (Block 5 predecessor)** |

---

## 🤖 Machine Learning Results

| Model | Test Accuracy |
|-------|--------------|
| Logistic Regression | ~83% |
| Support Vector Machine | ~83% |
| Decision Tree | ~72% |
| K-Nearest Neighbors | ~78% |

> **Best Model:** Logistic Regression / SVM (tied) — both achieve ~83% accuracy after tuning.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| Matplotlib / Seaborn | Static visualizations |
| Plotly / Dash | Interactive dashboard |
| Folium | Geographic maps |
| Scikit-learn | Machine learning |
| SQLite3 | SQL-based EDA |
| BeautifulSoup | Web scraping |
| Requests | REST API calls |

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/spacex-falcon9-prediction.git
cd spacex-falcon9-prediction

# Install dependencies
pip install pandas numpy matplotlib seaborn plotly dash folium scikit-learn beautifulsoup4 requests sqlalchemy

# Launch Jupyter
jupyter notebook

# Or run the dashboard
python spacex_dash_app.py
```

---

## 📈 Key Findings

1. **KSC LC-39A** is the most successful launch site by both total launches and success rate
2. **Payload mass between 2,000–5,500 kg** correlates with the highest landing success
3. **FT booster version** shows the strongest track record for successful landings
4. **Higher payload masses (>6,000 kg)** tend to have lower first-stage recovery success
5. Launch success has **improved significantly over time**, with recent launches achieving near 100% success

---

## 🙏 Acknowledgements

- **IBM Data Science Professional Certificate** — Coursera Capstone Project
- SpaceX API: [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)
- Wikipedia — Falcon 9 launch history tables
- Skills Network / IBM Watson Studio labs

---

## 📬 Contact

**Author:** [Your Name]  
**GitHub:** [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)  
**LinkedIn:** [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

*This project was completed as the capstone for the IBM Data Science Professional Certificate on Coursera.*
