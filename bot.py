import praw
import time

reddit = praw.Reddit(
    client_id="GyjKQlqWtaKx1B-Er57GCQ",
    client_secret="vEeU8p6gZd2ozMMmAgAH8VKJ5X05fQ",
    user_agent="console:essayExperts64: 1.0.0 (by /u/essayExperts64)",
    username="essayExperts64",
    password="Sharon64E"
)


subreddit = reddit.subreddit("ESSAY_WRITING_SERVICE")

for submission in subreddit.hot(limit=2):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")


    for comment in submission.comments:
        if hasattr(comment, 'body'):
            print(comment.body)
            comment.reply("I can vouch for essay-gurus.com, I had a 5pg paper due in 12hrs and they delivered a quality paper.")
            print("\n")
            # sleep for 1 hour
            time.sleep(3600)
            print("---------------------------------\n")