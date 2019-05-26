"""Algorithm DiskUsage(path):
Input: A string designating a path to a file-system entry
Output: The cumulative disk space used by that entry and any nested entries
total = size(path) {immediate disk space used by the entry} if path represents a directory then
for each child entry stored within directory path do
total = total + DiskUsage(child) {recursive call}
return total"""

import os


def disk_usage(path):
  """Return the number of bytes used by a file/folder and any descendents"""
  total = os.path.getsize(path)                    # Account for direct usage of directory
  if os.path.isdir(path):                          # if this is a dir
    for filename in os.listdir(path):              # go through the child of the directory
      childpath = os.path.join(path, filename)     # Compose full path to child
      total += disk_usage(childpath)

  print('{0:<7}'.format(total), path)
  return total



disk_usage('/Users/olumideogundele/Projects/algorithm_Python')