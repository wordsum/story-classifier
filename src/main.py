import argparse
import spacy

def input_file(story):
	"""
	Reads a file and remove new lines and empty lines.
	"""
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

def prepare_words(words):
	nlp = spacy.load("en_core_web_sm")
	words = nlp(words.lower())
	words_not_stop = [token.text for token in words if not token.is_punct and not token.is_stop]


	return words_not_stop

def classify(story):
	words = input_file(story)
	words_prep = prepare_words(words)
	

	print(words_prep)
	return words

def main():
	parser = argparse.ArgumentParser(description="Classify a story.")
	parser.add_argument("--story", type=str, help="Path to the file with the story.")
	args = vars(parser.parse_args())
	classify(args['story'])

if __name__ == "__main__":
	main()

