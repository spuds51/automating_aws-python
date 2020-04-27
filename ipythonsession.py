import boto3
session = boto3.Session(profile_name='raysup')
s3 = session.resource('s3')
