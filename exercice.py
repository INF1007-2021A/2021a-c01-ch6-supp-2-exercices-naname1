#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools
from matplotlib.colors import cnames

def get_even_keys(dictionary):
	list = [integer for integer in dictionary if integer % 2 == 0]
	return list

def join_dictionaries(dictionaries):
	dict_res = dictionaries[0]

	for i in range(1,len(dictionaries)):
		dict_res.update(dictionaries[i])
	return dict_res

def dictionary_from_lists(keys, values):
	dictionary = dict.fromkeys(keys)
	for key, value in zip(keys, values):
		dictionary[key] = value

	return dictionary

def get_greatest_values(dictionnary, num_values):
	maxValues = []
	maxdict = max(dictionnary)
	maxValues.append(maxdict)
	maxCurrent = 0
	return sorted(dictionnary, key=dictionnary.__getitem__, reverse=True)[0:num_values]

def get_sum_values_from_key(dictionnaries, key):
	sum = 0

	for dict in dictionnaries:
		if key in dict:
			sum += dict[key]
	return sum


if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print()

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print()
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print()
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print()

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print()
