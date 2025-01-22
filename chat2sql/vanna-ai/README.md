# chat2SQL

基于[Vanna.AI](https://vanna.ai/) 自然语言生成SQL并执行，生成查询结果和Chart。

## 本地运行

- 安装 [Ollama](https://ollama.com/)
- 拉取LLM，如 `ollama pull llama3:latest`，建议本地使用llama3模型，与`my_vanna.py`文件中的配置相对应;
- 安装python3.11+
- 创建虚拟环境，`python -m venv .venv`
- 进入虚拟环境，`.venv/bin/activate` (退出时执行 `deactivate`)
- 安装依赖 `pip install -r requirements.txt`
- 修改配置：
  - `main.py` 中 `import training`只应运行一次，在首次运行前去掉前面的 `#`；
  - `my_vanna.py`中 配置模型及数据库连接信息，模型与本地拉取的LLM对应。
- 本地启动 `python main.py`

在浏览器中打开 [http://localhost:8084/](http://localhost:8084/)

## 目录说明

- `ddl/*` : 数据库DDL，其中`db.sql`包含整个数据库Schema和数据,可用来构建数据库，其余为各个表结构。
- `trainings/*` : 训练数据
- `.gitignore`: git忽略文件
- `main.py` : 项目主文件
- `requirements.txt` : Python项目依赖文件

## 运行截图

![截图](./demo.JPG)
