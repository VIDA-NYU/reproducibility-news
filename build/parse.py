from datetime import datetime
import io
import sys
import traceback


class StrippedCountedIterator(object):
    def __init__(self, fp):
        self.fp = fp
        self.line_number = 0

    def __iter__(self):
        return self

    def next(self):
        l = next(self.fp).strip()
        self.line_number += 1
        return l


def list_entries(filename):
    with io.open(filename, encoding='utf-8') as fp_:
        fp = StrippedCountedIterator(fp_)
        while True:
            try:
                title = next(fp)
            except StopIteration:
                break
            else:
                if not title:
                    continue
                try:
                    link = next(fp)
                    date = next(fp)
                    date = datetime.strptime(date, '%Y-%m-%d')
                    tags = next(fp)
                    if not tags.strip():
                        tags = []
                    else:
                        tags = [tag.strip() for tag in tags.split(',')]
                    description = []
                    try:
                        while True:
                            line = next(fp)
                            if not line:
                                line = next(fp)
                                if not line:
                                    break
                                else:
                                    description.append('')
                            description.append(line)
                    except StopIteration:
                        pass
                    if not description:
                        sys.stderr.write("Missing description line %d\n" %
                                         fp.line_number)
                        sys.exit(1)
                    description = '\n'.join(description)

                    yield {
                        'title': title,
                        'link': link,
                        'date': date,
                        'tags': tags,
                        'description': description,
                    }
                except StopIteration:
                    sys.stderr.write("The last entry is incomplete\n")
                    sys.exit(1)
                except Exception:
                    traceback.print_exc()
                    sys.stderr.write("Error located on line %d\n" %
                                     fp.line_number)
                    sys.exit(1)
