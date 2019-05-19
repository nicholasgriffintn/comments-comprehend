import os, boto3

NEGATIVE_COMMENT_MESSAGE="Your comment is too negative to post, please edit it."
POSITIVE_COMMENT_MESSAGE="Your comment looks great. Keep up the good work!"

client = boto3.client('comprehend')

def lambda_handler(event, context):
    sentiment=client.detect_sentiment(Text=event['inputTranscript'],LanguageCode='en')['Sentiment']
    if sentiment=='NEGATIVE':
        return NEGATIVE_COMMENT_MESSAGE;
    else:
        return POSITIVE_COMMENT_MESSAGE;