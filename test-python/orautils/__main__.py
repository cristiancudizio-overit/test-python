from .orautils.init_rds_config import init_rds_config
from orautils.orautils.load_mreti_mareeistat_from_csv import load_mreti_mareeistat_from_csv
import sys
#from .orautils import create_oracle_rds_user 
from .orautils.create_oracle_rds_user import create_oracle_rds_user
from .orautils.drop_oracle_rds_user import drop_oracle_rds_user
from .orautils.create_oracle_rds_user import get_connection_string
#from .orautils.uploadMultipleBlobStream import uploadMultipleBlobStream
from .orautils.uploadMultipleBlobStream import run as uploadMultipleBlobStream, writeFileOnDir
from .orautils.uploadMultipleBlobStream import writeondirMAREEISTATCSV
from .orautils.uploadMultipleBlobStream import writeondirMRETICSV
from .orautils.downloadBlobDump import downloadBlobDump
from .orautils.uploadDumpToAWS import uploadDumpToAWS
from .orautils.oracle_dp_export import oracle_dp_export
from .orautils.oracle_dp_import import oracle_dp_import
from .orautils.oracle_dp_copy import oracle_dp_copy
from .orautils.export_censimentoRDS_on_xls import exportReport2XLS
from .orautils.S3Utils import copyFromRDSToS3
from .orautils.S3Utils import copyFromS3ToRDS
from .orautils.S3Utils import upload_file
from .orautils.S3Utils import copy_file

#print("Type: ", type(create_oracle_rds_user))
#print(sys.argv)
#main(sys.argv[1:])
#create_oracle_rds_user(sys.argv[1:])
#uploadMultipleBlobStream(sys.argv[1:])
#downloadBlobDump(sys.argv[1:])
print(__name__)
if __name__ == "__main__":
    #print(sys.argv,'\n\n')
    if (len(sys.argv) == 1):
        print("available options:\n")
        print("\t- get_connection_string")
        print("\t- create_oracle_rds_user")
        print("\t- uploadMultipleBlobStream")
        print("\t- writeFileOnDir")
        print("\t- writeondirMAREEISTATCSV")
        print("\t- downloadBlobDump")
        print("\t- uploadDumpToAWS")
        print("\t- oracle_dp_export")
        print("\t- oracle_dp_import")
        print("\t- oracle_dp_copy")
        print("\t- load_mreti_mareeistat_from_csv")
        print("\t- exportReport2XLS")
        print("\t- drop_oracle_rds_user")
        print("\t- init_rds_config")
        print("\t- copyFromRDSToS3")
        print("\t- copyFromS3ToRDS")
        print("\t- upload_file")
        print("\t- copy_file")
    elif (sys.argv[1] == 'get_connection_string'):
        print('get_connection_string','\n\n')
        get_connection_string(sys.argv[2:])
    elif (sys.argv[1] == 'create_oracle_rds_user'):
        print('create_oracle_rds_user','\n\n')
        create_oracle_rds_user(sys.argv[2:])
    elif (sys.argv[1] == 'drop_oracle_rds_user'):
        print('drop_oracle_rds_user','\n\n')
        drop_oracle_rds_user(sys.argv[2:])
    elif (sys.argv[1] == 'init_rds_config'):
        print('init_rds_config','\n\n')
        init_rds_config(sys.argv[2:])
    elif (sys.argv[1] == 'uploadMultipleBlobStream'):
        print('uploadMultipleBlobStream','\n\n')
        uploadMultipleBlobStream(sys.argv[2:])
    elif (sys.argv[1] == 'writeFileOnDir'):
        print('writeFileOnDir','\n\n')
        writeFileOnDir(sys.argv[2:])
    elif (sys.argv[1] == 'writeondirMAREEISTATCSV'):
        print('writeondirMAREEISTATCSV','\n\n')
        writeondirMAREEISTATCSV(sys.argv[2:])
    elif (sys.argv[1] == 'writeondirMRETICSV'):
        print('writeondirMRETICSV','\n\n')
        writeondirMRETICSV(sys.argv[2:])    
    elif (sys.argv[1] == 'downloadBlobDump'):
        print('downloadBlobDump','\n\n')
        downloadBlobDump(sys.argv[2:])
    elif (sys.argv[1] == 'uploadDumpToAWS'):
        print('uploadDumpToAWS','\n\n')
        uploadDumpToAWS(sys.argv[2:])
    elif (sys.argv[1] == 'oracle_dp_export'):
        print('oracle_dp_export','\n\n')
        oracle_dp_export(sys.argv[2:])
    elif (sys.argv[1] == 'oracle_dp_import'):
        print('oracle_dp_import','\n\n')
        oracle_dp_import(sys.argv[2:])
    elif (sys.argv[1] == 'oracle_dp_copy'):
        print('oracle_dp_copy','\n\n')
        oracle_dp_copy(sys.argv[2:])
    elif (sys.argv[1] == 'load_mreti_mareeistat_from_csv'):
        print('load_mreti_mareeistat_from_csv','\n\n')
        #load_mreti_mareeistat_from_csv(sys.argv[2:])
        locals()[sys.argv[1]](sys.argv[2:])
    elif (sys.argv[1] == 'exportReport2XLS'):
        print(sys.argv[1],'\n\n')
        locals()[sys.argv[1]](sys.argv[2:])
    elif (sys.argv[1] == 'copyFromRDSToS3'):
        print('copyFromRDSToS3','\n\n')
        copyFromRDSToS3(sys.argv[2:])
    elif (sys.argv[1] == 'copyFromS3ToRDS'):
        print('copyFromS3ToRDS','\n\n')
        copyFromS3ToRDS(sys.argv[2:])
    elif (sys.argv[1] == 'upload_file'):
        print('upload_file','\n\n')
        upload_file(sys.argv[2:])
    elif (sys.argv[1] == 'copy_file'):
        print('copy_file','\n\n')
        copy_file(sys.argv[2:])

        
    