# Запуск локального Fooocus с вашими моделями в Google Colab

Чтобы в Colab использовать **ваш** Fooocus и **все подгруженные модели** (CyberIllustrious, URPM, Deliberate, SDXL Base/Refiner/Turbo, RealCoreXL и т.д.), нужно один раз загрузить папку Fooocus в Google Drive, затем открывать ноутбук и запускать его.

---

## Шаг 1. Подготовка папки на компьютере

На Mac нужно собрать папку Fooocus **без** тяжёлого окружения (venv), чтобы объём загрузки был разумным.

### Что включить

- Весь код: `webui.py`, `launch.py`, `entry_with_update.py`, папки `modules/`, `ldm_patched/`, `extras/`, `javascript/`, `css/`, `presets/`, `sdxl_styles/`, `wildcards/` и т.д.
- **Папку с моделями** — та, где у вас чекпоинты:
  - либо `models 12.07.29/` (в т.ч. `checkpoints/`, `loras/`, `clip_vision/` и т.д.),
  - либо скопируйте только нужное в одну папку `models/` (см. ниже).

### Что не загружать (сильно уменьшит размер)

- Папку **`venv/`** — в Colab зависимости ставятся заново.
- Папку **`.git/`** (если есть) — для Colab не обязательна.
- Временные и кэш: `outputs/`, `temp/`, большие логи — по желанию.

### Вариант через архив

1. В Finder откройте папку проекта и зайдите в `Fooocus`.
2. Выделите всё, кроме `venv` (и по желанию `.git`).
3. ПКМ → «Сжать» (получится `Archive.zip` или другое имя).
4. При необходимости переименуйте, например: `Fooocus_with_models.zip`.

Размер архива с моделями может быть **50–100+ ГБ** (зависит от числа чекпоинтов). Загрузка в Drive займёт время; можно оставить на ночь.

---

## Шаг 2. Загрузка в Google Drive

1. Откройте [Google Drive](https://drive.google.com/).
2. Создайте папку, например **`Fooocus`** (или оставьте имя как у вас в проекте).
3. **Вариант A:** загрузите готовый архив `Fooocus_with_models.zip` в эту папку.
4. **Вариант B:** загрузите содержимое папки Fooocus (без venv) прямо в папку на Drive.

После загрузки архива:

1. В Drive откройте папку, куда положили архив.
2. ПКМ по `Fooocus_with_models.zip` → «Открыть с помощью» → «Google Drive» (распаковка в облаке),  
   **или** распакуйте архив на компьютере и загрузите уже распакованную папку.

Итоговая структура на Drive должна быть такой (или аналогичной):

```
Мой диск/
  Fooocus/                    ← можно другое имя
    launch.py
    webui.py
    entry_with_update.py
    modules/
    ldm_patched/
    models 12.07.29/          ← ваши модели
      checkpoints/
        CyberIllustrious_V8.0_FP16.safetensors
        Deliberate_v6.safetensors
        SDXL_Base_1.0.safetensors
        ...
      loras/
      ...
    presets/
    ...
```

Если у вас модели лежат в папке с другим именем — ничего страшного, ноутбук ищет и `models 12.07.29/checkpoints`, и `models/checkpoints`.

---

## Шаг 3. Запуск в Colab

1. Откройте [Google Colab](https://colab.research.google.com/).
2. **File → Upload notebook** и выберите файл **`fooocus_colab_local_drive.ipynb`** из папки Fooocus вашего проекта.
3. В меню: **Runtime → Change runtime type**. В **Hardware accelerator** выберите **GPU** (лучше **T4**).
4. В первой ячейке с кодом задайте путь к папке Fooocus на Drive:
   - если папка лежит в корне «Моего диска» и называется `Fooocus`, оставьте:  
     `DRIVE_FOOOCUS_PATH = "Fooocus"`
   - если путь вложенный, например `Мои проекты/AI-modeli/Fooocus`, укажите:  
     `DRIVE_FOOOCUS_PATH = "Мои проекты/AI-modeli/Fooocus"`
5. Запустите ячейки по порядку (**Shift+Enter**):
   - подключение Drive и проверка пути к Fooocus;
   - обновление `config.txt` под Colab (пути к моделям);
   - установка зависимостей и запуск Fooocus.

При первом запуске Colab установит torch и зависимости (несколько минут). В конце в выводе появится ссылка вида:

```
Running on public URL: https://xxxxx.gradio.live
```

Откройте её в браузере — откроется ваш Fooocus со всеми моделями с Drive.

---

## Важно

- **Диск Colab и Drive:** модели читаются с Google Drive, поэтому первый запуск и переключение моделей могут быть медленнее, чем на локальном диске.
- **Сессия Colab:** при долгом простое сессия может оборваться; тогда перезапустите ячейку с `python launch.py ...` и снова откройте выданную ссылку.
- **config.txt:** ноутбук перезаписывает пути в `config.txt` под текущий запуск в Colab (чтобы работали пути к вашим моделям). Если потом будете запускать Fooocus на Mac, при необходимости восстановите свой `config.txt` из бэкапа.

---

## Если папка на Drive называется иначе

В ячейке с путём укажите полный путь от «Моего диска», например:

```python
DRIVE_FOOOCUS_PATH = "Мои проекты/AI-modeli/Fooocus"
```

или

```python
DRIVE_FOOOCUS_PATH = "Fooocus_with_models"   # если распаковали архив в папку с таким именем
```

Главное — внутри выбранной папки должны быть `launch.py` и папка с чекпоинтами (`models 12.07.29/checkpoints` или `models/checkpoints`).
