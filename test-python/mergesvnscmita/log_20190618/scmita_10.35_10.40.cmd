REM 2019-06-18 11:24:46.514912
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.35
set BRANCH_TO=10.40
set REV_FROM=374809
set REV_TO=375100
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:24:46.514912 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374809 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375100 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.35 da rev 374809 a 375100 sul 10.40" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.40\overit 

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn update 
Updating '.':
Alla revisione 375100.

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn merge -r 374809:375100 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.35/src/overit --accept postpone 
--- Fusione di r374810 attraverso r375100 in '.':
U    geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
U    geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
 G   .
--- Recording mergeinfo for merge of r374810 through r375100 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374809 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375100 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.35 da rev 374809 a 375100 sul 10.40" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.40\overit 

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn commit -m "riportate modifiche dal branch 10.35 da rev 374809 a 375100 sul 10.40" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
Trasmetto      geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
Trasmissione dati ...
Committed revision 375101.
