import boto3

s3_resource=boto3.client("s3")

objects=s3_resource.list_objects(Bucket="wlawrence-bucket-test-boto3")["Contents"]

len(objects)

if len(objects)>0:
    print("objects exits")
    
    for object in objects:
     print(object["Key"])