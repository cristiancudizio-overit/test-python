set PROJECT_NAME=Damasco
set BRANCH_FROM=10.5
set BRANCH_TO=10.20
set REV_FROM=374796
set REV_TO=375060
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn_commit.cmd