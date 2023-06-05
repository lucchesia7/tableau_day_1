# Imports
import pandas as pd

# Create wrangle function
def wrangle(filepath):
    # Pre-exploration: only returning a dataframe object
    return pd.read_csv(filepath)


def wrangle(filepath):
    # Post exploration: Any necessary edits
    df = pd.read_csv(filepath)
    
    # Change the fare column to be rounded to two decimal places:
    df['Fare'] = round(df['Fare'], 2)
    
    # Fill null values in the age column with a zero
    df['Age'].fillna(0.00, inplace=True)
    
    # Cast the age column as an int type
    df['Age'] = df['Age'].astype(int)
    
    # Renaming all columns in the dataframe to match snake casing
    df.rename(columns={
    'PassengerId': 'passenger_id',
    'Survived':'survived',
    'Pclass': 'p_class',
    'Name': 'name',
    'Sex': 'gender',
    'Age': 'age',
    'SibSp': 'siblings_or_spouse_aboard',
    'Parch': "parents_or_child_aboard",
    'Ticket':'ticket',
    'Fare': 'fare',
    'Cabin': 'cabin',
    'Embarked':'embarked'
    }, inplace=True)
    
    # Drop the ticket column:
    df = df.drop(columns=['ticket'])
    
    # Return dataframe object
    return df

if __name__ == '__main__':
    df = wrangle(r'C:\Users\Alex Lucchesi\OneDrive\Desktop\tableau_teaching_day_1\train.csv')
    df.to_csv('titanic_cleaned.csv', index=False)