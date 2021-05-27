g_plsql_fremove_mreti_csv = """BEGIN
        UTL_FILE.FREMOVE (
        location => 'DATA_PUMP_DIR',
        filename => 'MRETI.csv');
        END;"""
g_plsql_fremove_mareeistat_csv = """BEGIN
        UTL_FILE.FREMOVE (
        location => 'DATA_PUMP_DIR',
        filename => 'MAREEISTAT.csv');
        END;"""