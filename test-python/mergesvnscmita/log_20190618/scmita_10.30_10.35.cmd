REM 2019-06-18 11:24:37.687169
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.30
set BRANCH_TO=10.35
set REV_FROM=374808
set REV_TO=375099
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:24:37.687169 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374808 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375099 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.30 da rev 374808 a 375099 sul 10.35" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.35\overit 

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn update 
Updating '.':
Alla revisione 375099.

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn merge -r 374808:375099 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.30/src/overit --accept postpone 
--- Fusione di r374809 attraverso r375099 in '.':
U    geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
U    geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
 G   .
--- Recording mergeinfo for merge of r374809 through r375099 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374808 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375099 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.30 da rev 374808 a 375099 sul 10.35" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.35\overit 

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.35\overit>svn commit -m "riportate modifiche dal branch 10.30 da rev 374808 a 375099 sul 10.35" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
Trasmetto      geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
Trasmissione dati ...
Committed revision 375100.