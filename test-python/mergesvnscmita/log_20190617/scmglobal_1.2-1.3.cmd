REM 2019-06-17 09:18:25.847568
set PROJECT_NAME=SCMGlobal
set BRANCH_FROM=1.2
set BRANCH_TO=1.3
set REV_FROM=374051
set REV_TO=374800
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:18:25.847568 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.2 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.3 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374051 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374800 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.2 da rev 374051 a 374800 sul 1.3" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.3\overit 

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn update 
Updating '.':
Alla revisione 374800.

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn merge -r 374051:374800 http://svn.overit.it/repositories/geocall/SCMGlobal/branches/1.2/src/overit --accept postpone 
--- Fusione di r374052 attraverso r374800 in '.':
 G   .
--- Recording mergeinfo for merge of r374052 through r374800 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.2 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.3 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374051 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374800 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.2 da rev 374051 a 374800 sul 1.3" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.3\overit 

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMGlobal-1.3\overit>svn commit -m "riportate modifiche dal branch 1.2 da rev 374051 a 374800 sul 1.3" 
Trasmetto      .

Committed revision 374801.
