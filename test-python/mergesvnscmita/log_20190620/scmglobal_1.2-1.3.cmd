REM 2019-06-20 10:36:05.926730
set PROJECT_NAME=SCMGlobal
set BRANCH_FROM=1.2
set BRANCH_TO=1.3
set REV_FROM=375092
set REV_TO=375531
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 10:36:05.926730 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.2 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.3 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375092 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375531 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.2 da rev 375092 a 375531 sul 1.3" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.3\overit 

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn update 
Updating '.':
Alla revisione 375531.

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn merge -r 375092:375531 http://svn.overit.it/repositories/geocall/SCMGlobal/branches/1.2/src/overit --accept postpone 
--- Fusione di r375093 attraverso r375531 in '.':
 G   .
--- Recording mergeinfo for merge of r375093 through r375531 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.2 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.3 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375092 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375531 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.2 da rev 375092 a 375531 sul 1.3" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.3\overit 

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn commit -m "riportate modifiche dal branch 1.2 da rev 375092 a 375531 sul 1.3" 
Trasmetto      .

Committed revision 375532.
