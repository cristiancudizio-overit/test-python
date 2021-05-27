g_sql_drop_external_table_dplog = "drop table dp_log_et"
g_sql_ddl_external_table_dplog = """
        create table dp_log_et 
           (
          textline    VARCHAR2(2048)
        )
           organization external (
           type oracle_loader
           default directory {.directory}
           access parameters (
           records delimited by newline
           CHARACTERSET AL32UTF8
           BADFILE 'dp_log_et.bad'
           LOGFILE 'dp_log_et.log'
           skip 0
           fields terminated by ";" optionally enclosed by "'"
           MISSING FIELD VALUES ARE NULL
           (
                textline char(2048)
           )
           )
           location
           (
           'py_dp.log'
           )
        )"""