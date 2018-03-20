---
title: Component usage
permalink: /docs/example_component_usage/
---

```python
import time
from example_botX_export import botXexport

zed_camera = botXexport['zed_camera']['module']()

zed_camera.setup()

time.sleep(10)

zed_camera.shutdown()
```
