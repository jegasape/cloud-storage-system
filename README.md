Instructions
Your task is to implement a simple cloud storage system. All operations that should be supported are listed below.

Solving this task consists of several levels. Subsequent levels are opened when the current level is correctly solved. You always have access to the data for the current and all previous levels.

Requirements
Your task is to implement a simple cloud storage system that maps objects (files) to their metainformation. Specifically, the storage system should maintain files along with some information about them (name, size, etc.). Note that this system should be in-memory, you do not need to work with the real filesystem.

Plan your design according to the level specifications below:

Level 1: The cloud storage system should support adding new files, retrieving, and copying files.

Expand to see level 1 details.
Level 2: The cloud storage system should support finding files by matching prefixes and suffixes.

Level 3: The cloud storage system should support adding users with various capacity limits.

Level 4: The cloud storage system should support compressing and decompressing files.

To move to the next level, you need to pass all the tests at this level.

Note

You will receive a list of queries to the system, and the final output should be an array of strings representing the returned values of all queries. Each query will only call one operation.

It is guaranteed that the given queries will never call operations that result in collisions between file and directory names.

Level 2
Implement support for retrieving file names by searching directories via prefixes and suffixes.

FIND_FILE <prefix> <suffix> — should search for files with names starting with prefix and ending with suffix. Returns a string representing all matching files in this format: "<name1>(<size1>), <name2>(<size2>), ...". The output should be sorted in descending order of file sizes or, in the case of ties, lexicographically. If no files match the required properties, should return an empty string.
Examples
The example below shows how these operations should work (the section is scrollable to the right):

Queries	Explanations
queries = [
  ["ADD_FILE", "/root/dir/another_dir/file.mp3", "10"],
  ["ADD_FILE", "/root/file.mp3", "5"],
  ["ADD_FILE", "/root/music/file.mp3", "7"],
  ["COPY_FILE", "/root/music/file.mp3", "/root/dir/file.mp3"],
  ["FIND_FILE", "/root", ".mp3"],
  ["FIND_FILE", "/root", "file.txt"],
  ["FIND_FILE", "/dir", "file.mp3"]
]

returns "true"
returns "true"
returns "true"
returns "true"
returns "/root/dir/another_dir/file.mp3(10), /root/dir/file.mp3(7), /root/music/file.mp3(7), /root/file.mp3(5)"
returns ""; there is no file with the prefix "/root" and suffix "file.txt"
returns ""; there is no file with the prefix "/dir" and suffix "file.mp3"

the output should be ["true", "true", "true", "true", "/root/dir/another_dir/file.mp3(10), /root/dir/file.mp3(7), /root/music/file.mp3(7), /root/file.mp3(5)", "", ""].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.string queries

An array of queries to the system. It is guaranteed that all the queries parameters are valid: each query calls one of the operations described in the description, all operation parameters are given in the correct format, and all conditions required for each operation are satisfied.

Guaranteed constraints:
1 ≤ queries.length ≤ 500.

[output] array.string

An array of strings representing the returned values of queries.
