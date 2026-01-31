#!/usr/bin/env python3
"""
Скрипт для загрузки моделей для генерации реалистичных фотографий
"""

import os
from huggingface_hub import hf_hub_download
from pathlib import Path
import sys

# Путь к папке с моделями
MODELS_DIR = Path(__file__).parent / "models 12.07.29" / "checkpoints"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Список моделей для реалистичных фотографий
REALISTIC_MODELS = [
    {
        "repo_id": "stabilityai/stable-diffusion-xl-base-1.0",
        "filename": "sd_xl_base_1.0.safetensors",
        "local_filename": "SDXL_Base_1.0.safetensors",
        "description": "SDXL Base 1.0 (SDXL) - официальная базовая модель для реалистичных фото",
        "type": "SDXL",
        "priority": "high"
    },
    {
        "repo_id": "stabilityai/stable-diffusion-xl-refiner-1.0",
        "filename": "sd_xl_refiner_1.0.safetensors",
        "local_filename": "SDXL_Refiner_1.0.safetensors",
        "description": "SDXL Refiner 1.0 (SDXL) - для улучшения качества реалистичных фото",
        "type": "SDXL",
        "priority": "high"
    },
    {
        "repo_id": "stabilityai/sdxl-turbo",
        "filename": "sd_xl_turbo_1.0_fp16.safetensors",
        "local_filename": "SDXL_Turbo_1.0_FP16.safetensors",
        "description": "SDXL Turbo 1.0 FP16 (SDXL) - быстрая генерация реалистичных фото (1-4 шага)",
        "type": "SDXL",
        "priority": "high"
    },
    {
        "repo_id": "rityak/RealCoreXL",
        "filename": "RealCoreXL.safetensors",
        "local_filename": "RealCoreXL.safetensors",
        "description": "RealCoreXL (SDXL) - реалистичные и любительские фото стили",
        "type": "SDXL",
        "priority": "medium"
    }
    # Примечание: Realism SDXL доступна только в формате diffusers
    # Для Fooocus нужны единые файлы .safetensors
]

def download_model(repo_id, filename, description, local_filename=None, **kwargs):
    """Загружает модель с Hugging Face"""
    if local_filename is None:
        local_filename = filename
    
    output_path = MODELS_DIR / local_filename
    model_type = kwargs.get('type', 'Unknown')
    priority = kwargs.get('priority', 'low')
    
    # Проверяем, не загружена ли уже модель
    if output_path.exists():
        file_size = output_path.stat().st_size / (1024 * 1024 * 1024)  # GB
        print(f"✓ {description}")
        print(f"  Уже загружена: {local_filename} ({file_size:.2f} GB)")
        return True
    
    print(f"\n📥 Загрузка: {description}")
    print(f"   Репозиторий: {repo_id}")
    print(f"   Тип: {model_type} | Приоритет: {priority}")
    print(f"   Файл: {filename}")
    print(f"   Сохранится как: {local_filename}")
    print(f"   Путь: {output_path}")
    print("   Это может занять некоторое время...")
    sys.stdout.flush()
    
    try:
        # Загружаем модель
        downloaded_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=str(MODELS_DIR),
        )
        
        # Переименовываем файл, если нужно
        if local_filename != filename and os.path.exists(downloaded_path):
            final_path = MODELS_DIR / local_filename
            if os.path.exists(final_path):
                os.remove(final_path)  # Удаляем старый файл, если есть
            os.rename(downloaded_path, final_path)
            downloaded_path = final_path
        
        # Проверяем размер файла
        if os.path.exists(downloaded_path):
            file_size = os.path.getsize(downloaded_path) / (1024 * 1024 * 1024)  # GB
            print(f"✓ Успешно загружено: {local_filename} ({file_size:.2f} GB)")
            return True
        else:
            print(f"❌ Ошибка: файл не найден после загрузки")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка при загрузке {filename}: {str(e)}")
        print(f"   Попробуйте проверить доступность репозитория: https://huggingface.co/{repo_id}")
        return False

def main():
    print("=" * 60)
    print("Загрузка моделей для генерации реалистичных фотографий")
    print("=" * 60)
    print(f"\nПапка для моделей: {MODELS_DIR}")
    print(f"Всего моделей для загрузки: {len(REALISTIC_MODELS)}\n")
    
    # Проверяем существующие модели
    existing_models = list(MODELS_DIR.glob("*.safetensors"))
    if existing_models:
        print("Существующие модели:")
        for model in existing_models:
            size = model.stat().st_size / (1024 * 1024 * 1024)
            print(f"  - {model.name} ({size:.2f} GB)")
        print()
    
    # Сортируем по приоритету
    high_priority = [m for m in REALISTIC_MODELS if m.get('priority') == 'high']
    medium_priority = [m for m in REALISTIC_MODELS if m.get('priority') == 'medium']
    
    print("Приоритет загрузки:")
    print(f"  Высокий: {len(high_priority)} моделей")
    print(f"  Средний: {len(medium_priority)} моделей")
    print()
    
    # Загружаем модели по приоритету
    all_models = high_priority + medium_priority
    success_count = 0
    
    for model_info in all_models:
        if download_model(**model_info):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"Загрузка завершена: {success_count}/{len(REALISTIC_MODELS)} моделей")
    print("=" * 60)
    
    if success_count == len(REALISTIC_MODELS):
        print("\n✓ Все модели успешно загружены!")
        print("\nПерезапустите Fooocus, чтобы увидеть новые модели в списке.")
    else:
        print(f"\n⚠ Некоторые модели не были загружены. Проверьте ошибки выше.")
        print("   Возможно, нужно проверить точные имена файлов в репозиториях.")

if __name__ == "__main__":
    main()
