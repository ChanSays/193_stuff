# setup boto3

import boto3

import uuid

from pathlib import Path
import os
home = str(Path.home())
folder = home+"/environment/trainA"
os.chdir(folder)



def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])
    
def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name
    
def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response
    
def runDel(bucket_name,file_name):
    s3_resource.Object(bucket_name, file_name).delete()
    #first_object = s3_resource.Object(bucket_name=first_bucket_name, key=pic)
    #first_object.upload_file(pic)
    

# s3_resource.create_bucket(Bucket=YOUR_BUCKET_NAME,CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})


s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

first_bucket_name, first_response = create_bucket(bucket_prefix='firstpythonbucket', s3_connection=s3_resource.meta.client)

first_bucket = s3_resource.Bucket(name=first_bucket_name)



    
    # upload imgs
    # download imgs
    # upload folder
    # download folder
    



# open all files in folder
# from pathlib import Path
#pathlist = Path(directory_in_str).glob('**/*.asm')

pathlist = Path(os.getcwd()).glob('**/*.jpg')


upflag=True
if upflag is True:
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        pic = str(path)
        print('UPLOADING: '+str(path))
        
        first_object = s3_resource.Object(bucket_name=first_bucket_name, key=pic)
        first_object.upload_file(pic)


    # first_file_name = pic
    # first_object_again = first_bucket.Object(pic)
    # s3_resource.Bucket(first_bucket_name).upload_file(Filename=first_file_name, Key=first_file_name)
    # s3_resource.meta.client.upload_file(Filename=first_file_name, Bucket=first_bucket_name,Key=first_file_name)
    # first_object.upload_file(first_file_name)
    # s3_resource.Object(first_bucket_name, first_file_name).upload_file(Filename=first_file_name)
    

delflag=False

val = input("DELETING??(y/n): ") 

if val is 'y':
    for path in pathlist:
        pic = str(path)
        print('DELETING: '+str(path))
        runDel(first_bucket_name,pic)
