@echo off
echo ========================================
echo Instagram Non-Followers Checker
echo Metodo AUTOMATICO - Instaloader
echo ========================================
echo.
echo AVISO: Este metodo pode violar os termos
echo de servico do Instagram!
echo.

python check_followers_auto.py

if errorlevel 1 (
    echo.
    echo [ERRO] Ocorreu um erro ao executar o script
    pause
    exit /b 1
)

echo.
pause

