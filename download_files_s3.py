import boto3
from botocore.session import Session
import sagemaker
import argparse

# def get_images_from_s3():
#     session = sagemaker.Session()

def main(folder):
    session = Session()
    s3 = session.create_client('s3')

    sess = sagemaker.Session()
    bucket_name = 'adxtinct-test'
    prefix = f'images/{folder}/'

    res = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    # print(res)
    for _ in res['Contents']:
        key = _['Key']
        print(key)
        sess.download_data('TestImages/', bucket=bucket_name, key_prefix=key)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str)
    args = parser.parse_args()
    main(args.folder)