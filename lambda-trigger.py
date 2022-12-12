import json
import boto3
from io import BytesIO
import zipfile

def lambda_handler(event, context):
    # TODO implement
    
    s3_resource = boto3.resource('s3')
    source_bucket = 'zip-s3'
    target_bucket = 'filter-s3'
    type_folder = 'other'
    Images = ['.ai','.bmp' , '.gif' , '.ico' , '.jpeg' , '.jpg' , '.png' , '.ps' , '.psd' , '.svg' , '.tif' , '.tiff']
    
    

    my_bucket = s3_resource.Bucket(source_bucket)

    for file in my_bucket.objects.all():
        if(str(file.key).endswith('.zip')):
            zip_obj = s3_resource.Object(bucket_name=source_bucket, key=file.key)
            buffer = BytesIO(zip_obj.get()["Body"].read())
            
            z = zipfile.ZipFile(buffer)
            
            for filename in z.namelist():
                flag = 1
                for type in Images:
                    if filename.endswith(type):
                        type_folder = type
                        flag=0
                
                if flag !=0:    
                    type_folder = 'not image'                
                    
                file_info = z.getinfo(filename)
                try:
                    response = s3_resource.meta.client.upload_fileobj(
                        z.open(filename),
                        Bucket=target_bucket,
                        Key=type_folder + '/{}'.format(filename)
                    )
                except Exception as e:
                    print(e)
        else:
            print(file.key+ ' is not a zip file.')
