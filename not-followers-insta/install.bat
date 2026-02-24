@echo off
echo ========================================
echo Instagram Non-Followers Checker - POC
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo Por favor, instale Python 3.7+ de https://www.python.org/
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Verifica se pip está instalado
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] pip nao encontrado!
    pause
    exit /b 1
)

echo [OK] pip encontrado
echo.

REM Instala dependências
echo Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias
    pause
    exit /b 1
)

echo.
echo ========================================
echo Instalacao concluida com sucesso!
echo ========================================
echo.
echo Agora voce pode executar:
echo   - run_safe.bat (metodo SEGURO - recomendado)
echo   - run_auto.bat (metodo automatico - ARRISCADO)
echo.
pause

