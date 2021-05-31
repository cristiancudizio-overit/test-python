from orautils.orautils.load_mreti_mareeistat_from_csv import load_mreti_mareeistat_from_csv
import sys
#from .orautils import create_oracle_rds_user 
from .orautils.create_oracle_rds_user import create_oracle_rds_user
from .orautils.uploadMultipleBlobStream import uploadMultipleBlobStream
from .orautils.downloadBlobDump import downloadBlobDump
from .orautils.oracle_dp_export import oracle_dp_export
from .orautils.oracle_dp_import import oracle_dp_import
from .orautils.export_censimentoRDS_on_xls import exportReport2XLS

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
        print("\t- create_oracle_rds_user")
        print("\t- uploadMultipleBlobStream")
        print("\t- downloadBlobDump")
        print("\t- oracle_dp_export")
        print("\t- oracle_dp_import")
        print("\t- load_mreti_mareeistat_from_csv")
        print("\t- exportReport2XLS")
    elif (sys.argv[1] == 'create_oracle_rds_user'):
        print('create_oracle_rds_user','\n\n')
        create_oracle_rds_user(sys.argv[2:])
    elif (sys.argv[1] == 'uploadMultipleBlobStream'):
        print('uploadMultipleBlobStream','\n\n')
        uploadMultipleBlobStream(sys.argv[2:])
    elif (sys.argv[1] == 'downloadBlobDump'):
        print('downloadBlobDump','\n\n')
        downloadBlobDump(sys.argv[2:])
    elif (sys.argv[1] == 'oracle_dp_export'):
        print('oracle_dp_export','\n\n')
        oracle_dp_export(sys.argv[2:])
    elif (sys.argv[1] == 'oracle_dp_import'):
        print('oracle_dp_import','\n\n')
        oracle_dp_import(sys.argv[2:])
    elif (sys.argv[1] == 'load_mreti_mareeistat_from_csv'):
        print('load_mreti_mareeistat_from_csv','\n\n')
        #load_mreti_mareeistat_from_csv(sys.argv[2:])
        locals()[sys.argv[1]](sys.argv[2:])
    elif (sys.argv[1] == 'exportReport2XLS'):
        print('load_mreexportReport2XLSti_mareeistat_from_csv','\n\n')
        locals()[sys.argv[1]](sys.argv[2:])

        
    