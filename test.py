__author__ = 'Matt'

file_list = ['1', '2@eadir']

file_list = [file for file in file_list if not "@eadir" in file]

print file_list