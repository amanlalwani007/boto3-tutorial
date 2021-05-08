import  logging
import boto3

def create_bucket(bucket_name, region=None):
    '''if region is  not specified then s3 will create bucket in the default region(us-east-1)'''
    try:
        if region is None:
            s3_client=boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client= boto3.client('s3',region_name =region)
            location={'LocationConstraint':region}
            s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    except Exception as e:
        logging.error(e)
        return True

def list_existing_buckets():
    s3=boto3.client('s3')
    response=s3.list_buckets()
    print("Existing Buckets")
    for bucket in response['Buckets']:
        print(bucket["Name"])

def uploading_files (file_name,bucket,object_name=None):
    if object_name is None:
        object_name= file_name
    s3_client=boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(file_name,bucket,object_name)
    except Exception as e:
        logging.error(e)
        return False
    return True

    ''' Add ExtraArgs Parameter
     s3.upload_file(file_name,bucket_name,object_name,
     ExtraArgs={'MetaData':{'mykey':'myavalue'}}
     )
     
     The following extraargs settings assigns  ACL (access control list) value 'public-read' to the s3 
     object
     
     s3.upload_file(
     file_name,bucket_name,object_name
     ExtraArgs={'ACL':'public-read'}
     )
     
     s3.upload_file(
     file_name,bucket_name,object_name
     ExtraArgs={'GrantRead':'',
     'GrantFullControl':'id'}
     )
     
     
     
     '''




def download_file():
    s3=boto3.client('s3')
    with open("aman_1.jpeg","wb") as f:
        s3.download_fileobj('bucketuploadfile','aman.jpeg',f)

if __name__ == '__main__':
    #create_bucket("bucketuploadfile","ap-south-1")
    list_existing_buckets()
    # with open("aman.jpeg","rb") as f:
    #     uploading_files(f,"bucketuploadfile","aman.jpeg")
    download_file()









