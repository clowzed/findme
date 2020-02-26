import requests
import json
import concurrent.futures
import http.client as httplib
from colors import *
import csv
import os
from typing import Callable


class Finder():
	def __init__(self, **kwargs):
		self.settings = {
			'save_json': False,
			'save_csv': False, }

		self.site_parsers = self.get_parsers()
		self.settings.update(kwargs)
		self.universals = list()

	def found(self, info:dict):
		print(f"[{green('+')}] - {info['url']} - {info['nickname']}")

	def not_found(self, info:dict):
		print(f"[{red('-')}] - {info['url']} - {info['nickname']}")

	def run_custom_parser(self, site_parser:Callable, name:str):
		try:
			data = site_parser().search(name)
		except Exception as e:
			pass
		else:
			if data['found']:
				self.found(data)
			else:
				if not self.settings['print_success']:
					self.not_found(data)

			if self.settings['save_json']:
				self.save_json(data)
			if self.settings['save_csv']:
				self.save_csv(data)
		return

	def run_universal_parser(self, parser, name:str):
		try:
			data = parser.search(name)
		except Exception as e:
			pass
		else:
			if data['found']:
				self.found(data)
			else:
				if not self.settings['print_success']:
					self.not_found(data)

			if self.settings['save_json']:
				self.save_json(data)
			if self.settings['save_csv']:
				self.save_csv(data)
		return

	def find(self, name:str):
		print("Running custom parsers...")
		with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
			parsed = {executor.submit(self.run_custom_parser, site_parser, name): site_parser for site_parser in self.site_parsers}
			for parsed_data in concurrent.futures.as_completed(parsed):
				try:
					data = parsed_data.result()
				except Exception as e:
					pass

	def save_json(self, data:dict):
		with open(f"{data['nickname']}.json", 'a') as f:
			json.dump(data, f, indent=4)
			f.write("\n")

	def save_csv(self, data:dict):
		filename = f'{data["nickname"]}.csv'
		headers_already_written = os.path.isfile(filename)
		with open(filename, mode='a') as csv_file:
			fieldnames = ['url', 'nickname', 'is_found']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

			if not headers_already_written:
				writer.writeheader()
			writer.writerow({'url': data['url'], 'nickname': data['nickname'], 'is_found': data['found']})

	@classmethod
	def get_parsers(cls):
		return cls.__subclasses__()

	def register_universal(self, url:str):
		parser = UniversalParser()
		parser.set_url(url)
		self.universals.append(parser)

	def find_universal(self, name:str):
		print("Running universal parsers...")
		with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
			parsed = {executor.submit(self.run_universal_parser, site_parser, name): site_parser for site_parser in self.universals}
			for parsed_data in concurrent.futures.as_completed(parsed):
				try:
					data = parsed_data.result()
				except Exception as e:
					pass

	def get_site_data(self, url:str):
		a = requests.get(url, timeout=1)
		return a.status_code, a.text

	def have_internet(self):
		conn = httplib.HTTPConnection("www.google.com", timeout=5)
		try:
			conn.request("HEAD", "/")
			conn.close()
			return True
		except:
			conn.close()
			return False


class UniversalParser():
	def __init__(self):
		pass

	def search(self, name:str):
		url = self.url + name
		response, data = self.get_site_data(url)
		return {
			'nickname': name,
			'url': url,
			'found': response == 200
		}

	def set_url(self, url):
		self.url = url.rstrip('/') + '/'

	def get_site_data(self, url):
		a = requests.get(url)
		return a.status_code, a.text
