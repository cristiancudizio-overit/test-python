REM 2019-06-17 09:18:49.983569
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.5
set BRANCH_TO=10.10
set REV_FROM=374053
set REV_TO=374802
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:18:49.983569 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.5 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.10 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374053 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374802 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.5 da rev 374053 a 374802 sul 10.10" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.10\overit 

C:\OVERIT\geocall61\SCMIta-10.10\overit>svn update 
Updating '.':
Alla revisione 374802.

C:\OVERIT\geocall61\SCMIta-10.10\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.10\overit>svn merge -r 374053:374802 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.5/src/overit --accept postpone 
--- Recording mergeinfo for merge of r374054 through r374802 into '.':
 U   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.5 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.10 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374053 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374802 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.5 da rev 374053 a 374802 sul 10.10" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.10\overit 

C:\OVERIT\geocall61\SCMIta-10.10\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.10\overit>svn commit -m "riportate modifiche dal branch 10.5 da rev 374053 a 374802 sul 10.10" 
Trasmetto      .

Committed revision 374803.
