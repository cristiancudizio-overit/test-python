REM 2019-06-17 09:21:08.430171
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.40
set BRANCH_TO=10.50
set REV_FROM=374061
set REV_TO=374810
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:21:08.430171 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374061 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374810 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.40 da rev 374061 a 374810 sul 10.50" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.50\overit 

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn update 
Updating '.':
Alla revisione 374810.

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn merge -r 374061:374810 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.40/src/overit --accept postpone 
--- Fusione di r374062 attraverso r374810 in '.':
U    geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
U    geocallapp\scmita\visitesorveglianza\report\reportmaster\DATReportMaster.java
 G   .
--- Recording mergeinfo for merge of r374062 through r374810 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374061 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374810 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.40 da rev 374061 a 374810 sul 10.50" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.50\overit 

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn commit -m "riportate modifiche dal branch 10.40 da rev 374061 a 374810 sul 10.50" 
Trasmetto      .
Trasmetto      geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
Trasmetto      geocallapp\scmita\visitesorveglianza\report\reportmaster\DATReportMaster.java
Trasmissione dati ..
Committed revision 374811.
