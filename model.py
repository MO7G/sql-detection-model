import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Reading the dataset from the provided CSV file
dataset = pd.read_csv("Modified_SQL_Dataset.csv")

# Displaying the first few rows of the dataset for a quick overview
print(dataset.head())

# Preparing the dataset for the model
# 'QueryText' holds the SQL queries and 'QueryLabel' holds their corresponding labels
QueryText = dataset["Query"]
QueryLabel = dataset["Label"]

# Splitting the dataset into training and testing sets
train_text, test_text, train_label, test_label = train_test_split(QueryText, QueryLabel, test_size=0.2, random_state=42)

# Applying TF-IDF transformation to the SQL query texts
tfidf_transformer = TfidfVectorizer()
train_tfidf = tfidf_transformer.fit_transform(train_text)
test_tfidf = tfidf_transformer.transform(test_text)

# Creating and training the Logistic Regression model
sql_injection_detector = LogisticRegression()
sql_injection_detector.fit(train_tfidf, train_label)

# Predicting labels for the test set
predicted_labels = sql_injection_detector.predict(test_tfidf)

# Evaluating the model's performance
model_accuracy = accuracy_score(test_label, predicted_labels)
model_report = classification_report(test_label, predicted_labels)

print(f"Model Accuracy: {model_accuracy}")
print("Detailed Classification Report:\n", model_report)

# Saving the trained model and the TF-IDF transformer for future use
pickle.dump(sql_injection_detector, open("sql_injection_model.pkl", "wb"))
pickle.dump(tfidf_transformer, open("tfidf_transformer.pkl", "wb"))
