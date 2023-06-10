import pandas as pd

# define categories
categories = {
    'Category A': ['keyword1', 'Best', 'keyword3'],
    'Category B': ['keyword4', 'better', 'keyword6'],
    'Category C': ['love', 'keyword8', 'keyword9']
}

def perform_sorting(filename):
    # load data into a Pandas DataFrame
    data = pd.read_csv(filename)

    # create a new column to store the category
    data['Category'] = ''

    # loop through each row in the DataFrame
    for index, row in data.iterrows():
        # check each category for keywords
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in row['Description']:
                    data.loc[index, 'Category'] = category
                    break

    # return the sorted data as a list of dictionaries
    return data.to_dict(orient='records')
