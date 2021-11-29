g_plsql_carica_mareeistat = """DECLARE
	p_version varchar2(16) := :p_version;
begin
-- this procedure must be preceded by recreation on _NEW sequences and tables 
-- CARICAMENTO MAREEISTAT                   
insert into mareeistat_NEW 
(
	MAREID,
	MAREISTCAP,
	MARECOMUNE,
	MARECAP,
	MAREISTAT,
	MARECODICE_LPRO,
	MARESIGLAPRO,
	MARECODICEREGIONE,
	MAREXCOORD,
	MAREYCOORD,
	MAREAREA,
	MAREPESO
)
select
 SMAREEISTAT_NEW.NEXTVAL,
 MAREISTCAP,
 MARECOMUNE,
 MARECAP,
 MAREISTAT,
 MARECODICE_LPRO,
 MARESIGLAPRO,
 MARECODICEREGIONE,
 decode(instr(MAREXCOORD,'e-'), 0, TO_NUMBER(MAREXCOORD,'999D9999999999999999', 'NLS_NUMERIC_CHARACTERS=''.,'''), TO_NUMBER(MAREXCOORD,'999D99EEEE', 'NLS_NUMERIC_CHARACTERS=''.,''')),
 decode(instr(MAREYCOORD,'e-'), 0, TO_NUMBER(MAREYCOORD,'999D9999999999999999', 'NLS_NUMERIC_CHARACTERS=''.,'''), TO_NUMBER(MAREYCOORD,'999D99EEEE', 'NLS_NUMERIC_CHARACTERS=''.,''')),
 decode(instr(marearea,'e-'),0, TO_NUMBER(marearea,'999999D99999999999999999999', 'NLS_NUMERIC_CHARACTERS=''.,'''),0),
 decode(instr(marearea,'e-'),0, NULL, MAREAREA)
 from mareeistat_csv ;

COMMIT; 

 
-- CREAZIONE INDICI, ci sono differenze rispetto allo standard --

 execute immediate 'create unique index IDXMARE_'||p_version||'01 on MAREEISTAT_NEW (MAREISTCAP) tablespace MRETIINDX';
 execute immediate 'create index IDXMARE_'||p_version||'02 on MAREEISTAT_NEW (MARECOMUNE) tablespace MRETIINDX';
 execute immediate 'create index IDXMARE_'||p_version||'03 on MAREEISTAT_NEW (MARECODICE_LPRO) tablespace MRETIINDX';
 execute immediate 'create index IDXMARE_'||p_version||'04 on MAREEISTAT_NEW (MAREISTAT, MARECAP) tablespace MRETIINDX';
 execute immediate 'create index IDXMARE_'||p_version||'05 on MAREEISTAT_NEW (MAREXCOORD, MAREYCOORD) tablespace MRETIINDX';
 execute immediate 'create index IDXMARE_'||p_version||'06 on MAREEISTAT_NEW (MAREYCOORD, MAREXCOORD, MAREISTCAP) tablespace MRETIINDX';
 execute immediate 'create index IDXMARE_'||p_version||'LREG on MAREEISTAT_NEW (MAREID_LREG) tablespace MRETIINDX';
  -- RINOMINA TABELLE
 execute immediate 'ALTER TABLE MAREEISTAT_NEW RENAME TO MAREEISTAT_'||p_version;
end;"""
