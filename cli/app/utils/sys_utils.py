"""Sytem utilities"""

import signal


class SignalInterrupt:

  interrupted = False

  def __init__(self):
    signal.signal(signal.SIGINT, self.signal_handler)

  def signal_handler(self, sig, frame):
    self.interrupted = True

  def check(self):
  	if self.interrupted:
  		sys.exit('Exiting. Signal interrupted')
  