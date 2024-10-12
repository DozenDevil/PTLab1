# Лабораторная 1 по дисциплине "Технологии программирования"

#### У данной лабораторной работы были следующие цели:
1. Познакомиться c распределенной системой контроля версий кода Git и ее функциями;
2. Познакомиться с понятиями «непрерывная интеграция» (CI) и «непрерывное развертывание» (CD), определить их место в современной разработке программного обеспечения;
3. Получить навыки разработки ООП-программ и написания модульных тестов к ним на современных языках программирования;
4. Получить навыки работы с системой Git для хранения и управления версиями ПО;
5. Получить навыки управления автоматизированным тестированием программного обеспечения, расположенного в системе Git, с помощью инструмента GitHub Actions.

#### Описание проекта
Проект состоит из комплекса программ и тестов, которые вместе составляют программу, позволяющую считывать оценки студентов и обрабатывать их. Основа программы была получина из последовательного выполнения основных положений из методички. Модификации были добавлены согласно индивидуальному заданию под вариантом 8.

Ход работы описан в истории коммитов.

#### Диаграмма классов
![alt text](https://github.com/DozenDevil/PTLab1/blob/main/ClassDiagram.png?raw=true)

#### Используемые ресурсы
- **Языки:** Pyhon;
- **Библиотеки:** pytest (создание тестов), pycodestyle (проверка соответствия кода стандартам форматирования), pyyaml (упрощение работы с файлами YAML для индивидуального задания), numpy (вычисление квартилей для индивидуального задания);
- **Технологии:** Anaconda (консольный интерпритатор Python), git (консольный интерфейс СКВ для GitHub), Notepad++ (текстовый редактор), GitHub Desktop (альтернатива git), PyCharm (среда разработки Python-приложений), StarUML (ПО для создания UML-диаграмм).

#### Ответы на контрольные вопросы
**1. Системы управления версиями: понятие и назначение. Локальные, централизованные и распределенные системы контроля версий, их особенности. Система Git.**

СКВ - это системы, которые позволяют отслеживать изменения в приложении, публиковать открытый исходный код, а также синхронизировать версии между несколькими разработчиками.
Локальные СКВ представляют из себя простейшую базу данных, которые хранят записи обо всех изменениях в файлах.
Централизованные СКВ предназначены для решения основной проблемы локальных систем контроля версий. Для организации такой системы контроля версий используется единственный сервер, который содержит все версии файлов. Клиенты, обращаясь к этому серверу, получают из этого централизованного хранилища.
Распределённые СКВ подразумевают, что клиент выкачает себе весь репозиторий целиком заместо выкачки конкретных интересующих клиента файлов. Если откажет любая копия репозитория, то это не приведет к потере кодовой базы, поскольку она может быть восстановлена с компьютера любого разработчика. Каждая копия является полным бэкапом данных. 

Git — это бесплатная распределенная система управления версиями с открытым исходным кодом, предназначенная для быстрой и эффективной обработки любых проектов.

**2. Создание репозитория в Git. Клонирование репозитория.**

Для создания репозитория используется команда `git init`. Для клонирования - `git clone`.

**3. Запись изменений в репозиторий Git. Зафиксированное, модифицированное и индексированное состояние файлов. Основные команды Git.**

Изменения в репозиторий фиксируются с помощью `git commit`, а публикуются с помощью `git push`. Зафиксированные файлы - изменённые и отмеченные в истории изменений с помощью коммита, модифицированные - изменённые, но неотмеченные коммитом, индексированные - впервые попавшие в список отслеживаемых.

**4. Основные типы лицензий, поддерживаемых Git. Особенности их использования.**

Лицензия позволит защитить авторские права и опишет условия использования репозитория другими людьми или компаниями. Схема выбора типа лицензии:

Свободное использование? Если да, то лицензия свободная и может быть:

условно-бесплатной — ShareWare, TrialWare, Demoware;
открытой — Open Source;
бесплатной — Nagware/Begware, Postcardware, Adware, Denationware, Freeware, GPL.
Если нет, то лицензия проприетарная и может быть:

платной — Commercial;
условно-бесплатной.
Схема выбора типа лицензии.

![Схема выбора типа лицензии](https://github.com/user-attachments/assets/04d21ab0-e53d-4214-a385-abb23d9fd43f)

Схема выбора открытой лицензии из числа самых распространённых:

![Схема выбора открытой лицензии](https://github.com/user-attachments/assets/d10a6adb-11f0-4c39-ad85-4ecc4ffe85f8)


Требуется указать имя автора? Если нет, это The Unilicense. Если да, переходите ко второму или третьему пунктам.
Изменённые файлы должны быть помечены? Если нет, лицензия на условиях первоначальной? Да → лицензия не определена. Нет → название должно отличаться → нет → это BSD или MIT. Если название не должно отличаться, то это Apache software license.
Изменённые файлы должны быть помечены? Если да, то лицензия на условиях первоначальной? В случае нет лицензия не определена. Когда ответ да, указана ли территория распространения? Нет → GPL, да → Mozilla public license.
Схема выбора открытой лицензии. Описание перед скриншотом.

**5. Понятия «непрерывная интеграция» (CI) и «непрерывное развертывание» (CD). Роль процессов CI/CD в современной разработке ПО.**

Непрерывная интеграция — это методология разработки и набор практик, при которых в код вносятся небольшие изменения с частыми коммитами. И поскольку большинство современных приложений разрабатываются с использованием различных платформ и инструментов, то появляется необходимость в механизме интеграции и тестировании вносимых изменений.

С технической точки зрения, цель CI — обеспечить последовательный и автоматизированный способ сборки, упаковки и тестирования приложений. При налаженном процессе непрерывной интеграции разработчики с большей вероятностью будут делать частые коммиты, что, в свою очередь, будет способствовать улучшению коммуникации и повышению качества программного обеспечения.

Непрерывная поставка начинается там, где заканчивается непрерывная интеграция. Она автоматизирует развертывание приложений в различные окружения: большинство разработчиков работают как с продакшн-окружением, так и со средами разработки и тестирования.

**6. Инструмент GitHub Actions и его функции.**

GitHub Actions — это платформа непрерывной интеграции и непрерывной поставки (CI/CD), которая позволяет автоматизировать конвейер сборки, тестирования и развертывания. Вы можете создавать рабочие процессы для построения и тестирования каждого запроса на вытягивание в репозиторий или развертывания объединенных запросов на вытягивание в рабочую среду.

GitHub Actions выходит за рамки только DevOps и позволяет запускать рабочие процессы, когда в репозитории происходят определенные события. Например, можно запустить рабочий процесс для автоматического добавления соответствующих меток, когда кто-то создает проблему в репозитории.

GitHub предоставляет виртуальные машины Linux, Windows и macOS для выполнения рабочих процессов, либо вы можете разместить собственные локальные средства выполнения в собственном центре обработки данных или облачной инфраструктуре.

#### Вывод
Научился разрабатывать приложения в парадигме CI/CD в рамках СКВ.
