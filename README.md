# 🚲 Explore US BikeShare Data

_This project is part of the Udacity Programming for Data Science with Python Nanodegree.
It explores U.S. bike share data from three cities: Chicago, New York City, and Washington._

_This project provides insights into how people use bike share systems in major U.S. cities 
through a simple and interactive Python-based analysis tool._

_The program is an interactive command-line application that lets users:_
- Choose a city and filter data by month, day, both, or view all data.
- View raw data in increments of 5 rows upon request.
- Explore key statistics about bike share usage, including:
- Most common travel times (month, day, hour).
- Most popular stations and trip combinations.
- Trip duration statistics (total and average).
- User demographics such as type, gender, and birth year (if available).

#### 🛠️ Tools & Libraries Used

- Python 3
- Libraries: pandas, numpy, time

#### 📑 Dataset Description

_The datasets used in this project were provided by Motivate, a bike share system provider in the U.S.
Each file (chicago.csv, new_york_city.csv, washington.csv) contains data for the first six months of 2017._

**📊 Dataset Columns**

- **Start Time**	When the trip started (datetime)
- **End Time**	When the trip ended (datetime)
- **Trip Duration**	Total travel time in seconds
- **Start Station**	Name of the starting station
- **End Station**	Name of the ending station
- **User Type**	Subscriber (member) or Customer (casual rider)
- **Gender (Chicago & NYC only)**	Gender of the rider
- **Birth Year (Chicago & NYC only)**	Year of birth of the rider

_Note: The Washington dataset does not include Gender or Birth Year information._

#### 🖥️ Sample Output

_Example run for Chicago with no filters:_

```
Hello! Let's explore some US bikeshare data!
Q: Would you like to see data for Chicago, New York City, or Washington?
        chicago

Q: Would you like to see raw data? Enter yes or no.
        yes
   Unnamed: 0           Start Time             End Time  Trip Duration                  Start Station                   End Station   User Type  Gender  Birth Year
0     1423854  2017-06-23 15:09:32  2017-06-23 15:14:53            321           Wood St & Hubbard St       Damen Ave & Chicago Ave  Subscriber    Male      1992.0
1      955915  2017-05-25 18:19:03  2017-05-25 18:45:53           1610            Theater on the Lake  Sheffield Ave & Waveland Ave  Subscriber  Female      1992.0
2        9031  2017-01-04 08:27:49  2017-01-04 08:34:45            416             May St & Taylor St           Wood St & Taylor St  Subscriber    Male      1981.0
3      304487  2017-03-06 13:49:38  2017-03-06 13:55:28            350  Christiana Ave & Lawrence Ave  St. Louis Ave & Balmoral Ave  Subscriber    Male      1986.0
4       45207  2017-01-17 14:53:07  2017-01-17 15:02:01            534         Clark St & Randolph St  Desplaines St & Jackson Blvd  Subscriber    Male      1975.0

Q: Would you like to see more? Enter yes or no.
        no

Q: Would you like to filter data by month, day, both, or no filter at all? If your choice is no filter at all, Please type None.
        none
----------------------------------------
Loading data for Chicago ...



Calculating The Most Frequent Times of Travel...

- The most common month of the year is "June" for total number of "98081" trips
- The most common day of the week is "Tuesday" for total number of "45912" trips
- The most common starting hour in the day is "17" for total number of "35992" trips

This took 0.23455190658569336 seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...

- The most commonly used Start Station is "Streeter Dr & Grand Ave" for total number of "6911" trips
- The most commonly used End Station is "Streeter Dr & Grand Ave" for total number of "7512" trips
- The most frequent combination of start station and end station trip is from "Lake Shore Dr & Monroe St" to "Streeter Dr & Grand Ave" for total number of "854" trips

This took 0.28517723083496094 seconds.
----------------------------------------

Calculating Trip Duration...

- The total travel time is "280871787" seconds for total number of "300001" trips
- The mean travel time is 936.23929 seconds

This took 0.0011610984802246094 seconds.
----------------------------------------

Calculating User Stats...

- Counts of user types:
 User Type
Subscriber    238889
Customer       61110
Dependent          1
Name: count, dtype: int64

- Counts of gender:
 Gender
Male      181190
Female     57758
Name: count, dtype: int64

- The earliest year of birth is "1899" for "14" births.
- The most recent year of birth is "1899" for "14" births.
- The most common year of birth is "1989" for "14666" births.

This took 0.06603050231933594 seconds.
----------------------------------------

Would you like to restart? Enter yes or no.
no



