import os
import importlib
from dotenv import load_dotenv
import re

load_dotenv()

def format_task_name(name):
    # Convert camelCase to a more readable format
    formatted_name = re.sub(r'(?<!^)(?=[A-Z])', ' ', name).title()
    return formatted_name

def autoload_tasks():
    task_modules = {}
    task_dir = os.path.join(os.path.dirname(__file__), 'tasks')
    
    default_tasks = os.getenv('DEFAULT_TASKS').split(',')

    for filename in os.listdir(task_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module = importlib.import_module(f'tasks.{module_name}')
            task_modules[module_name] = module.run
    
    default_task_modules = {format_task_name(name): task_modules[name] for name in default_tasks if name in task_modules}
    other_task_modules = {format_task_name(name): func for name, func in task_modules.items() if name not in default_tasks}
    
    return default_task_modules, other_task_modules

default_tasks, other_tasks = autoload_tasks()
