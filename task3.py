# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nUBNlNjiwYD-FL3XUQNG-zpOQ3c3s3F7

**Installing Libraries**
"""

!pip install -q kaggle pandas scikit-learn

"""**Upload the Dataset from kaggle**"""

from google.colab import files
files.upload()

"""**Load the Dataset**"""

import pandas as pd

# Load the dataset
df = pd.read_csv('/content/Disease_symptom_and_patient_profile_dataset.csv')
print(df.head())
print(df.columns)

"""**Preprocess the Data**"""

from sklearn.preprocessing import LabelEncoder

# Encode categorical variables
label_encoders = {}
for column in ['Disease', 'Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 'Gender', 'Blood Pressure', 'Cholesterol Level', 'Outcome Variable']:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Verify the DataFrame after encoding
print(df.head())
print(df.columns)

# Split the data into features and target
X = df.drop('Outcome Variable', axis=1)
y = df['Outcome Variable']

"""**Split the Data**"""

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""**Train a Classification Model**"""

from sklearn.ensemble import RandomForestClassifier

# Initialize the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

"""**Evaluate the Model**"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')

"""**Making Predictions with new data**"""

# Example of making predictions with new data
new_data = {
    'Disease': 'Influenza',
    'Fever': 'Yes',
    'Cough': 'No',
    'Fatigue': 'Yes',
    'Difficulty Breathing': 'Yes',
    'Age': 20,
    'Gender': 'Female',
    'Blood Pressure': 'Low',
    'Cholesterol Level': 'Normal'
}

# Encode the new data
new_data_encoded = {}
for column, value in new_data.items():
    if column in label_encoders:
        new_data_encoded[column] = label_encoders[column].transform([value])[0]
    else:
        new_data_encoded[column] = value

# Convert the encoded new data into a DataFrame with the same columns as X_train
new_data_df = pd.DataFrame([new_data_encoded], columns=X.columns)

# Make a prediction
prediction = model.predict(new_data_df)
# Decode the prediction
prediction_decoded = label_encoders['Outcome Variable'].inverse_transform(prediction)
print(f'Prediction: {prediction_decoded[0]}')

# Example of making predictions with new data
new_data = {
    'Disease': 'Common Cold',
    'Fever': 'No',
    'Cough': 'Yes',
    'Fatigue': 'Yes',
    'Difficulty Breathing': 'No',
    'Age': 25,
    'Gender': 'Female',
    'Blood Pressure': 'Normal',
    'Cholesterol Level': 'Normal'
}

# Encode the new data
new_data_encoded = {}
for column, value in new_data.items():
    if column in label_encoders:
        new_data_encoded[column] = label_encoders[column].transform([value])[0]
    else:
        new_data_encoded[column] = value

# Convert the encoded new data into a DataFrame with the same columns as X_train
new_data_df = pd.DataFrame([new_data_encoded], columns=X.columns)

# Make a prediction
prediction = model.predict(new_data_df)
# Decode the prediction
prediction_decoded = label_encoders['Outcome Variable'].inverse_transform(prediction)
print(f'Prediction: {prediction_decoded[0]}')