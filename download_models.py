#!/usr/bin/env python3
"""
Скрипт для загрузки моделей Stable Diffusion в Fooocus
"""

import os
from huggingface_hub import hf_hub_download
from pathlib import Path

# Путь к папке с моделями
MODELS_DIR = Path(__file__).parent / "models 12.07.29" / "checkpoints"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Список моделей для загрузки
MODELS_TO_DOWNLOAD = [
    {
        "repo_id": "cyberdelia/CyberIllustrious",
        "filename": "CyberIllustrious_V8.0_FP16.safetensors",
        "local_filename": "CyberIllustrious_V8.0_FP16.safetensors",
        "description": "CyberIllustrious V8.0 (SDXL) - фотореалистичная модель",
        "type": "SDXL"
    },
    {
        "repo_id": "TheImposterImposters/URPM-v2.3Final",
        "filename": "uberRealisticPornMerge_v23Final.safetensors",
        "local_filename": "URPM-v2.3Final.safetensors",
        "description": "URPM v2.3 Final (SD 1.5) - реалистичная модель",
        "type": "SD 1.5"
    },
    {
        "repo_id": "XpucT/Deliberate",
        "filename": "Deliberate_v6.safetensors",
        "local_filename": "Deliberate_v6.safetensors",
        "description": "Deliberate v6 (SD 1.5) - модель для коротких промптов",
        "type": "SD 1.5"
    }
    # Примечание: henmixreal доступен только в формате diffusers (не единый файл)
    # Для использования в Fooocus нужна конвертация или использование через API
]

def download_model(repo_id, filename, description, local_filename=None, **kwargs):
    """Загружает модель с Hugging Face"""
    if local_filename is None:
        local_filename = filename
    
    output_path = MODELS_DIR / local_filename
    model_type = kwargs.get('type', 'Unknown')
    
    # Проверяем, не загружена ли уже модель
    if output_path.exists():
        file_size = output_path.stat().st_size / (1024 * 1024 * 1024)  # GB
        print(f"✓ {description}")
        print(f"  Уже загружена: {local_filename} ({file_size:.2f} GB)")
        return True
    
    print(f"\n📥 Загрузка: {description}")
    print(f"   Репозиторий: {repo_id}")
    print(f"   Тип: {model_type}")
    print(f"   Файл: {filename}")
    print(f"   Сохранится как: {local_filename}")
    print(f"   Путь: {output_path}")
    print("   Это может занять некоторое время...")
    
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
        return False

def main():
    print("=" * 60)
    print("Загрузка моделей Stable Diffusion для Fooocus")
    print("=" * 60)
    print(f"\nПапка для моделей: {MODELS_DIR}")
    print(f"Всего моделей для загрузки: {len(MODELS_TO_DOWNLOAD)}\n")
    
    # Проверяем существующие модели
    existing_models = list(MODELS_DIR.glob("*.safetensors"))
    if existing_models:
        print("Существующие модели:")
        for model in existing_models:
            size = model.stat().st_size / (1024 * 1024 * 1024)
            print(f"  - {model.name} ({size:.2f} GB)")
        print()
    
    # Загружаем модели
    success_count = 0
    for model_info in MODELS_TO_DOWNLOAD:
        if download_model(**model_info):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"Загрузка завершена: {success_count}/{len(MODELS_TO_DOWNLOAD)} моделей")
    print("=" * 60)
    
    if success_count == len(MODELS_TO_DOWNLOAD):
        print("\n✓ Все модели успешно загружены!")
        print("\nПерезапустите Fooocus, чтобы увидеть новые модели в списке.")
    else:
        print(f"\n⚠ Некоторые модели не были загружены. Проверьте ошибки выше.")

if __name__ == "__main__":
    main()
