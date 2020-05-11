import os,shutil


dict_extensios={
    'audio_extensions':('.mp3','.m4a','.wav','.flac'),
    'video_extensions':('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'document_extensions':('.doc','.pdf','.txt','.docx'),
}


folderpath= input('enter folder path : ')

def file_finder(folder_path, file_extension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files

# print(file_finder(folderpath, video_extensions))

for extension_type, extensions_tuple in dict_extensios.items():
    # print("Calling file finder")
    # print(file_finder(folderpath, extensions_tuple))
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath, folder_name)
    if(os.path.isdir(folder_path)):
        print("Moving...")
    else:   
        print("Creating New File")
        os.mkdir(folder_path)
        print("Moving...") 
    for item in file_finder(folderpath, extensions_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
