import datetime

def partBegin(partNum):
  start = datetime.datetime.now().replace(microsecond=0)
  print("Part " + str(partNum) + " initialized")
  return start

def partEnd(partNum, start):
  end = datetime.datetime.now().replace(microsecond=0)
  duration = end-start
  print("Part " + str(partNum) + " completed")
  print("Part " + str(partNum) + " duration: " + str(duration))