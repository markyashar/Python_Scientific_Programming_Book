# For this problem, want to compare evolution of stock prices of 3 giant companies in computer industry:
# Microsoft, Sun Microsystems, & Google. Relevant data files are company_monthly.csv, where company is 
# Microsfot, Sun, or Google.
#
# Data file format: columns are separated by comma, 1st line contains column headings, and lines of data
# (rows) have date in 1st column (1st entry in each line/row) and various measures of stock prices in next
# columns. Our interest concerns final column (final entry in each row; these prices are adusted for splits 
# & dividends).
#
# Task: Plot evolution of stock prices of the 3 companies. It's natural to scale prices to start at unit
# value in January 1988 and let Google price start at max. of Sun & Microsoft stock values in January 2005.
#
# Solution: 2 major parts of problem: (1) reading file, (2) plotting data. Reading part is straightforward,
# while plotting part needs some special consideratons since "x" values in plot are dates & not real numbers.

def read_file(filename):  # Since reading will be repeated for 3 files, make function w/filename as argument.
    infile = open(filename, 'r') # Open the file.
    infile.readline()  # Read column headings. This is the 1st line and is of no interest.
    dates = [];  prices = []  # Result of reading a file should be 2 lists (or arrays) w/dates & stock prices, respectively.
                              # We therefore return these 2 lists from the function. Here, we're simply creating 2 empty 
                              # lists, dates & prices, for collecting the data.
    for line in infile:       # For each line in the rest of the file: 
        columns = line.split(',') # Split the line w.r.t. comma,
        date = columns[0]  # For appending 1st word on line to dates list.
        date = date[:-3]  # Skip day of month. The 1st word, the date, has form year-month-day (e.g., 2008-02-04). Since
                          # we asked for monthly data only, day part is of no interest. Skipping day part can be done by 
                          # extracting substring of date string: date[:-3], which means everything in string except last
                          # 3 characters. Remaining date specification is now of form year-month (e.g., 2008-02), represented
                          # as a string. 
        price = columns[-1]  # For appending last word in line to prices list.
        dates.append(date) # Append 1st word on line to dates list.
        prices.append(float(price))  # Append last word on line to prices list. Note: the words on a line are strings, & at
                                     # least the prices (last word) should be converted to a float.
            
    infile.close()   # Close file.
    dates.reverse()  # The files have the most recent date @ top & oldest @ bottom, while it's natural to plot evolution of
                     # stock prices against increasing time. Therefore, must reverse the 2 lists of data before we return them 
    prices.reverse() # to the calling code.
    return dates, prices

dates = {};  prices = {}   # Instead of working w/separate variables for the file data, we may collect data in dictionaries,
                           # w/company name as key. One possibility is to use 2 dictionaries:
d, p = read_file('stockprices_Sun.csv')
dates['Sun'] = d;  prices['Sun'] = p
d, p = read_file('stockprices_Microsoft.csv')
dates['MS'] = d;  prices['MS'] = p
d, p = read_file('stockprices_Google.csv')
dates['Google'] = d;  prices['Google'] = p

data = {'prices': prices, 'dates': dates}   # Can also collect dates and prices dictionaries in a dictionary data.
                                            # Note: 'data' is a nested dictionary, so that to extract, e.g., prices
                                            # of Microsoft stock, write data['prices']['MS'].

# Normalize prices so that we can easitly compare them.
norm_price = prices['Sun'][0]   # Here we let Sun and Microsoft (below) start out w/unit price and let Google start
prices['Sun'] = [p/norm_price for p in prices['Sun']]  # out w/best of Sun & Microsoft. Normalizing Sun & Microsoft 
                                                       # prices is done by dividing by the first prices.
norm_price = prices['MS'][0]
prices['MS'] = [p/norm_price for p in prices['MS']]

# Normalizing the Google prices is more involved as we need to extract prices of Sun and & Microsoft stocks from
# January 2005. Since 'dates' & 'prices' lists correspond to each other, element by element, can get the index
# corresponding to date '2005-01' in the list of dates and use this index to extract corresponding price. 
# Normalization ca then be coded as
jan05_MS = prices['MS'][dates['MS'].index('2005-01')]
jan05_Sun = prices['Sun'][dates['Sun'].index('2005-01')]
norm_price = prices['Google'][0]/max(jan05_MS, jan05_Sun)
prices['Google'] = [p/norm_price for p in prices['Google']]

# Purpose of final plot is to show how prices evolve in time. Problem is that tine data consists of strings of form
# year-month. Need to convert this string info. to some "x" coordinate info. in plot. 
# Let the "x" values in the plot just be the indices. Simplest strategy is to just plot prices against list index, i.e.,
# "x" coordinates correspond to counting months. Suitable lists of monthly based indices for Sun & Microsoft are 
# straightforward to create w/range function:
x = {}
x['Sun'] = range(len(prices['Sun']))
x['MS']  = range(len(prices['MS']))

# The "x" coordinates for Google prices are somewhat more complicated, because indices must start @ index corresponding 
# to Jan. 2005 in Sun & Microsoft data i.e., for google we must start on the corresponding Sun/MS index
# for January 2005. However, we extracted that index in normalization of Google prices, so we've already done most of
# the work:
jan05 = dates['Sun'].index('2005-01')
x['Google'] = range(jan05, jan05 + len(prices['Google']), 1)

# Final step is to plot 3 sets of data:

# from scitools.std import plot
# plot(x['MS'], prices['MS'], 'r-',
#      x['Sun'], prices['Sun'], 'b-',
#      x['Google'], prices['Google'], 'y-',
#      legend=('Microsoft', 'Sun', 'Google'),
#      savefig='tmp.eps')

from matplotlib.pylab import *
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1)
plt.plot(x['MS'], prices['MS'], 'r-',                                                                                                                                         x['Sun'], prices['Sun'], 'b-',                                                                                                                                    
     x['Google'], prices['Google'], 'y-')                                                                                                                              
ax.legend(['Microsoft', 'Sun', 'Google'],loc='best', fancybox=True, framealpha=0.5)                                                                                                                            
plt.savefig('tmp.eps')
