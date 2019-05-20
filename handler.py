import os, boto3, json

NEGATIVE_COMMENT_MESSAGE="Your comment is too negative to post, please edit it."
POSITIVE_COMMENT_MESSAGE="Your comment looks great. Keep up the good work!"

client = boto3.client('comprehend')

def sentimentAnalysis(event, context):
    
    inputTranscriptData = event['queryStringParameters']['inputTranscript']
    print(inputTranscriptData);
    
    sentiment=client.detect_sentiment(Text=inputTranscriptData,LanguageCode='en')['Sentiment']
    if sentiment=='NEGATIVE':
        return {
            "statusCode": 200,
            "body": json.dumps(NEGATIVE_COMMENT_MESSAGE)
        }
    else:
        return {
            "statusCode": 200,
            "body": json.dumps(POSITIVE_COMMENT_MESSAGE)
        }
