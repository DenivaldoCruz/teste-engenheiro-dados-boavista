import os
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'MYACCESSKEYID'
SECRET_KEY = 'MYACCESSKEYSECRET'


def aws_session(region_name='us-east-1'):
    return boto3.session.Session(aws_access_key_id=ACCESS_KEY,
                                 aws_secret_access_key=SECRET_KEY,
                                 region_name=region_name)
#    return boto3.session.Session(region_name=region_name)


def upload_file_to_bucket(local_file, bucket_name, s3_file):
    session = aws_session()
    s3_resource = session.resource('s3')

    bucket = s3_resource.Bucket(bucket_name)
    bucket.upload_file(
      Filename=local_file,
      Key=s3_file
    )

    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_file}"
    print("File", local_file, "uploaded successfully")
    return s3_url


if __name__ == '__main__':

    bucket_name = 'teste-engenheiro-dados-boavista'

    s3_url = upload_file_to_bucket('comp_boss.csv', bucket_name, 'comp-boss/comp_boss.csv')
    print(s3_url)

    s3_url = upload_file_to_bucket('bill_of_materials.csv', bucket_name, 'bill-of-materials/bill_of_materials.csv')
    print(s3_url)

    s3_url = upload_file_to_bucket('price_quote.csv', bucket_name, 'price-quote/price_quote.csv')
    print(s3_url)