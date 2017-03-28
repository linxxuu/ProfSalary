class GoogleScholarPublication(object):

    def __init__(self, title, authors, publisher, citations, year):
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.citations = citations
        self.year = year

class GoogleScholarScholar(object):

    def __init__(self, scholar, citations, hindex, i10index, publications):
        self.scholar = scholar
        self.citations = citations
        self.hindex = hindex
        self.i10index = i10index
        self.publications = publications
