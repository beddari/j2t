#!/usr/bin/env python3

import subprocess
import unittest

class TestJinja2TemplatingUtility(unittest.TestCase):
	def test_yaml(self):
		output = subprocess.check_output('j2t --add-yaml test1.yml --template test1.j2', shell=True)
		self.assertEqual('hello world!', output)

	def test_json(self):
		output = subprocess.check_output('j2t --add-json test1.json --template test1.j2', shell=True)
		self.assertEqual('hello world!', output)

	def test_kv(self):
		output = subprocess.check_output('j2t --add-kv a=hello --add-kv b=world --template test1.j2', shell=True)
		self.assertEqual('hello world!', output)

	def test_data_order(self):
		output = subprocess.check_output('j2t --add-yaml test2.yml --add-json test2.json --add-kv c=3 --template test2.j2', shell=True)
		self.assertEqual('123', output)

	def test_stdin_stdout(self):
		output = subprocess.check_output('echo "hello world!" | j2t', shell=True)
		self.assertEqual('hello world!', output)

if __name__ == '__main__':
	unittest.main()
