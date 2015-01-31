#!/usr/bin/env python

import json

# If a token requires another token then please specify it before the needed token
def definitions(self):
    definitions = {
        '@DOMAIN@': "DOMAIN.NAME.COM",
        '@DC_LOWER@': str(self.params.farm).lower(),
        '@DC_UPPER@': self.params.farm,
    }

# The new code for appending or write some new defs: - adapted from code provided by @beeva-javiermartincaro
    if self.params.definitions:
        for extra in self.params.definitions:
            if str(extra).startswith("{"):
                try:
                    extra_data = json.loads(extra)
                    definitions.update(extra_data)
                except Exception as e:
                    self.log.debug(e)
                    quit("There is a problem loading your definitions JSON. Check it with a JSON parser")
            else:
                try:
                    extra_data = json.loads(open(str(extra)))
                    definitions.update(extra_data)
                except Exception as e:
                    self.log.debug(e)
                    continue
    return definitions

