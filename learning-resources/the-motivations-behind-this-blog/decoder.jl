#=
Created on Thu Feb 22 19:09:12 2023

@author: pablo aguirre

GitHub: https://github.com/pabloagn
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact

Part of Blog Article: the-motivations-behind-this-blog
=#

function decodeString(my_arr, my_alphabet)
    #=
    Parameters
    ----------
    my_arr : array
        An encrypted message.

    my_alphabet : vector
        Uppercase letters of the alphabet

    Returns
    -------
    decoded : string
        A decoded message.
    =#
    
    decoded = join([if x ≥ 0 my_alphabet[x+1] else ' ' end for x in my_arr])
    
    println(decoded)
    
    return decoded

end

# Declare message and alphabet
my_arr = [0 -1 [
         9] 14 20 17 13 4 24 -1 [
         19] 7 17 14 20 6 7 -1 [
         3] 0 19 0 -1 [
         18] 2 8 4 13 2 4]

my_alphabet = collect('A':'Z')

decodeString(my_arr, my_alphabet)