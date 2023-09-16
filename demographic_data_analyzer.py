import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mask = df['sex'] == 'Male' 
    average_age_men = round(df[mask].age.mean())

    # What is the percentage of people who have a Bachelor's degree?
    mask = df['education'] == 'Bachelors'  
    percentage_bachelors = (df[mask].education.value_counts() / len(df))*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
  
    #mask for higher education
    pattern = 'Bachelors|Masters|Doctorate'
    mask_hi = (df['education'].str.contains(pattern, case=False, na=False)) & df['salary'].str.contains('>50K')
    mask_hi2 = df['education'].str.contains(pattern, case=False, na=False)
    #mask for lower education
    mask_lo = (df["education"].str.contains(pattern)==False) & df['salary'].str.contains('>50K')
    mask_lo2 = df["education"].str.contains(pattern)==False
  
    higher_education = (len(df[mask_hi].education) / len(df[mask_hi2]))*100
    lower_education = (len(df[mask_lo].education) / len(df[mask_lo2]))*100

    # percentage with salary >50K
    higher_education_rich = (len(df[mask_hi].education) / len(df[mask_hi2]))*100
    lower_education_rich = (len(df[mask_lo].education) / len(df[mask_lo2]))*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df['hours-per-week'] == 1 #total works who work min hours per week
    mask = (df['hours-per-week'] == 1) & (df['salary']).str.contains('>50K')

    rich_percentage = (len(df[mask])/ len(df[num_min_workers].race))*100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts()/ df['native-country'].value_counts() * 100).idxmax()
    highest_earning_country_percentage = round(len(df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')]) / len(df[(df['native-country'] == highest_earning_country)])*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask = (df['native-country'].str.contains('India')) & (df['salary']).str.contains('>50K')

    top_IN_occupation = df[mask].occupation.value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
