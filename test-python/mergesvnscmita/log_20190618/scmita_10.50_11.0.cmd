REM 2019-06-18 11:25:05.826783
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.50
set BRANCH_TO=11.0
set REV_FROM=374811
set REV_TO=375102
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:25:05.826783 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374811 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375102 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.50 da rev 374811 a 375102 sul 11.0" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.0\overit 

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn update 
Updating '.':
Alla revisione 375102.

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn merge -r 374811:375102 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.50/src/overit --accept postpone 
--- Fusione di r374812 attraverso r375102 in '.':
U    geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
U    geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
 G   .
--- Recording mergeinfo for merge of r374812 through r375102 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374811 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375102 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.50 da rev 374811 a 375102 sul 11.0" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.0\overit 

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-11.0\overit>svn commit -m "riportate modifiche dal branch 10.50 da rev 374811 a 375102 sul 11.0" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
Trasmetto      geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
Trasmissione dati ...
Committed revision 375104.
