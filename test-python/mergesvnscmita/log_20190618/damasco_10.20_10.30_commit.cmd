set PROJECT_NAME=Damasco
set BRANCH_FROM=10.20
set BRANCH_TO=10.30
set REV_FROM=374797
set REV_TO=375085
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn_commit.cmd
