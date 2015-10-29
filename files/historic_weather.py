import urllib
url = 'http://www.metoffice.gov.uk/climate/uk/stationdata/oxforddata.txt'
local_file = 'Oxford.txt'
urllib.urlretrieve(url, filename=local_file)

infile = open(local_file, 'r')
data = {}
data['place'] = infile.readline().strip()
data['location'] = infile.readline().strip()
# Skip the next 5 lines
for i in range(5):
    infile.readline()

data['data'] ={}
for line in infile:
    columns = line.split()

    year = int(columns[0])
    month = int(columns[1])

    if columns[-1] == 'Provisional':
        del columns[-1]
    for i in range(2, len(columns)):
        if columns[i] == '---':
            columns[i] = None
        elif columns[i][-1] == '*' or columns[i][-1] == '#':
            # Strip off trailing character
            columns[i] = float(columns[i][:-1])
        else:
            columns[i] = float(columns[i])

    tmax, tmin, air_frost, rain, sun = columns[2:]

    if not year in data['data']:
        data['data'][year] = {}
    data['data'][year][month] = {'tmax': tmax,
                                 'tmin': tmin,
                                 'air frost': air_frost,
                                 'sun': sun}
infile.close()
# pick a an item to verify that temps is correct:
# 2006   2    6.6     0.8      12    33.0    73.1
year = 2006; month = 2
print data['data'][year][month]

import pprint
# pprint.pprint(data)

# Here, we extract a 2-D array of number of sun hours in a month (these data are available from year 1929):  
sun = [[data['data'][y][m]['sun'] for m in range(1,13)] \
       for y in range(1929, 2010)]
pprint.pprint(sun)

"""
OUTPUT:

bash-3.2$ python historic_weather.py  | more
{'sun': 73.1, 'tmax': 6.6, 'air frost': 12.0, 'tmin': 0.8}
[[43.8,
  60.5,
  190.2,
  144.7,
  240.9,
  210.3,
  219.7,
  176.3,
  199.1,
  109.2,
  78.7,
  67.0],
 [49.9,
  54.3,
  109.7,
  102.0,
  134.5,
  211.2,
  174.1,
  207.5,
  108.2,
  113.5,
  68.7,
  23.3],
 [63.7,
  72.0,
  142.3,
  93.5,
  150.1,
  158.7,
  127.9,
  135.5,
  92.3,
  102.5,
  62.4,
  38.5],
 [51.0,
  57.9,
  133.4,
  110.9,
  112.4,
  199.3,
  124.0,
  178.3,
  102.1,
  100.7,
  55.7,
  58.0],
 [69.5,
  94.3,
  187.6,
  152.5,
  170.2,
  226.9,
  237.6,
  242.7,
  177.3,
  101.3,
  53.9,
  59.0],
 [65.9,
  96.6,
.
.
.
"""

    


