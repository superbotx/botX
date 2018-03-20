---
title: Botx export
permalink: /docs/example_botX_export/
---

```python
from example_customized_componenet import ZedCameraComponent

botXexport = {
    'zed_camera': {
        'module': ZedCameraComponent,
        'type': 'api',
        'inputs': [],
        'outputs': [],
        'requirements': ['camera', 'ros'],
        'description': 'example api'
    },
}
```
