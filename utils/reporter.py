import datetime
import os
from shutil import copyfile

def report(item):

  experimentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  experimentDir = './experiments/' + experimentDate
  
  if not os.path.exists(experimentDir):
    os.makedirs(experimentDir)
  
  item.tree.save2file(experimentDir + '/item.tree')
  print("Saved to %s/item.tree" % experimentDir)

  itemJson = item.tree.to_json()

  with open(experimentDir + '/champion.tree.json', 'w') as outfile:
    outfile.write(itemJson)

  print("Saved to %s/champion.tree.json" % experimentDir)

  copyfile('settings/variables.py', experimentDir + '/settings.txt')

  print("Saved experiment settings to %s/settings.txt" % experimentDir)
  

  print(experimentDate)
  
