REM 2019-06-17 09:19:05.460504
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.10
set BRANCH_TO=10.11
set REV_FROM=374054
set REV_TO=374803
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:19:05.460504 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.10 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374054 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374803 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.10 da rev 374054 a 374803 sul 10.11" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.11\overit 

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn update 
Updating '.':
Alla revisione 374803.

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn merge -r 374054:374803 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.10/src/overit --accept postpone 
--- Fusione di r374055 attraverso r374803 in '.':
U    geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
 G   .
--- Recording mergeinfo for merge of r374055 through r374803 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.10 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374054 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374803 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.10 da rev 374054 a 374803 sul 10.11" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.11\overit 

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn commit -m "riportate modifiche dal branch 10.10 da rev 374054 a 374803 sul 10.11" 
Trasmetto      .
Trasmetto      geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
Trasmissione dati .
Committed revision 374804.
