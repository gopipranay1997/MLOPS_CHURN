import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Set path for the input
RAW_DATA_DIR = os.environ["RAW_DATA_DIR"]
RAW_DATA_FILE = os.environ["RAW_DATA_FILE"]
raw_data_path = os.path.join(RAW_DATA_DIR, RAW_DATA_FILE)


#### Read the Dataset #### 
#df = pd.read_csv("D:/UCI_Credit_Card.csv/Churn_Prediction.csv")
df = pd.read_csv(raw_data_path, sep=',')
#### Drop Unwanted Features from the Dataset ####
df.drop(['RowNumber', 'CustomerId', 'Surname'], inplace=True, axis=1)

#### Encoding the Categorical Features ####
# df = pd.get_dummies(df, drop_first=True)

#### Dividing the Dataset into Independent & Dependent Features ####
X = df.drop("Exited", axis=1)
y = df['Exited']

X_continous = X[['CreditScore', 'Age', 'Balance','EstimatedSalary']]
X_categorical = X[["Tenure","NumOfProducts","HasCrCard","IsActiveMember","Geography","Gender"]]

X_encoded = pd.get_dummies(X_categorical, drop_first=True)

X_final = pd.concat([X_continous, X_encoded,y], axis=1)

#### Data Partioning into Training Data & Testing Data(Holdout Method) ####
X_train, X_test = train_test_split(X_final, test_size=0.25, random_state=42)

X_train_continous = X_train[list(X_continous.columns)]
X_test_continous = X_test[list(X_continous.columns)]

#### Normalizing the Data to Set the Data with in the Range  ####
sc = StandardScaler()
X_train_continous_scaled = sc.fit_transform(X_train_continous)
X_test_continous_scaled = sc.transform(X_test_continous)

print(X_train_continous_scaled.shape)
print(X_test_continous_scaled.shape)
X_train_scaled = pd.concat([pd.DataFrame(X_train_continous_scaled).reset_index(drop=True), X_train[list(X_encoded.columns)].reset_index(drop=True),X_train['Exited'].reset_index(drop=True)], axis=1)
X_test_scaled = pd.concat([pd.DataFrame(X_test_continous_scaled).reset_index(drop=True), X_test[list(X_encoded.columns)].reset_index(drop=True),X_test['Exited'].reset_index(drop=True)], axis=1)


# Set path to the outputs
PROCESSED_DATA_DIR = os.environ["PROCESSED_DATA_DIR"]
train_path = os.path.join(PROCESSED_DATA_DIR, 'X_train_scaled.csv')
test_path = os.path.join(PROCESSED_DATA_DIR, 'X_test_scaled.csv')

# Save csv
X_train_scaled.to_csv(train_path, index=False)
X_test_scaled.to_csv(test_path,  index=False)