REM 2019-06-17 09:20:54.236090
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.35
set BRANCH_TO=10.40
set REV_FROM=374059
set REV_TO=374809
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:20:54.236090 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374059 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374809 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.35 da rev 374059 a 374809 sul 10.40" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.40\overit 

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn update 
Updating '.':
Alla revisione 374809.

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn merge -r 374059:374809 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.35/src/overit --accept postpone 
--- Fusione di r374060 attraverso r374809 in '.':
U    geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
U    geocallapp\scmita\visitesorveglianza\report\reportmaster\DATReportMaster.java
 G   .
--- Recording mergeinfo for merge of r374060 through r374809 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374059 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374809 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.35 da rev 374059 a 374809 sul 10.40" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.40\overit 

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn commit -m "riportate modifiche dal branch 10.35 da rev 374059 a 374809 sul 10.40" 
Trasmetto      .
Trasmetto      geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
Trasmetto      geocallapp\scmita\visitesorveglianza\report\reportmaster\DATReportMaster.java
Trasmissione dati ..
Committed revision 374810.
