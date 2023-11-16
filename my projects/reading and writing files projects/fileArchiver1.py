# Walk a directory tree and archive just files with certain extensions, such as .txt or .py, and nothing else
import os, zipfile

def archive(folder):
    # backup only the .txt and .py files in a folder
    folder = os.path.abspath(folder)
    # make sure the path is absolute
    print('creating the zipfile...')
    print('zipfile name is txt&py.zip.')
    zipFile = zipfile.ZipFile('txt&py.zip', 'w')
    # create the zipfile all the files would be archived to

    # walk the entire folder tree and archive only .txt and .py files
    for foldername, subfolders, filenames in os.walk(folder):
        print('creating folder')
        zipFile.write(foldername)
        for files in filenames:
            if files.endswith('.txt') or files.endswith('.py'):
                print('adding .txt and .py files...')
                zipFile.write(os.path.join(foldername, files))
    zipFile.close()
    print('done')

archive('C:\\bacon_backup')
