import time
from MyRepository import MyRepository, create_folder
from RefactoringMiner import RefactoringMiner
from jsonUtils import JsonUtils
from utils2 import RMDetect
from utils import outputTime


def normal_detect(RMPath:str,repoPath:str,output:str):

    '''Initialize workspace'''
    #set Repository
    repo = MyRepository(repoPath)
    repo.createWorkSpace()

    # create_folder(squashedOutput)
    '''Obtain git commit info in Json form'''
    #create a json file read json file
    jU=JsonUtils()
    jU.setRepoPath(repo.repoPath)
    jU.gitJson()
    commits=jU.jsonToCommit()

    rm = RefactoringMiner(RMPath)


    create_folder(output)
    'RM detect commits after squash'
    repo.setRMoutputPath(output)
    time_start = time.time()
    for each in commits:
        RMDetect(rm,each.commitID, repo)
    time_end = time.time()
    t = time_end - time_start
    tResult = outputTime(t)
    print(tResult)
    with open("./time.txt", "w") as f:
        f.writelines(tResult)

if __name__ =="__main__":
    'server'
    RMPath="/home/chenlei/RA/RefactoringMiner/build/distributions/RefactoringMiner-2.1.0/bin/RefactoringMiner"
    'local'
    RMPath="/Users/leichen/ResearchAssistant/RefactoringMiner_commandline/RefactoringMiner-2.1.0/bin/RefactoringMiner"

    repoPath = "/home/chenlei/RA/data/RoboBinding"
    repoPath = "/Users/leichen/ResearchAssistant/InteractiveRebase/data/refactoring-toy-example"

    output = repoPath+"/normal_detect"

    normal_detect(RMPath=RMPath,repoPath=repoPath,output=output)