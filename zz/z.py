import sqlite3
import sys
from data import example_data, \
				 example_text, \
				 example_tables, \
				 lexema_id_by_inf, \
				 denotat_id_by_lexema_id, \
				 denotat_title_by_id, \
				 relation_by_den_id
from rutermextract import TermExtractor
import pymystem3

def init_database(filename = "denotator.db"):
	try:
		conn = sqlite3.connect(filename)
		cursor = conn.cursor()
	except sqlite3.OperationalError:
		sys.exit(1)

	need_to_load_example_data = False

	for table in ["rootobject", "relation", "denotat", "lexema", "lexema_to_denotat", "argument", "scopos", "question", "text_problematics", "dictionary", "collocation", "text", "subject_area", "key_words", "figure_of_speech", "sentence", "research_topic"] :
		try:
			cursor.execute("select * from %s limit 1" % table)
		except Exception as e:
			if "no such table" in str(e):
				need_to_load_example_data = example_tables(conn, cursor, table)


	if need_to_load_example_data:
		example_data(conn, cursor)
		print("Example data loaded")

	return (conn, cursor)

def get_lexemas_from_text(cursor, atext = ""):
	term_extractor = TermExtractor()
	mystem = pymystem3.Mystem()
	lexemas = []
	for term in term_extractor(atext):
		for lexema in str(term.normalized).split(" "):
			lexema = mystem.analyze(lexema)[0]['analysis'][0]['lex']
			id_lexema = lexema_id_by_inf(cursor, lexema)
			lexemas += [id_lexema]
	return lexemas

def get_denotats_from_lexemas(cursor, lexemas = []):
	denotats = []
	for id_lexema in lexemas:
		id_denotat = denotat_id_by_lexema_id(cursor, id_lexema)
		denotats += id_denotat
	return denotats

def get_relations_for_denotats(cursor, denotats = []):
	relations = []
	for id_denotat_from in denotats:
		for id_denotat_to in denotats:
			rel_id = relation_by_den_id(cursor, id_denotat_from, id_denotat_to)
			try:
				assert rel_id[0] != None
				relations += [(id_denotat_from, rel_id[0], id_denotat_to)]
			except:
				pass
	return relations

def print_result(cursor, atext, result):
	print(atext)
	for relation in result:
		print(
			denotat_title_by_id(cursor, relation[0]),
			denotat_title_by_id(cursor, relation[1]),
			denotat_title_by_id(cursor, relation[2])
		)

def main():
	connection, cursor = init_database('denotator.db')
	lexemas = get_lexemas_from_text(cursor, example_text)
	print("Лексемы: ", lexemas)
	denotats = get_denotats_from_lexemas(cursor, lexemas)
	print("Денотаты: ", denotats)
	relations = get_relations_for_denotats(cursor, denotats)
	print("Денотатные пары: ", relations)
	print_result(cursor, example_text, relations)
	connection.close()

if __name__ == '__main__':
	main()
