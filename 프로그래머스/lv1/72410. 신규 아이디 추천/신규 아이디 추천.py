import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]','',new_id)
    
    while new_id.find('..')>=0:
        new_id = new_id.replace('..','.')
    
    new_id = re.sub(r'^[.]|[.]$','',new_id)
    
    if not new_id:
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
    new_id = re.sub(r'[.]$','',new_id)
    
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id