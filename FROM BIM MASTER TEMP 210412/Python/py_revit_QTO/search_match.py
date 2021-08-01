
import re,random
import unidecode
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#


def lookup(search_text,lookup_value,return_value):
    flag_exist = False
    flag_match_vowel = False
    flag_match_consonent = False
    flag_match_start_end = False

    flag_char_in_lk_75_percentage = False

    # flag_math_random = False # TODO: next
    #INPUT LIST LOOKUP
    lookup_values= [unidecode.unidecode(s).lower().strip().replace(' ','') for s in lookup_value.split(',')]
    print(lookup_values)
    # Check Exist toàn bộ nội dung text xuất hiện trong Danh sách tìm kiếm
    flag_exist = search_text in lookup_values
    # Check match Nguyên âm
    search_text_vowels = search_text
    for c in vowels:
        if c in search_text_vowels:
            search_text_vowels = search_text_vowels.replace(c,'.')
    # print(search_text_vowels)
    X = sum([len(re.findall(search_text_vowels, lk)) for lk in lookup_values])
    print(X)
    flag_match_vowel = X >0

    # Check match phụ âm
    search_text_consonent = search_text
    for c in consonent:
        if c in search_text_consonent:
            search_text_consonent = search_text_consonent.replace(c,'.')
    # print(search_text_consonent)
    Y = sum([len(re.findall(search_text_consonent, lk)) for lk in lookup_values])
    print(Y)
    flag_match_consonent =  Y > 0

    # Check start with 
    percentage = 0.33
    if len(search_text) > 6:
        start_with = search_text[:int(len(search_text)*percentage)]
        end_with = search_text[-int(len(search_text)*percentage)]
        flag_match_start_end = True in [start_with in s and end_with in s for s in lookup_values]

    print(flag_exist,flag_match_vowel,flag_match_consonent,flag_match_start_end)
    if flag_exist:
        return return_value
    # elif  flag_match_vowel and flag_match_consonent: # TODO: RECHECK LOGIC FLOW
    #     return return_value
    elif flag_match_start_end:
        return return_value
    else:
        return "NA"

#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':  
    #-----------------------------#
    # GLOBAL VARIABLE
    #-----------------------------#
    vowels = 'ueoaiy'
    consonent = 'bcdfghjklmnpqrstvwxyz'
    #INPUT SEARCH TEXT
    search_text = 'crete'
    lookup_values = "SW,PARAPET WALL,SHEAR WALL,CONCRETE WALL"
    return_value = 'SW'

    print(lookup(search_text,lookup_values,return_value))




