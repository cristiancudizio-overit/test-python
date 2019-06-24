REM 2019-06-20 10:37:52.489199
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.25
set BRANCH_TO=10.30
set REV_FROM=375098
set REV_TO=375539
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 10:37:52.489199 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375098 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375539 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.25 da rev 375098 a 375539 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.30\overit 

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn update 
Updating '.':
Alla revisione 375539.

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn merge -r 375098:375539 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.25/src/overit --accept postpone 
--- Fusione di r375099 attraverso r375539 in '.':
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
C    geocallapp\scmita\scmita_prod.xml
 G   .
--- Recording mergeinfo for merge of r375099 through r375539 into '.':
 G   .
Summary of conflicts:
  Text conflicts: 1

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.30 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375098 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375539 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.25 da rev 375098 a 375539 sul 10.30" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.30\overit 

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.30\overit>svn commit -m "riportate modifiche dal branch 10.25 da rev 375098 a 375539 sul 10.30" 
Trasmetto      .
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
Trasmetto      geocallapp\scmita\scmita_prod.xml
Trasmissione dati .......
Committed revision 375584.
