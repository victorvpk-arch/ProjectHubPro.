
---

### Шаг 2. Перенесите скачанный файл в репозиторий и отправьте на GitHub (1 команда в `cmd`)
После того как вы нажали синюю кнопку **«Скачать код»**, откройте `cmd` (`Win + R` → `cmd` → `Enter`) и вставьте одну строку:

```bat
copy /y "%USERPROFILE%\Downloads\block_*.dat" "C:\ProjectHub_Repo\ProjectHubPro.py" && cd /d C:\ProjectHub_Repo && git add ProjectHubPro.py && git commit -m "Release v4.0.0" && git push -u origin main
