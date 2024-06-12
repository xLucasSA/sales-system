@echo off
chcp 65001

cd %USERPROFILE%\desktop\sistema_igreja\

if EXIST "venv\" (
    echo Ativando o ambiente virtual existente...
    call venv\Scripts\activate
) else (
    echo Criando um novo ambiente virtual...
    python -m venv venv
    call venv\Scripts\activate
)

echo Instalando as dependências...
pip install --upgrade pip
pip install -r requirements.txt

echo Aplicando migrações...
python manage.py migrate

echo Iniciando o servidor...
start http://localhost:8000
python manage.py runserver 0.0.0.0:8000