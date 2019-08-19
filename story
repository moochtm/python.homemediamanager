

**********************************************************************
*** Story ***
**********************************************************************


When a new volume is mounted a BackupMediaFilesJob is triggered. The Job:

    (1) Determines if there is a volume with home media files on it
    (2) If there is, the files are processed.

with camera photos or movies is mounted, a Job is triggered. the media files are compared against a file history of previously processed files. Any "new" (unprocessed files) are:
    (1) renamed (renaming depends on camera and media type)
    (2) backed up to two archive volumes using a specific folder hierarchy
    (3) deleted from the volume (if backup successful and depending on source volume)

Notifications are sent out containing info like:
- Job status. Volume name. Number of files. Number of Errors (and erroring filenames).


**********************************************************************
*** Architecture ***
**********************************************************************


* JobBackupFromVolume
    @ CurrentStatus (InProgress, Complete)
    @ EndStatus (NoNewFiles, Success (x of x files copied), Errors (y of x files copied)
    @ Know        @ DeleteFilesAfterBackup (True/False)nSourceVolumes
        @ Name (e.g. "CAM_SD")
        @ FilenamePrefix (e.g. matt.iphone5s.)

    - Run
        - Lock()
        - CheckForVolumesToProcess
        - For Each VolumeToProcess
            - Send notification - "job starting"
            - Check for HistoryFileList and load if exists
            - Create CurrentFileList
            - For each file:
                - Check if file is in HistoryAlready (i.e. already processed)
                - If New, for each Archive:
                    - Copy file to temp folder
                    - Use sortphotos to rename and file
                - Remove original File (depending on Volume)
            Send Notification:
                - Volume Name
                - Job Summary:
                    - Files processed, New Files archived, Old Files removed, Error Files
                - File List:
                    - Details
        - Unlock()

* FileList
    - load
    - save
    - generate from path (path, filter)
    - append
    @ Files
        @ Hash
            @ Name
            @ Path
            @ Size
            @ Processed (True/False)

* Message
    @ Subject
    @ Body
    - Send
    * PushPalMessage

1. file plus details
for each archive:
2. file in a temp folder
3. renamed file in folder

