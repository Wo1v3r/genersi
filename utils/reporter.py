import datetime, os, json
from shutil import copyfile

def report(item, experimentTime, generation, generationFitness,  results):

  experimentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  experimentDir = './experiments/' + experimentDate
  
  if not os.path.exists(experimentDir):
    os.makedirs(experimentDir)
  
  item.tree.save2file(experimentDir + '/item.tree')
  print("Saved item tree to %s/item.tree" % experimentDir)

  itemJson = item.tree.to_json()

  with open(experimentDir + '/item.tree.json', 'w') as outfile:
    outfile.write(itemJson)

  print("Saved to %s/item.tree.json" % experimentDir)


  copyfile(experimentDir + '/item.tree.json', './champion.tree.json')
  print("Copied champion.tree.json to root dir.")

  
  copyfile('settings/variables.py', experimentDir + '/settings.txt')
  print("Copied experiment settings to %s/settings.txt" % experimentDir)

  
  
  with open(experimentDir + '/genersi.log.json', 'w') as outfile:
    runLog = {
      "Experiment Time": experimentTime,
      "Last Generation": generation,
      "Fitness": generationFitness,
      "Contest Results:": str(results[0]) + "/" + str(results[1]),
    }

    json.dump(runLog, outfile)
  
  print("Saved run log to %s/genersi.log.json" % experimentDir)
  
