#!/bin/bash

# Скрипт для загрузки всех моделей в фоновом режиме

cd "/Users/nikitaamurcev/Yandex.Disk.localized/Мак/Мои проекты/AI-modeli/Fooocus"

echo "Запуск загрузки моделей..."
echo "Лог будет сохранен в: download_all_models.log"
echo ""

# Запускаем Python скрипт в фоне с логированием
nohup python3 download_models.py > download_all_models.log 2>&1 &

# Сохраняем PID процесса
echo $! > download_models.pid

echo "Загрузка запущена в фоновом режиме (PID: $(cat download_models.pid))"
echo "Для проверки прогресса выполните: tail -f download_all_models.log"
echo "Для остановки выполните: kill \$(cat download_models.pid)"
