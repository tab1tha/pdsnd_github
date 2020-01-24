import time
import pandas as pd

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
    cities = ('chicago', 'new york city', 'washington')
    while True:
        try:
            city = (input("Would you like to investigate Chicago, New York City or Washington?:")).lower().strip()
            if city not in cities:
                raise Exception('Please choose one of the suggested cities')
        except :
            print('Please try again with more valid input, you might have misspelt a word')
        else:
            break
                

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        try:
            month = (input("Valid months exist from January to June.\nWhich month should I filter by?(say 'all' for no filter):")).lower().strip()
            if month not in months:
                raise Exception('Please choose a valid month')
        except :
            print('Please try again with more valid input, you might have misspelt a word')
        else:
            break 
            
                  
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        try:
            day = (input("What day of the week should I filter by? (say 'all' for no filter):")).lower().strip()
            if day not in days:
                raise Exception('Please choose a valid day of the week')
            break
        except :
            print('Please try again with more valid input, you might have misspelt a word')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month       #returns a number
    df['day_of_week'] = df['Start Time'].dt.weekday_name  #returns a string
    df['hour'] = df['Start Time'].dt.hour
    #filter by month
    if month != 'all':
        months = ('january', 'february', 'march', 'april', 'may', 'june')
        month = months.index(month) + 1
        df = df[df['month'] == month]
    #filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe month with the highest occurence is', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nThe weekday with the most travel is', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('\nThe most common start hour of travel is', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\n',df['Start Station'].mode()[0],'is the most popular start station among bikers')

    # TO DO: display most commonly used end station
    print('\nThe most common end station is ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nIn total, {} hours were spent in travel'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('\nOn average, {} hours were spent in travel'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nUser types and their respective frequencies:', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('\nThe gender distribution of bikers is\n ', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
 
        print('\nThe earliest year of birth is', df['Birth Year'].min())
        print('\nThe most recent year of birth is ', df['Birth Year'].max())
        print('\nThe most common year of birth is', df['Birth Year'].mode()[0])
    except:
        print('The Gender and Birth Year columns are not available for this city')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_five(city):
    '''Reads data in chunks of 5 lines on request by the user. '''
    with open(CITY_DATA[city]) as f:
                chunk = pd.read_csv(f, chunksize=5)
    while True:
        view = (input('Would you like to view 5 lines of the raw data?')).lower().strip()
        if view != 'no':
            print(next(chunk))
        else:
            break
     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_five(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
