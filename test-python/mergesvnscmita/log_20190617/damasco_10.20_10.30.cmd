REM 2019-06-17 09:14:39.148046
set PROJECT_NAME=Damasco
set BRANCH_FROM=10.20
set BRANCH_TO=10.30
set REV_FROM=374047
set REV_TO=374797
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:14:39.148046 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374047 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374797 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 374047 a 374797 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.30\overit 

C:\OVERIT\geocall61\Damasco-10.30\overit>svn update 
Updating '.':
Alla revisione 374797.

C:\OVERIT\geocall61\Damasco-10.30\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\Damasco-10.30\overit>svn merge -r 374047:374797 http://svn.overit.it/repositories/geocall/Damasco/branches/10.20/src/overit --accept postpone 
--- Fusione di r374048 attraverso r374797 in '.':
 G   .
--- Recording mergeinfo for merge of r374048 through r374797 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374047 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374797 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 374047 a 374797 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.30\overit 

C:\OVERIT\geocall61\Damasco-10.30\overit>svn_commit.cmd

C:\OVERIT\geocall61\Damasco-10.30\overit>svn commit -m "riportate modifiche dal branch 10.20 da rev 374047 a 374797 sul 10.30" 
Trasmetto      .

Committed revision 374798.
