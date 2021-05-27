#alter session set nls_numeric_characters='.,';    
g_sql_ddl_mreti_csv = """create table MRETI_CSV 
   (
  MRETCODICE_LNAZ    VARCHAR2(3),
  MRETCODICE_LPRO    VARCHAR2(3),
  MRETCODICECOMUNE   VARCHAR2(3),
  MRETCODICELOCALITA VARCHAR2(3),
  MRETLIVELLO        varchar2(2), 
  MRETISTAT          VARCHAR2(6),
  MRETCAP            VARCHAR2(5),
  MRETISTCAP         VARCHAR2(11),
  MRETCOMUNE         VARCHAR2(40),
  MRETLOCALITA       VARCHAR2(50),
  MRETID_TSPE        varchar2(10), 
  MRETSPECIE         VARCHAR2(50),
  MRETVIA            VARCHAR2(70),
  MRETCIVICO         varchar2(10), 
  MRETINTERNO        VARCHAR2(4),
  MRETSIGLAPRO       VARCHAR2(2),
  MRETXCOORD         VARCHAR2(12),
  MRETYCOORD         VARCHAR2(12),
  MRETANOMALO        CHAR(1),
  MRETDESTRO         VARCHAR2(2),
  MRETID2            VARCHAR2(10) 
)
   organization external (
   type oracle_loader
   default directory DATA_PUMP_DIR
   access parameters (
   records delimited by newline
   CHARACTERSET WE8ISO8859P1
   BADFILE 'mreti.bad'
   LOGFILE 'mreti.log'
   skip 0
   fields terminated by ";" optionally enclosed by "'"
   MISSING FIELD VALUES ARE NULL
   (
	MRETID2,
	MRETCODICE_LNAZ,
	MRETCODICE_LPRO,
	MRETCODICECOMUNE,
	MRETCODICELOCALITA,
	MRETLIVELLO NULLIF mretlivello=BLANKS ,
	MRETISTAT,
	MRETCAP,
	MRETANOMALO,
	MRETISTCAP,
	MRETCOMUNE,
	MRETLOCALITA,
	MRETID_TSPE NULLIF mretid_tspe=BLANKS,
	MRETSPECIE,
	MRETVIA,
	MRETCIVICO NULLIF mretcivico=BLANKS,
	MRETDESTRO,
	MRETINTERNO,
	MRETSIGLAPRO,
	MRETXCOORD,
	MRETYCOORD
   )
   )
   location
   (
   'MRETI.csv'
   )
)"""
g_sql_ddl_mareeistat_csv = """create table MAREEISTAT_CSV 
   (
	MAREISTCAP VARCHAR2(11), 
	MARECOMUNE VARCHAR2(50), 
	MARECAP VARCHAR2(5), 
	MAREISTAT VARCHAR2(6), 
	MARECODICE_LPRO VARCHAR2(3), 
	MARESIGLAPRO VARCHAR2(2), 	
	MARECODICEREGIONE VARCHAR2(15), 
	MAREXCOORD VARCHAR2(22), 
	MAREYCOORD VARCHAR2(22), 
	MAREAREA VARCHAR2(22) 	
)
   organization external (
   type oracle_loader
   default directory DATA_PUMP_DIR
   access parameters (
   records delimited by newline
   CHARACTERSET WE8ISO8859P1
   TERRITORY ITALY
   BADFILE 'mareeistat.bad'
   LOGFILE 'mareeistat.log'
   skip 0
   fields terminated by ";" optionally enclosed by "'"
   MISSING FIELD VALUES ARE NULL
   (
	MAREISTCAP,
	MARECOMUNE,
	MARECAP,
	MAREISTAT,
	MARECODICE_LPRO,
	MARESIGLAPRO,
	MARECODICEREGIONE,
	MAREXCOORD,
	MAREYCOORD,
	MAREAREA
   )
   )
   location
   (
   'MAREEISTAT.csv'
   )
)"""
