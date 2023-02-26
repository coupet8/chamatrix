1. Приложение по расчету матрицы: **new_client**
2. Авторизация и регистрация: **user**
3. Страница с формой и кнопкой "Расчитать": **new_client/templates/new_client/index.html**
4. **matrix.py** - этот скрипт осуществляет расчет всех значений по вводу даты рождения
5. **add_text.py** - этот скрипт осуществляет вставку рассчитанных значений в шаблон картинки формата .png и сохранение картинки под названием **"matrix_with_text.png"**
6. **personal_matrix.py** - этот скрипт формирует окончательный документ. В шаблоне **"your_matrix_template.docx"** происходит замена значений на персональный текст из БД **db.sqlite3** по результатам расчета значений. Также в этот шаблон вставляется картинка, получаемая с помощью **add_text.py**, документ сохраняется локально под названием **"your_matrix_1.docx"**