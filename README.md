# PRODIGY_DS_02
Task 2 - Data Science internship at Prodigy InfoTech 
Data Cleaning and Exploratory Data Analysis (EDA) on Titanic Dataset
Task Overview
In this task, I performed data cleaning and exploratory data analysis (EDA) on the Titanic dataset. The main goal was to clean the data, handle missing values, and explore the relationships between different features to identify patterns and trends in the dataset.

Dataset
The dataset used for this task is the Titanic dataset, which contains information about passengers on the Titanic, such as their age, gender, class, and survival status.

Dataset URL: Titanic Dataset

Key Steps Performed
1. Data Cleaning
Handling Missing Values:

The missing values in the Age column were filled with the median value of the column.
The missing values in the Embarked column were filled with the most frequent value (mode).
The Cabin column, which had too many missing values, was dropped from the dataset.
The missing values in the Fare column were filled with the median value.
Feature Engineering:

A new feature, Title, was extracted from the Name column to identify the title of each passenger (e.g., Mr, Mrs, etc.).
Categorical Encoding:

The Sex column was mapped to numeric values (0 for male, 1 for female).
The Embarked column was also encoded as numeric values (C = 0, Q = 1, S = 2).
2. Exploratory Data Analysis (EDA)
Summary Statistics: Used describe() to get the basic statistics of numerical columns.

Visualizations:

Age Distribution: Created a histogram to visualize the distribution of passengers' ages.
Survival by Gender: Created a count plot to show the number of survivors based on gender.
Survival by Class: Visualized the survival count for each passenger class using a count plot.
Correlation Heatmap: Generated a heatmap to explore the correlation between numerical features.
Boxplot of Age vs Survival: Visualized how age affected survival.
Exploring Relationships: Used various plots to explore how different factors (such as Pclass, Sex, Age) relate to survival.

Libraries Used
pandas for data manipulation
matplotlib and seaborn for data visualization
Conclusion
The analysis helped to uncover several trends in the data, such as:

Women had a higher survival rate compared to men.
Passengers in the first class had a higher survival rate than those in second and third class.
Age distribution also showed that younger passengers had a higher chance of survival.

