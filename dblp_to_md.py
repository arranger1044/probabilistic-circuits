import re

BIBTEX_ENTRIES = {'@inproceedings', '@article'}
SKIP_LIST = {'a', 'an', 'the', 'on', 'to', 'for', 'in'}

def extract_ref(entry):
    for b in BIBTEX_ENTRIES:
        entry = entry.replace(b, "")
    return remove_parenthesis(entry)

def remove_parenthesis(token):
    return token.strip("{}")

def invert_author(author):
    #
    # very crude heuristics
    names = author.split(' ')
    first_name = [names[0]]
    for n in names[1:]:
        if '.' in n:
            first_name.append(n)
        else:
            break
    # return names[-1] + ", " + " ".join(names[:-1])
    return " ".join([n for n in names if n not in first_name]) + ", " + " ".join(first_name)

def process_authors(token):

    token = remove_parenthesis(token)
    authors = token.split(" and\n")
    authors = [invert_author(a.strip()) for a in authors]
    return authors
    
def process_title(token):
    token = token.replace("\n", "")
    token = remove_parenthesis(token)    
    token = re.sub(' +', ' ', token)
    return token

def process_year(token):
    token = token.replace("\n", "")
    token = remove_parenthesis(token)
    return token

def process_venue(venue, year):
    venue = venue.replace("\n", "")
    venue = remove_parenthesis(venue)
    return "{} {}".format(venue, year)

def get_first_word(words):

    for w in words:
        if w.lower() not in SKIP_LIST:
            return w
    return ""

def process_ref(authors, year, title):
    first_author = authors.split(",")[0].strip().lower()
    first_author = re.sub(' +', '', first_author)
    first_word = get_first_word(title.split(" ")).strip().lower()
    return "{}{}{}".format(first_author, year, first_word)

def replace_ref(bibtex, new_ref):
    tokens = bibtex.split(',')
    entry = tokens[0]
    ref = extract_ref(str(entry))
    tokens[0] = entry.replace(ref, new_ref)
    return ','.join(tokens)

def replace_authors(bibtex, old_authors, new_authors):

    return bibtex.replace(old_authors, f"{{{new_authors}}}")
    
def break_tokens(bibtex):
    bibtex = bibtex.strip()
    tokens = bibtex.split(',')
    entry = tokens[0]

    #
    # discard first
    tokens = tokens[1:]
    tokens = [t.split("=") for t in tokens]
    data = {k.strip():v.strip() for k, v in tokens}
    old_authors = data["author"]
    data["author"] = " and ".join(process_authors(data["author"]))
    data["title"] = process_title(data["title"])
    data["year"] = process_year(data["year"])
    if "booktitle" in data:
        data["venue"] = process_venue(data["booktitle"], data["year"])
    else:
        data["venue"] = process_venue(data["journal"], data["year"])
    data["ref"] = process_ref(data["author"], data["year"], data["title"])

    bibtex = replace_ref(bibtex, data["ref"])
    bibtex = replace_authors(bibtex, old_authors, data["author"])
    bibtex = bibtex.replace('\n', '<br/>')
    return data, bibtex

def gen_markdown(data, bibtex, id):
    md = """---
layout: paper
ref: "{}"
title:  "{}"
date:   {}-08-{} 00:00
tags: ""
image: ""
authors: "{}"
pdf: ""
venue: "{}"
abstract: ""
bibtex: "{}"
---

    """.format(data["ref"], data["title"], data["year"], id, data["author"], data["venue"], bibtex)

    return md

if __name__ == "__main__":

    
    a = """


@inproceedings{DBLP:conf/icmla/DennisV17a,
  author    = {Aaron W. Dennis and
               Dan Ventura},
  title     = {Autoencoder-Enhanced Sum-Product Networks},
  booktitle = {{ICMLA}},
  pages     = {1041--1044},
  publisher = {{IEEE}},
  year      = {2017}
}

"""


    data, bibtex = break_tokens(a)
    print(gen_markdown(data, bibtex, 9))


