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
    names = author.split(' ')
    return names[-1] + ", " + " ".join(names[:-1])

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
date:   {}-06-{} 00:00
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

    
    a = """@inproceedings{DBLP:conf/bracis/SguerraC16,
  author    = {Bruno Massoni Sguerra and
               F{\'{a}}bio Gagliardi Cozman},
  title     = {Image Classification Using Sum-Product Networks for Autonomous Flight
               of Micro Aerial Vehicles},
  booktitle = {{BRACIS}},
  pages     = {139--144},
  publisher = {{IEEE} Computer Society},
  year      = {2016}
}"""


    data, bibtex = break_tokens(a)
    print(gen_markdown(data, bibtex, 27))


