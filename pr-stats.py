from datetime import date, datetime
import requests
import argparse

# Parsing arguments
parser = argparse.ArgumentParser(add_help=True,
                                 description='Get Pull-request statistics from GitHub')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

parser.add_argument('-o', '--owner', help="owner of repository", type=str, default="alenaPy")
parser.add_argument('-r', '--repo', help="name of repository", type=str, default="devops_lab")
parser.add_argument('-p', '--pull', help="name of pull request", type=int, default=42)

parser.add_argument('-t', '--token', help="add token for access", type=str)

parser.add_argument('--all', help="output all available parameters", action="store_true")

parser.add_argument('-uo', help='output username,who opened pull request', action="store_true")
parser.add_argument('-dw', help='output day of week,when opened pull request', action="store_true")
parser.add_argument('-ho', help='output hour,when opened pull request', action="store_true")
parser.add_argument('-wo', help='output week,when opened pull request', action="store_true")
parser.add_argument('-do', help='output quantity of days,when opened pull request',
                    action="store_true")

args = parser.parse_args()

repos_url = "https://api.github.com/repos/" + args.owner + "/" + args.repo + "/pulls/" \
            + str(args.pull)
token = args.token

# Create request
headers = {'Authorization': 'token ' + token}
repos = requests.get(repos_url, headers=headers).json()

# Get info about creation_PR
cr_date = repos['created_at']
dt = cr_date[:10]
year, month, day = (int(x) for x in dt.split('-'))
date_opened = date(year, month, day)

# Get necessary info
UserName = repos['user']['login']
DayofWeek = date_opened.strftime('%A')
Week = date_opened.strftime('%U')
Hour = cr_date[11:13]

# Get NumberofDays_opened_PR
previous_date = datetime.strptime(dt, '%Y-%m-%d')
today = datetime.today()
Ndays = str((today - previous_date).days)

if not args.token:
    parser.error('Action requested, add --token')

if args.all or args.uo:
    print('User_opened_PR: ' + UserName)

if args.all or args.dw:
    print('DayoftheWeek_opened_PR: ' + DayofWeek)

if args.all or args.wo:
    print('Week_opened_PR: ' + Week)

if args.all or args.ho:
    print('Hour_opened_PR: ' + Hour)

if args.all or args.do:
    print('NumberofDays_opened_PR: ' + Ndays)
