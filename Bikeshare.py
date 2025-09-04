import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def switch_assignment (sa_current_state, sa_filtertype):
    """
    Switch Assignment (sa):
    Assigns the state where the loop should return to incase of valid input
    based on the current state and filter type
    Args:
        (str) sa_current_state - current state
        (str) sa_filtertype - filter type
    Returns:
        (str) sa_valid_switch - the state to switch to in case of valid input
    """
# in case current state is Choose City
    if sa_current_state == 'choose_city':
        sa_valid_switch = 'choose_filter'

# in case current state is Choose Filter
    elif sa_current_state == 'choose_filter':
        if  sa_filtertype in ('month', 'both'):
            sa_valid_switch = 'choose_month' # switch to choose_month if filter is month or both
        elif sa_filtertype == 'day':
            sa_valid_switch ='choose_day'    # switch to choose_day if filter is day
        else:
            sa_valid_switch ='end_loop'      # switch to end if filter is none

# in case current state is Choose month
    elif sa_current_state == 'choose_month':
        if sa_filtertype == 'both':          # if filter is both, go choose the day
            sa_valid_switch = 'choose_day'   # switch to choose_day
        else:
            sa_valid_switch = 'end_loop'     # switch to end if filter is month

# in case current state is Choose day
    elif sa_current_state == 'choose_day':
        sa_valid_switch = 'end_loop'

    else:
        sa_valid_switch = 'end_loop'


    return sa_valid_switch


def check_input_validity(civ_userinput, civ_inputslist, civ_invalidmsg, civ_currentstate,
                        civ_filtertype):
    """
    Check Input Validity (civ):
    Checks the user input validity in comparison with the expected inputs
    Args:
        (str) civ_userinput - user input
        (tuple) civ_inputslist - valid/expected inputs  to be compared with user input
        (str) civ_invalidmsg - the msg to be printed whenever the user input is invalid
        (str) civ_currentstate - the current state
        (str) civ_filtertype - filter type
    Returns:
        (str) civ_switch_to - the state to switch to in case of valid input
    """
    if civ_userinput not in civ_inputslist:
        print(civ_invalidmsg)              # print invalid msg
        civ_switch_to = civ_currentstate   # stay in the current state
    else:                                  # incase the input is valid, switch to the next state
        civ_switch_to = switch_assignment(civ_currentstate, civ_filtertype)

    return civ_switch_to


def raw_data (rd_city):
    """
    Raw Data (rd):
    Prints five rows of raw data every time the user enters types

    Args:
        (str) rd_city - name of the city to analyze
    """

    rd_city_df = pd.read_csv(CITY_DATA[rd_city.lower()])    # read data from csv file

    while True:
        rw_input = (input('\nQ: Would you like to see raw data? Enter yes or no.\n\t')).lower()

        if rw_input not in ('yes', 'no'):                   # handle wrong input
            print('\n\tInvalid input data, Please try again...\n\tHint: Please enter yes '\
                  'or no.')
        elif rw_input == 'yes':                             # print raw data
            for rd_iterator in range(0, len(rd_city_df.index), 5):
                rd_raw_data = rd_city_df.iloc[rd_iterator:rd_iterator+5]
                print(rd_raw_data)

                rw_input = (input('\nQ: Would you like to see more? Enter yes or no.\n\t')).lower()
                if rw_input not in ('yes', 'no'):           # handle wrong data
                    print('\n\tInvalid input data, Please try again...\n\tHint: Please enter yes '\
                        'or no.')
                elif rw_input == 'no':                      # break if the answer is no
                    break

            break
        else:                                               # break if the answer is no
            break


def get_filters():
    """
    Get Filters (gf):
    Asks user to specify a city, month, and day to analyze.
    implementing switch case to control the flow, the code will be in one of the following cases:
    #   1- inserting city name : choose_city
    #   2- choosing filter type: choose_filter
    #   3- choosing month: choose_month
    #   4- choosing day: choose_day
    #   5- ending loop after getting the expected inputs: End Loop
    # the initial case is : choose_city

    Returns:
        (str) gf_city - name of the city to analyze
        (str) gf_month - name of the month to filter by, or "all" to apply no month filter
        (str) gf_day - name of the day of week to filter by, or "all" to apply no day filter
        (str) gf_filter_type - filter type
        (bool) gf_user_info_availability - whether the gender & birth year info is available or not
    """
#initialinzing variables
    gf_city = ''
    gf_month = ''
    gf_day = ''

    gf_switch_case = 'choose_city'
    gf_filter_type = 'NA'
    gf_user_info_availability = True

# identifing tuples of valid inputs that the user is expected to use. i.e:used
# to check input data validity to handle unexpected data input
    gf_valid_cities = ('chicago','new york city','washington')
    gf_valid_filters = ('month', 'day', 'both', 'none')
    gf_valid_months = ('jan', 'feb', 'mar','apr', 'may', 'jun')
    gf_valid_days = ('m', 'tu', 'w', 'th', 'f', 'sa', 'su')

# Welcome Message
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:    # implementing while loop to get the correct answers
# _(1)_ switch_case = input_city, get user input for city (chicago, new york or washington)
        if gf_switch_case == 'choose_city':
            gf_city = (input('Q: Would you like to see data for Chicago, New York City, or '\
                        'Washington?\n\t')).lower()
        # check input validity:
            gf_invalid_msg = '\n\tInvalid input data, Please try again...\n\tHint: you '\
                             'can only choose one of those cities \"Chicago, New York '\
                             'City, or Washington!\"\n\n'
            gf_switch_case = check_input_validity(gf_city, gf_valid_cities, gf_invalid_msg,
                                                  'choose_city', gf_filter_type)
            raw_data(gf_city)
# _(2)_ switch_case = choose_filter, get user input for filtering option (month, day, both or none)
        elif gf_switch_case == 'choose_filter':
            gf_filter_type = (input('\nQ: Would you like to filter data by month, day, both, '\
                                    'or no filter at all? If your choice is no filter at all, '\
                                    'Please type None.\n\t')).lower()
        # check input validity:
            gf_invalid_msg = '\n\tInvalid input data, Please try again...\n\tHint: Select one'\
                             'of the filtering options (month, day, both or None)! \n\n'
            gf_switch_case = check_input_validity(gf_filter_type, gf_valid_filters, gf_invalid_msg,
                                               'choose_filter', gf_filter_type)
# _(3)_ switch_case = choose_month, get user input for month (january, february, ... , june)
        elif gf_switch_case =='choose_month':
            gf_month = (input('\nQ: Which month \"Jan, Feb, Mar, Apr, May, Jun\"?\n\t')).lower()
        # check input validity:
            gf_invalid_msg = '\n\tInvalid input data... \n\tHint: Please choose from \"Jan, Feb, '\
                             'Mar, Apr, May, Jun\".\n\n'
            gf_switch_case = check_input_validity(gf_month, gf_valid_months, gf_invalid_msg,
                                                  'choose_month', gf_filter_type)
# _(4)_ switch_case = choose_day, get user input for day "M, Tu, W, Th, F, Sa, Su"
        elif gf_switch_case == 'choose_day':
            gf_day = (input('\nQ: Which day "M, Tu, W, Th, F, Sa, Su"?\n\t')).lower()
        # check input validity:
            gf_invalid_msg = '\n\tInvalid input data... \n\tHint: Please choose one of \"M, Tu, '\
                             'W, Th, F, Sa, Su\".\n\n'
            gf_switch_case = check_input_validity(gf_day, gf_valid_days, gf_invalid_msg,
                                                 'choose_day', gf_filter_type)
# _(5)_ switch_case = end_loop
        else:
            break

    if gf_city == 'washington': # gender and birth year columns are unavailable for washington city
        gf_user_info_availability = False

# returning city, month, day, filter type & user info availablity variables
    print('-'*40)
    return gf_city, gf_month, gf_day, gf_filter_type, gf_user_info_availability


def load_data(ld_city, ld_month, ld_day):
    """
    Load Data (ld):
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) ld_city - name of the city to analyze
        (str) ld_month - name of the month to filter by, or "all" to apply no month filter
        (str) ld_day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        ld_filtered_df - Pandas DataFrame containing city data filtered by month and day
    """
    ld_months_dict = {'jan': 'January', 'feb': 'February', 'mar':'March',
                    'apr':'April', 'may': 'May', 'jun': 'June'}
    ld_days_dict = {'m': 'Monday', 'tu': 'Tuesday', 'w': 'Wednesday',
                 'th': 'Thursday', 'f': 'Friday', 'sa': 'Saturday',
                 'su': 'Sunday'}

    print('Loading data for', ld_city.title(),'...\n\n')
# Reading city csv file
    #city_name =  city.lower().replace(' ','_') + '.csv'
    ld_city_df = pd.read_csv(CITY_DATA[ld_city.lower()])

# convert Start Time and End Time columns into datetime type
    ld_city_df['Start Time'] = pd.to_datetime(ld_city_df['Start Time'])
    ld_city_df['End Time'] = pd.to_datetime(ld_city_df['End Time'])

#filtering data by month, day, both or none
 # filtering by both
    if (ld_month != '') and (ld_day != ''):
        ld_month_df = ld_city_df[ld_city_df['Start Time'].dt.month_name() ==
                      ld_months_dict[ld_month]]
        ld_filtered_df = ld_month_df[ld_month_df['Start Time'].dt.day_name() ==
                         ld_days_dict[ld_day]]
 # filtering by month
    elif ld_month != '':
        ld_filtered_df = ld_city_df[ld_city_df['Start Time'].dt.month_name() ==
                         ld_months_dict[ld_month]]
 # filtering by day
    elif ld_day != '':
        ld_filtered_df = ld_city_df[ld_city_df['Start Time'].dt.day_name() == ld_days_dict[ld_day]]
 # no time filter
    else:
        ld_filtered_df = ld_city_df

    return ld_filtered_df


def stats_and_count (sc_filtered_df, sc_column, sc_stat_type):
    """
    Stats and Count(sc):
    gets the requested stat element in a specified dataframe column and its number of occurence

    Args:
        (dataframe) sc_filtered_df - filtered dataframe
        (str) sc_column - dataframe column
        (str) sc_stat_type - stat type
    Returns:
        (str) sc_element - the most frequent element
        (int) mfc_count- no. of occurence
    """
    if sc_stat_type == 'max':
        sc_element = sc_filtered_df[sc_column].min()                     # get max
        sc_count = sc_filtered_df[sc_column].value_counts()[sc_element]  # count
    elif sc_stat_type == 'min':
        sc_element = sc_filtered_df[sc_column].min()                     # get min
        sc_count = sc_filtered_df[sc_column].value_counts()[sc_element]  # count
    elif sc_stat_type == 'most frequent':
        sc_element = sc_filtered_df[sc_column].mode()[0]  # get the most frequent
        sc_count = sc_filtered_df[sc_column].value_counts()[sc_element]  # count
    elif sc_stat_type == 'sum':
        sc_element = sc_filtered_df[sc_column].sum()                     # get sum
        sc_count = len(sc_filtered_df.index) + 1                         # count

    return sc_element, sc_count


def time_stats(ts_filtered_df, ts_filter_type):
    """
    Time Stats (ts):
    Displays statistics on the most frequent times of travel.

    Args:
        (dataframe) ts_filtered_df - filtered dataframe
        (str) ts_filter_type - filter type
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# _(1)_ display the most common month
    # note: if the data is filtered by (month or both), the frequent month will make no sense
    if ts_filter_type in ('day', 'none'):
    # create new column month
        ts_filtered_df['month'] = ts_filtered_df['Start Time'].dt.month_name()
    # get the most frequent element & display for the user
        ts_most_common_element, ts_its_count = stats_and_count(ts_filtered_df, 'month',
                                                                'most frequent')
        print('- The most common month of the year is "{}" for total number of "{}" trips'.format(
                ts_most_common_element, ts_its_count))
# _(2)_ display the most common day of week
    # note: if the data is filtered by (day or both), the frequent day will make no sense
    if ts_filter_type in ('month','none'):
    # create new column day
        ts_filtered_df['day'] = ts_filtered_df['Start Time'].dt.day_name()
    # get the most frequent element & display for the user
        ts_most_common_element, ts_its_count = stats_and_count(ts_filtered_df, 'day',
                                                                'most frequent')
        print('- The most common day of the week is "{}" for total number of "{}" trips'.format(
                ts_most_common_element, ts_its_count))
# _(3)_ display the most common start hour
 # create new column hour
    ts_filtered_df['hour'] = ts_filtered_df['Start Time'].dt.hour
 # get the most frequent element & display for the user
    ts_most_common_element, ts_its_count = stats_and_count(ts_filtered_df, 'hour', 'most frequent')
    print('- The most common starting hour in the day is "{}" for total number of "{}" trips'.\
            format(ts_most_common_element, ts_its_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(ss_filtered_df):
    """
    Station Stats (ss):
    Displays statistics on the most popular stations and trip.

    Args:
        (dataframe) ss_filtered_df - filtered dataframe
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

 # _(1)_ display most commonly used start station
    ss_most_common_element, ss_its_count = stats_and_count(ss_filtered_df,
                                            'Start Station', 'most frequent')
    print('- The most commonly used Start Station is "{}" for total number of "{}" trips'.format(
            ss_most_common_element, ss_its_count))
 # _(2)_ display most commonly used end station
    ss_most_common_element, ss_its_count = stats_and_count(ss_filtered_df, 'End Station',
                                            'most frequent')
    print('- The most commonly used End Station is "{}" for total number of "{}" trips'.format(
            ss_most_common_element, ss_its_count))
 # _(3)_ display most frequent combination of start station and end station trip
    # create new column Start & end Stations
    ss_filtered_df['Start & End Stations']  = 'from \"' + ss_filtered_df['Start Station'] +\
                                            '\" to \"' + ss_filtered_df['End Station'] +'\"'
    ss_most_common_element, ss_its_count = stats_and_count(ss_filtered_df,
                                            'Start & End Stations', 'most frequent')
    print('- The most frequent combination of start station and end station trip is {} for total'
          ' number of "{}" trips'.format(ss_most_common_element, ss_its_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(tds_filtered_df):
    """
    Trip Duration Stats (tds):
    Displays statistics on the total and average trip duration.

    Args:
        (dataframe) tds_filtered_df - filtered dataframe
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

 # _(1)_ display total travel time
    tds_total_duration, tds_its_count = stats_and_count(tds_filtered_df, 'Trip Duration', 'sum')
    print('- The total travel time is "{}" seconds for total number of "{}" trips'.format(
                tds_total_duration, tds_its_count))

 #_(2)_ display mean travel time
    print('- The mean travel time is {} seconds'.format(tds_filtered_df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(us_filtered_df,us_user_info_availability):
    """
    User Stats (us):
    Displays statistics on bikeshare users.

    Args:
        (dataframe) us_filtered_df - filtered dataframe
        (bool) gf_user_info_availability - whether the gender & birth year info is available or not
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # _(1)_ Display counts of user types
    print('- Counts of user types:\n',us_filtered_df['User Type'].value_counts())

    if us_user_info_availability is True:
    # _(2)_ Display counts of gender
        print('\n- Counts of gender:\n',us_filtered_df['Gender'].value_counts())

    # _(3)_Display earliest, most recent, and most common year of birth
        us_birth_year, us_its_count = stats_and_count(us_filtered_df, 'Birth Year', 'min')
        print('\n- The earliest year of birth is "{}" for "{}" births.'.format(int(us_birth_year),
                us_its_count))
        us_birth_year, us_its_count = stats_and_count(us_filtered_df, 'Birth Year', 'max')
        print('- The most recent year of birth is "{}" for "{}" births.'.format(int(us_birth_year),
                us_its_count))
        us_birth_year, us_its_count = stats_and_count(us_filtered_df, 'Birth Year',
                                      'most frequent')
        print('- The most common year of birth is "{}" for "{}" births.'.format(int(us_birth_year),
                us_its_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    """ Main Function """
    while True:

        city, month, day, filter_type, user_info_availability = get_filters()
        filtered_df = load_data(city, month, day)

        time_stats(filtered_df, filter_type)
        station_stats(filtered_df)
        trip_duration_stats(filtered_df)
        user_stats(filtered_df, user_info_availability)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
