from boto.s3.connection import S3Connection
from filechunkio import FileChunkIO
#from server_config import *
import time 
from datetime import datetime
from boto.s3.key import Key 
import os
import math

AWS_ACCESS_KEY_ID = 'AKIAJSPWAOYFMZJNQFZA'
AWS_SECRET_ACCESS_KEY = '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'

DEFAULT_S3_UPLOAD_FILENAME ='ugmeant'
SOURCE_STORAGE_DIR = '/home/harish/Downloads/'
S3_BUCKET = 'https://s3-us-west-1.amazonaws.com/augmeant'
#S3_UPLOAD_CHUNK_SIZE = 52428800
S3_UPLOAD_CHUNK_SIZE = 524880



class AugmeantS3:
    
    def __init__(self):
        # Get s3 connection handle 
        try:
            self.conn = S3Connection(AWS_ACCESS_KEY_ID,
                                AWS_SECRET_ACCESS_KEY)
        except Exception,e:
            print "Sorry could not get s3 connection handle in s3 utils"

    def get_current_date_time(self):
        current_date_time = None
        try:
            current_date_time = str(datetime.now())+str(int(time.time()))
        except Exception,e:
            print "Could not get current date time",str(e)
        return current_date_time

    def create_s3_file(self,source_storage_dir=SOURCE_STORAGE_DIR,
                        S3_BUCKET='augmeant',filename='augmeant'):
        current_date_time = self.get_current_date_time()
        upload_file_name = DEFAULT_S3_UPLOAD_FILENAME + current_date_time
        source_file = source_storage_dir + filename
        bucket_name = self.conn.get_bucket(S3_BUCKET,validate=False)
        source_size = os.stat(source_file).st_size
        chunk_size = S3_UPLOAD_CHUNK_SIZE 
        source_path = S3_BUCKET
        mp = bucket_name.initiate_multipart_upload(os.path.basename(source_file))
        chunk_count = int(math.ceil(source_size/float(chunk_size)))
        for i in range(chunk_count):
            offset = chunk_size * i 
            print "progress of upload ",offset
            bytes = min(chunk_size, source_size - offset)
            with FileChunkIO(source_file,'r',
                            offset=offset,bytes=bytes) as fp:
                mp.upload_part_from_file(fp,part_num=i+1)
        mp.complete_upload()





if __name__ =='__main__':
    aug_obj = AugmeantS3()
    aug_obj.create_s3_file(filename='augmeant.mp4')