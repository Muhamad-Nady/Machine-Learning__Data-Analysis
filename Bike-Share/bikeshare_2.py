import time
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('cities: ', CITY_DATA.keys())
    while True:
        city = input('please input city you want data about:').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('pls enter one of above cities', CITY_DATA.keys())
            pass

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    print('months: ', months )
    while True:
        month = input('for any month you need to retrieve data: ').lower()
        if month in months:
            break
        else:
            print('pls enter one of above months', months)
            pass    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('days: ', days)
    while True:
        day = input("please enter your day:").lower()
        if day in days:
            break
        else:
            print('pls enter a one of above days', days)
            pass
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
    # Load the data 
    df = pd.read_csv(CITY_DATA[city])
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Create new columns
    df['month'] = df['Start Time'].dt.month    
    df['day of week'] = df['Start Time'].dt.day_name()    
    df['hour'] = df['Start Time'].dt.hour
    
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    if month != 'all':
        df = df[df['month'] == months.index(month)]
    #days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day != 'all':
        df = df[df['day of week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    print('Most commen month: ', df['month'].mode()[0])
    # display the most common day of week
    print('Most commen dat_of_week: ', df['day of week'].mode()[0])
    # display the most common start hour
    print('Most commen hour: ', df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station is: ",most_start_station)
    # display most commonly used end station
    most_end_station =  df['End Station'].value_counts().idxmax()
    print("The most commonly used start station is: ",most_end_station)

    # display most frequent combination of start station and end station trip
    most_combination =  (df['Start Station'] + " , " + df['End Station']).value_counts().idxmax()
    print("The most frequent combination of start station and end station trip is : ", most_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time in seconds is: ", df['Trip Duration'].sum())

    # display mean travel time
    print("average travel time in seconds is: ", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print("User type numbers: ", df['User Type'].value_counts())
    except KeyError:
        print('\nNo data avialable about user type')
    # Display counts of gender
    try:
        print("Gender counts: ", df['Gender'].value_counts())
    except KeyError:
        print("\nNo data avialable about gender")

    # Display earliest, most recent, and most common year of birth
    try:   
        print("The earliest year of birth is:  ", df['Birth Year'].min())
        print("The recent year of bith is:  ", df['Birth Year'].max())
        print("The most common year of bithis:  ", df['Birth Year'].mode())
    except KeyError:
        print('\nNO data avialable about the year of birth')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_rows(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == 'yes'):
        end_loc = start_loc + 5
        try:
            print(df.iloc[start_loc:end_loc])
        except KeyError:
            print("\nYou get to the end of data")
        start_loc += 5
        view_display = input("Do you wish to continue?:").lower()
        if view_display != 'yes':
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_rows(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
