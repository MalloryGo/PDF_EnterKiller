import time
import pyperclip
copy_cache = ""
while True:
    time.sleep(2)
    copyed_text = pyperclip.paste()
    if copy_cache != copyed_text:
        copy_cache = copyed_text
        changed_text = copyed_text.replace("\r","\\r").replace("\n","\\n").replace("-\\r\\n","").replace("\\r\\n"," ")
        pyperclip.copy(changed_text)
    else:
        pass
