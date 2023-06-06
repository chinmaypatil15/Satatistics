import pandas as pd
from scipy.stats import f_oneway, levene
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load the data
data = pd.read_csv(r'G:\project\Satatistics\data.csv')

# Step 3: Statistical analysis
# a. Check whether the distribution of all the classes is the same or not
class_data = [data[data['class'] == c]['feature'] for c in data['class'].unique()]
statistic, p_value = f_oneway(*class_data)
print("a. p-value for distribution equality:", p_value)

# b. Check for the equality of variance
variance_test_statistic, variance_p_value = levene(*class_data)
print("b. p-value for variance equality:", variance_p_value)

# c. Determine which model (LDA or QDA) would perform better for classification
X_train, X_test, y_train, y_test = train_test_split(data['feature'], data['class'], test_size=0.2, random_state=42)
lda_model = LinearDiscriminantAnalysis()
lda_model.fit(X_train.values.reshape(-1, 1), y_train)
lda_predictions = lda_model.predict(X_test.values.reshape(-1, 1))

qda_model = QuadraticDiscriminantAnalysis()
qda_model.fit(X_train.values.reshape(-1, 1), y_train)
qda_predictions = qda_model.predict(X_test.values.reshape(-1, 1))

lda_accuracy = accuracy_score(y_test, lda_predictions)
qda_accuracy = accuracy_score(y_test, qda_predictions)
print("c. Accuracy of LDA:", lda_accuracy)
print("   Accuracy of QDA:", qda_accuracy)

# d. Check the equality of mean between all the classes
class_means = [class_data[i].mean() for i in range(len(class_data))]
anova_statistic, anova_p_value = f_oneway(*class_data)
print("d. p-value for mean equality:", anova_p_value)
