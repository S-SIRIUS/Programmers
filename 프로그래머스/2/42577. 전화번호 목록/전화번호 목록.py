def solution(phone_book):
    
    phone_book_hash={}
    for phone in phone_book:
        phone_book_hash[phone] = 1
    
    for phone in phone_book:
        jeobdoo=""
        for sub in phone:
            jeobdoo+=sub
            if jeobdoo in phone_book_hash and jeobdoo!=phone:
                return False
    return True
        
    
            
    return True