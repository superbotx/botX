---
title: Customized componenet
permalink: /docs/example_customized_componenet/
---

```python
from botX.components import BaseComponent
from botX.applications import external_command_pool

class ZedCameraComponent(BaseComponent):

    def setup(self):
        """
        setup is the method we must implement which will be called
        in the robot interface
        """
        cmd = 'python fake_camera.py'
        proc_id = external_command_pool.start_command(cmd)
        self.camera_proc_id = proc_id

    def shutdown(self):
        external_command_pool.end_command(self.camera_proc_id)
```
