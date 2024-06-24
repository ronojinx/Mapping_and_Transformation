def transformation_matrix(turtle_list):
    turtle_str = f""
    mdd = "PREFIX mdd: <https://dictionary.mydata.org/#>"
    xsd = "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"
    rdf = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
    cco = "PREFIX cco: <http://www.ontologyrepository.com/CommonCoreOntologies/>"
    pop = "PREFIX pop: <https://opensource.ieee.org/person-ontology-group/person-ontology-project/-/blob/master/dev/Person-Ontology-dev.ttl->"
    
    turtle_str += f"{mdd} \n{xsd} \n{rdf} \n{cco} \n{pop} \n"

    for row in turtle_list:
        turtle_str += f"\n cco:Person rdf:type cco:OccupationRole "
        if row[0] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-firstname "{row[0]}" '
        if row[1] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-lastname "{row[1]}" '
        if row[2] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-birthdate "{row[2]}"^^xsd:date '
        if row[3] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-mailingstreet "{row[3]}" '
        if row[4] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-mailingcity "{row[4]}" '
        if row[5] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-mailingstate "{row[5]}" '
        if row[6] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-mailingcountry "{row[6]}" '
        if row[7] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-mailingpostcode "{row[7]}" '
        if row[8] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-email "{row[8]}" '
        if row[9] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-mobilephonenumber "{row[9]}" '
        if row[10] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-homephonenumber "{row[10]}" '
        turtle_str += ' . \n'

        if row[11] != "":
            turtle_str += f'\n cco:OccupationRole mdd:my-employeetitle "{row[11]}" '
            if row[12] != "":
                turtle_str += ' ; \n'
                turtle_str += f'mdd:my-employername "{row[12]}" '
            if row[13] != "":
                turtle_str += ' ; \n'
                turtle_str += f'mdd:my-employerindustry "{row[13]}" '
            if row[14] != "":
                turtle_str += ' ; \n'
                turtle_str += f'mdd:my-employerstreet "{row[14]}" '
            if row[15] != "":
                turtle_str += ' ; \n'
                turtle_str += f'mdd:my-employercity "{row[15]}" '
            if row[16] != "":
                turtle_str += ' ; \n'
                turtle_str += f'mdd:my-employerstate "{row[16]}" '
            if row[17] != "":
                turtle_str += ' ; \n'
                turtle_str += f'mdd:employerpostcode "{row[17]}" '
            if row[18] != "":
                turtle_str += ' ; \n'
                turtle_str += f'mdd:employercountry "{row[18]}" '
            if row[19] != "":
                turtle_str += ' ; \n'
                turtle_str += f'mdd:employerphone "{row[19]}" '
            if row[20] != "":
                turtle_str += ' ; \n'
                turtle_str += f'mdd:employerfax "{row[20]}" '
            turtle_str += ' . '
      
    turtle_str += "\n\n # END!"
    print(turtle_str)

    return turtle_str

def transformation_form_matrix(row):
    turtle_str = f""
    mdd = "PREFIX mdd: <https://dictionary.mydata.org/#>"
    xsd = "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"
    rdf = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
    cco = "PREFIX cco: <http://www.ontologyrepository.com/CommonCoreOntologies/>"
    pop = "PREFIX pop: <https://opensource.ieee.org/person-ontology-group/person-ontology-project/-/blob/master/dev/Person-Ontology-dev.ttl->"
    
    turtle_str += f"{mdd} \n{xsd} \n{rdf} \n{cco} \n{pop} \n"

    turtle_str += f"\n cco:Person rdf:type cco:OccupationRole "
    if row[0] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-firstname "{row[0]}" '
    if row[1] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-lastname "{row[1]}" '
    if row[2] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-birthdate "{row[2]}"^^xsd:date '
    if row[3] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-mailingstreet "{row[3]}" '
    if row[4] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-mailingcity "{row[4]}" '
    if row[5] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-mailingstate "{row[5]}" '
    if row[6] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-mailingcountry "{row[6]}" '
    if row[7] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-mailingpostcode "{row[7]}" '
    if row[8] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-email "{row[8]}" '
    if row[9] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-mobilephonenumber "{row[9]}" '
    if row[10] != "":
        turtle_str += ' ; \n'
        turtle_str += f'mdd:my-homephonenumber "{row[10]}" '
    turtle_str += ' . \n'
    
    if row[11] != "":
        turtle_str += f'\n cco:OccupationRole mdd:my-employeetitle "{row[11]}" '
        if row[12] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-employername "{row[12]}" '
        if row[13] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-employerindustry "{row[13]}" '
        if row[14] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-employerstreet "{row[14]}" '
        if row[15] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-employercity "{row[15]}" '
        if row[16] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:my-employerstate "{row[16]}" '
        if row[17] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:employerpostcode "{row[17]}" '
        if row[18] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:employercountry "{row[18]}" '
        if row[19] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:employerphone "{row[19]}" '
        if row[20] != "":
            turtle_str += ' ; \n'
            turtle_str += f'mdd:employerfax "{row[20]}" '
        turtle_str += ' . '
      
    turtle_str += "\n\n # END!"
    return turtle_str