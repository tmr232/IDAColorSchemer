import itertools
import re
import pprint

COLOR_PAT = re.compile(r'^([0-9a-f]{6})\s+//(.*)$', re.MULTILINE)


def flip_rgb(rgb):
    return rgb[4:6] + rgb[2:4] + rgb[0:2]


def repl_maker(mapping: dict):
    counter = itertools.count(step=0xfff)

    def repl(m):
        color = next(counter)
        mapping[m.group(2)] = color
        print(f'{color:06x}')
        return f'{color :06x}\t'

    return repl


def create_mapped_clr(in_, out):
    with open(in_) as f:
        data = f.read()

    mapping = {}
    repl = repl_maker(mapping)
    mapped_clr = COLOR_PAT.sub(repl, data)

    with open(out, 'w') as f:
        f.write(mapped_clr)

    return mapping


def make_class_name(name: str) -> str:
    return name.replace(' ', '_')


def generate_style(mapping: dict):
    def gen_class_styles():
        for name, color in mapping.items():
            class_ = make_class_name(name)
            class_style = f'.{class_}{{color:#{color:06x};}}'
            yield class_style

    styles = '\n'.join(gen_class_styles())
    return f'<style>{styles}</style>'


def fixup_html(in_, out, mapping):
    with open(in_, encoding='utf-8') as f:
        data = f.read()

    new_data = data.replace('</head>', f'{generate_style(mapping)}</head>')

    reverse_mapping = {value: key for key, value in mapping.items()}

    for key, value in mapping.items():
        print(f'{value:06x} : {key}')

    not_found = set()
    def repl(m):
        try:
            return f'class="{make_class_name(reverse_mapping[int(flip_rgb(m.group(2)), 16)])}"'
        except:
            not_found.add(m.group(2))
            return f'class="Instruction"'
    new_data = re.sub('(style="color:#([0-9a-f]{6})")', repl, new_data)
    print(not_found)

    with open(out, 'w', encoding='utf-8') as f:
        f.write(new_data)


def main():
    mapping = create_mapped_clr('ugly.clr', 'mapped.clr')
    fixup_html('base.html', 'styled.html', mapping)
    print(flip_rgb('123456'))

if __name__ == '__main__':
    main()
