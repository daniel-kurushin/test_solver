def lexema_id_by_inf(cur, lexema):
	cur.execute('select id from lexema where infinitive = "%s";' % (lexema))
	for row in cur.fetchall():
		return row [0]
	return 0

def denotat_id_by_lexema_id(cur, id_lexema):
	ret = []
	cur.execute('select id_den from lexema_to_denotat where id_lexema = %s;' % (id_lexema))
	for row in cur.fetchall():
		ret += [row[0]]
	return ret

def relation_by_den_id(cur, id_from, id_to):
	ret = []
	cur.execute('select id_how from relation where id_from = %s and id_to = %s;' % (id_from, id_to))
	for row in cur.fetchall():
		ret += [row[0]]
	return ret

def denotat_title_by_id(cur, id):
	cur.execute('select title from denotat where id = %s;' % (id))
	for row in cur.fetchall():
		return row[0]
	return 0

example_text = u' Компьютер  –  это машина (в основном электронная), которая\
может принимать информацию (ввод) и вносить изменения в информацию (обрабатывать\
ее) для создания новой информации (вывода). Компьютеры существовали на\
протяжении большей части человеческой истории. Примерами ранних компьютеров\
являются астролябия и счеты. На компьютере есть четыре основных этапа обработки:\
они вводятся, хранятся, выводятся и обрабатываются.'

example_text = u'Для программной реализации логическое программирование\
использует язык пролог.  Программы на прологе включает в себя такие объекты,\
как факты, правила и вопросы. Факты в прологе это истинные значения, правила это\
заключения, а вопросы это цель. Обычно, правила состоят из предикатов.'

def example_tables(conn,cursor,table):
	if table == "rootobject":
		print("create table %s" % table)
		cursor.execute("create table rootobject (id integer primary key autoincrement not null, title varchar(255))")
		return True
	if table == "relation":
		print("create table %s" % table) # Отношения
		cursor.execute("create table relation (id integer primary key autoincrement not null, id_from integer references denotat (id), id_to integer references denotat (id), id_how integer references denotat (id), weight float, direction integer)")
		return True
	if table == "denotat":              # Денотат
		print("create table %s" % table)
		cursor.execute("create table denotat (id integer primary key autoincrement not null, title varchar(255))")
		return True
	if table == "lexema":                 # Слово
		print("create table %s" % table)
		cursor.execute("create table lexema (id integer primary key autoincrement not null, infinitive varchar(255), linguistic_characteristics_word varchar(255))")
		return True
	if table == "lexema_to_denotat":    # Таблица связей
		print("create table %s" % table)
		cursor.execute("create table lexema_to_denotat (id integer primary key autoincrement not null, id_den integer references denotat (id), id_lexema integer references lexema (id), weight float)")
		return True
	if table == "argument":             #Аргумент
		print("create table %s" % table)
		cursor.execute("create table argument (id integer primary key autoincrement not null, key_collocation varchar(255))")
		return True
	if table == "scopos":               # Скопос
		print("create table %s" % table)
		cursor.execute("create table scopos (id integer primary key autoincrement not null, the_target_audience varchar(255))")
		return True
	if table == "question":             # Вопрос
		print("create table %s" % table)
		cursor.execute("create table question (id integer primary key autoincrement not null, user_request varchar(255))")
		return True
	if table == "text_problematics":    # Проблематика текста
		print("create table %s" % table)
		cursor.execute("create table text_problematics (id integer primary key autoincrement not null, objectives varchar(255), tasks varchar(255))")
		return True
	if table == "dictionary":           # Словарь
		print("create table %s" % table)
		cursor.execute("create table dictionary (id integer primary key autoincrement not null, id_lexema integer references lexema (id), description text)")
		return True
	if table == "collocation":          # Словосочетание
		print("create table %s" % table)
		cursor.execute("create table collocation (id integer primary key autoincrement not null, linguistic_characteristics_collocation varchar(255))")
		return True
	if table == "text":                 # Текст
		print("create table %s" % table)
		cursor.execute("create table text (id integer primary key autoincrement not null, caption varchar(255), author varchar(255), output varchar(255))")
		return True
	if table == "subject_area":         # Предметная область
		print("create table %s" % table)
		cursor.execute("create table subject_area (id integer primary key autoincrement not null, name_area varchar(255), deskription_area varchar(255))")
		return True
	if table == "key_words":            # Ключевые слова
		print("create table %s" % table)
		cursor.execute("create table key_words (id integer primary key autoincrement not null, repetition_rate varchar(255), science_area varchar(255))")
		return True
	if table == "figure_of_speech":     # Устойчивые выражения
		print("create table %s" % table)
		cursor.execute("create table figure_of_speech (id integer primary key autoincrement not null, linguistic_characteristics_of_speech varchar(255))")
		return True
	if table == "sentence":             # Предложение
		print("create table %s" % table)
		cursor.execute("create table sentence (id integer primary key autoincrement not null, linguistic_characteristics_sentence varchar(255))")
		return True
	if table == "research_topic":       # Область науки
		print("create table %s" % table)
		cursor.execute("create table research_topic (id integer primary key autoincrement not null, section_science_area varchar(255))")
		return True
	conn.commit()
	return False

def example_data(conn, cursor):
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("логический","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("программирование","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("организовываеть","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("с","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("помощь","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("математический","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("логика","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("реализовать","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("в","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("пролог","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("создать","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("программа","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("состоять","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("из","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("факт","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("являеться","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("истина","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("правило","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("заключение","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("предикат","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("вопрос","");')
    conn.commit()
    cursor.execute('insert into lexema (infinitive, linguistic_characteristics_word)\
    values ("цель","");')

    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("логическое программирование");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("организовывано с помощью");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("математическая логика");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("реализовывано в");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("пролог");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("создает");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("программа");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("состоит из");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("является");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("логическое программирование");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("факт");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("правило");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("вопрос");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("истина");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("заключение");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("предикат");')
    conn.commit()
    cursor.execute('insert into denotat (title)\
    values ("цель");')

    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "логическое программирование"),(select id from lexema where infinitive = "логический"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "логическое программирование"),(select id from lexema where infinitive = "программирование"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "логическое программирование"),(select id from lexema where infinitive = "помощь"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "математическая логика"),(select id from lexema where infinitive = "математический"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "математическая логика"),(select id from lexema where infinitive = "логика"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "пролог"),(select id from lexema where infinitive = "пролог"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "программа"),(select id from lexema where infinitive = "программа"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "факт"),(select id from lexema where infinitive = "факт"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "истина"),(select id from lexema where infinitive = "истина"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "правило"),(select id from lexema where infinitive = "правило"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "заключение"),(select id from lexema where infinitive = "заключение"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "предикат"),(select id from lexema where infinitive = "предикат"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "вопрос"),(select id from lexema where infinitive = "вопрос"),1);')
    conn.commit()
    cursor.execute('insert into lexema_to_denotat (id_den, id_lexema, weight)\
    values ((select id from denotat where title = "цель"),(select id from lexema where infinitive = "цель"),1);')

    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "логический"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "программирование"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "организовывать"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "с"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "помощью"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "математический"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "логика"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "реализовывать"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "в"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "пролог"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "создавать"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "программа"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "состоять"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "из"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "факт"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "являться"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "истина"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "правило"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "заключение"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "предикат"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "вопрос"),"");')
    conn.commit()
    cursor.execute('insert into dictionary (id_lexema, description)\
    values ((select id from lexema where infinitive = "цель"),"");')

    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "логическое программирование"),\
            (select id from denotat where title = "математическая логика"),\
            (select id from denotat where title = "организовано с помощью"),1,1);')
    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "логическое программирование"),\
            (select id from denotat where title = "пролог"),\
            (select id from denotat where title = "реализовано в"),1,1);')
    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "пролог"),\
            (select id from denotat where title = "программа"),\
            (select id from denotat where title = "создает"),1,1);')
    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "программа"),\
            (select id from denotat where title = "факт"),\
            (select id from denotat where title = "состоит из"),1,1);')
    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "программа"),\
            (select id from denotat where title = "правило"),\
            (select id from denotat where title = "состоит из"),1,1);')
    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "программа"),\
            (select id from denotat where title = "вопрос"),\
            (select id from denotat where title = "состоит из"),1,1);')
    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "факт"),\
            (select id from denotat where title = "истина"),\
            (select id from denotat where title = "является"),1,1);')
    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "правило"),\
            (select id from denotat where title = "заключение"),\
            (select id from denotat where title = "является"),1,1);')
    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "правило"),\
            (select id from denotat where title = "состоит из"),\
            (select id from denotat where title = "предикат"),1,1);')
    conn.commit()
    cursor.execute('insert into relation (id_from, id_to, id_how, weight, direction)\
    values ((select id from denotat where title = "вопрос"),\
            (select id from denotat where title = "цель"),\
            (select id from denotat where title = "является"),1,1);')
    conn.commit()
    cursor.execute('select * from denotat;')
