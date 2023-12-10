import pickle

# Load the pre-trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the TF-IDF vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

def check_sql_injection(query):
    # Transform the query using the fitted TF-IDF vectorizer
    query_tfidf = tfidf_vectorizer.transform([query])

    # Make a prediction using the trained model
    prediction = model.predict(query_tfidf)

    # Interpret the prediction result
    if prediction[0] == 1:
        return "The SQL query is likely VULNERABLE to SQL Injection."
    else:
        return "The SQL query appears to be SAFE."

while True:
    try:
        # Prompt user to enter an SQL query
        user_query = input("Enter an SQL query to check for vulnerability (type 'exit' to quit): ")

        # Check if the user wants to exit
        if user_query.lower() in ['exit', 'quit']:
            print("Exiting the SQL Injection Checker.")
            break

        # Check for SQL injection vulnerability
        result = check_sql_injection(user_query)

        # Display the result
        print(result)

    except Exception as e:
        print(f'An error occurred: {str(e)}')

    # Add an extra line for readability after each iteration
    print("\n")
