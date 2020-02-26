from finder import Finder
from argparse import ArgumentParser
import os

CUSTOM_SITE_PARSERS_FOLDER_NAME = 'custom'
CUSTOM_SITE_PARSERS_FOLDER_PATH = os.path.join(
	os.getcwd(), CUSTOM_SITE_PARSERS_FOLDER_NAME)


def import_custom_parsers():
	for *root, files in os.walk(CUSTOM_SITE_PARSERS_FOLDER_PATH):
		for file in files:
			if file.endswith('.py'):
				try:
					file = file[::-1].replace('yp.', '')[::-1]
					command = f"from {CUSTOM_SITE_PARSERS_FOLDER_NAME}.{file} import *"
					exec(command)
				except Exception as e:
					print(f"Impossible to import anything from : {file}")


if not os.path.isdir(CUSTOM_SITE_PARSERS_FOLDER_PATH):
	os.mkdir(CUSTOM_SITE_PARSERS_FOLDER_PATH)
else:
	import_custom_parsers()


arg_parser = ArgumentParser()

arg_parser.add_argument('-n', '--name', required=True)

arg_parser.add_argument('-j', '--json', required=False,
						default=False, action='store_true')

arg_parser.add_argument('-c', '--csv', required=False,
						default=False, action='store_true')

arg_parser.add_argument('-u', '--universal', required=False,
						default=False, action='store_true')

arg_parser.add_argument('-s', '--success', required=False,
						default=False, action='store_true')

args = arg_parser.parse_args()

settings = {
	'save_json': args.json,
	'save_csv': args.csv,
	'print_success': args.success,
}


fndr = Finder(**settings)

if fndr.have_internet():
	fndr.find(args.name)

	if args.universal:

		with open('sites.txt') as sites_file:
			for url in sites_file:
				fndr.register_universal(url.strip())

		fndr.find_universal(args.name)
