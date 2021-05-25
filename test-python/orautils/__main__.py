import sys
#from .orautils import create_oracle_rds_user 
#from .orautils.create_oracle_rds_user import create_oracle_rds_user
from .orautils.uploadMultipleBlobStream import uploadMultipleBlobStream
from .orautils.downloadBlobDump import downloadBlobDump
#print("Type: ", type(create_oracle_rds_user))
#print(sys.argv)
#main(sys.argv[1:])
#create_oracle_rds_user(sys.argv[1:])
uploadMultipleBlobStream(sys.argv[1:])
#downloadBlobDump(sys.argv[1:])