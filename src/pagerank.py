import sys

def main(args):
    
    if len(args) >= 2:
        inputFile = args[1]
    else:
        #inputFile = "links.srt.gz"
        inputFile = "small.srt"
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
    inputFileR = open(inputFile, 'r').read()
    inLinks1 = inputFileR.splitlines()
    pageList = []

    inLinks2 = []
    for line in inLinks1:
        inLinks2.append(line.split('\t'))
    for addrCount, addr in enumerate(inputFileR):
        pass
    addrCount += 1
    inLinks = inLinks2
    #find number of unique pages
    for site, links in inLinks2:
        if site not in pageList:
            #print(site)
            pageList.append(site)
        #if links 
    numPages = len(pageList)
    #print(pageList)
    #for site in inLinks2:
    #    if site[1] not in pageList:
     #       print(site)
     #       pageList.append(site[0])
    inLinks1 = []
    isTrue = False

    #remove dead inlinks
    for sites in inLinks2:
        for site, link in inLinks2:
            if sites[1] == site:
                isTrue = True
        if isTrue == True:
            inLinks1.append(sites)
            isTrue = False
    inLinks2 = []
    reached = []

    #group inlinks from same sites
    for site, link in inLinks1:
        newLink = []          
        newLink.append(site)
        newLink.append(link)
        if site not in reached:
            for site2, link2 in inLinks1:
                if site == site2 and link != link2 and site not in reached:
                    newLink.append(link2)
            inLinks2.append(newLink)
            reached.append(site)
            print(inLinks2)
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
            
            
    for page in inLinks2:
        pr = (1-lmbda)+ lmbda*((1/numPages)* (len(page)-1))
        print(pr)
        newPR.append((1-lmbda)+ lmbda*((1/numPages)* (len(page)-1)))
        oldPR.append((1-lmbda)+ lmbda*((1/numPages)* (len(page)-1)))
    print(inLinks2)

main(sys.argv)