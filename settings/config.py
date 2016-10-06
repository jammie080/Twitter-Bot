from os.path import join, dirname,os
from dotenv import load_dotenv,find_dotenv

try:
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    os.system('cls')
    TWITTER_USERNAME = os.environ.get('')
    TWITTER_PASSWORD = os.environ.get('')
except:
    os.system('cls')
    TWITTER_USERNAME = ''
    TWITTER_PASSWORD = ''

twitter = {
    'files': {
        'twitter-users':'\\output\\scraped.txt',
        'follow-users':'\\output\\follow.txt',
        'dont-follow-users':'\\output\\dont-follow.txt'
    },
    'auth': {
        'twitter':{

            'username': '%s' % TWITTER_USERNAME,
            'password': '%s' % TWITTER_PASSWORD

        }

        
    },
        'url':{
            'home':'https://www.twitter.com/login'
        }    

}
