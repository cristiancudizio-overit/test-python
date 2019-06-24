REM 2019-06-17 09:20:43.771019
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.30
set BRANCH_TO=10.35
set REV_FROM=374058
set REV_TO=374808
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:20:43.771019 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374058 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374808 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.30 da rev 374058 a 374808 sul 10.35" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.35\overit 

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn update 
Updating '.':
Alla revisione 374808.

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn merge -r 374058:374808 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.30/src/overit --accept postpone 
--- Fusione di r374059 attraverso r374808 in '.':
U    geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
 G   .
--- Recording mergeinfo for merge of r374059 through r374808 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374058 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374808 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.30 da rev 374058 a 374808 sul 10.35" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.35\overit 

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn commit -m "riportate modifiche dal branch 10.30 da rev 374058 a 374808 sul 10.35" 
Trasmetto      .
Trasmetto      geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
Trasmissione dati .
Committed revision 374809.
