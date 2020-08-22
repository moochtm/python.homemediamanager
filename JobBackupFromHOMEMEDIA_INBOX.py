__author__ = 'matt_barr'

import os
import sys
import inspect
import shutil
import copy
import platform
import pprint

import configobj

from homemediamanager import message, archiver

################################################################################
# SETUP LOGGING
################################################################################

import logging

pathToThisPyFile = inspect.getfile(inspect.currentframe())
path, filename = os.path.split(pathToThisPyFile)
filename = os.path.splitext(filename)[0] + '.log'
log_path = os.path.join(path, filename)

# set up logging to file
logging.basicConfig(level=logging.INFO,
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

logger = logging.getLogger(__name__)

################################################################################
# Define Local Achives
################################################################################

archives = []

archives.append('/Volumes/DiskStation/media/_inbox/AUDITION_&_SORTING_INBOX')

################################################################################
# Define Other Constants
################################################################################

pathToVolumes = '/Volumes/1TB ARCHIVE/HOMEMEDIA_INBOX/'

file_extensions_filter = ('.JPG', '.MTS', '.CR2', '.DNG', '.MOV', '.MP4', '.HEIC')
file_extensions_filter = [s.lower() for s in file_extensions_filter]
temp_folder_name = "jobbackupfromvolume_temp"

testing = False

################################################################################
# Utility Methods
################################################################################

def nice_list(list):
    nice_list = ""
    for item in list:
        print(item)
        nice_list = nice_list + item + "\n"
        print(nice_list)
    return nice_list

def error_handler(file_path, status):
    print("------------------------------")
    print("ERROR processing file: %s" % file_path)
    print("Status when error occured: %s" % status)
    print("------------------------------")


################################################################################
# Main Run Method
################################################################################


def run():

    logger.info("Starting...")

    pathToThisPyFile = inspect.getfile(inspect.currentframe())

    # LOAD CONFIG FILE
    # ------------------------------------------
    logger.info('Loading config file...')
    hostname = platform.node()
    # remove .local if exists
    hostname = hostname.split('.local')[0]
    # remove .home if exists
    hostname = hostname.split('.home')[0]
    path, filename = os.path.split(pathToThisPyFile)
    filename = os.path.splitext(filename)[0]
    filename = "%s_%s.cfg" % (filename, hostname)
    path_to_config_file = os.path.join(path, filename)
    if not os.path.exists(path_to_config_file):
        logger.warning("cannot find config file: %s" % path_to_config_file)
        sys.exit()
    config = configobj.ConfigObj(path_to_config_file)
    logger.info('Loaded config:')
    logger.info(config)

    pushbullet_acc_id = config['Messages']['PushBullet']['recipientAccountID']


    # LOCK
    # ------------------------------------------
    locked = os.path.exists('%s.locked' % pathToThisPyFile)
    if locked:
        msg = message.PushBulletMessage()
        msg.subject = 'New volume mounted but script is locked (presumed already running)'
        #msg.send(account_id=pushbullet_acc_id)
        logger.warning('New volume mounted but script is locked (presumed already running)')
        sys.exit()
    else:
        open('%s.locked' % pathToThisPyFile, 'a').close()


    # CHECK FOR VOLUMES TO PROCESS
    # ------------------------------------------
    logger.info('Checking volumes...')
    volumes_to_process = []
    for volume in os.listdir(config['General']['pathToVolumes']):
        if volume in list(config['SourceVolumes'].keys()):
            volumes_to_process.append(volume)

    logger.info('Volumes to be processed: %s' % str(volumes_to_process))


    # FOR EACH VOLUME TO PROCESS:
    # ------------------------------------------
    for volume in volumes_to_process:

        try:

            logger.info('Processing "%s"...' % volume)

            # SEND MESSAGE
            msg = message.PushBulletMessage()
            msg.subject = '%s mounted, processing now.' % (volume)
            logger.info('%s mounted, processing now.' % (volume))
            #msg.send(account_id=pushbullet_acc_id)

            # CREATE ARCHIVER: source folder, destination folder/s, file rename format, dest folder structure format,
            # del source files
            a = archiver.Archiver()

            src_path = os.path.join(config['General']['pathToVolumes'], volume)
            dest_paths = config['ArchiveVolumes']['paths']
            logger.info('Destination paths: %s' % (dest_paths))
            filename_prefix = config['SourceVolumes'][volume]['filenamePrefix']
            dest_folder_structure_format = config['SourceVolumes'][volume]['destFolderStructureFormat']
            remove_source_files = config['SourceVolumes'][volume]['deleteFilesAfterBackup']

            results = a.archive_files(src_path, dest_paths, file_extensions_filter, filename_prefix,
                                      dest_folder_structure_format, remove_source_files)

            # CREATE NICER LOOKING RESULTS FOR SENDING IN A MESSAGE (NEW LINE FOR EACH FILE)
            printable_results = ""
            for item in list(results.items()):
                printable_results += str(item) + "\n"

            # SEND MESSAGE
            msg = message.PushBulletMessage()
            msg.subject = '%s mounted, processing finished.' % (volume)
            msg.body = printable_results
            logger.info(printable_results)
            logger.info('%s mounted, processing finished.' % (volume))
            #msg.send(account_id=pushbullet_acc_id)

            logger.info('Finished processing "%s"' % volume)

        except Exception as e:
            logger.exception(e)

    # UNLOCK
    os.remove('%s.locked' % pathToThisPyFile)

if __name__ == '__main__':
    sys.exit(run())