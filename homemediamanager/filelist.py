__author__ = 'matt_barr'

import os
import hashlib
import pickle
import inspect

__history_filename__ = 'filelist_history.pickle'

################################################################################
# SETUP LOGGING
################################################################################

import logging
logger = logging.getLogger(__name__)

def print_to_log(d, indent=0, level="DEBUG"):
    try:
        for key, value in d.iteritems():
            # logger.info('\t' * indent + str(key) + str(value))
            if isinstance(value, dict):
                if level == "INFO": logger.info('\t' * indent + str(key) + ":")
                elif level == "WARN": logger.warn('\t' * indent + str(key) + ":")
                elif level == "ERROR": logger.error('\t' * indent + str(key) + ":")
                else: logger.debug('\t' * indent + str(key) + ":")
                print_to_log(value, indent+1, level)
            else:
                if level == "INFO": logger.info('\t' * (indent+1) + str(key) + ": " + str(value))
                elif level == "WARN": logger.warn('\t' * (indent+1) + str(key) + ": " + str(value))
                elif level == "ERROR": logger.error('\t' * (indent+1) + str(key) + ": " + str(value))
                else: logger.debug('\t' * (indent+1) + str(key) + ": " + str(value))
    except:
        if level == "INFO": logger.info(d)
        elif level == "WARN": logger.warn(d)
        elif level == "ERROR": logger.error(d)
        else:logger.debug(d)


class FileList:
    def __init__(self):
        self.files = {}
        pass

    def load(self, path):
        if os.path.isfile(os.path.join(path, __history_filename__)):
            f = open(os.path.join(path, __history_filename__), 'r')
            self.files = pickle.load(f)
            print_to_log("Loaded Filelist")
            print_to_log(self.files)
            return True
        else:
            print_to_log("No FileList to Load")
            return False

    def save(self, path):
        f = open(os.path.join(path, __history_filename__), 'w')
        pickle.dump(self.files, f)
        f.close()

    def generate(self, path, file_extensions_filter):
        file_extensions_filter = [s.lower() for s in file_extensions_filter]
        for dir_name, sub_dirs, file_list in os.walk(path):
            print_to_log([dir_name, sub_dirs, file_list])
            if "@eaDir" in dir_name:
                continue
            if file_extensions_filter:
                files = [[file, os.path.splitext(file)] for file in file_list]
                found_media_files = [file[0] for file in files if file[1][1].lower() in file_extensions_filter]
            else:
                found_media_files = file_list
            for f_name in found_media_files:
                f_path = os.path.join(dir_name, f_name)
                print_to_log('Generating FileList info for "%s"' % f_path, level="INFO")
                f_size = os.path.getsize(f_path)
                f_hash = self.__hash_file(f_path)
                self.files[f_hash] = {
                    'name': f_name,
                    'path': f_path,
                    'size': f_size,
                }
        print_to_log("Generated Filelist")
        print_to_log(self.files)
        return True

    def list_names(self):
        list_names = []
        for file in self.files:
            list_names.append(self.files[file]['name'])
        return list_names

    def contains_this_file(self, file):
        result = False
        if file in self.files.items():
            result = true
        return result

    """
        def not_in_filelist(self, dir, items):

            returns a list of file items that are NOT in the filelist's files
            :param dir:
            :param items:
            :return:

            not_in_filelist = []
            for item in items:
                if os.path.isdir(os.path.join(dir, item)):
                    break
                in_filelist = False
                for k, v in self.files.iteritems():
                    if os.path.join(dir, item) in v.values():
                        in_filelist = True
                if not in_filelist:
                    not_in_filelist.append(item)
            return not_in_filelist
    """

    def compare_with_filelist(self, test_file):
        test_hash = self.__hash_file(test_file)
        result = None
        if test_hash in self.files:
            result = self.files[test_hash]
        return result

    def remove_file(self, file_hash):
        file_path = self.files[file_hash]['path']
        os.remove(file_path)
        del self.files[file_hash]

    def __hash_file(self, path, block_size=65536):
        a_file = open(path, 'rb')
        hasher = hashlib.md5()
        buf = a_file.read(block_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = a_file.read(block_size)
        a_file.close()
        return hasher.hexdigest()