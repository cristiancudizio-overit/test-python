REM 2019-06-18 11:24:19.906352
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.20
set BRANCH_TO=10.25
set REV_FROM=374806
set REV_TO=375097
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:24:19.906352 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374806 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375097 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 374806 a 375097 sul 10.25" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.25\overit 

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn update 
Updating '.':
Alla revisione 375097.

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn merge -r 374806:375097 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.20/src/overit --accept postpone 
--- Fusione di r374807 attraverso r375097 in '.':
U    geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
U    geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
 G   .
--- Recording mergeinfo for merge of r374807 through r375097 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374806 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375097 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 374806 a 375097 sul 10.25" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.25\overit 

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn commit -m "riportate modifiche dal branch 10.20 da rev 374806 a 375097 sul 10.25" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
Trasmetto      geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
Trasmissione dati ...
Committed revision 375098.
