set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.35
set BRANCH_TO=10.40
set REV_FROM=374059
set REV_TO=374809
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn_commit.cmd
