# "We rate dogs" data wrangling project

1. The WeRateDogs Twitter archive. I am giving this file to you, so imagine it as a file on hand. Download this file manually by clicking the following link: [```twitter_archive_enhanced.csv```](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59a4e958_twitter-archive-enhanced/twitter-archive-enhanced.csv)

1. The tweet image predictions, i.e., what breed of dog (or other object, animal, etc.) is present in each tweet according to a neural network. This file (```image_predictions.tsv```) is hosted on Udacity's servers and should be downloaded programmatically using the Requests library and the following [URL](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv).

1. Each tweet's *retweet count* and *favorite ("like") count* at minimum, and any additional data you find interesting. Using the tweet IDs in the WeRateDogs Twitter archive, query the Twitter API for each tweet's JSON data using Python's [Tweepy](http://www.tweepy.org/) library and store each tweet's entire set of JSON data in a file called ```tweet_json.txt``` file. Each tweet's JSON data should be written to its own line. Then read this .txt file line by line into a pandas DataFrame with (at minimum) tweet ID, retweet count, and favorite count.

Note: do not include your Twitter API keys, secrets, and tokens in your project submission.

## Gather Data

Data for this projects originates from 3 sources:

1. A `twitter-archive-enhanced.csv` file, provided by Udacity
1. A `image-predictions.tsv` file, also provided by udacity, but downloaded with python `requests` function.
1. A `tweet_coverage.csv` file, created for this project with a twitter API.

The first hurdle was to download the tab separated file from udacity. It hat do be loaded as
with ```stream=True``` option.

```python
def get_image_predictions():
    """Load image-predictions from disk if present, else load it from udacity.

    WARNING: This only works from within the udacity project workspace!

    """

    if  not os.path.exists('image-predictions.tsv'):
        r = requests.get("https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv",
                         stream=True)
        tsv = r.raw.read()
        with open('image-predictions.tsv', 'wb') as f:
            f.write(tsv)

    df_image_predictions = pd.read_csv('image-predictions.tsv', sep='\t')

    return df_image_predictions
```

To asses the coverage of the "we rete dogs" twitter account another function was written, to
scrape twitter account data:

```python
def get_tweet_coverage():
    """Load tweet_coverage from disk if present, else scrape it from twitter."""

    if  os.path.exists('tweet_coverage.csv'):
        df_tweet_coverage = pd.read_csv('tweet_coverage.csv')
    else:
        consumer_key = os.environ.get("TWITTER_API")
        consumer_secret = os.environ.get("TWITTER_API_SECRET")
        access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
        access_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)
        retweet_count = []
        favorite_count = []
        favorited = []
        retweeted = []

        for index, row in df_twitter_archive.iterrows():
            try:
                tweet_status = api.get_status(row.tweet_id, tweet_mode='extended')._json
                retweet_count.append(tweet_status['retweet_count'])
                favorite_count.append(tweet_status['favorite_count'])
                favorited.append(tweet_status['favorited'])
                retweeted.append(tweet_status['retweeted'])
            except:
                retweet_count.append(np.nan)
                favorite_count.append(np.nan)
                favorited.append(np.nan)
                retweeted.append(np.nan)

            if index % 100 == 0:
                print('Index is %d' % (index))
        print('ready')
        df_tweet_coverage = pd.DataFrame(data = list(zip(df_image_predictions['tweet_id'].values, retweet_count,
                                                         favorite_count, favorited, retweeted)),
                                         columns=['tweet_id', 'retweet_count',
                                                  'favorite_count', 'favorited', 'retweeted'])
        df_tweet_coverage.to_csv('tweet_coverage.csv', index=False)

    return df_tweet_coverage

```

To lower the risk of loosing the Twitter API Keys, I stored my keys in environmental variables,
as suggested in the Twitter [authentication best practices](https://developer.twitter.com/en/docs/basics/authentication/guides/authentication-best-practices).

## Assess Data

### Issues found in the files present

#### Quality

1. In `df_twitter_archive` the **None** values in the columns `doggo`, `floofer`, `pupper` and `puppo` are strings.
1. In `df_twitter_archive` the name column always contains the word after "This is ...", which is not always the dogs name.
1. In `df_twitter_archive` the `retweeted_status_id` is float.
1. In `df_twitter_archive` the `retweeted_status_user_id` is float.
1. In `df_twitter_archive` the `timestamp`  column is of type object.
1. In `df_image_predictions` not all predicted dog breeds are actually dog breeds.
1. In `df_image_predictions` tweed id 762316489655476224 actually is a dog, not a parrot (african grey).
1. In `df_tweet_coverage` retweet_count and favorite_count are float.
1. In `df_tweet_coverage` favorited and retweeted are objects.

#### Tidiness

1. In `df_twitter_archive` the columns doggo, floofer, pupper and puppo always contain "None" or the column name.
1. In `df_twitter_archive` the overall rating is not present, only nominator and denominator.
1. Data is spread around three data frames (tables).

## Clean Data

The following steps were taken to clean the issues found above:

### Quality Enhancement

1. In `df_twitter_archive` the **None** values in the columns `doggo`, `floofer`, `pupper` and `puppo` are strings.

   **Solution:** Change the column type to Boolean, this will also enhance the tidiness. Since according to
   [Dogtionary](https://video.udacity-data.com/topher/2017/October/59e04ceb_dogtionary-combined/dogtionary-combined.png)
   dogs can be "doggo" and "pupper" at the same time, the columns will not be merged to one categoracal column.

1. In `df_twitter_archive` the name column always containts the word after "This is ...", which is not always the dogs name.

   **Solution:** This can only be dealt with manually. Since the dog's name column containts faulty data I will erase it.

1. In `df_twitter_archive` the `retweeted_status_id` is float.

   **Solution:** Convert `retweeted_status_id`  column to int64 and set NaN to 0.

1. In `df_twitter_archive` the `retweeted_status_user_id` is float.

   **Solution:** Convert `retweeted_status_user_id` column to int64 and set NaN to 0.

1. In `df_twitter_archive` the `timestamp` column is of type object.

   **Solution:** Convert `timestamp`  column to datetime.

1. In `df_image_predictions` not all predicted dog breeds are actually dog breeds.

   **Solution:** Erase all rows, that do not contain pictures of dogs (p123_dog == False), with a confidence `p123_conf` of more than 90%.

1. In `df_tweet_coverage` retweet_count and favorite_count are float.

   **Solution:** convert retweet_count and favorite_count to `int64`.

1. In `df_tweet_coverage` favorited and retweeted are objects.

   **Solution:** cast favorited and retweeted to `Bool`.

### Tidiness Cleaning

1. In `df_twitter_archive` the columns doggo, floofer, pupper and puppo always contain "None" or the column name.

   **Solution:** Already taken care of in Quality section (cast to `Boolean`).
1. In `df_twitter_archive` the overall rating is not present, only numerator and denominator.

   **Solution:** Calcuate an overall rating and normalize it to a value between 0 and 1. If the denominator is 0, use 10.
   Drop the numerator and denominator columns afterwards.

1. Data is spread arount three data frames (tables).

   **Solution:** Outer join all data frames with common tweet_id, reassess afterwards.
