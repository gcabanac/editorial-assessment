# Harvest Crossref for editorial assessment dates for ISSN 1866-7538: Arabian Journal of Geosciences (https://www.springer.com/journal/12517)
# See also https://retractionwatch.com/2021/08/26/guest-editor-says-journal-will-retract-dozens-of-inappropriate-papers-after-his-email-was-hacked/
# See also https://retractionwatch.com/2021/09/28/springer-nature-slaps-more-than-400-papers-with-expressions-of-concern-all-at-once/
# @since   06-SEP-2021
# @version 29-SEP-2021

# Crossref (https://github.com/fabiobatalha/crossrefapi)
import crossref.restful as cr
import jmespath

# Please use the polite method to query the Crossref API (https://github.com/CrossRef/rest-api-doc#good-manners--more-reliable-service)
# crossref = cr.Journals(etiquette=cr.Etiquette('editorial-assessment', '1.0', 'your URL', 'your email'))

# Public Crossref API with no etiquette
crossref = cr.Journals()
# https://github.com/CrossRef/rest-api-doc#multiple-filters
for pub in crossref.works('1866-7538').filter(from_pub_date='2018-01-01').select('author,assertion,DOI,title,volume').sort('published-print').order('desc'): 
    doi     = pub.get('DOI')
    title   = pub.get('title')[0]
    volume  = pub.get('volume')
    dateReceived = jmespath.search("assertion[?name == 'received'].value|[0]", pub)
    dateAccepted = jmespath.search("assertion[?name == 'accepted'].value|[0]", pub)
    dateOnline   = jmespath.search("assertion[?name == 'first_online'].value|[0]", pub)
    
    authors = '; '.join([a.get('family') +', '+a.get('given', 'NO-GIVEN-NAME') for a in pub.get('author')]) if pub.get('author') else 'NO-AUTHORS'

    print(doi, volume, dateReceived, dateAccepted, dateOnline, title, authors, sep='\t')