from imhotep.tools import Tool
from collections import defaultdict
import json
import os


class Flake8Linter(Tool):
    def get_configs(self):
        return {'flake8', '.flake8'}

    def invoke(self, dirname, filenames=set(), linter_configs=set()):
        retval = defaultdict(lambda: defaultdict(list))
        config = ''
        for config_file in linter_configs:
            if 'flake8' in config_file:
                config = "--config=%s " % config_file
        if len(filenames) == 0:
            cmd = "find %s -name '*.py' | xargs flake8 %s" % (dirname, config)
        else:
            python_files = []
            for filename in filenames:
                if '.py' in filename:
                    python_files.append("%s/%s" % (dirname, filename))

            cmd = "flake8 %s %s" % (config, " ".join(python_files))
        try:
            output = self.executor(cmd)
            for line in output.split('\n'):
                path, line, column, message = line.split(':')
                file_name = os.path.abspath(path)
                file_name = file_name.replace(dirname, "")[1:]
                retval[str(file_name)][line].append(message.lstrip(' '))
        except:
            pass
        return retval
