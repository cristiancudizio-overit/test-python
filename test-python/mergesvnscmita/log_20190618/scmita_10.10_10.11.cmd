REM 2019-06-18 11:23:57.672665
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.10
set BRANCH_TO=10.11
set REV_FROM=374803
set REV_TO=375095
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:23:57.672665 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.10 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374803 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375095 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.10 da rev 374803 a 375095 sul 10.11" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.11\overit 

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn update 
Updating '.':
Alla revisione 375095.

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn merge -r 374803:375095 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.10/src/overit --accept postpone 
--- Fusione di r374804 attraverso r375095 in '.':
U    geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
U    geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
 G   .
--- Recording mergeinfo for merge of r374804 through r375095 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.10 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374803 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375095 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.10 da rev 374803 a 375095 sul 10.11" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.11\overit 

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn commit -m "riportate modifiche dal branch 10.10 da rev 374803 a 375095 sul 10.11" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
Trasmetto      geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
Trasmissione dati ...
Committed revision 375096.
