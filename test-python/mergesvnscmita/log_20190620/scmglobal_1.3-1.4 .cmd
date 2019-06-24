REM 2019-06-20 10:36:22.879684
set PROJECT_NAME=SCMGlobal
set BRANCH_FROM=1.3
set BRANCH_TO=1.4
set REV_FROM=375093
set REV_TO=375532
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 10:36:22.879684 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.3 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.4 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375093 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375532 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.3 da rev 375093 a 375532 sul 1.4" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.4\overit 

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn update 
Updating '.':
Alla revisione 375532.

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn merge -r 375093:375532 http://svn.overit.it/repositories/geocall/SCMGlobal/branches/1.3/src/overit --accept postpone 
--- Fusione di r375094 attraverso r375532 in '.':
 G   .
--- Recording mergeinfo for merge of r375094 through r375532 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.3 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.4 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375093 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375532 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.3 da rev 375093 a 375532 sul 1.4" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.4\overit 

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn commit -m "riportate modifiche dal branch 1.3 da rev 375093 a 375532 sul 1.4" 
Trasmetto      .

Committed revision 375533.
