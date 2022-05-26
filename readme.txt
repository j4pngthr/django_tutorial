tutorial1
https://docs.djangoproject.com/ja/2.2/intro/tutorial01/
似てるの
https://programming-beginner-zeroichi.jp/articles/115

python manage.py runserver
でエラーが出る
→python3を使う
https://teratail.com/questions/237108
→bash_profileにaliasを登録

pollsを作ってから
python manage.py runserver
http://127.0.0.1:8000/
でPage not found
→
https://teratail.com/questions/91869

python manage.py runserver
Django開発サーバの起動

プロジェクトA
　アプリケーションA
プロジェクトB
　アプリケーションA
　アプリケーションB

python manage.py startapp polls
pollsはアプリケーション

モデルを変更
python manage.py makemigrations
変更のためのマイグレーションを作成
python manage.py migrate
データベースに変更を適用

sqlite3 db.sqlite3
.schema
...> ;
sqlite> .exist

python manage.py shell
from polls.models import Choice, Question
