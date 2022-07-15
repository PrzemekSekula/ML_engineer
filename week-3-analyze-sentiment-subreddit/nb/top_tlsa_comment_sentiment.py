
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Tensorflow errors only

#import secrets
import yaml

import argparse
import random
from typing import Dict, List

from praw import Reddit
from praw.models.reddit.subreddit import Subreddit
from praw.models import MoreComments

from transformers import pipeline


def parse_args():
    parser=argparse.ArgumentParser(description="Setiment analysis script")
    parser.add_argument("-c", "--credentials", default='../credentials/secrets_reddit.yaml',
                        help="yaml with credentials")
    args=parser.parse_args()
    return args

def get_subreddit(display_name:str, credentials_file:str) -> Subreddit:
    """Get subreddit object from display name

    Args:
        display_name (str): [description]

    Returns:
        Subreddit: [description]
    """
    with open(credentials_file, "r") as f:
        credentials = yaml.safe_load(f)    
        reddit = Reddit(
            client_id=credentials['REDDIT']['REDDIT_API_CLIENT_ID'],        
            client_secret=credentials['REDDIT']['REDDIT_API_CLIENT_SECRET'],
            user_agent=credentials['REDDIT']['REDDIT_API_USER_AGENT']
        )
    
    subreddit = reddit.subreddit(display_name=display_name)
    return subreddit


def get_comments(subreddit:Subreddit, limit:int=3) -> List[str]:
    """ Get comments from subreddit

    Args:
        subreddit (Subreddit): [description]
        limit (int, optional): [description]. Defaults to 3.

    Returns:
        List[str]: List of comments
    """
    top_comments = []
    for submission in subreddit.top(limit=limit):
        #for top_level_comment in submission.comments:
        #    if isinstance(top_level_comment, MoreComments):
        #        continue
        #    top_comments.append(top_level_comment.body)
        top_comments += [x.body for x in submission.comments if not isinstance(x, MoreComments)]
    return top_comments

def run_sentiment_analysis(comment:str) -> Dict:
    """Run sentiment analysis on comment using default distilbert model
    
    Args:
        comment (str): [description]
        
    Returns:
        str: Sentiment analysis result
    """
    sentiment_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
    sentiment = sentiment_model(comment)
    return sentiment[0]



if __name__ == '__main__':
    args = parse_args()
    subreddit = get_subreddit('tsla', credentials_file=args.credentials)
    comments = get_comments(subreddit)
    comment = random.choice(comments)
    sentiment = run_sentiment_analysis(comment)
    
    print(f'The comment: {comment}')
    print(f'Predicted Label is {sentiment["label"]} and the score is {sentiment["score"]:.3f}')
