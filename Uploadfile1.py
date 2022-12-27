import boto3

#how to upload single file
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="TimeOfYear.jpeg",
    Bucket="wlawrence-bucket-test-boto3",
    Key="uploadtest.jpeg")
    