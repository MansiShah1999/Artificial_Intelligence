import os,copy
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    val=corpus[page]
    out={}
    n=len(corpus.keys())
    k=round(float((1-damping_factor)/n),5)

    for key in corpus.keys():
    	out[key]=k

    if len(val)==0:
    	for key in corpus.keys():
    		out[key]+=(damping_factor/n)
    	return out

    for link in val:
    	out[link]+=(damping_factor/len(val))
    return out

    

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ans=dict()
    #select any one random no for random sample
    r=random.randint(0,len(corpus.keys())-1)
    sample=list(corpus.keys())[r]
    i=0
    for key in corpus.keys():
    	ans[key]=0

    while i<n:
    	i+=1
    	#increase the value of our sample by 1
    	ans[sample]+=1
    	#now select a random probability btw 0 to 1
    	prob=random.random()
    	model=transition_model(corpus,sample,damping_factor)
    	for page in model.keys():
    		if model[page]<prob:
    			prob-=model[page]
    		else:
    			#select the next page having max probability
    			sample=page
    			break
    normalize=sum(ans.values())
    for key in ans.keys():
    	#based on how many times a page was selected by sampling find pagerank
    	ans[key]=round(ans[key]/normalize,5)
    return ans
    



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ans={}
    n=len(corpus.keys())

    for i in corpus.keys():
    	ans[i]=float(1/n)

    flag=0
    while  not flag:
    	temp={}
    	flag=1

    	for i in ans.keys():
    		new=ans[i]
    		temp[i]=float((1-damping_factor)/n)
    		for page,link in corpus.items():
    			if i in link:
    				temp[i]+=float(damping_factor*ans[page]/len(link))

    		if abs(new-temp[i])>0.001:
    			flag=0
    	for i in ans.keys():
    		ans[i]=temp[i]
    return ans

if __name__ == "__main__":
    main()
