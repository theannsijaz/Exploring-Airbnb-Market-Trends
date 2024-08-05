# Import necessary packages
import pandas as pd
import numpy as np

def readFile():
    data = pd.read_excel('airbnb_room_type.xlsx')
    return data


def countPrivateRooms(data):
    data['room_type'] = data['room_type'].str.lower()
    private_room_count = 0
    for i in data['room_type']:
        if i == "private room":
            private_room_count = private_room_count+1
    print('Private rooms are: ', private_room_count)
    return private_room_count
    
    
#Question 1

# Load the TSV file containing review data
review_data = pd.read_csv('airbnb_last_review.tsv', sep='\t')

# Ensure the 'last_review' column is in datetime format
review_data['last_review'] = pd.to_datetime(review_data['last_review'])

# Get the earliest and most recent review dates
earliest_review_date = review_data['last_review'].min()
most_recent_review_date = review_data['last_review'].max()

# Print the results
print(f'The earliest review date is {earliest_review_date}')
print(f'The most recent review date is {most_recent_review_date}')



# Question 3
# What is the average listing price? Round to the nearest two decimal places and save into a variable.
data_price = pd.read_csv('airbnb_price.csv')
# Remove ' dollars' and convert to numeric
data_price['price'] = data_price['price'].str.replace(' dollars', '').astype(int)

count = data_price['price'].count()
sum = 0
for i in data_price['price']:
    sum = sum + i
avg_price = (sum/count).round(2)
print('The average listing price rounded to two decimal places is:', avg_price)

    
if __name__ == '__main__':
    data = readFile()
    private_room_count = countPrivateRooms(data)
    
    # Question 4
    review_dates = pd.DataFrame({
        'first_reviewed': [earliest_review_date],
        'last_reviewed': [most_recent_review_date],
        'nb_private_rooms': [private_room_count],
        'avg_price': [avg_price]
    })
    print(review_dates)