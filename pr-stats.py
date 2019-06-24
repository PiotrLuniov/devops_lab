from datetime import date, datetime
import requests
import json
import argparse

# Parsing arguments
parser = argparse.ArgumentParser(add_help=True,
                                 description='Get Pull-request statistics from GitHub')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-user', type=str, help='add username')
parser.add_argument('-repo',
                    type=str,
                    default='https://api.github.com/repos/alenaPy/devops_lab/pulls/42',
                    help='add pull url')

args = parser.parse_args()

if not args.user:
    parser.error('Action requested, add -user')

if args.user:
    username = args.user
    repos_url = args.repo

    token = '842d1bcfb91f4083e049f075d966aeca51da065f'

    # Create a re-usable session object with the user creds in-built
    gh_session = requests.Session()
    gh_session.auth = (username, token)

    # Get PR info
    repos = json.loads(gh_session.get(repos_url).text)

    # User who opened
    print('User_opened_PR: ' + repos['user']['login'])

    # Day of the week opened
    cr_date = repos['created_at']
    dt = cr_date[:10]
    year, month, day = (int(x) for x in dt.split('-'))
    date_opened = date(year, month, day)
    DayofWeek = date_opened.strftime('%A')
    print('DayoftheWeek_opened_PR: ' + DayofWeek)

    # NumberofWeek
    Week = date_opened.strftime('%U')
    print('Week_opened_PR: ' + Week)

    # Hour of the day opened
    Hour = cr_date[11:13]
    print('Hour_opened_PR: ' + Hour)

    # Number of days opened
    previous_date = datetime.strptime(dt, '%Y-%m-%d')
    today = datetime.today()
    ndays = (today - previous_date).days
    print('NumberofDays_opened_PR: ' + str(ndays))
