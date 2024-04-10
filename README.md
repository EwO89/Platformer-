

# Прыжки это здорово!

 "Прыжки это здорово!" - это 2d платформер, где игроку предстоит пройти через различные уровни, собирая монеты и избегая врагов. Как такового сложного сюжета и различного спектра врагов нет, смысл игры в том, чтобы собирать монеты,
проходить уровни, которые определенным интересным образом разнятся от уровня к уровню своей сложностью. Совокупность приятной музыки, графического сопровождения, легких и понятных интерфейсных элементов, моделей окружающих объектов,
минимализация количества багов - делают эту простую игру приятной для времяпровождения. Среднее время прохождения игры от игрока к игроку может разнится, но в среднем - 10 минут.

### Предварительные требования

Для запуска этой игры не потребуется мощного железа, игру потянет даже школьный компьютер из 2000-х!

**Корректная работа на устройствах MacOS не гарантируется**

### Установка

Шаги для запуска игры:

1. Клонируйте репозиторий или скачайте исходный код. Сделать это можно, например, в git bash:
   
 ```sh
  git clone https://github.com/EwO89/Platformer-.git
 ```
2. Установите необходимые зависимости:

  ```sh
  pip install -r requirements.txt
  ```
3. Запустите файл main.py и наслаждайтесь игрой!
   
 ```sh
  python main.py
 ```
### Используемые технологии (основные и ключевые)

1. Сразу начну с того, где тут база данных и есть ли вообще. Это мой первый проект, в который я решил не включать никакие СУБД для хранения состояний и данных, чтобы попробовать решения попроще, ведь и игра простая, грузить сюда технологии ради технологий я не хотел. В моей игре  я использую файловую систему для хранения данных, таких как уровни игры и прогресс игрока. Вместо классической базы данных, я применяю сериализацию объектов с помощью модуля pickle для сохранения состояний игровых объектов напрямую в файлы. Этот подход позволяет мне быстро сохранять и восстанавливать сложные структуры данных, например, списки и словари, что является удобным и эффективным решением для моего однопользовательского приложения. Когда игра загружается или переходит на новый уровень, я просто десериализую данные обратно в  объекты Python. Это решение отлично подходит для моей игры, так как оно просто в реализации и не требует сложной настройки СУБД или работы с сетевыми запросами.
2. Библиотека pygame 



