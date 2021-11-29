g_plsql_init_rds_db = """
 -- usage: @create_init_db_config_rds 
alter profile default limit password_life_time unlimited;
create profile geocall_profile limit password_life_time unlimited FAILED_LOGIN_ATTEMPTS UNLIMITED;
CREATE ROLE GEOCALL_ROLE;
GRANT CREATE SESSION, CREATE TABLE, CREATE SYNONYM, CREATE VIEW, CREATE SEQUENCE, CREATE PROCEDURE, CREATE TRIGGER, CREATE JOB, CREATE TYPE, CREATE MATERIALIZED VIEW, SELECT_CATALOG_ROLE, create database link TO GEOCALL_ROLE;
grant SELECT_CATALOG_ROLE to GEOCALL_ROLE;
create  tablespace geodata ;
create  tablespace geolob ;
create  tablespace geoindx ;
create  tablespace mretidata;
create  tablespace mretiindx;
create user mreti identified by mreti default tablespace mretidata quota unlimited on mretidata quota unlimited on mretiindx profile geocall_profile;
grant geocall_role to mreti;
grant read,write on directory data_pump_dir to mreti;"""