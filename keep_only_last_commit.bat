@echo off
REM Navigate to your Git repo directory first or place this file there
echo Cleaning Git history to keep only the latest commit...

REM Get first commit hash
for /f %%i in ('git rev-list --max-parents=0 HEAD') do set FIRST_COMMIT=%%i

REM Reset to first commit softly (keep changes staged)
git reset --soft %FIRST_COMMIT%

REM Replace commit history with one commit
git commit --amend -m "Clean single commit"

REM Force push to overwrite history
git push origin main --force

echo Done. Only the latest commit remains.
pause
