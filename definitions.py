#!/usr/bin/env python

#If a token requires another token then please specify it before the needed token

def definitions(self):
    definitions = {
        '@DOMAIN@' : "DOMAIN.NAME.COM",
        '@DC_LOWER@' : str(self.params.farm).lower(),
        '@DC_UPPER@' : self.params.farm,
    }

    # The new code for appending or write some new defs: - adapted from code provided by @beeva-javiermartincaro

    if self.params.definitions:
        for extras in self.params.definitions:
            if str(extra).startswith("{"):
                extra_data = json.loads(extras)
            else:
                try:
                    extra_data = json.loads(open(str(extra)))
                except Exception:
                    continue
                definitions.update(extra_data)
    return definitions

