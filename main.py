import os
import sys
import easygui  # pip install easygui, this allows to open the file manager to get and select file/folder location
# without using tkinter module
import rarfile  # pip install rarfile
import zipfile
# import tarfile  # pip install tarfile
import pyautogui  # pip install pyautogui
from plyer import notification  # pip install pyler, used for notification prompt in windows.

while True:
    try:
        # asking the user if he/sh wants to choose the file or to cancel the process.
        ask_source = pyautogui.confirm('Choose a file to extract.', buttons=['Choose', 'Cancel'])
        # Getting the file path if user clicks 'Choose'.
        if ask_source == 'Choose':
            source_file_path = easygui.fileopenbox()
            # Print the selected file path
            print("Selected file:", source_file_path)

            # asking the user if e/she wants to select the destination folder or not.
            ask_destination = pyautogui.confirm('Choose a location to extract.', buttons=['Choose', 'Cancel'])
            if ask_destination == 'Choose':
                destination_path = easygui.diropenbox(msg='Select a folder for saving the file')
                # Print the selected file path
                print("Selected destination:", destination_path)

                # The following two def are the main code that extracts the file
                # Function to extract files from RAR archive
                def extract_rar(source_file_path, destination_path):
                    """This function extracts the rar file from the file_path (source) to the
                    destination path (destination"""
                    with rarfile.RarFile(source_file_path) as archive:
                        archive.extractall(destination_path)

                # Function to extract files from ZIP archive
                def extract_zip(source_file_path, destination_path):
                    """This function extracts the zip file from the file_path (source) to the
                                       destination path (destination"""
                    with zipfile.ZipFile(source_file_path) as archive:
                        archive.extractall(destination_path)


                pyautogui.alert('Stay tuned while the file is being is being extracted,'
                                '\nYou will be notified when the task is completed.')


                def notify_task_completed():
                    """This function notify the user when the task is completed and opens the file in file manager."""
                    # Set the title and message of the notification
                    title = 'Task Completed.'
                    message = 'File is successfully extracted to {}'.format(destination_path)
                    # Display the notification
                    notification.notify(
                        title=title,
                        message=message,
                        app_name='File Extractor',
                        timeout=30
                    )
                    os.startfile(destination_path)  # Starting a file in a file manager when the task is completed.


                file_extension = os.path.splitext(source_file_path)[1]
                # Working with .rar file
                if source_file_path.endswith(".rar"):
                    extract_rar(source_file_path, destination_path)  # calling extract_rar function
                    notify_task_completed()  # calling notify_task_completed function

                # working with .zip file
                elif source_file_path.endswith(".zip"):
                    extract_zip(source_file_path, destination_path)  # calling extract_rar function
                    notify_task_completed()  # calling notify_task_completed function

                else:
                    pyautogui.alert('The file you selected has the'
                                    ' unsupported file format: {}'.format(file_extension, button='Ok'))
                    break

            elif ask_destination == 'Cancel':
                pyautogui.alert('Process has been terminated.', button='Ok')
                sys.exit(0)
        elif ask_source == 'Cancel':
            pyautogui.alert('Process has been terminated.', button='Ok')
            sys.exit(0)

        sys.exit(0)

    except rarfile.NotRarFile as e:
        pyautogui.alert('The file you provided is not a RAR file.', button='Ok')
        sys.exit(1)

    except Exception as e:
        pyautogui.alert('Error occurred as {}'.format(e))
        sys.exit(1)
