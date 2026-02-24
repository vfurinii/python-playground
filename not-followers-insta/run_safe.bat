@echo off
echo ========================================
echo Instagram Non-Followers Checker
echo Metodo SEGURO - Dados Exportados
echo ========================================
echo.

python check_followers.py

if errorlevel 1 (
    echo.
    echo [ERRO] Ocorreu um erro ao executar o script
    pause
    exit /b 1
)

echo.
pause

