from datetime import datetime,date
import cx_Oracle
import getpass
import getopt
import sys


NON AGGIORNATO --> vedere uploadMultipleBlobStream-


#v_password = getpass.getpass()
 #h argument without parameter, i: parameter with argument, o: parameter with argumenti
#ifile longoptions
def uploadBlobStream(argv):
    opts, args = getopt.getopt(argv,"hd:f:l:",["help","dbstring=","dumpfilename=", "logfilename="])    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(sys.argv[0]+' -d dbstring -u username [-f dumpfilename -p directory ...] ')
            sys.exit()
        elif opt in ("-d", "--dbstring"):
            if arg!='':
                l_dbstring = arg
        elif opt in ("-f", "--dumpfilename"):
            if arg!='':
                l_dump_name = arg
        elif opt in ("-l", "--logfilename"):
            if arg!='':
                l_log_file_name = arg
    v_risposta = input('Dumpfilename: '+l_dump_name+' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    con = cx_Oracle.connect(l_dbstring)
    cur = con.cursor()
    lobDumpVar = cur.var(cx_Oracle.BLOB)
    lobLogVar = cur.var(cx_Oracle.BLOB)
    cur.execute("""
        insert into odpdumps (
            id, 
            dump_name,
            dump_file, 
            datetime, 
            log_file_name, 
            log_file, 
            notes)
            values (
            odpdumps_seq.nextval,
            :1,
            empty_blob(),
            sysdate,
            :2,
            empty_blob(),
            'import test')
        returning dump_file, log_file into :3, :4 """, [l_dump_name, l_log_file_name, lobDumpVar, lobLogVar])

    blobDump, = lobDumpVar.getvalue()
    blobLog, = lobLogVar.getvalue()
    offset = 1
    numBytesInChunk = 65536
    with open(l_dump_name, "rb") as f:
        while True:
            data = f.read(numBytesInChunk)
            if data:
                blobDump.write(data, offset)
            if len(data) < numBytesInChunk:
                break
            offset += len(data)
    offset = 1        
    with open(l_log_file_name, "rb") as f:
        while True:
            data = f.read(numBytesInChunk)
            if data:
                blobLog.write(data, offset)
            if len(data) < numBytesInChunk:
                break
            offset += len(data)
    con.commit()
    print("Files uploaded to BLOBs")
    #now unload blobs on DIRECTORY
    l_plsql_code = """DECLARE
    l_dirname   VARCHAR2(30);
    l_file      UTL_FILE.FILE_TYPE;
    l_buffer    RAW(32767);
    l_amount    BINARY_INTEGER := 32767;
    l_pos       INTEGER := 1;
    l_blob_len  INTEGER;
    cursor cur_odpdumps(cp_dumpname varchar2) is
        SELECT id, dump_name, dump_file, datetime, log_file_name, log_file 
        from odpdumps 
        where dump_name = cp_dumpname;
    rec_odpdumps cur_odpdumps%ROWTYPE;
    BEGIN
    l_dirname := 'DATA_PUMP_DIR';
    for rec_odpdumps in cur_odpdumps('p_dump_name') loop
            l_blob_len := DBMS_LOB.getlength(rec_odpdumps.dump_file);
            l_pos := 1;
            l_amount := 32767; -- !!!
            -- Open the destination file.
            l_file := UTL_FILE.fopen(l_dirname, rec_odpdumps.dump_name, 'wb', 32767);
            -- Read chunks of the BLOB and write them to the file
            -- until complete.
            WHILE l_pos < l_blob_len LOOP
                DBMS_LOB.read(rec_odpdumps.dump_File, l_amount, l_pos, l_buffer);
                UTL_FILE.put_raw(l_file, l_buffer, TRUE);
                l_pos := l_pos + l_amount;
            END LOOP;
            -- Close the file.
            UTL_FILE.fclose(l_file);
            --log 
            l_blob_len := DBMS_LOB.getlength(rec_odpdumps.log_file);
            l_pos := 1;
            l_amount := 32767; -- !!!
            -- Open the destination file.
            l_file := UTL_FILE.fopen(l_dirname, rec_odpdumps.log_file_name, 'wb', 32767);
            -- Read chunks of the BLOB and write them to the file
            -- until complete.
            WHILE l_pos < l_blob_len LOOP
                DBMS_LOB.read(rec_odpdumps.log_file, l_amount, l_pos, l_buffer);
                UTL_FILE.put_raw(l_file, l_buffer, TRUE);
                l_pos := l_pos + l_amount;
            END LOOP;
            -- Close the file.
            UTL_FILE.fclose(l_file);
    end loop;
    EXCEPTION
    WHEN OTHERS THEN
        -- Close the file if something goes wrong.
        IF UTL_FILE.is_open(l_file) THEN
        UTL_FILE.fclose(l_file);
        END IF;
        RAISE;
    END;"""
    cur.execute(l_plsql_code.replace('p_dump_name',l_dump_name))
    print("Blobs unloaded to DIRECTORY")
    cur.close()
    con.close()

if __name__ == "__main__":
   uploadBlobStream(sys.argv[1:])