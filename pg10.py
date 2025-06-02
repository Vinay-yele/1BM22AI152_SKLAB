from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# 1. Generate a simple dataset
X, y = make_classification(n_samples=100, n_features=2, n_informative=2,
                           n_redundant=0, random_state=1)

# 2. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Define individual models
model1 = LogisticRegression()
model2 = DecisionTreeClassifier()
model3 = KNeighborsClassifier()

# 4. Create Ensemble using Voting Classifier
ensemble = VotingClassifier(estimators=[
    ('lr', model1),
    ('dt', model2),
    ('knn', model3)
], voting='hard')  # Use 'soft' for probabilities

# 5. Train models
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
model3.fit(X_train, y_train)
ensemble.fit(X_train, y_train)

# 6. Predict using individual models and ensemble
pred1 = model1.predict(X_test)
pred2 = model2.predict(X_test)
pred3 = model3.predict(X_test)
pred_ens = ensemble.predict(X_test)

# 7. Display accuracy
print("Accuracy of Logistic Regression:", accuracy_score(y_test, pred1))
print("Accuracy of Decision Tree      :", accuracy_score(y_test, pred2))
print("Accuracy of KNN                :", accuracy_score(y_test, pred3))
print("Accuracy of Ensemble Model     :", accuracy_score(y_test, pred_ens))

# 8. Display sample predictions
print("\nSample Predictions (first 5 test points):")
print("LR  :", pred1[:5])
print("DT  :", pred2[:5])
print("KNN :", pred3[:5])
print("Ensemble:", pred_ens[:5])
