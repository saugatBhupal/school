import requests
import xmltodict

urlOAI = 'http://localhost:8080/oai/request?verb=ListRecords&metadataPrefix=ore&set=com_123456789_3'
reqOAI = requests.get(urlOAI)
OAI = xmltodict.parse(reqOAI.content)
#[print(key) for key in OAI.keys]
print(OAI['OAI-PMH']['@xmlns'])


url = 'http://localhost:8080/xmlui/bitstream/123456789/5/1/3.1_Enzymes_Theory_qp.pdf'
req = requests.get(url, stream=True)

with open('/Users/saugatsingh/Documents/Python/Dspace/metadata.pdf', 'wb') as fd:
    for chunk in req.iter_content(2000):
        fd.write(chunk)
