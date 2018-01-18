import argparse
import datetime
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# parser for arguments  
parser = argparse.ArgumentParser()
parser.add_argument('--month', help='month for the comic')
parser.add_argument('--day', help='day for the comic')
parser.add_argument('--year', help='year for the comic')

args = parser.parse_args()

date = datetime.datetime.now()

# handles empty args
month = args.month if args.month else date.month
day = args.day if args.day else date.day
year = args.year if args.year else date.year

# parse the initial page
commitstrip = 'http://www.commitstrip.com/en/{}/{}/{}'.format(year, month, day)
page = urlopen(commitstrip)
soup = BeautifulSoup(page, 'html.parser')

# parse the comic page
entry = soup.find('div', class_='excerpt').section.a['href']
e_page = urlopen(entry)
e_soup = BeautifulSoup(e_page, 'html.parser')

# download the image
img_url = e_soup.find('div', class_='entry-content').p.img['src']
urlretrieve(img_url, '{}-{}-{}.jpg'.format(year, month, day))