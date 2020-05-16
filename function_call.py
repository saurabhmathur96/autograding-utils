import signal
import time

# source: https://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish/22348885#22348885
class timeout:
  ''' a timeout context. 
  all code executed within it will be interrupted if it does not finish within the given time limit 

  Attributes:
    seconds (int)
    error_message (str)

  Example: 
    >>> with timeout(seconds=2):
    ...   try:
    ...     time.sleep(10)
    ...   except TimeoutError:
    ...     print ('Timed out!')
    ... 
    Timed out!
  '''
  def __init__(self, seconds=1, error_message='Timeout'):
    self.seconds = seconds
    self.error_message = error_message
  def handle_timeout(self, signum, frame):
    raise TimeoutError(self.error_message)
  def __enter__(self):
    signal.signal(signal.SIGALRM, self.handle_timeout)
    signal.alarm(self.seconds)
  def __exit__(self, type, value, traceback):
    signal.alarm(0)


