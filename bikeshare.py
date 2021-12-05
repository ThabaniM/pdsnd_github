import time
import re
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    print('Hello! Let\'s explore some US bikeshare data!')

 
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ''
    
    while(city not in CITY_DATA):
        city = input('Please type the city/cities you want to look at').lower()
        if city in CITY_DATA:
            break
    
    month = ''
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
                  'august', 'september', 'october', 'november', 'december', 'all']
   
    # TO DO: get user input for month (all, january, february, ... , june)  
    while(month not in months):
        month = input('Please enter the month(s) you are interested in').lower()
        if month in months:
            break
    
    day = ''
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    
    while(day not in days_of_week):
        day = input('Please enter the day(s) you are interested in').lower()
        if day in days_of_week:
            break
        
      

    if city == '' or month == ''  or day == '':
        raise Exception('There is at least one missing value please try again')
    elif re.findall('\d', city) != [] or re.findall('\d', month) != []  or re.findall('\d', day) != []:
        raise Exception('A number value was entered, please enter values in words')
        
    
    
      
                    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])
    print(df.head())
    return df

def display_data(df):
    """display df after code runs initially"""
    #template for code below from a review from one of udacity's reviewers"""

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    end_loc = 5
    while (view_data == 'yes' ):
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == 'no':
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    readable_start_time = time.ctime(start_time)
    print(readable_start_time, start_time)
   
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    # TO DO: display the most common month
    # extract month from the Start Time column to create a month column
    
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    
  
    print(popular_month, ' NB print statement worked')
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    popular_day = df['month'].mode()[0]
    # TO DO: display the most common start hour
    # find the most common hour (from 0 to 23)no
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(df.head())    
    print('Most Frequent Start Hour:', popular_hour)

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)
          
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " " + df['End Station']
    popular_combined_station = df['Trip'].mode()[0]
    print('Most Popular Trip:', popular_combined_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time, 'seconds')
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('Number of User for Each Type:', count_user_types, '\n', sep='\n')
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_gender = df['Gender'].value_counts()
        print('Gender count:', count_gender, sep='\n')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest Birth:', df['Birth Year'].min())
        print('Most Recent:', df['Birth Year'].max())
        print('Most Common:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
