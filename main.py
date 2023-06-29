class CloudStorage:
    def __init__(self):
        self.files = {}

    def add_file(self, name, size):
        if name in self.files:
            return "false"
        self.files[name] = int(size)
        return "true"

    def copy_file(self, name_from, name_to):
        if name_from not in self.files or name_to in self.files:
            return "false"
        self.files[name_to] = self.files[name_from]
        return "true"

    def get_file_size(self, name):
        return str(self.files.get(name, ""))

    def find_file(self, directory, file_name):
        matching_files = [name for name in self.files.keys() if name.startswith(directory) and name.endswith(file_name)]
        matching_files = sorted(matching_files, key=lambda x: (-self.files[x], -x.count("/")))
        return ", ".join([f"{name}({self.files[name]})" for name in matching_files])

def solution(queries):
    storage = CloudStorage()
    results = []
    for query in queries:
        operation = query[0]
        if operation == "ADD_FILE":
            results.append(storage.add_file(query[1], query[2]))
        elif operation == "COPY_FILE":
            results.append(storage.copy_file(query[1], query[2]))
        elif operation == "GET_FILE_SIZE":
            results.append(storage.get_file_size(query[1]))
        elif operation == "FIND_FILE":
            results.append(storage.find_file(query[1], query[2]))

    return results

