REM 2019-06-18 11:25:13.279729
set PROJECT_NAME=SCMIta
set BRANCH_FROM=11.0
set BRANCH_TO=11.20
set REV_FROM=374812
set REV_TO=375104
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-18 11:25:13.279729 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374812 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375104 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 11.0 da rev 374812 a 375104 sul 11.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.20\overit 

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn update 
Updating '.':
Alla revisione 375104.

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn merge -r 374812:375104 http://svn.overit.it/repositories/geocall/SCMIta/branches/11.0/src/overit --accept postpone 
--- Fusione di r374813 attraverso r375104 in '.':
U    geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
U    geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
 G   .
--- Recording mergeinfo for merge of r374813 through r375104 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=374812 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375104 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 11.0 da rev 374812 a 375104 sul 11.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.20\overit 

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn commit -m "riportate modifiche dal branch 11.0 da rev 374812 a 375104 sul 11.20" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\comunicazioni\DATSalvaComunicazione.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\IncarichiVF.xml
Trasmetto      geocallapp\scmita\fibraottica\parametrizzazione\rgidrisposteirr\DARGidRisposteIrr.java
Trasmissione dati ...
Committed revision 375105.
