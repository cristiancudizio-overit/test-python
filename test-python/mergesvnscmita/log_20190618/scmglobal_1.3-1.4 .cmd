REM 2019-06-18 11:23:37.865640
set PROJECT_NAME=SCMGlobal
set BRANCH_FROM=1.3
set BRANCH_TO=1.4
set REV_FROM=374801
set REV_TO=375093
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:23:37.865640 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.3 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.4 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374801 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375093 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.3 da rev 374801 a 375093 sul 1.4" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.4\overit 

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn update 
Updating '.':
Alla revisione 375093.

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn merge -r 374801:375093 http://svn.overit.it/repositories/geocall/SCMGlobal/branches/1.3/src/overit --accept postpone 
--- Fusione di r374802 attraverso r375093 in '.':
 G   .
--- Recording mergeinfo for merge of r374802 through r375093 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMGlobal 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=1.3 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=1.4 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374801 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375093 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 1.3 da rev 374801 a 375093 sul 1.4" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMGlobal-1.4\overit 

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMGlobal-1.4\overit>svn commit -m "riportate modifiche dal branch 1.3 da rev 374801 a 375093 sul 1.4" 
Trasmetto      .

Committed revision 375094.
