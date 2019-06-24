REM 2019-06-18 11:24:10.600983
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.11
set BRANCH_TO=10.20
set REV_FROM=374804
set REV_TO=375096
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:24:10.600983 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374804 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375096 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.11 da rev 374804 a 375096 sul 10.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.20\overit 

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn update 
Updating '.':
Alla revisione 375096.

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn merge -r 374804:375096 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.11/src/overit --accept postpone 
--- Fusione di r374805 attraverso r375096 in '.':
U    geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
U    geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
 G   .
--- Recording mergeinfo for merge of r374805 through r375096 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374804 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375096 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.11 da rev 374804 a 375096 sul 10.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.20\overit 

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.20\overit>svn commit -m "riportate modifiche dal branch 10.11 da rev 374804 a 375096 sul 10.20" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
Trasmetto      geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
Trasmissione dati ...
Committed revision 375097.
