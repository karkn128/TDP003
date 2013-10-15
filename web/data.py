import json
from operator import itemgetter

def load(filename):
    """Loads JSON formatted project data from a file and returns a list."""
    try:
        with open(filename) as f:
            data = json.load(f)
            return data
    except: return None

def get_project_count(db):
    """Retrieves the number of projects in a project list."""
    return len(db)

def get_project(db, id):
    """Fetches the project with the specified id from the specified list."""
    for project in db:
        if project["project_no"] == id:
            return project
    return None

def get_techniques(db):
    """Fetches a list of all the techniques from the specified project list."""
    result = []
    for project in db:
        for technique in project["techniques_used"]:
            if not technique in result:
                result.append(technique)
    result.sort()
    return result

def get_technique_stats(db):
    """Collects and returns statistics for all techniques in the specified project list."""
    result = {}
    techniques = get_techniques(db)
    for technique in techniques: #Creates dict with all techniques as keys, empty lists as values
        result[technique] = []

    for technique in techniques: #Fills the dict with projects matching the key
        for project in db:
            if technique in project["techniques_used"]:
                result[technique].append({u'id': project["project_no"], u'name': project["project_name"]})
        result[technique].sort(key=itemgetter(u'name'))

    return result

def search(db, sort_by=u'start_date', sort_order=u'desc', techniques=None, 
search=None, search_fields=None): #Öka läsbarhet
    """Fetches and sorts projects matching criteria from the specified list."""
    result = [] #List for storage of matching projects
    for project in db:
        project_found = False #Assume project doesn't match search reqs
        field_list = list(project.values()) #Create a list with project dict values

        #If search_fields are specified
        if not search_fields == None:
            field_list.clear() #Empty list
            #Fill list with project values from user
            for field in search_fields: 
                field_list.append(project[field])

        #Elif field_list
        
        #If both search and techniques are sent
        if not search == None and not techniques == None:
            #If all techniques specified are in the project do the text search
            if set(techniques) <= set(project['techniques_used']):
                #Text search
                #Case insensitive 
                if search.upper() in [str(s).upper() for s in field_list]:
                    project_found = True
        #If only search is sent
        elif not search == None:
            #Case insensitive
            if search.upper() in [str(s).upper() for s in field_list]:
                project_found = True
        #If only techniques are sent
        elif not techniques == None:
            if set(techniques) <= set(project['techniques_used']):
                project_found = True
        #If neither search nor techniques are sent
        else:
            project_found = True            
                
        if project_found == True:
            result.append(project)  

    #Sort list ***************************
    result.sort(key=itemgetter(sort_by)) #Kolla om det går att fixa med parametrar
    if sort_order == 'desc':
        result.reverse()

    return result
