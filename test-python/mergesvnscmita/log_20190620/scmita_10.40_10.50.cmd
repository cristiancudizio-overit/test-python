REM 2019-06-20 12:42:02.010133
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.40
set BRANCH_TO=10.50
set REV_FROM=375101
set REV_TO=375586
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 12:42:02.010133 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375101 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375586 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.40 da rev 375101 a 375586 sul 10.50" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.50\overit 

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn update 
Updating '.':
Alla revisione 375586.

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn merge -r 375101:375586 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.40/src/overit --accept postpone 
--- Fusione di r375102 attraverso r375586 in '.':
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
U    geocallapp\scmita\scmita_prod.xml
 G   .
--- Recording mergeinfo for merge of r375102 through r375586 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.50 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375101 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375586 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.40 da rev 375101 a 375586 sul 10.50" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.50\overit 

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.50\overit>svn commit -m "riportate modifiche dal branch 10.40 da rev 375101 a 375586 sul 10.50" 
Trasmetto      .
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
Trasmetto      geocallapp\scmita\scmita_prod.xml
Trasmissione dati .......
Committed revision 375587.
