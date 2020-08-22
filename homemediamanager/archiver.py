__author__ = 'Matt'

import os
import copy
import inspect
import uuid
import shutil
import collections

from . import filelist

from .thirdparty import sortphotos

################################################################################
# SETUP LOGGING
################################################################################

import logging

log_seperator = '============================================================='
"""
pathToThisPyFile = inspect.getfile(inspect.currentframe())
path, filename = os.path.split(pathToThisPyFile)
filename = os.path.splitext(filename)[0] + '.log'
log_path = os.path.join(path, filename)

# set up logging to file
# logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=log_path,
                    filemode='w')

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
"""

logger = logging.getLogger(__name__)

class Archiver():
    def __init__(self):
        pass

    def archive_files(self, src_path, dest_paths, file_extensions_filter=None, filename_prefix=None,
                dest_folder_structure_format=None, remove_source_files=False):

        results = {}

        current_filelist = filelist.FileList()
        current_filelist.generate(src_path, file_extensions_filter)
        if not current_filelist.files:
            results['Summary'] = 'No files found to process'
            return results

        history_filelist = filelist.FileList()
        history_filelist.load(src_path)

        # make copy of current_filelist for editing during processing...
        dummy_current_filelist = copy.deepcopy(current_filelist)

        # for every file to process:
        for file in current_filelist.files:

            file_path = current_filelist.files[file]['path']
            results[file_path] = {}
            # set end status to Error - it will be changed further down if processing is successful
            results[file_path]['end status'] = 'Error'

            try:
                logger.info(log_seperator)
                logger.info('Processing file: %s' % file_path)

                status = "Checking if file has been archived before"
                if history_filelist.files.get(file):
                    file_already_archived = True
                    results[file_path]['history'] = 'Old'
                else:
                    file_already_archived = False
                    results[file_path]['history'] = 'New'

                if not file_already_archived:
                    if isinstance(dest_paths, str):
                    	dest_paths = [dest_paths]
                    for dest in dest_paths:

                        results[file_path][dest] = "started"
                        logger.info('Sending to dest: %s' % dest)

                        # CHECK THE DESTINATION DOES EXIST...
                        if not os.path.isdir(dest):
                            logger.error ("Destination doesn't exist: %s" % dest)
                            raise

                        temp_folder_path = os.path.join(dest, str(uuid.uuid1()))
                        os.mkdir(temp_folder_path)
                        shutil.copy2(current_filelist.files[file]['path'], temp_folder_path)

                        # create the sortphotos file rename format string
                        file_rename_format = filename_prefix + '.%Y-%m-%d.{orig}'
                        print("here")
                        # use the [extended] sortphotos module to move, sort and rename all files
                        sorted_photos = sortphotos.sortPhotos(src_dir=temp_folder_path, dest_dir=dest,
                                                              sort_format=dest_folder_structure_format,
                                                              rename_format=file_rename_format, recursive=True,
                                                              additional_groups_to_ignore=[], verbose=False)

                        print("here")
                        shutil.rmtree(temp_folder_path)

                        logger.info("Checking archived file against original:")
                        logger.info("\tOriginal file: %s" % file_path)
                        archived_file = sorted_photos[0]['dest_file']
                        logger.info("\tArchived file: %s" % archived_file)

                        if current_filelist.files[file] != current_filelist.compare_with_filelist(archived_file):
                            logger.warn ("\tResult: Archived file is not identical to original file")
                            results[file_path][dest] = "error"
                            raise
                        else:
                            logger.info("\tResult: Archived file is identical to original file")
                            results[file_path][dest] = "finished"

                # remove original file
                if remove_source_files == True or remove_source_files == 'True':
                    logger.info("Deleting original file")
                    status = "Removing original file from volume"
                    dummy_current_filelist.remove_file(file)
                    results[file_path]['end status'] = 'Deleted'
                else:
                    results[file_path]['end status'] = 'Kept'

                logger.info("Adding file to history filelist")
                history_filelist.files[file] = current_filelist.files[file]
                history_filelist.save(src_path)

            except:
                logger.error(log_seperator)
                logger.error("Error processing file: %s" % file_path)
                logger.error(log_seperator)
                results[file_path]['end status'] = 'Error'

        results["Summary"] = {}
        results["Summary"]["History"] = {}
        results["Summary"]["History"]["New"] = 0
        results["Summary"]["History"]["Old"] = 0
        results["Summary"]["End Status"] = {}
        results["Summary"]["End Status"]["Kept"] = 0
        results["Summary"]["End Status"]["Deleted"] = 0
        results["Summary"]["End Status"]["Error"] = 0

        for item in list(results.items()):
            if item[1].get('end status') == "Kept":
                results["Summary"]["End Status"]["Kept"] += 1
            if item[1].get('end status') == "Deleted":
                results["Summary"]["End Status"]["Deleted"] += 1
            if item[1].get('end status') == "Error":
                results["Summary"]["End Status"]["Error"] += 1
            if item[1].get('history') == "New":
                results["Summary"]["History"]["New"] += 1
            if item[1].get('history') == "Old":
                results["Summary"]["History"]["Old"] += 1

        results = collections.OrderedDict(sorted(list(results.items()), key=lambda t: t[0]))

        return results


if __name__ == '__main__':
    src_path = '/Users/Matt/Volumes/2TB DRIVE'
    dest_paths = ['/Users/Matt/Volumes/1TB ARCHIVE', '/Users/Matt/Volumes/1TB ARCHIVE BUP']
    filename_prefix = 'test'
    a = Archiver()
    a.archive_files(src_path, dest_paths, file_extensions_filter=['JPG', 'MTS', 'CR2', 'DNG', 'MOV'],
                    filename_prefix=filename_prefix, dest_folder_structure_format='%Y/%m-%b',
                    remove_source_files=True)