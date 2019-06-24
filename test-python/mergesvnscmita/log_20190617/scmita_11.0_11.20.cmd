REM 2019-06-17 09:21:50.356044
set PROJECT_NAME=SCMIta
set BRANCH_FROM=11.0
set BRANCH_TO=11.20
set REV_FROM=374064
set REV_TO=374812
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-17 09:21:50.356044 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374064 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374812 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 11.0 da rev 374064 a 374812 sul 11.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.20\overit 

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn update 
Updating '.':
Alla revisione 374812.

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn merge -r 374064:374812 http://svn.overit.it/repositories/geocall/SCMIta/branches/11.0/src/overit --accept postpone 
--- Fusione di r374065 attraverso r374812 in '.':
U    geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
U    geocallapp\scmita\visitesorveglianza\report\reportmaster\DATReportMaster.java
 G   .
--- Recording mergeinfo for merge of r374065 through r374812 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374064 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=374812 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 11.0 da rev 374064 a 374812 sul 11.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.20\overit 

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn commit -m "riportate modifiche dal branch 11.0 da rev 374064 a 374812 sul 11.20" 
Trasmetto      .
Trasmetto      geocallapp\scmita\cxf\gwfesitoverifiche\wrapper\DATCallEsitoVerificaFinale.java
Trasmetto      geocallapp\scmita\visitesorveglianza\report\reportmaster\DATReportMaster.java
Trasmissione dati ..
Committed revision 374813.
