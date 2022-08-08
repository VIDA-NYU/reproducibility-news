import sys
import yaml


def list_entries(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        for nb, entry in enumerate(yaml.safe_load_all(fp)):
            for key in ['title', 'link', 'date', 'tags', 'description']:
                if not key in entry:
                    print(
                        "Missing key '%s' in entry #%d\n" % (key, nb),
                        file=sys.stderr,
                    )
                    sys.exit(1)

            entry['title'] = entry['title'].strip()
            entry['link'] = entry['link'].strip()
            entry['description'] = entry['description'].strip()
            if not entry['tags']:
                entry['tags'] = []

            yield entry
