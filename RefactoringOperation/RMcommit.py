import json
from RefactoringOperation import RefactoringOperation

class RMcommit:
    def __init__(self,jsonPath):
        self.jsonPath = jsonPath
        self.commitID = ""
        self.refactorings=list()
        self._initFromRMjson()

    def _initFromRMjson(self):
        '''
        using result extracted from RefactoringMiner to initialize RefactoringOperation class
        :param jsonPath: file path for RefactoringMiner json result
        :return: sha1,type,description
        '''
        with open(self.jsonPath) as f:
            data = json.load(f)
        self.commitID = data["commits"][0]["sha1"]
        refactorings = data["commits"][0]["refactorings"]
        for each in refactorings:
            self.refactorings.append(RefactoringOperation(each))

if __name__ == "__main__":
    filePath1 = "/Users/leichen/Desktop/RTEcommit.json"
    filePath2 = "/Users/leichen/Desktop/RTEcommit4.json"
    filePath3 = "/Users/leichen/Desktop/RTEcommit2.json"
    rMcommit = RMcommit(filePath1)
    rMcommit2 = RMcommit(filePath2)
    rMcommitSquashed = RMcommit(filePath2)
    print(rMcommitSquashed.refactorings[1].description)
    print(rMcommit.refactorings[1].description)
    print(rMcommitSquashed.refactorings[1]==rMcommit.refactorings[1])
    test = set()
    for ro in rMcommit.refactorings:
        test.add(ro)
    print(len(test))
    for ro in rMcommit2.refactorings:
        test.add(ro)

    test2 = set()
    for ro in rMcommitSquashed.refactorings:
        test2.add(ro)
    test = test-test2
    print(len(test))