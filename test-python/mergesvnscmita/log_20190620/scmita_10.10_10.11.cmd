REM 2019-06-20 10:37:16.660216
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.10
set BRANCH_TO=10.11
set REV_FROM=375095
set REV_TO=375534
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 10:37:16.660216 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.10 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375095 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375534 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.10 da rev 375095 a 375534 sul 10.11" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.11\overit 

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn update 
Updating '.':
Alla revisione 375534.

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn merge -r 375095:375534 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.10/src/overit --accept postpone 
--- Fusione di r375096 attraverso r375534 in '.':
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
 G   .
--- Recording mergeinfo for merge of r375096 through r375534 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.10 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.11 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375095 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375534 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.10 da rev 375095 a 375534 sul 10.11" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.11\overit 

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.11\overit>svn commit -m "riportate modifiche dal branch 10.10 da rev 375095 a 375534 sul 10.11" 
Trasmetto      .
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
Trasmissione dati ......
Committed revision 375536.
