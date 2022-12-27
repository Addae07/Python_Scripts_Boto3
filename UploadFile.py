import boto3

#how to upload single file
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="Fi13523X0AIHJQe.png",
    Bucket="wlawrence-bucket-test-boto3",
    Key="uploadtest.png")
    
    #how to upload multiple files
#import os
#import glob

#cwd=os.getcwd()

#cwd=cwd+"/upload/"

#files=glob.glob(cwd+"*.png")

#files


#for file in files:
#    s3_resource=boto3.client("s3")
 #   s3_resource.upload_file(
 #   Filename=file,
 #   Bucket="wlawrence-bucket-test-boto3",
  #  Key=file.split("/")[-1])