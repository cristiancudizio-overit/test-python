REM 2019-06-20 12:42:45.258324
set PROJECT_NAME=SCMIta
set BRANCH_FROM=11.0
set BRANCH_TO=11.20
set REV_FROM=375104
set REV_TO=375588
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 12:42:45.258324 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375104 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375588 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 11.0 da rev 375104 a 375588 sul 11.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.20\overit 

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn update 
Updating '.':
Alla revisione 375588.

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn merge -r 375104:375588 http://svn.overit.it/repositories/geocall/SCMIta/branches/11.0/src/overit --accept postpone 
--- Fusione di r375105 attraverso r375588 in '.':
U    geocallapp\scmita\anagrafiche\libretti\DATSalvaLibretto.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
U    geocallapp\scmita\scmita_prod.xml
 G   .
--- Recording mergeinfo for merge of r375105 through r375588 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=11.0 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=11.20 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375104 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375588 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 11.0 da rev 375104 a 375588 sul 11.20" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-11.20\overit 

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-11.20\overit>svn commit -m "riportate modifiche dal branch 11.0 da rev 375104 a 375588 sul 11.20" 
Trasmetto      .
Trasmetto      geocallapp\scmita\anagrafiche\libretti\DATSalvaLibretto.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
Trasmetto      geocallapp\scmita\scmita_prod.xml
Trasmissione dati ........
Committed revision 375589.
