from data import db_session
from data.news import News, Category
from data.users import Users, UsersTypes


def add_users_types(db_sess):
    """
    Создаем типы пользователей
    :param db_sess:
    :return:
    """
    types1 = UsersTypes(id=1,
                        users_type="Администраторы")
    types2 = UsersTypes(id=2,
                        users_type="Обычные пользователи")
    types3 = UsersTypes(id=3,
                        users_type="Пользователи только для чтения")
    db_sess.add(types1)
    db_sess.add(types2)
    db_sess.add(types3)
    db_sess.commit()


def add_user(db_sess):
    """
    для теста создаем юзеров
    :param db_sess:
    :return:
    """
    user1 = Users(name="Редактор",
                  login="admin",
                  email="email@email.ru",
                  user_type_id=1,
                  hashed_password='12345'
                  )
    user2 = Users(name="Обычный пользователь",
                  login="user",
                  email="email1@email.ru",
                  user_type_id=2,
                  hashed_password='123'
                  )
    user3 = Users(name="Прохожий",
                  login="user2",
                  email="email2@email.ru",
                  user_type_id=2,
                  hashed_password='123'
                  )
    user1.set_password(user1.hashed_password)
    user2.set_password(user2.hashed_password)
    user3.set_password(user3.hashed_password)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()


def add_category(db_sess):
    """
    для теста создаем категории
    :param db_sess:
    :return:
    Главное
    """
    raw = ["Россия",
           "Мир",
           "Экономика",
           "Наука и техника",
           "Культура",
           "Спорт",
           "Интернет и СМИ",
           "Ценности",
           "Путешествия",
           "Из жизни",
           "Дом"]
    for n, name in enumerate(raw, 1):
        category = Category(name=name,
                            id=n)
        db_sess.add(category)

    db_sess.commit()


def add_news(db_sess):
    """
    для теста создаем Новости
    :param db_sess:
    :return:
    """
    raw = [
        ("Участвовавший в боях под Ленинградом немецкий солдат описал войну и русских",
         """Немецкий солдат Вальтер Годель, который воевал в составе 18-й армии группы «Север» и участвовал в боях под Ленинградом, описал войну в письмах, которые были опубликованы газетой Die Welt.
         <br>
         <img alt="" class="g-picture" rel="image_src" style="max-width: 420px; width: 420px; height: 280px;" src="https://icdn.lenta.ru/images/2021/05/06/17/20210506173257604/pic_817ae58822b4fc1a57db3ec4c2efa5c0.jpg" width="420" height="280">
         <br>
         Годель, будучи сыном простого немецкого крестьянина, который прежде не выезжал за пределы родной деревни в Швабии, писал родным, что путь на Восточный фронт стал для него «лучшим впечатлением за всю жизнь». Также он называл блокаду Ленинграда «неплохим» событием.
         <br>
         «У меня все всегда замечательно. Вчера состоялось мое первое боевое крещение», — писал солдат в письме, которое прислал домой в сентябре 1941 года. В статье отмечается, что сначала восторг Годеля разделяли многие солдаты вермахта, однако вскоре им пришлось познакомиться с другой стороной событий.""",
         1),
        ("Прожившие в браке 68 лет супруги умерли с разницей в 72 часа",
         """Мужчина и женщина умерли друг за другом с разницей в 72 часа после 68 лет совместной жизни. Об этом сообщает газета Mirror.
<br>
27 сентября Бренда Стадд (Brenda Studd) скончалась от сепсиса, вызванного осложнениями COVID-19. Как сообщает газета, после того, как муж узнал о ее смерти, он ни разу больше не заговорил.
<br>
30 сентября Терренс Стадд (Terrance Studd) умер от рака поджелудочной железы. Отмечается, что в момент смерти он плакал и держал в руках слепок руки жены. На момент смерти обоим супругам было по 83 года.
<br>
Дочь пожилой пары Джули Макклуни (Julie Mccluney) отметила, что после смерти Бренды ее отец сдался и перестал бороться. «Они были просто счастливы и довольны тем, что любили простые вещи: друг друга, танцы, рестораны, оперу и лото», — добавила она.
         """,
         1),
        ("Генсек НАТО заявил о десятках тысяч российских военных у границ с Украиной",
         """
         <img alt="" class="g-picture" rel="image_src" style="max-width: 420px; width: 420px; height: 280px;" src="https://icdn.lenta.ru/images/2021/05/06/14/20210506141852318/pic_fcebf97bd96d14a7062e97ba74f30d12.jpg" width="420" height="280">
         <br>
         ️После отвода российских войск от границы с Украиной там еще остаются десятки тысяч военных. Об этом заявил генеральный секретарь НАТО Йенс Столтенберг, отметив, что это больше, чем было до обострения ситуации. Его слова передает ТАСС.
<br>
«Мы будем обсуждать Россию. Мы зафиксировали отвод части российских военных от границы с Украиной, однако десятки тысяч российских военных остаются возле нее и на Украине (под этим НАТО подразумевает войска РФ в Крыму, который альянс считает частью украинской территории — прим. "Ленты.ру"). В целом остается значительное российское военное присутствие в регионе, там остается гораздо больше российских войск, чем до недавнего обострения ситуации», — сказал генсек альянса по прибытии на встречу министров обороны стран Евросоюза.
         """,
         2),
        ("Блинкен пообещал ответить России на агрессию и захотел стабильных отношений",
         """Вашингтон хочет стабильных отношений с Москвой. Об этом госсекретарь США Энтони Блинкен заявил в интервью BBC News.
<br>
По его словам, американская сторона обещает отвечать на безрассудные или агрессивные действия России. В то же время, «мы бы предпочли более стабильные и предсказуемые отношения», указал дипломат.
         """,
         2),
        ("«Это была отличная сделка»",
         """Смешные картинки, забавные видео и старые твиты превратились в объекты успешного инвестирования. Короткий ролик теперь можно продать за сотни тысяч долларов, а пиксельные аватары уходят за миллионы. На торги выставляются даже твиты или гифки, которые видели, возможно, все пользователи интернета. И все это — из-за NFT. Технология, работающая на блокчейне, фактически является сертификатом, подтверждающим владение цифровым объектом, который может сохранить к себе на компьютер любой человек. Однако владелец у него благодаря NFT будет только один. И за это право владения люди уже платят огромные деньги. Жажда цифрового признания — в материале «Ленты.ру».
        <br> 
        <img alt="" class="g-picture" rel="image_src" style="max-width: 600px; width: 600px; height: 400px;" src="https://icdn.lenta.ru/images/2021/04/27/16/20210427163138131/detail_9b31eaf4376cdff03e0ba1bcaa826a01.jpg" width="600" height="400">
        <br>
         Появление NFT-объекта на аукционе Christie's можно считать признанием технологии, которая появилась в 2017 году, а заставила о себе говорить в 2020-м. NFT (Non-Fungible Token, или невзаимозаменяемый токен) работает на основе блокчейна и является по сути уникальным сертификатом, привязанным к цифровому объекту — картине, ролику, гифке, тексту. От криптовалюты его отличает та самая «невзаимозаменяемость»: условный биткоин можно обменять на точно такой же биткоин, но два идентичных NFT найти нельзя.
<br>
Подобный «документ» содержит в себе сведения о прикрепленном объекте и хранится на тысячах компьютеров, а значит, доступ к нему есть у каждого. Соответственно, пользователи в любой момент могут узнать, кому эксклюзивно принадлежит тот или иной токен — и сам объект. Возможность присвоения объектов привела к буму коллекционирования цифровых предметов искусства: теперь их можно продавать, покупать и перепродавать.
         """,
         3),

        ("Юрист раскрыл способы обмана россиян банками",
         """Многие банки используют уловки, пользуясь отсутствием у клиентов финансового образования и нежеланием их вчитываться в текст договора. Об этом агентству «Прайм» рассказал юрист Павел Уткин.
<br>
<img alt="" class="g-picture" rel="image_src" style="max-width: 420px; width: 420px; height: 280px;" src="https://icdn.lenta.ru/images/2021/05/06/03/20210506035624299/pic_900920e63e2b476bab408ec52a4d64f3.jpg" width="420" height="280">
<br>
В частности, он указал на такой финансовый инструмент как ипотека. «Здесь способов может быть несколько — это повышение ставки в случае допущения просрочек, навязывание различных страховых продуктов или открытие якобы бесплатной кредитной карты бонусом».
<br>
Еще один популярный способ обмана клиентов — это завышенная ставка по вкладам. Суть заключается в том, что повышенная ставка будет действовать не более трех месяцев, а после этого она опустится много ниже той, по которой вклад был открыт до этого, пояснил Уткин.
         """,
         3),

        ("Взяли высоту",
         """
         Основатель, генеральный и технический директор Rocket Lab Питер Бек родился в Новой Зеландии в семье директора музея и учительницы. Глава компании не получил университетского образования, хотя с детства планировал строить ракеты. Большинство инженерных знаний, необходимых для создания ракет, Бек освоил самостоятельно. Возможно, именно поэтому в 2019 году бизнесмен и инженер получил должность адъюнкт-профессора аэрокосмической инженерии в Оклендском университете (Новая Зеландия).
         <br>
         <img alt="Ракета Electron на пусковом столе" style="max-width: 620px; width: 620px; height: 420px; width: 100%; height: auto;" src="https://icdn.lenta.ru/images/2021/04/29/21/20210429211001209/pic_25688440a48a61637c4b3108521a0f5a.jpg" width="620" height="420">
         <br>
         В ноябре 2009 года, три года спустя после основания Rocket Lab, компания запустила свою первую ракету, достигнувшую космоса. Одноступенчатая Ātea-1 была способна поднять нагрузку массой до 2 килограммов на высоту до 150 километров. В длину ракета достигала 6 метров, в диаметре — 15 сантиметров. Стартовая масса носителя составляла 60 килограммов.
         """,
         4),

        ("В Африке нашли древнейшее захоронение человека",
         """Археологи обнаружили самое древнее из известных человеческих захоронений в Африке. Об этом сообщает Reuters.
         <br>
         <img alt="" class="g-picture" rel="image_src" style="max-width: 420px; width: 420px; height: 280px;" src="https://icdn.lenta.ru/images/2021/05/06/13/20210506132506007/pic_3724f4e292e97704d2f48b236a676747.jpeg" width="420" height="280">
         <br>
Во время раскопок в пещере Панга-я-Саиди, расположенной недалеко от побережья Кении, исследователи нашли останки ребенка возрастом около 2,5-3 лет. Установить пол погибшего исследователи не смогли, поскольку в раннем возрасте кости мальчиков и девочек практически идентичны, а необходимые для анализа фрагменты ДНК не сохранились. Исследователи назвали обнаруженного малыша Мтото, что в переводе с суахили означает «ребенок». На основании экспертизы ученые пришли к выводу, что он умер около 78 тысяч лет назад во времена среднего каменного века.
         <br>
Лабораторные исследования показали, что останки поместили в погребальную яму в согнутом положении. Под голову ребенку положили опору или подушку, а сверху тело укрыли листьями и шкурами животных, которые к настоящему времени истлели.
         <br>
Ученые предполагают, что ритуал свидетельствует об особом значении, которое люди того времени придавали погребению. Это может подтвердить гипотезу исследователей о том, что при захоронении проводился особый ритуал, а значит труп был закопан преднамеренно.
         """,
         4),

        ("Директор Моргенштерна прокомментировал слухи об отправке рэпера в армию",
         """
         Концертный директор рэпера Моргенштерна в беседе с 5-tv.ru заявил, что команда артиста пока не принимает никакие новые заявки на мероприятия. Так менеджер прокомментировал слухи об отправке музыканта в армию.
         <br>
«Пока все на стопе», — добавил собеседник канала.
         <br>
Как отмечает 5-tv.ru, слухи об отправке Моргенштерна в армию возникли на фоне публикаций издания PeopleTalk, 4 и 5 мая разместившего видеозаписи, на которых запечатлен похожий на артиста мужчина. В первом ролике виден сидящий на стуле призывник, которому бреют голову, и, как пишет PeopleTalk, он имеет внешнее сходство с Моргенштерном, хотя на кадрах разобрать какие-либо детали невозможно. На втором видео, снятом якобы на построении, запечатлены военнослужащие в зимнем обмундировании — теплой форме и шапках. Это нетипичное для начала мая обстоятельство: в последние годы в воинских частях и учреждениях Московского региона переход на летнюю форму одежды осуществляется, как правило, в первой половине апреля.
         """,
         5),

        ("Выбраны вакцины для участников Олимпиады в Токио",
         """
         <img alt="" class="g-picture" rel="image_src" style="max-width: 420px; width: 420px; height: 280px;" src="https://icdn.lenta.ru/images/2021/05/06/17/20210506172632529/pic_ab88d5926c5a79598efe96c4db9f7d8e.jpg" width="420" height="280">
         <br>
         Международный олимпийский комитет (МОК) выбрал вакцины для участников Олимпийских игр 2021 года в японском Токио. Об этом сообщается на сайте организации.
         <br>
В МОК заявили, что участники Олимпийских и Паралимпийских игр в Токио смогут привиться от коронавируса двумя видами вакцин — Pfizer и BioNTech. «Это делается не только для обеспечения безопасной среды во время Игр, но и из уважения к жителям Японии», — говорится в сообщении комитета.
         """,
         6),

        ("Трамп назвал позором для США блокировку его аккаунтов в соцсетях",
         """
         <img alt="" class="g-picture" rel="image_src" style="max-width: 420px; width: 420px; height: 280px;" src="https://icdn.lenta.ru/images/2021/05/05/18/20210505185925700/pic_01aad30824101ee2b07693b0c34f23ba.jpg" width="420" height="280">
         <br>
         Бывший президент США Дональда Трамп назвал «абсолютным позором» для Соединенных Штатов сохранение блокировки его аккаунтов в социальных сетях, передает ТАСС.
<br>
«Эти компании социальных сетей должны заплатить политическую цену, и им больше никогда нельзя позволять разрушать и превращать в руины наш выборный процесс», — заявил Трамп.
<br>
5 мая Надзорный совет Facebook принял решение сохранить блокировку аккаунтов бизнесмена в Facebook и Instagram, однако рекомендовал вновь рассмотреть этот вопрос в шестимесячный срок. В совете отметили, что в случае принятия решения о восстановлении аккаунтов, это должно быть сделано в соответствии с правилами, применяемыми к другим пользователям. Соответствующее решение было опубликовано на его сайте в среду, 5 мая.
<br>
7 января 2021 года главные мировые соцсети заблокировали аккаунты Трампа. Речь идет о Twitter, YouTube, Facebook, Instagram и Twitch. Блокировки прошли после беспорядков, которые сторонники республиканца учинили 6 января в Капитолии.
<br>
Ранее сообщалось, что бывший президент США обнародовал собственный сайт. Ресурс называется From the Desk of Donald J. Trump («С рабочего стола Дональда Трампа»). На нем Трамп собирается публиковать обращения к сторонникам.
         """,
         7),
    ]

    for line in raw:
        news = News(content=line[1],
                    category_id=line[2],
                    title=line[0],
                    is_published=True,
                    user_id=1)
        db_sess.add(news)
    db_sess.commit()


def main():
    db_session.global_init("db/base.db")
    db_sess = db_session.create_session()
    add_users_types(db_sess)
    add_user(db_sess)
    add_category(db_sess)
    add_news(db_sess)


if __name__ == '__main__':
    main()