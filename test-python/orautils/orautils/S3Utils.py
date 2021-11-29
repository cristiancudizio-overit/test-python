#https://towardsdatascience.com/stop-using-print-to-debug-in-python-use-icecream-instead-79e17b963fcc

import subprocess
import shutil
import sys
import getopt
import os
from datetime import datetime, date, time
import cx_Oracle
import getpass
from . import connectionfactory
import boto3 
import logging
from botocore.exceptions import ClientError
"""
copy file to S3 bucket rds-overit-dumps
"""
def upload_file(argv):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    v_filename =''
    v_bucket = ''
    v_targetfilename = ''
    v_tenant = 'overit-prod-001'
    opts, args = getopt.getopt(argv,"hf:b:t:n:",["help","filename=","bucket=","targetfilename=","tenant="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print('')
         print(sys.argv[0]+' -f filename -b bucket -t targetfilename -n tenant ')
         sys.exit()
      elif opt in ("-f", "--filename"):
          if arg!='':
              v_filename = arg
      elif opt in ("-b", "--bucket"):
          if arg!='':
              v_bucket = arg
      elif opt in ("-t", "--targetfilename"):
          if arg!='':
              v_targetfilename = arg
      elif opt in ("-n", "--tenant"):
          if arg!='':
              v_tenant = arg
    if v_targetfilename == '':
              v_targetfilename = os.path.basename(v_filename)              
    session = boto3.Session(profile_name=v_tenant)
    s3_client = session.client('s3')
    #copy_source for copy between buckets
    #copy_source = {
    #    'Bucket': v_bucket,
    #    'Key': v_filename
    #}
    print(v_targetfilename)
    response = s3_client.upload_file(v_filename, v_bucket, v_targetfilename)
    print("Response: ", response)
    # test copy from one bucket to another (different account different region, see security policy)
    #q= s3_client.copy(copy_source, 'test-pg-lambda', 'otherkey.dpdmp')

def copy_file(argv):
    """copy file from one bucket to another

    """
    v_filename =''
    v_sourcebucket = ''
    v_targetbucket = ''
    v_destfilename = ''
    v_tenant = 'overit-prod-001'
    v_destregion = 'eu-west-1'
    opts, args = getopt.getopt(argv,"hf:s:t:n:d:r:",["help","filename=","sourcebucket=","targetbucket=","tenant=","destfilename=","region="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -f filename -s sourcebucket -t targetbucket  -d destfilename -r destregion -n tenant ')
         sys.exit()
      elif opt in ("-f", "--filename"):
          if arg!='':
              v_filename = arg
      elif opt in ("-s", "--sourcebucket"):
          if arg!='':
              v_sourcebucket = arg
      elif opt in ("-t", "--targetbucket"):
          if arg!='':
              v_targetbucket = arg
      elif opt in ("-n", "--tenant"):
          if arg!='':
              v_tenant = arg
      elif opt in ("-d", "--destfilename"):
          if arg!='':
              v_destfilename = arg
      elif opt in ("-r", "--region"):
          if arg!='':
              v_destregion = arg
    if v_destfilename == '':
              v_destfilename = os.path.basename(v_filename)              
    session = boto3.Session(profile_name=v_tenant, region_name=v_destregion)
    s3_client = session.client('s3')
    #copy_source for copy between buckets
    copy_source = {
        'Bucket': v_sourcebucket,
        'Key': v_filename
    }
    print(v_destfilename)
    #response = s3_client.upload_file(v_filename, v_bucket, v_targetfilename)
    #print("Response: ", response)
    # test copy from one bucket to another (different account different region, see security policy)
    q= s3_client.copy(copy_source, v_targetbucket, v_destfilename,
                      ExtraArgs={'MetadataDirective': 'REPLACE'})
    print(q)


def copyFromRDSToS3(argv):
    v_dbtarget = 'geoctest'
    v_file_name = 'xxxxx'
    v_destbucket = 'rds-overit-dumps'
    #h argument without parameter, i: parameter with argument, o: parameter with argumenti
    #ifile longoptions
    opts, args = getopt.getopt(argv,"hd:f:b:",["help","dbtarget=","filename=","bucket="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print('copy file from RDS to S3') 
         print(sys.argv[0]+' -d dbtarget -f file_name  [-b bucket] defaults to rds-overit-dumps')
         sys.exit()
      elif opt in ("-d", "--dbtarget"):
          if arg!='':
              v_dbtarget = arg
      elif opt in ("-f", "--filename"):
          if arg!='':
              v_file_name = arg
      elif opt in ("-b", "--bucket"):
          if arg!='':
              v_destbucket = arg
    conn = connectionfactory.getdbconnection(v_dbtarget)
    v_query = """
    SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(
        p_s3_prefix => null,
        p_prefix => :p_file_name,
        p_bucket_name    =>  :p_destbucket,
        p_directory_name =>  'DATA_PUMP_DIR')
        AS TASK_ID FROM DUAL
    """
    v_data = {"p_file_name": v_file_name, "p_destbucket": v_destbucket}
    #v_query = v_query.replace(':p_file_name',v_file_name)
    print(v_query)
    v_risposta = input('file name: '+v_file_name+' target db:'+connectionfactory.getDBConnectionString(v_dbtarget)+ ' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    cur = conn.cursor()
    cur.execute(v_query, v_data)
    result = cur.fetchall()
    v_num_rows = cur.rowcount
    v_num_cols = len(cur.description)
    v_description_length = len(cur.description)
    for i in range(v_description_length):
        #print(curUtil.description[i][0])
        pass
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_col_value = result[i][j]
            print("{0:30}:{1}".format(cur.description[j][0], v_col_value))
            #print(curUtil.description[j][0], v_col_value)
    print("Run SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','dbtask-"+v_col_value+".log')); ")
    cur.close()
    conn.close()

def copyFromS3ToRDS(argv):
    v_dbtarget = 'geoctest'
    v_file_name = 'xxxxx'
    v_bucket = 'rds-overit-dumps'
    #h argument without parameter, i: parameter with argument, o: parameter with argumenti
    #ifile longoptions
    opts, args = getopt.getopt(argv,"hd:f:b:",["help","dbtarget=","filename=","bucket="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbtarget -f file_name  [-b bucket] defaults to rds-overit-dumps')
         sys.exit()
      elif opt in ("-d", "--dbtarget"):
          if arg!='':
              v_dbtarget = arg
      elif opt in ("-f", "--filename"):
          if arg!='':
              v_file_name = arg
      elif opt in ("-b", "--bucket"):
          if arg!='':
              v_bucket = arg
    conn = connectionfactory.getdbconnection(v_dbtarget)
    v_query = """
    SELECT rdsadmin.rdsadmin_s3_tasks.download_from_s3(
        p_s3_prefix => :p_file_name,
        p_bucket_name    =>  :p_bucket,
        p_directory_name =>  'DATA_PUMP_DIR')
        AS TASK_ID FROM DUAL
    """
    v_data = {"p_file_name": v_file_name, "p_bucket": v_bucket}
    #v_query = v_query.replace(':p_file_name',v_file_name)
    print(v_query)
    v_risposta = input('file name: '+v_file_name+' target db:'+connectionfactory.getDBConnectionString(v_dbtarget)+ ' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    cur = conn.cursor()
    cur.execute(v_query, v_data)
    result = cur.fetchall()
    v_num_rows = cur.rowcount
    v_num_cols = len(cur.description)
    v_description_length = len(cur.description)
    for i in range(v_description_length):
        #print(curUtil.description[i][0])
        pass
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_col_value = result[i][j]
            print("{0:30}:{1}".format(cur.description[j][0], v_col_value))
            #print(curUtil.description[j][0], v_col_value)
    print("Run SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','dbtask-"+v_col_value+".log')); ")
    cur.close()
    conn.close()
    
  
if __name__ == "__main__":
   copyToS3(sys.argv[1:])
    
