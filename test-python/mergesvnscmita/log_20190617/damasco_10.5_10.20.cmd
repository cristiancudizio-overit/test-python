REM 2019-06-17 09:12:35.051651
set PROJECT_NAME=Damasco
set BRANCH_FROM=10.5
set BRANCH_TO=10.20
set REV_FROM=374046
set REV_TO=374796
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:12:35.051651 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.5 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374046 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374796 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.5 da rev 374046 a 374796 sul 10.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.20\overit 

C:\OVERIT\geocall61\Damasco-10.20\overit>svn update 
Updating '.':
Alla revisione 374796.

C:\OVERIT\geocall61\Damasco-10.20\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\Damasco-10.20\overit>svn merge -r 374046:374796 http://svn.overit.it/repositories/geocall/Damasco/branches/10.5/src/overit --accept postpone 
--- Recording mergeinfo for merge of r374047 through r374796 into '.':
 U   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.5 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374046 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374796 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.5 da rev 374046 a 374796 sul 10.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.20\overit 

C:\OVERIT\geocall61\Damasco-10.20\overit>svn_commit.cmd

C:\OVERIT\geocall61\Damasco-10.20\overit>svn commit -m "riportate modifiche dal branch 10.5 da rev 374046 a 374796 sul 10.20" 
Trasmetto      .

Committed revision 374797.
