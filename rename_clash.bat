@echo off
chcp 65001 >nul
echo Clash配置自动重命名工具
echo ========================
echo.

if "%~1"=="" (
    echo 用法: %0 ^<配置文件路径^>
    echo 示例: %0 config.yaml
    echo.
    echo 这会直接修改原文件，如果想保留原文件：
    echo %0 config.yaml renamed_config.yaml
    pause
    exit /b 1
)

python auto_rename.py %*
if %errorlevel% equ 0 (
    echo.
    echo 重命名成功完成！
) else (
    echo.
    echo 重命名失败，请检查Python环境和文件路径
)

pause
