REM 2019-06-18 11:24:29.484400
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.25
set BRANCH_TO=10.30
set REV_FROM=374807
set REV_TO=375098
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:24:29.484400 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374807 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375098 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.25 da rev 374807 a 375098 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.30\overit 

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn update 
Updating '.':
Alla revisione 375098.

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn merge -r 374807:375098 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.25/src/overit --accept postpone 
--- Fusione di r374808 attraverso r375098 in '.':
U    geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
U    geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
 G   .
--- Recording mergeinfo for merge of r374808 through r375098 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374807 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375098 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.25 da rev 374807 a 375098 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.30\overit 

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn commit -m "riportate modifiche dal branch 10.25 da rev 374807 a 375098 sul 10.30" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
Trasmetto      geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
Trasmissione dati ...
Committed revision 375099.
