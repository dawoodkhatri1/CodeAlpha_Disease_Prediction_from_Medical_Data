# CodeAlpha_Disease_Prediction_from_Medical_Data

You can run the file in Google Colab and Jupiter Notebook

_**Explanation:**_

**Installing Libraries**

Essential libraries, including kaggle, pandas, and scikit-learn, are installed to facilitate data manipulation, analysis, and machine learning.

**Uploading the Dataset from Kaggle**

The user is prompted to upload necessary files, such as Kaggle API credentials, to access and download the dataset.

**Loading the Dataset**

The dataset is read into a pandas DataFrame, and an initial inspection is performed by displaying the first few rows and the column names to understand the structure of the data.

**Data Preprocessing**

Categorical variables in the dataset are encoded using LabelEncoder from scikit-learn to convert them into numeric values. 
This step involves:
 > Initializing a LabelEncoder for each categorical column.

 > Transforming the categorical columns into numeric format.
 
 > The dataset is then split into features (X) and target (y).

**Splitting the Data**

The dataset is divided into training and testing sets using train_test_split. A test size of 20% is specified to evaluate the model's performance on unseen data. A fixed random_state ensures reproducibility.

**Training a Classification Model**

A RandomForestClassifier is instantiated and trained on the training data (X_train and y_train). 
This involves:
 > Initializing the classifier with a fixed random_state.
 
 > Fitting the model to the training data.

**Evaluating the Model**

The trained model is evaluated on the testing data (X_test and y_test). Key performance metrics such as accuracy, precision, recall, and F1 score are calculated and printed to assess the model's effectiveness.

**Making Predictions with New Data**

New patient data is encoded using the previously fitted LabelEncoder instances. The encoded data is formatted into a DataFrame with the same structure as the training data. The trained model is then used to predict the outcome for this new data. The prediction is decoded back to its original categorical form and printed. This step ensures the model can make accurate predictions on new, unseen data.

The output looks like this:

Prediction 1:

![image](https://github.com/user-attachments/assets/873e595c-8eaa-481c-a371-da8ce9c7caa6)

Prediction 2:

![image](https://github.com/user-attachments/assets/265a4bb2-3666-448d-8189-d21d2fba0a53)

## License

[MIT License](LICENSE)
