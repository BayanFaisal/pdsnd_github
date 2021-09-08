import datetime,  time
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
   
    cities = ("chicago", "new york city", "washington")
        
    while True:
        try:
            city = input('Would you like to see data for chicago, washington or new york city for your analysis.\n').lower()
            if city in cities:
                print(city)
                break
            else:
                print('That\'s not a vaild input, please try again')  
        except ValueError:
            prit('Error input')
 
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ("all", "january", "february", "march", "april", "may", "june")
    while True:
        try:
            month = input('Which month you would like to choose -all, january, february, march, april, may, or june?. \n').lower()
            if month in months:
                print(month)
                break    
            else:
                print('That\'s not a vaild input, please try again')  
        except ValueError:
            prit('Error input')    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    while True:
        try:
           day = input('Which day of the week you would like to choose - all, monday, tuesday, ... sunday?\n').lower() 
           if day in days:
               print(day)
               break
           else:
            print('That\'s not a vaild input, please try again')
        except ValueError:
            prit('Error input')    
        
            
    print('-'*40)
    return city, month, day

                
        

def load_data(city, month, day):
                
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:popular_day = df['day'].mode()[0]


        df - Pandas DataFrame containing city data filtered by month and day
        
    """  
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


    df = pd.read_csv(CITY_DATA[city])
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['hour'] = df['Start Time'].dt.hour 
    
    df['month'] = df['Start Time'].dt.month
    
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    if month != "all":
        months =  ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df.loc[df['month'] == month] 
    
    
    if day != 'all':
       df = df.loc[df['day_of_week'] == day.title()]  
        
    return df

def display_raw_data(df):
    #asks user whether would he like to see the raw data or not.
    i = 0
    raw = input("Would you like to see the raw data?, please select yes or no.\n").lower()
        
    pd.set_option('display.max_columns',200)
        
    while True:
        if raw == "no":
            break
        elif raw == "yes":
            print(df[ : 10])
                
            raw = input(" Would you like to see 10 more  rows  of the data?, please select yes or no.\n").lower()  
            i = +10
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month_name()
                
   
                
    popular_month = df['month'].mode()[0]

    print('The most common month: ', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    
    popular_day = df['day'].mode()[0]

    print('The most common day of week: ', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
                
                
    popular_hour = df['hour'].mode()[0]
                
    print('The most common start hour: ', popular_hour)            

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_Start_Station = df['Start Station'].mode()[0]

    print('The most commonly used start station: \n',popular_Start_Station)

    # TO DO: display most commonly used end station
    popular_End_Station = df['End Station'].mode()[0]

    print('The most commonly used end station: \n', popular_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    
    fr_start_st_end_st = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending = False).head(1)
    print('The most frequent combination of start station and end station trip: \n', fr_start_st_end_st)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time: ', total_travel_time, 'seconds')
    
    total_travel_time1 = df['Trip Duration'].sum()
    
    result = datetime.timedelta(seconds = float(total_travel_time1))
    print('total_travel_time: ', result, "\n")
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean().round(2)
    print('mean travel time: ', mean_travel_time, 'seconds')
    
    mean_travel_time1 = df['Trip Duration'].mean().round(2)
    
    result1 = datetime.timedelta(seconds = mean_travel_time1)
    print('mean travel time: ', result1, "\n")
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('counts user types: ', user_types_counts)
    # TO DO: Display counts of gender
    if city != 'washington':
        gender_counts = df['Gender'].value_counts()
        print('counts of gender: ', gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
        most_recent_year_of_birth = df['Birth Year'].max()
        print('most recent common year of birth: ', int(most_recent_year_of_birth))
    
        earliest_year_of_birth = df['Birth Year'].min()
        print('earliest common year of birth: ', int(earliest_year_of_birth))
    
        most_common_year_of_birth = df['Birth Year'].mode()
        print('most common year of birth: ', int(most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break
            
        else:
            print('That\'s not a vaild input, please try again')

if __name__ == "__main__":
    main()
    
