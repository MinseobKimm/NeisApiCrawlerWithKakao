@echo OFF
setlocal
set CONDA_ENV=conda_env
set PYFILE_PATH=C:\Users\shine\PycharmProjects\SendTalk\main.py
echo Activate %CONDA_ENV%
call conda activate %CONDA_ENV%
echo Run %PYFILE_PATH%
python %PYFILE_PATH%