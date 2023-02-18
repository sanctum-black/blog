"""
Created on Fri Feb 17 14:23:00 2023
@author: Pablo Aguirre
GitHub: https://github.com/pabloagn
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact
Part of Blog: what-is-julia-and-why-it-matters
"""

# JuliaMono Font
# ------------------------------

# Exaple 1: Greek letters
𝛂, 𝛃 = [1, 2]
println(𝛂)
println(𝛃)

# Example 2: conditionals
if 𝛂 ≥ 𝛃
    println("𝛂 is greated than 𝛃")
else
    println("𝛃 is greated than 𝛂")
end

# Example 3: Emojis
🧑 = "We "
❤️ = "love "
⭕ = "Julia"

println(🧑, ❤️, ⭕)

# Example 3: Emojis Inverted
a = "🚀"
b = "👩‍🚀"
c = "🌕"

println(a, b, c)