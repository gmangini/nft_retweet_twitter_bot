import tweepy

FILE_NAME = "last_seen.txt"
userName = "bullgirlfriends"
query = "there will be a raffle to mint her"

consumer_key = 'ZYkkR51cHVGSbLEtKYICad5Pp'
consumer_secret = 'lXxbPbKc4iYYAJPL78SpWlRZ2naPXUAmdSksL4o48EVwN3fEL2'
key = '1450568581490511873-EPpQJxMTE2XISwEYTE6wOuAtWrhGbX'
secret = 'dNiFaIgYUjf7Qrw9vD5aohUA1TQi2AGqQreIj3GRdAa6S'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

def get_user_id_by_username(user):
    user = api.get_user(screen_name = user)
    return user.id

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def write_last_tweet(FILE_NAME, tweet_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(tweet_id))
    file_write.close()
    return

def lambda_handler(event, context):
    user_id = get_user_id_by_username(userName)
    last_tweet = read_last_seen(FILE_NAME)
    tweets = api.user_timeline(user_id = user_id, count = 500, since_id = last_tweet)
    for tweet in tweets:
        if query in tweet.text.lower():
            api.retweet(id = tweet.id)
            write_last_tweet(FILE_NAME, tweet.id)

    return print('done')

lambda_handler()