import time

def startTimer():
  startExperiment = time.time()
  
  def currentTime():

    return str((time.time() - startExperiment) / 60)
  
  return currentTime