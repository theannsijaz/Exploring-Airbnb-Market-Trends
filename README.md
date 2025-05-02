# Airbnb Data Analysis

I have collected Airbnb listing data from various sources to investigate the short-term rental market in New York. This project involves analyzing this data to provide insights on private rooms to the real estate company.

There are three files in the data folder: `airbnb_price.csv`, `airbnb_room_type.xlsx`, `airbnb_last_review.tsv`.

In this project, I will:

1. **Determine Review Dates:** Identify the dates of the earliest and most recent reviews and store these values as two separate variables.
2. **Count Private Rooms:** Count how many of the listings are private rooms and save the result into a variable.
3. **Calculate Average Listing Price:** Calculate the average listing price, rounded to the nearest two decimal places, and save it into a variable.
4. **Create a Summary DataFrame:** Combine the above variables into one DataFrame called `review_dates` with four columns in the following order: `first_reviewed`, `last_reviewed`, `nb_private_rooms`, and `avg_price`. The DataFrame will contain only one row of values.

## Project Files

- **`airbnb_room_type.xlsx`**: Excel file containing data on the types of rooms available in Airbnb listings.
- **`airbnb_last_review.tsv`**: TSV file that includes the last review dates for Airbnb listings.
- **`airbnb_price.csv`**: CSV file containing the price information for the listings.

## Installation

To run this project, you need to have Python installed along with the necessary packages:

- `pandas`
- `numpy`

You can install these packages using pip:

```bash
pip install pandas numpy
