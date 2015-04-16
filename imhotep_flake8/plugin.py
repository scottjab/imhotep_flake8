from imhotep.tools import Tool
from collections import defaultdict
import json
import os
import logging

log = logging.getLogger(__name__)

class Flake8Linter(Tool):
    def get_configs(self):
        return {'flake8', '.flake8', 'setup.cfg'}

    def invoke(self, dirname, filenames=set(), linter_configs=set()):
        retval = defaultdict(lambda: defaultdict(list))
        config = ''
        for config_file in linter_configs:
            config = "--config=%s " % config_file
            break

        if len(filenames) == 0:
            cmd = "find %s -name '*.py' | xargs flake8 %s" % (dirname, config)
        else:
            python_files = []
            for filename in filenames:
                if '.py' in filename:
                    python_files.append("%s/%s" % (dirname, filename))

            if len(python_files) == 0:
                # Exit early if no files, will speed linting.
                return retval
            cmd = "flake8 %s %s" % (config, " ".join(python_files))
        try:
            output = self.executor(cmd)
            for line in output.split('\n'):
                log.debug("flake8: %s", line)
                path, line, column, message = line.split(':')
                file_name = os.path.abspath(path)
                file_name = file_name.replace(dirname, "")[1:]
                retval[str(file_name)][line].append(message.lstrip(' '))
        except:
            pass
        return retval
