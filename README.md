# grocery

Установка (для пользователей операционных систем семейства MacOs/Linux):

Открыть терминал или консоль и перейти в нужную Вам директорию
Прописать команду git clone git@github.com:edzen12/grocery.git

Если Вы используете https, то: git clone https://github.com/edzen12/grocery.git

Прописать следующие команды:


python3 -m venv ДиректорияВиртуальногоОкружения
source ДиректорияВиртуальногоОкружения/bin/activate
Перейти в директорию django3-ecommerce

pip install -r requirements.txt
python manage.py migrate


Запустить сервер - python manage.py runserver

Не забудьте создать директорию media, куда будут сохраняться изображения для товара
