import sys
import gzip
import random
import math
def main(args):
    
    if len(args) >= 2:
        inputFile = args[1]
    else:
        #inputFile = "links.srt.gz"
        inputFile = "small.srt.gz"
    if len(args) >= 3:
        lmbda = float(args[2])
    else:
        lmbda = 0.2
    if len(args)>= 4:
        tu = float(args[3])
    else:
        tu = 0.005
    if len(args) >= 5:
        inLinksFile = args[4]
    else:
        inLinksFile = "inlinks.txt"
    if len(args) >= 6:
        pageRankFile = args[5]
    else:
        pageRankFile = "pagerank.txt"
    if len(args) >= 7:
        k = float(args[6])
    else:  
        k = 100

    r = random.random()
    rSurfer = False
    if r < lmbda:
        rSurfer = True
    
        
    inputFileR = gzip.open(inputFile).read().decode("utf-8")
    inLinks1 = inputFileR.splitlines()
    uniquePages = []
    inLinks2 = []
    for line in inLinks1:
        inLinks2.append(line.split('\t'))

    #find number of unique pages
    for site, link in inLinks2:
        if site not in uniquePages:
            uniquePages.append(site)
        if link not in uniquePages:
            uniquePages.append(link)

    numPages = len(uniquePages)
    initialPR = 1/numPages
    #print(pageList)
    #for site in inLinks2:
    #    if site[1] not in pageList:
     #       print(site)
     #       pageList.append(site[0])
    
    isTrue = False
    covered = []
    incomingLinksList = []
    incomingLinks = {}
    outgoingLinks = {}
    #get outbound links for each page
    incomingLinkCount = 0
    outgoingLinkCount = 0
    for currentSite in uniquePages:
        incomingLinkCount = 0
        outgoingLinkCount = 0
        if(currentSite not in covered):
            for site, link in inLinks2:
                if currentSite == link:
                    incomingLinkCount += 1
                if currentSite == site:
                    outgoingLinkCount += 1
        covered.append(currentSite)
        incomingLinksList.append([incomingLinkCount, currentSite])
        incomingLinks[currentSite] = incomingLinkCount
        outgoingLinks[currentSite] = outgoingLinkCount
    #print(outgoingLinks)
    
    incomingLinksList = sorted(incomingLinksList, key = lambda x: x[0], reverse=True)
    i = 1
    inLinksFile = open(inLinksFile, "w")

    #write page and links to file
    for pair in incomingLinksList:
        if i <= k:        
            inLinksFile.write(pair[1] + "\t" + str(i) + "\t" + str(pair[0])+ "\n")
            i += 1
        else:
            break

    inLinks1 = []
    """ for sites in inLinks2:
        for site, link in inLinks2:
            if sites[1] == site:
                isTrue = True
        if isTrue == True:
            inLinks1.append(sites)
            isTrue = False
    print(inLinks1, inLinks2) """
    #inLinks2 = []
    reached = []
    

    #group inlinks from same sites
    """ for site, link in inLinks1:
        newLink = []          
        newLink.append(site)
        newLink.append(link)
        if site not in reached:
            for site2, link2 in inLinks1:
                if site == site2 and link != link2 and site not in reached:
                    newLink.append(link2)
            inLinks2.append(newLink)
            reached.append(site)
            print(inLinks2) """
    newPR = []
    oldPR = []
    pageList1 = []
    linkList1 = []
    # for pages, links in inLinks:
    #     pageList1.append(pages)
    #     linkList1.append(links)
    # for iter1 in range(numPages):
    #     newPR[iter1] = 1/numPages
    #     oldPR[iter1] = 1/numPages
    #     for iter2 in range(numPages):
    #         for iter3 in range(numPages):
    #             if(inLinks2[iter2][0] != inLinks2[iter3][0]):
    #                 newPR[iter2] += oldPR[iter3]/ (len(inLinks2[iter3])-1)
    #     #for iter4 in range(numPages):
    i = 0
    
    pageRanks = {}
    newPageRanks = {}
    rButton = (lmbda / numPages)
    pageRanksList = []
    for page in uniquePages:
        pageRanks[page] = 1/numPages
    #print(pageRanks)
    #print(inLinks2)
    while i <= 5:
        for page in uniquePages:
            prSum = 0
            covered = []
            for comparePage in inLinks2:
                if len(covered) == incomingLinks[page]:
                    break
                if page is comparePage[1] and comparePage[0] not in covered:
                    print(prSum)
                    prSum += pow(pageRanks[comparePage[0]]/outgoingLinks[comparePage[0]],2)
                    
                    print(page, prSum,comparePage[0], pageRanks[comparePage[0]] , outgoingLinks[comparePage[0]])
                    covered.append(comparePage[0])
            

                    
            pr = rButton + (1-lmbda) * math.sqrt(prSum)
            print(page, pr, rButton, (1-lmbda), prSum, "\n")
            newPageRanks[page] = pr
            if i == 5:
                newPageRanks[page] = pr 
                pageRanksList.append([newPageRanks[page], page])
            #newPR.append((1-lmbda)+ lmbda*((1/numPages)* (len(page)-1)))
            #oldPR.append((1-lmbda)+ lmbda*((1/numPages)* (len(page)-1)))
        pageRanks = newPageRanks
        i += 1
    s = 0
    #print(inLinks2)
    pageRankFile = open(pageRankFile, "w")
    pageRanksList = sorted(pageRanksList, key = lambda x: x[0], reverse=True)
    #write page and links to file
    
    #this shouldnt be here
    #for i in uniquePages:
    #    pageRanks[i] = pageRanks[i]*1.58085604
    #    s += pageRanks[i]
    #    print(s, pageRanks[i])
    i = 1
    for pair in pageRanksList:
        if i <= k:   
            print(pair)     
            pageRankFile.write(pair[1] + "\t" + str(i) + "\t" + str(pair[0])+ "\n")
            i += 1
        else:
            break


main(sys.argv)