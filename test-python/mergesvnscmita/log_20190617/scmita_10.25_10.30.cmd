REM 2019-06-17 09:20:29.172088
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.25
set BRANCH_TO=10.30
set REV_FROM=374057
set REV_TO=374807
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:20:29.172088 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374057 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374807 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.25 da rev 374057 a 374807 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.30\overit 

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn update 
Updating '.':
Alla revisione 374807.

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn merge -r 374057:374807 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.25/src/overit --accept postpone 
--- Fusione di r374058 attraverso r374807 in '.':
U    geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
 G   .
--- Recording mergeinfo for merge of r374058 through r374807 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374057 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374807 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.25 da rev 374057 a 374807 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.30\overit 

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn commit -m "riportate modifiche dal branch 10.25 da rev 374057 a 374807 sul 10.30" 
Trasmetto      .
Trasmetto      geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
Trasmissione dati .
Committed revision 374808.
