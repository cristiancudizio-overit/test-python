set PROJECT_NAME=SCMGlobal
set BRANCH_FROM=1.2
set BRANCH_TO=1.3
set REV_FROM=374051
set REV_TO=374800
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn_commit.cmd
