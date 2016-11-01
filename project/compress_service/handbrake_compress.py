import os
import time 
import subprocess 
import sys

class Compressor:
    
    def __init__(self):
        self.file_type_list = ['.avi','.divx','.flv','.m4v','.mkv','.mov','.mpg','.wmv']
        self.files_list = []

    def get_all_files(file_dir_name=None):
        for root,subfolders,files in os.walk(file_dir_name):
            for file in files:
                one_file = os.path.join(root,file)
                file_name, file_extension = os.path.splitext(one_file)
                if file_extension.lower() in self.file_type_list:
                    print "Adding file to the list ->",the_file
                    self.files_list.append(the_file)
                    
           
    def start_handbreak_compression(self):
        while(self.files_list):
            input_file = self.files_list.pop()
            file_name, file_extension = os.path.splitext(input_file)
            output_file = file_name+'.mp4'
            print "Processng input file"
            return_code = subprocess.call(runsr.format(input_file,output_file))
            time.sleep(5)


    
    
