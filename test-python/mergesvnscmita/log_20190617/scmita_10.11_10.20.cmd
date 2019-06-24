REM 2019-06-17 09:19:21.716948
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.11
set BRANCH_TO=10.20
set REV_FROM=374055
set REV_TO=374804
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:19:21.716948 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374055 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374804 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.11 da rev 374055 a 374804 sul 10.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.20\overit 

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn update 
Updating '.':
Alla revisione 374804.

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn merge -r 374055:374804 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.11/src/overit --accept postpone 
--- Fusione di r374056 attraverso r374804 in '.':
U    geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
 G   .
--- Recording mergeinfo for merge of r374056 through r374804 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374055 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374804 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.11 da rev 374055 a 374804 sul 10.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.20\overit 

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn commit -m "riportate modifiche dal branch 10.11 da rev 374055 a 374804 sul 10.20" 
Trasmetto      .
Trasmetto      geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
Trasmissione dati .
Committed revision 374806.
