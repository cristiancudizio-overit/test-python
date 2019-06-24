REM 2019-06-20 10:37:43.831791
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.20
set BRANCH_TO=10.25
set REV_FROM=375097
set REV_TO=375537
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 10:37:43.831791 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375097 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375537 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 375097 a 375537 sul 10.25" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.25\overit 

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn update 
Updating '.':
Alla revisione 375538.

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn merge -r 375097:375537 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.20/src/overit --accept postpone 
--- Fusione di r375098 attraverso r375537 in '.':
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
U    geocallapp\scmita\scmita_prod.xml
 G   .
--- Recording mergeinfo for merge of r375098 through r375537 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.25 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375097 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375537 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.20 da rev 375097 a 375537 sul 10.25" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.25\overit 

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.25\overit>svn commit -m "riportate modifiche dal branch 10.20 da rev 375097 a 375537 sul 10.25" 
Trasmetto      .
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
Trasmetto      geocallapp\scmita\scmita_prod.xml
Trasmissione dati .......
Committed revision 375539.
