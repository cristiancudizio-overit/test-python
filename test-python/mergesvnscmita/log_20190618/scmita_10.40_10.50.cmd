REM 2019-06-18 11:24:54.690691
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.40
set BRANCH_TO=10.50
set REV_FROM=374810
set REV_TO=375101
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:24:54.690691 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374810 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375101 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.40 da rev 374810 a 375101 sul 10.50" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.50\overit 

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn update 
Updating '.':
Alla revisione 375101.

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn merge -r 374810:375101 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.40/src/overit --accept postpone 
--- Fusione di r374811 attraverso r375101 in '.':
U    geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
U    geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
 G   .
--- Recording mergeinfo for merge of r374811 through r375101 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374810 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375101 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.40 da rev 374810 a 375101 sul 10.50" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.50\overit 

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn commit -m "riportate modifiche dal branch 10.40 da rev 374810 a 375101 sul 10.50" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
Trasmetto      geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
Trasmissione dati ...
Committed revision 375102.
