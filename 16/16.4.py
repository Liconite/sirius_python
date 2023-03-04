import os
import threading
import time

def replace_ids(filename):
    path = os.path.join("files", filename)

    with open(path, "r+") as file:
        content = file.read()
        content = content.replace("ids", "id")
        file.seek(0)
        file.write(content)
        file.truncate()

files = os.listdir("files")

start_time = time.time()
threads = []
for filename in files:
    thread = threading.Thread(target=replace_ids, args=(filename,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
