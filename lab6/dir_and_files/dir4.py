def count_lines(docx_path):
    with open(docx_path, 'r') as file:
      count_of_lines = len(
         file.read()\
             .split('\n')
      )
    return count_of_lines

file_path = "/Users/uldanakonyratbaeva/lab6/opinion_essay.txt"
print("Total lines:", count_lines(file_path))
