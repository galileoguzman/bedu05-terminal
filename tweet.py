from datetime import datetime

class Tweet():
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.created_at = datetime.now()
        self.retweets_counter = 0

    def __str__(self):
        return f'{self.author}`s tweet.'

    def date_friendly(self):
        print(f'{self.created_at.month} {self.created_at.day}')

    def retweet(self):
        self.retweets_counter = self.retweets_counter + 1

mariela_tweet = Tweet(
    '@MarielaJZenteno',
    'Estoy aprendiendo python en @bedu con @galileoguzman')
print(mariela_tweet.retweets_counter)
print(mariela_tweet.created_at)

mariela_tweet.retweet()
mariela_tweet.retweet()
mariela_tweet.retweet()
mariela_tweet.retweet()

print(mariela_tweet.retweets_counter)
print(mariela_tweet.created_at)
