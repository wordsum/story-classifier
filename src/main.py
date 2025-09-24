import argparse
import spacy
import csv

def input_file(story):
	words = []
	try:
		with open(story, 'r') as input:
			for line in input:
				stripped_line = line.strip()
				if stripped_line:
					words.append(stripped_line + " ")

		return "".join(words)
	except FileNotFoundError:
		return f"Error: File not found: {story}"
	except Exception as e:
		return f"And error happened: {e}"
	
def output_file(words, classification, file):
	try:
		with open(file, 'a', newline='') as csvfile:
			csv_writer = csv.writer(csvfile)
			csv_writer.writerows([[classification, words]])
	except FileNotFoundError:
		return f"Error: File not found to write words."
	except Exception as e:
		return f"And error happened: {e}"	


def prepare_words(words):
	nlp = spacy.load("en_core_web_sm")

	words_lower = nlp(words.lower())
	words_stop_punc = [token.lemma_ for token in words_lower if not token.is_punct and not token.is_stop]

	return " ".join(words_stop_punc)

def classify(story):
	words = input_file(story)
	words_prep = prepare_words(words)
	
	print(words_prep)
	return words

def main():
	parser = argparse.ArgumentParser(description="Story Classifier.")
	parser.add_argument("--prepare", type=str, help="Directory and file to clean.")
	parser.add_argument("--classification", type=str, help="The classification of the prepared file.")
	parser.add_argument("--output", type=str, help="Directory and csv file to output prepared.")
	parser.add_argument("--story", type=str, help="Directory path and file to the story.")
	args = vars(parser.parse_args())
    
	if args['prepare'] is not None and args['classification'] and args['output']:
		words = input_file(args['prepare'])
		prepared_words = prepare_words(words)
		output_file(prepared_words, args['classification'], args['output'])

     
	if args['story'] is not None:
		classify(args['story'])

if __name__ == "__main__":
	main()

