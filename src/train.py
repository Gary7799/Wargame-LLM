import os
import pandas as pd
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer

# 文件夹路径
folder_path = 'D:\\Replays'

# 初始化空列表存储数据
data = []

# 遍历文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('summary.txt'):
            file_path = os.path.join(root, file)
            # 文件名（路径）作为标签
            label = os.path.basename(os.path.dirname(file_path))
            # print(label)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read().strip()
                data.append({'label': label, 'text': text})

# 将数据转换为DataFrame
df = pd.DataFrame(data)
# print(df.head())
# print(df.describe())

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = [word for word in text.split() if word not in ENGLISH_STOP_WORDS]
    return ' '.join(words)

# 应用预处理
df['text'] = df['text'].apply(preprocess_text)
# print(df.describe())
# print(df.head())
#
vectorizer = TfidfVectorizer()
# vectorizer = CountVectorizer()

X = vectorizer.fit_transform(df['text'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# #逻辑回归
# model = LogisticRegression(max_iter=1000)

model = SVC(kernel='linear')

# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=100)

# from sklearn.ensemble import GradientBoostingClassifier
# model = GradientBoostingClassifier(n_estimators=100)
model.fit(X_train, y_train)
#
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
# report = classification_report(y_test, y_pred)
from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
#

# print(report)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# from sklearn.model_selection import learning_curve
#
# train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5)
#
# plt.figure()
# plt.plot(train_sizes, train_scores.mean(axis=1), label='Training score')
# plt.plot(train_sizes, test_scores.mean(axis=1), label='Cross-validation score')
# plt.xlabel('Training Size')
# plt.ylabel('Score')
# plt.title('Learning Curve')
# plt.legend(loc='best')
# plt.show()

# from sklearn.model_selection import GridSearchCV
#
# param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
#
# grid_search = GridSearchCV(SVC(), param_grid, cv=5)
# grid_search.fit(X_train, y_train)
#
# print(f'Best Parameters: {grid_search.best_params_}')
# print(f'Best Cross-Validation Score: {grid_search.best_score_}')

# import numpy as np
#
#
# models = ['Logistic Regression', 'SVM', 'Random Forest', 'Gradient Boosting']
# accuracies = [0.49, 0.52, 0.39, 0.47]
# precisions = [0.49, 0.60, 0.44, 0.47]
# recalls = [0.49, 0.52, 0.39, 0.47]
# f1_scores = [0.46, 0.50, 0.37, 0.46]
#
# x = np.arange(len(models))
# width = 0.1
#
# fig, ax = plt.subplots(figsize=(16, 8))
# rects1 = ax.bar(x - width, accuracies, width, label='Accuracy')
# rects2 = ax.bar(x, precisions, width, label='Precision')
# rects3 = ax.bar(x + width, recalls, width, label='Recall')
# rects4 = ax.bar(x + 2*width, f1_scores, width, label='F1 Score')
#
# ax.set_xlabel('Models')
# ax.set_ylabel('Scores')
# ax.set_title('Performance Comparison of Different Models')
# ax.set_xticks(x)
# ax.set_xticklabels(models)
# ax.legend()
#
# fig.tight_layout()
# plt.show()