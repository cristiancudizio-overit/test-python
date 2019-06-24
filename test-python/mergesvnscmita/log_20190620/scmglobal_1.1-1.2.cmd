REM 2019-06-20 10:35:33.895932
set PROJECT_NAME=SCMGlobal
set BRANCH_FROM=1.1
set BRANCH_TO=1.2
set REV_FROM=375089
set REV_TO=375530
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 10:35:33.895932 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.1 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.2 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375089 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375530 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.1 da rev 375089 a 375530 sul 1.2" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.2\overit 

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn update 
Updating '.':
Alla revisione 375530.

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn merge -r 375089:375530 http://svn.overit.it/repositories/geocall/SCMGlobal/branches/1.1/src/overit --accept postpone 
--- Recording mergeinfo for merge of r375090 through r375530 into '.':
 U   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.1 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.2 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375089 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375530 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.1 da rev 375089 a 375530 sul 1.2" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.2\overit 

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn commit -m "riportate modifiche dal branch 1.1 da rev 375089 a 375530 sul 1.2" 
Trasmetto      .

Committed revision 375531.
