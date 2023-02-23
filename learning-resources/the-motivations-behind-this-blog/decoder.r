# Created on Thu Feb 22 19:09:12 2023
# 
# @author: pablo aguirre
# 
# GitHub: https://github.com/pabloagn
# Website: https://pabloagn.com
# Contact: https://pabloagn.com/contact
# 
# Part of Blog Article: the-motivations-behind-this-blog

library(comprehenr)

decodeString <- function(my_list, my_alphabet) {

  paste(
    to_list(
      for(x in my_list) ifelse(x >= 0, my_alphabet[x+1], ' ')
      ),
    collapse = '')

}

my_list = list(0, -1,
           9, 14, 20, 17, 13, 4, 24, -1,
           19, 7, 17, 14, 20, 6, 7, -1,
           3, 0, 19, 0, -1,
           18, 2, 8, 4, 13, 2, 4)

my_alphabet = LETTERS

decodeString(my_list, my_alphabet)