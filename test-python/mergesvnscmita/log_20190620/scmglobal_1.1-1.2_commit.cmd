set PROJECT_NAME=SCMGlobal
set BRANCH_FROM=1.1
set BRANCH_TO=1.2
set REV_FROM=375089
set REV_TO=375530
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn_commit.cmd
