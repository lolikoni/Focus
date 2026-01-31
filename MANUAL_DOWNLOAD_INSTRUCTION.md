# Инструкция: Ручная загрузка моделей для Fooocus

Если на Mac Fooocus не может что-то скачать автоматически, вы можете скачать все необходимые файлы заранее вручную.

## Что уже есть у вас:

### ✅ Уже скачанные файлы:

1. **Базовая модель:** `realisticStockPhoto_v20.safetensors` (6.5 GB)
   - Расположение: `models/checkpoints/realisticStockPhoto_v20.safetensors`

2. **LoRA модель:** `SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors` (870 MB)
   - Расположение: `models/loras/SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors`

3. **VAE Approximate файлы:**
   - `xlvaeapp.pth` (209 KB)
   - `vaeapp_sd15.pth` (209 KB)
   - `xl-to-v1_interposer-v4.0.safetensors` (5.4 MB)

4. **Fooocus Expansion:**
   - `pytorch_model.bin` (335 MB)

## Автоматическая загрузка (скрипт)

Используйте готовый скрипт для загрузки всех файлов:

```bash
cd "/Users/nikitaamurcev/Documents/Мои проекты/AI-modeli/Fooocus"
./download_models_manual.sh
```

Скрипт автоматически:
- Проверит, какие файлы уже есть
- Скачает только недостающие файлы
- Разместит их в правильных папках

## Ручная загрузка (если скрипт не работает)

### 1. Базовая модель (уже есть)
- **Файл:** `realisticStockPhoto_v20.safetensors`
- **URL:** https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/realisticStockPhoto_v20.safetensors
- **Путь:** `Fooocus/models/checkpoints/realisticStockPhoto_v20.safetensors`
- **Размер:** ~6.5 GB

### 2. LoRA модель (уже есть)
- **Файл:** `SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors`
- **URL:** https://huggingface.co/mashb1t/fav_models/resolve/main/fav/SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors
- **Путь:** `Fooocus/models/loras/SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors`
- **Размер:** ~870 MB

### 3. VAE Approximate файлы (уже есть)

#### xlvaeapp.pth
- **URL:** https://huggingface.co/lllyasviel/misc/resolve/main/xlvaeapp.pth
- **Путь:** `Fooocus/models/vae_approx/xlvaeapp.pth`
- **Размер:** ~209 KB

#### vaeapp_sd15.pth
- **URL:** https://huggingface.co/lllyasviel/misc/resolve/main/vaeapp_sd15.pt
- **Путь:** `Fooocus/models/vae_approx/vaeapp_sd15.pth`
- **Примечание:** В URL файл называется `.pt`, но должен сохраняться как `.pth`
- **Размер:** ~209 KB

#### xl-to-v1_interposer-v4.0.safetensors
- **URL:** https://huggingface.co/mashb1t/misc/resolve/main/xl-to-v1_interposer-v4.0.safetensors
- **Путь:** `Fooocus/models/vae_approx/xl-to-v1_interposer-v4.0.safetensors`
- **Размер:** ~5.4 MB

### 4. Fooocus Expansion (уже есть)
- **Файл:** `pytorch_model.bin`
- **URL:** https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_expansion.bin
- **Путь:** `Fooocus/models/prompt_expansion/fooocus_expansion/pytorch_model.bin`
- **Размер:** ~335 MB
- **Примечание:** В URL файл называется `.bin`, но должен сохраняться как `pytorch_model.bin`

## Запуск без автоматической загрузки

После того, как все файлы загружены вручную, запускайте Fooocus с флагом `--disable-preset-download`:

```bash
cd "/Users/nikitaamurcev/Documents/Мои проекты/AI-modeli/Fooocus"
python3 entry_with_update.py --preset realistic --disable-preset-download
```

Этот флаг отключит автоматическую загрузку моделей из preset, и Fooocus будет использовать уже загруженные файлы.

## Команды для ручной загрузки (если нужны)

Если нужно скачать вручную через терминал:

```bash
cd "/Users/nikitaamurcev/Documents/Мои проекты/AI-modeli/Fooocus"

# Создание папок
mkdir -p models/checkpoints
mkdir -p models/loras
mkdir -p models/vae_approx
mkdir -p models/prompt_expansion/fooocus_expansion

# Базовая модель (если еще не скачана)
curl -L -o models/checkpoints/realisticStockPhoto_v20.safetensors \
    "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/realisticStockPhoto_v20.safetensors"

# LoRA модель (если еще не скачана)
curl -L -o models/loras/SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors \
    "https://huggingface.co/mashb1t/fav_models/resolve/main/fav/SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors"

# VAE Approximate файлы
curl -L -o models/vae_approx/xlvaeapp.pth \
    "https://huggingface.co/lllyasviel/misc/resolve/main/xlvaeapp.pth"

curl -L -o models/vae_approx/vaeapp_sd15.pth \
    "https://huggingface.co/lllyasviel/misc/resolve/main/vaeapp_sd15.pt"

curl -L -o models/vae_approx/xl-to-v1_interposer-v4.0.safetensors \
    "https://huggingface.co/mashb1t/misc/resolve/main/xl-to-v1_interposer-v4.0.safetensors"

# Fooocus Expansion
curl -L -o models/prompt_expansion/fooocus_expansion/pytorch_model.bin \
    "https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_expansion.bin"
```

## Проверка после загрузки

Проверьте, что все файлы на месте:

```bash
cd "/Users/nikitaamurcev/Documents/Мои проекты/AI-modeli/Fooocus"

ls -lh models/checkpoints/realisticStockPhoto_v20.safetensors
ls -lh models/loras/SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors
ls -lh models/vae_approx/*.pth
ls -lh models/vae_approx/*.safetensors
ls -lh models/prompt_expansion/fooocus_expansion/pytorch_model.bin
```

## Итог

После загрузки всех файлов запускайте Fooocus с флагом:
```bash
python3 entry_with_update.py --preset realistic --disable-preset-download
```

Это отключит автоматическую загрузку, и Fooocus будет использовать уже загруженные файлы.

---

**Примечание:** Судя по проверке, у вас уже есть все необходимые файлы! Попробуйте запустить с флагом `--disable-preset-download`.
