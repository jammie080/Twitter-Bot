from os.path import join, dirname,os
from dotenv import load_dotenv,find_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TWITTER_STUFF = os.environ.copy()
TWITTER_STUFF["TWITTER_USERNAME"] 
TWITTER_STUFF["TWITTER_PASSWORD"]

twitter = {
    'files': {
        'twitter-users':'\\output\\scraped.txt',
        'follow-users':'\\output\\follow.txt',
        'dont-follow-users':'\\output\\dont-follow.txt'
    },
    'auth': {
        'twitter':{

            'username': '%s' % TWITTER_STUFF["TWITTER_USERNAME"],
            'password': '%s' % TWITTER_STUFF["TWITTER_PASSWORD"]

        }

        
    },
        'url':{
            'home':'https://www.twitter.com/login'
        }    

}
