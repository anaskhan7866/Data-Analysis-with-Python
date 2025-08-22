import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv(r"C:\Users\annus\OneDrive\Desktop\data analyst\Freecodecamp\adult.csv")


    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    min_work_hours = df['hours-per-week'].min()

    rich_percentage = round((df[(df['hours-per-week'] == min_work_hours)]['salary'] == '>50K').mean() * 100, 1)

    highest_earning_country = ((df[df['salary'] == '>50K']['native-country']
                               .value_counts(normalize=True) * 100)).idxmax()
    highest_earning_country_percentage = round(((df[df['salary'] == '>50K']['native-country']
                                .value_counts(normalize=True) * 100)).max(), 1)

    top_IN_occupation = (df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
                        ['occupation'].value_counts().idxmax())

    result = {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    if print_data:
        for key, value in result.items():
            print(f"{key}: {value}")

    return result
    return result

if __name__ == "__main__":
    calculate_demographic_data(print_data=True)
