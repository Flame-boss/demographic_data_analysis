import pandas as pd

# Load the dataset into a DataFrame
data = pd.read_csv(r"F:\V\a code work place\data analysis\demograghic\adult.data.csv")  # Replace "your_dataset.csv" with the actual file path

# Question 1: How many people of each race are represented in this dataset?
race_counts = data['race'].value_counts()

# Question 2: What is the average age of men?
average_age_men = data[data['sex'] == 'Male']['age'].mean()

# Question 3: What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (data['education'] == 'Bachelors').mean() * 100

# Question 4: What percentage of people with advanced education make more than 50K?
higher_education = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_high_earning_education = (data[higher_education]['salary'] == '>50K').mean() * 100

# Question 5: What percentage of people without advanced education make more than 50K?
lower_education = higher_education
percentage_low_earning_education = (data[lower_education]['salary'] == '>50K').mean() * 100

# Question 6: What is the minimum number of hours a person works per week?
min_work_hours = data['hours-per-week'].min()

# Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = len(data[data['hours-per-week'] == min_work_hours])
percentage_min_workers_earning_50K = (len(data[(data['hours-per-week'] == min_work_hours) & (data['salary'] == '>50K')]) / num_min_workers) * 100

# Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
highest_earning_country = (data[data['salary'] == '>50K']['native-country'].value_counts() / data['native-country'].value_counts()).idxmax()
highest_earning_percentage = (data[data['native-country'] == highest_earning_country]['salary'] == '>50K').mean() * 100

# Question 9: Identify the most popular occupation for those who earn >50K in India.
indian_occupation_stats = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
most_popular_occupation_india = indian_occupation_stats['occupation'].mode()[0]
def calculate_demographic_data(print_data=False):
    return {
        'average_age_men': average_age_men,
        'higher_education': higher_education,
    }
# Round all decimals to the nearest tenth
average_age_men = round(average_age_men, 1)
percentage_bachelors = round(percentage_bachelors, 1)
percentage_high_earning_education = round(percentage_high_earning_education, 1)
percentage_low_earning_education = round(percentage_low_earning_education, 1)
percentage_min_workers_earning_50K = round(percentage_min_workers_earning_50K, 1)
highest_earning_percentage = round(highest_earning_percentage, 1)
print_data= ('print_data')
# Printing the result
if print_data:
        print("Number of each race:\n", race_counts) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education }%")
        print(f"Percentage without higher education that earn >50K: {lower_education}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_percentage}%")
        print("Top occupations in India:", most_popular_occupation_india)
