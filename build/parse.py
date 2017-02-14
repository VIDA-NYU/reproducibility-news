import io
import sys
import yaml


def list_entries(filename):
    with io.open(filename, encoding='utf-8') as fp:
        for nb, entry in enumerate(yaml.load_all(fp)):
            for key in ['title', 'link', 'date', 'tags', 'description']:
                if not key in entry:
                    sys.stderr.write("Missing key '%s' in entry #%d\n" % (
                                     key, nb))
                    sys.exit(1)

            entry['title'] = entry['title'].strip()
            entry['link'] = entry['link'].strip()
            entry['description'] = entry['description'].strip()
            if not entry['tags']:
                entry['tags'] = []

            yield entry
