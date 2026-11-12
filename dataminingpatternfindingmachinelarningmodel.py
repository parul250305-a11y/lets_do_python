import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

# 1. Load your 100 sales entries
df = pd.read_csv('sales_data.csv')

# 2. Convert dates and text into numbers so the ML model can read them
df['Date'] = pd.to_datetime(df['Date'])
df['Day_of_Week'] = df['Date'].dt.dayofweek  # Turns dates into 0 (Mon) to 6 (Sun)

# Automatically convert any text columns (like 'Product') into numbers
numeric_data = pd.get_dummies(df.drop(columns=['Date']), drop_first=True)

# 3. PATTERN 1: Let the model group similar sales together automatically
cluster_model = KMeans(n_clusters=3, random_state=42)
df['Auto_Group'] = cluster_model.fit_predict(numeric_data)

# 4. PATTERN 2: Let the model find unusual sales spikes/drops automatically
anomaly_model = IsolationForest(contamination=0.05, random_state=42)
df['Is_Unusual'] = anomaly_model.fit_predict(numeric_data) # -1 means unusual, 1 means normal

# See what the model discovered!
print("--- Data with Model-Discovered Patterns ---")
print(df[['Date', 'Amount', 'Auto_Group', 'Is_Unusual']].head(15))
