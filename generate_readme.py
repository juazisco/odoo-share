import os

directory_path = './' 
def find_text(text_complete,text_before, text_after):
    start_index = 0
    end_index = 0
    matching_occurrences = []
    text_found = ""
    while True:
        start_index = text_complete.find(text_before, start_index)
        if start_index == -1:
            break
        end_index = text_complete.find(text_after, start_index + len(text_before))
        if end_index == -1:
            break
                            
        matching_occurrences.append((start_index, end_index + len(text_after)))
        start_index = end_index + 1
    if len(matching_occurrences)>0:
        text_found = text_complete[matching_occurrences[0][0]:matching_occurrences[0][1]]
    text_found = text_found.replace("name\":","")
    text_found = text_found.replace("name': ","")
    text_found = text_found.replace("\",","")
    text_found = text_found.replace("',","")
    text_found = text_found.replace("\"","")
    text_found = text_found.replace("'","")
    text_found = text_found.replace("summary:","").replace("\n"," ")
    text_found = text_found.strip()
    return text_found

def find_text_in_files(directory):
    modules = []
    files = os.listdir(directory)    
    for filename in files:
        if filename not in ('.gitignore','generate_readme.py','README.md'):
            file_path = os.path.join(directory, filename)
            with open(file_path+'/__manifest__.py', 'r', encoding='utf-8') as file:
                content = file.read()
                name = find_text(content,"name", ",")
                summary = find_text(content,"summary", ",")
                modules.append("|["+file_path.replace("./","")+"]("+file_path.replace("./","")+")|"+name+"|"+summary+"|\n")
                
    return modules

## Create/Update README.md
with open("README.md", 'w+') as f:
    f.write("# odoo-share\n")
    f.write("| Módulo      | Nombre | Descripción     |\n")
    f.write("| :---        |    :---   |         :--- |\n")
    modules = find_text_in_files(directory_path)
    for module in modules:
        f.write(module)
