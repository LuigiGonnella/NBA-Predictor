# NBA Predictor 🏀

A machine learning project for predicting NBA game outcomes using advanced basketball analytics and team performance metrics.

## 📊 Project Overview

This project uses historical NBA game data to predict the outcomes of basketball games by analyzing team statistics, performance trends, and matchup dynamics. The model leverages advanced basketball metrics like Offensive Rating (ORtg), Defensive Rating (DRtg), and the "Four Factors" of basketball success.

## 🚀 Features

- **Advanced Basketball Metrics**: Uses ORtg, DRtg, Pace, Effective Field Goal %, Turnover %, Rebound %, and Free Throw metrics
- **Rolling Averages**: Calculates team performance over rolling windows (5, 10, 20 games) to capture recent form
- **Streak Analysis**: Tracks win/loss streaks and team momentum
- **Home/Away Splits**: Separate analysis for home and away performance
- **Rest Days Impact**: Considers days of rest between games
- **Opponent Strength**: Factors in the quality of opposition faced
- **Data Leakage Prevention**: Ensures only historical data is used for predictions

## 📁 Project Structure

```
NBA-Predictor/
├── src/
│   ├── data/
│   │   ├── data.csv              # Raw NBA game data
│   │   ├── load_data.py          # Data loading utilities
│   │   └── preprocess.py         # Data preprocessing pipeline
├── notebooks/
│   └── 01-exploration.ipynb     # Data exploration and analysis
├── README.md
└── .gitignore
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LuigiGonnella/NBA-Predictor.git
   cd NBA-Predictor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn jupyter
   ```

## 📈 Data Features

The model uses the following key features:

### Core Statistics
- **ORtg**: Offensive Rating (points scored per 100 possessions)
- **DRtg**: Defensive Rating (points allowed per 100 possessions)
- **Pace**: Game tempo (possessions per 48 minutes)

### Four Factors (Dean Oliver)
- **Effective Field Goal %**: Shooting efficiency
- **Turnover %**: Ball security
- **Offensive/Defensive Rebound %**: Rebounding performance
- **Free Throw Rate**: Getting to the line

### Advanced Features
- **Rolling Averages**: L5, L10, L20 game performance windows
- **Win Streaks**: Current winning/losing streaks
- **Home/Away Win %**: Venue-specific performance
- **Rest Days**: Days between games
- **Opponent Strength**: Quality of opposition

## 🔬 Methodology

1. **Data Preprocessing**
   - Remove data leakage (no game-specific results)
   - Calculate rolling averages with proper temporal ordering
   - Handle missing values and outliers

2. **Feature Engineering**
   - Create rolling statistics for all key metrics
   - Calculate opponent features and matchup differentials
   - Generate situational features (home/away, rest days, streaks)

3. **Model Training**
   - Use time-based train/test splits (no random splitting)
   - Feature selection using importance scores
   - Cross-validation with temporal constraints

4. **Evaluation**
   - Accuracy, precision, recall for win/loss prediction
   - Calibration plots for probability reliability
   - Feature importance analysis

## 📊 Usage

### Data Exploration
```python
# Load and explore the data
from src.data.preprocess import load_and_preprocess_data

# Load data
df, numerical_cols, categorical_cols = load_and_preprocess_data('src/data/data.csv')

# Basic exploration
print(df.head())
print(df.info())
```

### Feature Engineering
```python
# Add rolling averages and advanced features
df_enhanced = compute_rolling_averages(df)
df_final = compute_adding_features(df_enhanced)
```

### Model Training
```python
from src.models.train import train_model
from sklearn.ensemble import RandomForestClassifier

# Prepare features
features = ['ORtg_L10', 'DRtg_L10', 'win_pct_L5', 'RestDays', 'home_win_pt']
X = df_final[features].dropna()
y = df_final.loc[X.index, 'Win']

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)
```

## 🎯 Model Performance

The model focuses on:
- **Accuracy**: Overall prediction correctness
- **Calibration**: Probability reliability
- **Feature Importance**: Understanding what drives wins
- **Temporal Stability**: Consistent performance across seasons

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is for educational purposes. NBA data is used under fair use for research and analysis.

## 📧 Contact

Luigi Gonnella - [GitHub](https://github.com/LuigiGonnella)

Project Link: [https://github.com/LuigiGonnella/NBA-Predictor](https://github.com/LuigiGonnella/NBA-Predictor)

---

⭐ Star this repo if you find it useful for your NBA analytics projects!
