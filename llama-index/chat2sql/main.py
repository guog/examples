import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# 只训练一次就行
import training

from vanna.flask import VannaFlaskApp
from my_vanna import vn

app = VannaFlaskApp(vn, allow_llm_to_see_data=True)
app.run()
