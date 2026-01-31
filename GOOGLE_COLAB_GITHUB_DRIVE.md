# Fooocus в Colab: код с GitHub, модели с Drive

Так проще: код храните в GitHub, модели — один раз загружаете в Google Drive. В Colab клонируете репозиторий и подключаете папку с моделями с Drive (симлинк, без копирования).

---

## 1. Репозиторий на GitHub (только код)

В папке Fooocus уже есть **`.gitignore`**: в репозиторий не попадут `venv/`, папки `models/` и `models 12.07.29/`, `outputs/`, `config.txt` и т.д.

**На компьютере:**

1. Создайте репозиторий на GitHub (например, `fooocus` или `AI-modeli`).
2. В папке Fooocus выполните:
   ```bash
   cd /путь/к/AI-modeli/Fooocus
   git init
   git add .
   git commit -m "Fooocus: код без моделей"
   git remote add origin https://github.com/ВАШ_ЛОГИН/fooocus.git
   git push -u origin main
   ```
   (или `master` вместо `main`, если так у вас настроено.)

В репозитории будут только исходники и конфиги, без чекпоинтов.

---

## 2. Модели на Google Drive (один раз)

Загрузите на Drive **только папку с моделями**:

- либо папку **`models 12.07.29`** (или **`models`**) целиком,
- либо всю папку **Fooocus**, если удобнее — ноутбук найдёт внутри `models 12.07.29` или `models`.

Структура на Drive может быть такой:

```
Мой диск/
  Fooocus/              ← DRIVE_PATH в ноутбуке
    models 12.07.29/
      checkpoints/
        *.safetensors
      loras/
      ...
```

или отдельная папка только с моделями:

```
Мой диск/
  Fooocus_models/
    models 12.07.29/
      checkpoints/
      ...
```

В Colab вы потом укажете путь к этой папке (`Fooocus` или `Fooocus_models`).

---

## 3. Запуск в Colab

1. Откройте [Google Colab](https://colab.research.google.com/).
2. **File → Upload notebook** → выберите **`fooocus_colab_github_drive.ipynb`**.
3. **Runtime → Change runtime type → GPU** (T4).
4. В первой ячейке укажите:
   - **GITHUB_REPO** — ссылку на ваш репозиторий, например:  
     `https://github.com/ВАШ_ЛОГИН/fooocus.git`
   - **DRIVE_PATH** — путь на Drive к папке, где лежат модели:  
     `"Fooocus"` или `"Fooocus_models"` и т.п.
5. Запустите ячейки по порядку.

Ноутбук:

- клонирует код с GitHub в `/content/Fooocus`;
- монтирует Drive и создаёт симлинк на папку с моделями (без копирования десятков ГБ);
- обновляет `config.txt` и запускает `launch.py --share --always-high-vram`.

В конце в выводе будет ссылка вида `https://xxxxx.gradio.live` — откройте её в браузере.

---

## Плюсы такого варианта

- **Код** всегда актуален: `git pull` в Colab или перезапуск ячейки с `git clone` даёт последнюю версию с GitHub.
- **Модели** не дублируются: лежат на Drive, в Colab только симлинк.
- В GitHub не попадают тяжёлые файлы (лимит 100 МБ на файл, модели по 5–7 ГБ).
- Обновления кода делаете на компе, пушите в GitHub — в Colab при следующем запуске подтянете свежий код.
