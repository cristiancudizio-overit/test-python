REM 2019-06-17 09:19:40.236198
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.20
set BRANCH_TO=10.25
set REV_FROM=374056
set REV_TO=374806
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:19:40.236198 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374056 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374806 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 374056 a 374806 sul 10.25" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.25\overit 

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn update 
Updating '.':
Alla revisione 374806.

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn merge -r 374056:374806 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.20/src/overit --accept postpone 
--- Fusione di r374057 attraverso r374806 in '.':
U    geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
 G   .
--- Recording mergeinfo for merge of r374057 through r374806 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374056 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374806 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 374056 a 374806 sul 10.25" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.25\overit 

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn commit -m "riportate modifiche dal branch 10.20 da rev 374056 a 374806 sul 10.25" 
Trasmetto      .
Trasmetto      geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
Trasmissione dati .
Committed revision 374807.
