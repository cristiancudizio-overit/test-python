REM 2019-06-17 09:15:05.523974
set PROJECT_NAME=Damasco
set BRANCH_FROM=10.30
set BRANCH_TO=10.40
set REV_FROM=374048
set REV_TO=374798
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:15:05.523974 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374048 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374798 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.30 da rev 374048 a 374798 sul 10.40" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.40\overit 

C:\OVERIT\geocall61\Damasco-10.40\overit>svn update 
Updating '.':
Alla revisione 374798.

C:\OVERIT\geocall61\Damasco-10.40\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\Damasco-10.40\overit>svn merge -r 374048:374798 http://svn.overit.it/repositories/geocall/Damasco/branches/10.30/src/overit --accept postpone 
--- Fusione di r374049 attraverso r374798 in '.':
 G   .
--- Recording mergeinfo for merge of r374049 through r374798 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374048 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374798 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.30 da rev 374048 a 374798 sul 10.40" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.40\overit 

C:\OVERIT\geocall61\Damasco-10.40\overit>svn_commit.cmd

C:\OVERIT\geocall61\Damasco-10.40\overit>svn commit -m "riportate modifiche dal branch 10.30 da rev 374048 a 374798 sul 10.40" 
Trasmetto      .

Committed revision 374799.
