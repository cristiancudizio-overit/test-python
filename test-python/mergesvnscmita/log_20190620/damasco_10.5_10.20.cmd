REM 2019-06-20 10:33:26.522377
set PROJECT_NAME=Damasco
set BRANCH_FROM=10.5
set BRANCH_TO=10.20
set REV_FROM=375060
set REV_TO=375527
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 10:33:26.522377 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.5 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375060 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375527 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.5 da rev 375060 a 375527 sul 10.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.20\overit 

C:\OVERIT\geocall61\Damasco-10.20\overit>svn update 
Updating '.':
Alla revisione 375527.

C:\OVERIT\geocall61\Damasco-10.20\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\Damasco-10.20\overit>svn merge -r 375060:375527 http://svn.overit.it/repositories/geocall/Damasco/branches/10.5/src/overit --accept postpone 
--- Recording mergeinfo for merge of r375061 through r375527 into '.':
 U   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.5 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375060 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375527 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.5 da rev 375060 a 375527 sul 10.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.20\overit 

C:\OVERIT\geocall61\Damasco-10.20\overit>svn_commit.cmd

C:\OVERIT\geocall61\Damasco-10.20\overit>svn commit -m "riportate modifiche dal branch 10.5 da rev 375060 a 375527 sul 10.20" 
Trasmetto      .

Committed revision 375528.
