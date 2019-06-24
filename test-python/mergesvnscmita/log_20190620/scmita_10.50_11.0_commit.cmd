set PROJECT_NAME=SCMIta
set BRANCH_FROM=10.50
set BRANCH_TO=11.0
set REV_FROM=375102
set REV_TO=375587
set COMMENT="riportate modifiche dal branch %BRANCH_FROM% da rev %REV_FROM% a %REV_TO% sul %BRANCH_TO%"
cd \OVERIT\geocall61\%PROJECT_NAME%-%BRANCH_TO%\overit
svn_commit.cmd
