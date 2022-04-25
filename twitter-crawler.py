import os
from twython import Twython


class Crawler():

    def __init__(self):
        self.twitter_api = None
        self.api_key = os.environ['API_KEY']
        self.api_secret = os.environ['API_SECRET']
        self.access_token = os.environ['ACCESS_TOKEN']
        self.access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

    def authenticate(self):
        """Authenticate application with Twython."""
        success = False
        try:
            self.twitter_api = Twython(self.api_key, self.api_secret, self.access_token, self.access_token_secret)
            print("Authentication was successful!")
            success = True
        except Exception:
            raise
        finally:
            return success

    def search(self, search_params):
        results = None
        try:
            results = self.twitter_api.search(q=search_params, result_type='recent', count=100, lang='en')
        except Exception as e:
            raise Exception('Error while searching for tweets: {}'.format(str(e)))
        finally:
            return results['statuses']

    def main(self):

        search_params = "#zeroday OR #0day OR #zero-day OR #0-day -filter:retweets AND -filter:replies"

        self.authenticate()
        results = self.search(search_params=search_params)
        for r in results:
            if "new".lower() in r['text'] or "discovered".lower() in r['text']:
                print(r)


crawler = Crawler()
crawler.main()

