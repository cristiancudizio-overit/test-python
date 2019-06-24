REM 2019-06-17 09:21:38.922498
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.50
set BRANCH_TO=11.0
set REV_FROM=374063
set REV_TO=374811
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:21:38.922498 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374063 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374811 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.50 da rev 374063 a 374811 sul 11.0" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.0\overit 

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn update 
Updating '.':
Alla revisione 374811.

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn merge -r 374063:374811 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.50/src/overit --accept postpone 
--- Fusione di r374064 attraverso r374811 in '.':
U    geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
U    geocallapp\scmita\visitesorveglianza\report\reportmaster\DATReportMaster.java
 G   .
--- Recording mergeinfo for merge of r374064 through r374811 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374063 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374811 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.50 da rev 374063 a 374811 sul 11.0" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.0\overit 

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn commit -m "riportate modifiche dal branch 10.50 da rev 374063 a 374811 sul 11.0" 
Trasmetto      .
Trasmetto      geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
Trasmetto      geocallapp\scmita\visitesorveglianza\report\reportmaster\DATReportMaster.java
Trasmissione dati ..
Committed revision 374812.
