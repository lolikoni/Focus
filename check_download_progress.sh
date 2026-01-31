#!/bin/bash

# Скрипт для проверки прогресса загрузки моделей

cd "/Users/nikitaamurcev/Yandex.Disk.localized/Мак/Мои проекты/AI-modeli/Fooocus"

python3 << 'EOF'
from pathlib import Path
from datetime import datetime

MODELS_DIR = Path('models 12.07.29/checkpoints')

print('='*70)
print('📊 ПРОГРЕСС ЗАГРУЗКИ МОДЕЛЕЙ ДЛЯ РЕАЛИСТИЧНЫХ ФОТО')
print('='*70)
print()

models_to_check = {
    'SDXL_Base_1.0.safetensors': ('SDXL Base 1.0', 6.5),
    'SDXL_Refiner_1.0.safetensors': ('SDXL Refiner 1.0', 6.5),
    'SDXL_Turbo_1.0_FP16.safetensors': ('SDXL Turbo 1.0', 6.5),
    'RealCoreXL.safetensors': ('RealCoreXL', 6.5),
}

# Также проверяем оригинальные имена
original = {
    'sd_xl_base_1.0.safetensors': 'SDXL Base 1.0',
    'sd_xl_refiner_1.0.safetensors': 'SDXL Refiner 1.0',
    'sd_xl_turbo_1.0_fp16.safetensors': 'SDXL Turbo 1.0',
}

loaded = 0
total_size = 0

for filename, (name, expected) in models_to_check.items():
    file_path = MODELS_DIR / filename
    if file_path.exists():
        size = file_path.stat().st_size / (1024**3)
        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        total_size += size
        loaded += 1
        print(f'✅ {name:30s} ЗАГРУЖЕНА - {size:.2f} GB ({mtime.strftime("%H:%M:%S")})')
    else:
        # Проверяем оригинальное имя
        orig_found = False
        for orig_name, orig_display in original.items():
            if filename.startswith('SDXL') and orig_name.startswith('sd_xl'):
                orig_path = MODELS_DIR / orig_name
                if orig_path.exists():
                    size = orig_path.stat().st_size / (1024**3)
                    mtime = datetime.fromtimestamp(orig_path.stat().st_mtime)
                    total_size += size
                    loaded += 1
                    print(f'✅ {name:30s} ЗАГРУЖЕНА - {size:.2f} GB (как {orig_name}, {mtime.strftime("%H:%M:%S")})')
                    orig_found = True
                    break
        if not orig_found:
            # Проверяем, есть ли частично загруженный файл
            temp_files = list(MODELS_DIR.glob(f'{filename}*')) + list(MODELS_DIR.glob(f'*{filename.split("_")[-1]}*'))
            if temp_files:
                for temp_file in temp_files:
                    if temp_file.stat().st_size > 1000000:  # Больше 1MB
                        temp_size = temp_file.stat().st_size / (1024**3)
                        percent = min(100, (temp_size / expected) * 100)
                        print(f'⏳ {name:30s} ЗАГРУЖАЕТСЯ - {temp_size:.2f} GB / {expected:.2f} GB ({percent:.1f}%)')
                        break
            else:
                print(f'⏸ {name:30s} ОЖИДАНИЕ')

print()
print('='*70)
print(f'📈 Прогресс: {loaded}/4 моделей загружено')
if loaded > 0:
    print(f'💾 Общий размер загруженных: {total_size:.2f} GB')
    remaining = 4 - loaded
    if remaining > 0:
        print(f'⏳ Осталось загрузить: {remaining} моделей (~{remaining * 6.5:.1f} GB)')
else:
    print('⚠️  Загрузка в процессе...')
print('='*70)

# Проверяем активный процесс
import subprocess
result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
if 'download_realistic_models.py' in result.stdout:
    print('🔄 Процесс загрузки активен')
else:
    print('⚠️  Процесс загрузки не найден (возможно завершился)')
EOF
