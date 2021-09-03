import time
from utils2 import step
from utils import outputTime
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
def runServer():
    RMSupportedREF = "../RMSupportedREF.txt"
    # RMPath = "/Users/leichen/ResearchAssistant/RefactoringMiner_commandline/RefactoringMiner-2.1.0/bin/RefactoringMiner"
    RMPath = "/home/chenlei/RA/RefactoringMiner/build/distributions/RefactoringMiner-2.1.0/bin/RefactoringMiner"
    # tempList=["RoboBinding","goclipse","hydra","bitcoinj"]
    tempList=["RoboBinding"]
    for  temp in tempList:
        repoPath = "/home/chenlei/RA/data/" + temp
        git_stein = "/home/chenlei/RA/git-stein/build/libs/git-stein-all.jar"
        recipe = "./recipe.json"
        squashedOutput = "/home/chenlei/RA/output/" + temp


        for clusterNum in range(2, 5):
            time_start = time.time()

            miaomiao = squashedOutput
            miaomiao += str(clusterNum)
            CompareResult = miaomiao + "/compareResult.txt"
            step(RMPath=RMPath,repoPath=repoPath, recipe=recipe, git_stein=git_stein, squashedOutput=miaomiao, clusterNum=clusterNum,
                 compareResult=CompareResult,RMSupportedREF=RMSupportedREF)

            time_end = time.time()
            t = time_end - time_start
            tResult = outputTime(t)
            print(tResult)
            with open(CompareResult+"/time.txt", "w") as f:
                f.writelines(tResult)

if __name__ =="__main__":
    runServer()