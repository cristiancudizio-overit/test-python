REM 2019-06-18 11:19:14.674609
set PROJECT_NAME=Damasco
set BRANCH_FROM=10.20
set BRANCH_TO=10.30
set REV_FROM=374797
set REV_TO=375085
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:19:14.674609 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374797 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375085 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 374797 a 375085 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.30\overit 

C:\OVERIT\geocall61\Damasco-10.30\overit>svn update 
Updating '.':
Alla revisione 375085.

C:\OVERIT\geocall61\Damasco-10.30\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\Damasco-10.30\overit>svn merge -r 374797:375085 http://svn.overit.it/repositories/geocall/Damasco/branches/10.20/src/overit --accept postpone 
--- Fusione di r374798 attraverso r375085 in '.':
 G   .
--- Recording mergeinfo for merge of r374798 through r375085 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=Damasco 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374797 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375085 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 374797 a 375085 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\Damasco-10.30\overit 

C:\OVERIT\geocall61\Damasco-10.30\overit>svn_commit.cmd

C:\OVERIT\geocall61\Damasco-10.30\overit>svn commit -m "riportate modifiche dal branch 10.20 da rev 374797 a 375085 sul 10.30" 
Trasmetto      .

Committed revision 375088.
