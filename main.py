# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re

def sparql_to_mermaid(sparql_text, first_call=True):
    # Use a breakpoint in the code line below to debug your script.

    tokens = sparql_text.split('{', 1)[1].strip().replace('}','')
    if first_call:
        mermaid = """```mermaid
    graph TD 
"""
    else:
        mermaid = ""
    for token in tokens.split('.'):
        token = re.sub('#.*\n', '', token)
        subtoken = token.strip().split()
        if len(subtoken) == 3:
            mermaid += "\t\t" + subtoken[0] + "-->|" + subtoken[1] + "|" + subtoken[2].replace("\"","''") + "\n"
        elif len(subtoken) > 0 and subtoken[0].lower().__contains__("optional"):
            mermaid += sparql_to_mermaid(token, False)
    if first_call:
        mermaid += """```"""
    return mermaid



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   query =  """SELECT ?gene ?organ ?taxon_label WHERE {
				?gene genex:isExpressedIn ?organ .
				?organ rdfs:label "lung" .
				?gene orth:organism ?organism .
				?organism obo:RO_0002162 taxon:10116 .
OPTIONAL {taxon:10116 rdfs:label ?taxon_label}
			
			}
			"""
  # print(q)
   print(sparql_to_mermaid(query))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
