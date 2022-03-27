import praw
reddit = praw.Reddit(
    client_id="aCsxA497160GjRop_8DDXA",
    client_secret="rAuMc2mxJPwLMsX4xYqNrpg5ifa7ig",
    user_agent="reddit bot for udemy course",
    username="DistinctCap2574",
    password="this is the password",
    check_for_async=False
)

import random
import time
def karma():#Comments on every single post on Karma4U
  try:
    messages-["Upvoted,upvote in return?","GreatPost,care to share the upvotes"]#Create variety in comments
    for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions():#Stream submission
        submission.upvote()#Upvoting the submission
        print(submission.title)
        rand=random.randit(0,(len(messages)-1))
        submission.reply(messages[rand])
        time.sleep(30)#To prevent rate limitation
  except:
    time.sleep(300)
    karma()
karma()
  
#Karma Creation
