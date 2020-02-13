# Your code goes here

if __name__ == "__main__":

    filename = 'students.csv'

    # Ecrivez une fonction permettant de récupérer toutes les lignes
    # du fichier CSV dans une list() `data`
def getAllData():
    with open(filename, 'r') as student:
        data = []
        for line in student:
            words = line.split(',')
            data.append(words)
        return data
    
rows = getAllData()
print(f'\nLe fichier brut contient {len(rows)} lignes')

    # Les étudiants ont chacun un diplôme qui leur est attribué
    # La variable `degrees` contient la liste des diplômes
    
def getAllDegrees():
    students = getAllData()
    degrees = []
    exist = False 
       
    for student in students:
        for degree in degrees:
            if student[4] == degree:
                exist = True
        if not exist:
            degrees.append(student[4])
        exist = False
    return degrees
    
degrees = getAllDegrees()
print(f'\nLe fichier contient {len(degrees)} diplômes uniques')

    # Donnez, dans un dict, pour chaque diplôme le nombre d'étudiant
    # par catégorie d'utilisateur (student, alumni, ...)
def degPerStudent():
    students = getAllData()
    cats = {}
    exist = False
    
    for student in students:
        
        degree = student[5][:len(str(student[5]))-1]
        
        if len(cats)==0:
            cats.update({degree:1})
        else: 
            for cat in list(cats):
                
                if degree == cat:
                    
                    cats[degree]+=1
                    exist = True
                    
            if exist == False:
                cats.update({degree:1})
                
            exist = False
        
    return cats
    
    
users_per_degree = degPerStudent()
print(f'\nLa répartition des diplômes est la suivante :')
for degree in users_per_degree.keys():
    print(f' - {degree}, {users_per_degree[degree]} étudiants')


    # Enregistrez le dictionnaire dans un nouveau fichier `degree_count.json`

def exportJson(dict):
    json = open("degree_count.json", "w")
    count=0
    
    json.write("{\n")
    
    for degree in list(dict):
        
        count+=1
        
        json.write("\t'"+str(degree)+"':"+str(dict[degree]))
        
        if count != len(dict):
            json.write(",")
            
        json.write("\n")
        
    json.write("}")
        
    json.close() 

exportJson(degPerStudent())
print(f'\nFichier `degree_count.json` enregistré !')