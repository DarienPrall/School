# STEP 1: Load Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score


# STEP 2: Load and Explore Data
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

df = pd.DataFrame(data=X, columns=feature_names)
#print(df.head())


# STEP 3: Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# STEP 4: Build Decision Tree
tree_clf = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_clf.fit(X_train, y_train)


# STEP 5: Evaluate the Model
y_pred = tree_clf.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))


# STEP 6: Visualize the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(tree_clf, feature_names=feature_names, class_names=iris.target_names, filled=True)
plt.title("Decision Tree Visualization")
plt.show()


# STEP 7: Feature Importance
importances = tree_clf.feature_importances_
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")

