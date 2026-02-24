@echo off
cls
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║     INSTAGRAM NON-FOLLOWERS CHECKER - POC                     ║
echo ║     Descubra quem nao te segue de volta!                      ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo.
echo  O que voce deseja fazer?
echo.
echo  [1] Instalar dependencias (primeira vez)
echo  [2] Executar metodo SEGURO (dados exportados) - RECOMENDADO
echo  [3] Executar metodo AUTOMATICO (Instaloader) - ARRISCADO
echo  [4] Ler o guia completo
echo  [5] Sair
echo.
set /p choice="Digite sua opcao (1-5): "

if "%choice%"=="1" goto install
if "%choice%"=="2" goto safe
if "%choice%"=="3" goto auto
if "%choice%"=="4" goto guide
if "%choice%"=="5" goto end

echo.
echo Opcao invalida!
pause
goto start

:install
echo.
echo ========================================
echo Instalando dependencias...
echo ========================================
call install.bat
goto end

:safe
echo.
echo ========================================
echo Executando metodo SEGURO...
echo ========================================
call run_safe.bat
goto end

:auto
echo.
echo ========================================
echo AVISO: Metodo automatico pode ser arriscado!
echo ========================================
call run_auto.bat
goto end

:guide
echo.
echo ========================================
echo Abrindo guia de uso...
echo ========================================
type GUIA_DE_USO.md | more
pause
goto end

:end
echo.
echo Obrigado por usar o Instagram Non-Followers Checker!
echo.
pause

