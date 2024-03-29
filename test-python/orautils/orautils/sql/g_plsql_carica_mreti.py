g_plsql_carica_mreti = """DECLARE
	p_version varchar2(16) := :p_version;
begin
-- this procedure must be preceded by recreation on _NEW sequences and tables 


-- CARICAMENTO MRETI
INSERT INTO MRETI_NEW
(   MRETID,
	MRETID2,
	MRETCODICE_LNAZ,
	MRETCODICE_LPRO,
	MRETCODICECOMUNE,
	MRETCODICELOCALITA,
	MRETLIVELLO,
	MRETISTAT,
	MRETCAP,
	MRETANOMALO,
	MRETISTCAP,
	MRETCOMUNE,
	MRETLOCALITA,
	MRETID_TSPE,
	MRETSPECIE,
	MRETVIA,
	MRETCIVICO ,
	MRETDESTRO,
	MRETINTERNO,
	MRETSIGLAPRO,
	MRETXCOORD,
	MRETYCOORD,
	DATASTAMP,
	LOGIN,
	ACTION
)
SELECT
 SMRETI_NEW.NEXTVAL,
 MRETID2,
	MRETCODICE_LNAZ,
	MRETCODICE_LPRO,
	MRETCODICECOMUNE,
	MRETCODICELOCALITA,
	TO_NUMBER(MRETLIVELLO,'99'),
	MRETISTAT,
	MRETCAP,
	MRETANOMALO,
	MRETISTCAP,
	MRETCOMUNE,
	MRETLOCALITA,
	TO_NUMBER(MRETID_TSPE,'9999999999'),
	MRETSPECIE,
	MRETVIA,
	TO_NUMBER(MRETCIVICO,'99999'),
	MRETDESTRO,
	MRETINTERNO,
	MRETSIGLAPRO,
	TO_NUMBER(MRETXCOORD,'99D999999999','NLS_NUMERIC_CHARACTERS=''.,'''),
	TO_NUMBER(MRETYCOORD,'99D999999999','NLS_NUMERIC_CHARACTERS=''.,'''),
	SYSDATE,
	1,
	1973
FROM 
 MRETI_CSV;   
commit;
 
-- CREAZIONE INDICI, ci sono differenze rispetto allo standard --
 execute immediate 'create  index IDXMRET_'||p_version||'01 on MRETI_NEW (MRETLIVELLO, MRETCODICE_LNAZ, MRETCODICE_LPRO, MRETCOMUNE, MRETLOCALITA) tablespace MRETIINDX';
 execute immediate 'create  index IDXMRET_'||p_version||'02 on MRETI_NEW (MRETISTCAP) tablespace MRETIINDX';
 execute immediate 'create unique index IDXMRET_'||p_version||'03 on MRETI_NEW (MRETID) tablespace MRETIINDX';
 execute immediate 'create  index IDXMRET_'||p_version||'04 on MRETI_NEW (MRETLIVELLO, MRETISTAT) tablespace MRETIINDX';

  -- RINOMINA TABELLE
 execute immediate 'ALTER TABLE MRETI_NEW RENAME TO MRETI_'||p_version;
end;"""
