::Batch file
cd <PATH>

python create.py %1 %2

cd <PATH>\%1

git init

::Enter Github username
git remote rm origin
 git remote add origin https://github.com/<username>/%1.git

echo # %1 > README.md
git add .
git commit -m "initial commit"
git push -u origin master

:: Opens VsCode 
code .
