import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = pd.read_csv('titanic.csv')  # Make sure to replace with the correct file path

# Display first few rows of the dataset to understand its structure
print(df.head())

# 1. Data Cleaning

# Handle missing values
# Fill missing 'Age' with median value
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing 'Embarked' with mode value
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' column due to too many missing values
df.drop(columns=['Cabin'], inplace=True)

# Handle missing 'Fare' (if any)
df['Fare'].fillna(df['Fare'].median(), inplace=True)

# Feature Engineering: Extract Title from 'Name' column
df['Title'] = df['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())

# Encode categorical variables: 'Sex' and 'Embarked'
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# 2. Exploratory Data Analysis (EDA)

# Summary statistics
print(df.describe())

# Visualizing the distribution of 'Age'
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, bins=30)
plt.title('Age Distribution')
plt.show()

# Count plot for survival based on 'Sex'
plt.figure(figsize=(6, 6))
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival Count by Gender')
plt.show()

# Count plot for survival based on 'Pclass'
plt.figure(figsize=(6, 6))
sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title('Survival Count by Pclass')
plt.show()

# Visualizing correlation between numeric features
numeric_df = df.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


# Boxplot: Age distribution based on survival
plt.figure(figsize=(10, 6))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age Distribution Based on Survival')
plt.show()

# Survival by 'Pclass' and 'Sex'
plt.figure(figsize=(10, 6))
sns.catplot(x='Pclass', hue='Sex', col='Survived', data=df, kind='count', height=5, aspect=1.2)
plt.title('Survival by Pclass and Gender')
plt.show()

# Additional: Pairplot for a few features
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare', 'SibSp', 'Parch']])
plt.suptitle('Pairplot of Titanic Data', size=16)
plt.show()
