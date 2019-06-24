REM 2019-06-17 09:18:01.294429
set PROJECT_NAME=SCMGlobal
set BRANCH_FROM=1.1
set BRANCH_TO=1.2
set REV_FROM=374050
set REV_TO=374799
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:18:01.294429 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.1 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.2 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374050 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374799 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.1 da rev 374050 a 374799 sul 1.2" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.2\overit 

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn update 
Updating '.':
Alla revisione 374799.

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn merge -r 374050:374799 http://svn.overit.it/repositories/geocall/SCMGlobal/branches/1.1/src/overit --accept postpone 
--- Recording mergeinfo for merge of r374051 through r374799 into '.':
 U   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.1 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.2 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374050 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374799 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.1 da rev 374050 a 374799 sul 1.2" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.2\overit 

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMGlobal-1.2\overit>svn commit -m "riportate modifiche dal branch 1.1 da rev 374050 a 374799 sul 1.2" 
Trasmetto      .

Committed revision 374800.
