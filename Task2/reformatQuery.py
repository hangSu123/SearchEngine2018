#python script reformat querys


def readFile(filePath):
    with open(filePath, 'r') as queries:
        collection = queries.read().split('</top>')
    return collection


def trimQuery(queries):
    query = queries.split('\n\n')

    try:
        queryId = list(filter(lambda x: '<num>' in x, query))[0]
        queryId = '<num>' + [str(int(s))
                         for s in queryId.split() if s.isdigit()][0] + '</num>'

        eachQuery = list(filter(lambda x: '<title>' in x, query))[0].upper()
        eachQuery = eachQuery.replace('\t', '')
        eachQuery = eachQuery.replace('\n', '')
        eachQuery = eachQuery[15:]
        eachQuery = '<title>' + eachQuery + '</title>'
        queryHashmap = {'num': queryId, 'title': eachQuery}
        return queryHashmap

    except:
        print(query)


def saveToFile(split):
    def joinQuery(query):
        return '\n'.join(['<top>'] + list(query.values()) + ['</top>'])

    newQuery = '\n'.join([joinQuery(each) for each in split])
    with open('formatedQuery.trec', 'a') as queryFile:  
        queryFile.write(newQuery)


def reformatQuery(folderPath,queryFiles):
    merge = []
    for eachFile in queryFiles:
        text = readFile(folderPath + eachFile)
        merge += [x for x in [trimQuery(each) for each in text] if x is not None]

    return merge

def main():
    queryFiles = ['topics.51-100','topics.101-150','topics.151-200']
    folderPath = 'c:/A.study/cab431/AssignmentProject/query/'
    saveToFile(reformatQuery(folderPath,queryFiles))

if __name__ == "__main__":
    main()
