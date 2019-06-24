REM 2019-06-20 12:41:21.152157
set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.35
set BRANCH_TO=10.40
set REV_FROM=375100
set REV_TO=375585
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn update
svn_merge_branch.cmd

C:\development-cri\test-python\test-python\mergesvnscmita>REM 2019-06-20 12:41:21.152157 

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375100 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375585 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.35 da rev 375100 a 375585 sul 10.40" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.40\overit 

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn update 
Updating '.':
Alla revisione 375585.

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn_merge_branch.cmd

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn merge -r 375100:375585 http://svn.overit.it/repositories/geocall/SCMIta/branches/10.35/src/overit --accept postpone 
--- Fusione di r375101 attraverso r375585 in '.':
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
U    geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
U    geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
U    geocallapp\scmita\scmita_prod.xml
 G   .
--- Recording mergeinfo for merge of r375101 through r375585 into '.':
 G   .

C:\development-cri\test-python\test-python\mergesvnscmita>set PROJECT_NAME=SCMIta 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_FROM=10.35 

C:\development-cri\test-python\test-python\mergesvnscmita>set BRANCH_TO=10.40 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_FROM=375100 

C:\development-cri\test-python\test-python\mergesvnscmita>set REV_TO=375585 

C:\development-cri\test-python\test-python\mergesvnscmita>set COMMENT="riportate modifiche dal branch 10.35 da rev 375100 a 375585 sul 10.40" 

C:\development-cri\test-python\test-python\mergesvnscmita>cd \OVERIT\geocall61\SCMIta-10.40\overit 

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn_commit.cmd

C:\OVERIT\geocall61\SCMIta-10.40\overit>svn commit -m "riportate modifiche dal branch 10.35 da rev 375100 a 375585 sul 10.40" 
Trasmetto      .
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DAIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATGestioneIncaricoRichiestaSAB.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\DATSaveIncaricoVF.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\incarichivf\PEditIncaricoVF.xml
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\DASalAsBuiltTestata.java
Trasmetto      geocallapp\scmita\fibraottica\anagrafiche\salasbuilt\RicercaSAB.xml
Trasmetto      geocallapp\scmita\scmita_prod.xml
Trasmissione dati .......
Committed revision 375586.
