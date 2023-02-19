### A Pluto.jl notebook ###
# v0.19.22

using Markdown
using InteractiveUtils

# ╔═╡ 72152220-9129-4a0f-8d87-66db36edb0c1
using TypeTree

# ╔═╡ dd145092-afde-11ed-042f-4da8249ada73
md"""
# Julia Basic Syntax
"""

# ╔═╡ a11cfd20-1126-49f9-b258-3fe779625d20
md"""
## 1. Comments
"""

# ╔═╡ 84900720-b902-4a60-ab1b-301ae8ae9e85
# This is a single-line comment

#=
This is a multiline comment
=#

# ╔═╡ c80e1930-92cf-47bd-b5b5-276e664a2854
my_var = 3.1416 # This is Pi

# ╔═╡ e46df2a1-72ed-4aeb-b2b0-ed75da8f2721
md"""
## 2. Variables
"""

# ╔═╡ 1526e1e1-2472-42f3-975c-9ba17ffc2c08
begin
	# Assigning integer
	x = 10
	 
	# Assigning string types
	y = "Hello World"
	 
	# Assigning float types
	z = -3.1416
	 
	# Using a Unicode character as variable name
	λ = 30
	
	println(x)
	println(y)
	println(z)
	println(λ)
end

# ╔═╡ abd69392-ebaf-45ed-b3e6-eac36da98b59
γ, θ = 300, 200

# ╔═╡ 9d1ffffb-6bf6-4839-ae5b-d9c902d3a905
println(γ, " + ", θ)

# ╔═╡ 21a00515-1262-437d-aac6-4cb81971e20e
md"""
## 3. Print statements
"""

# ╔═╡ 21a9d373-e130-464f-b72d-4ef2cdbe2af1
π, ℯ = 3.1416, 0.5772

# ╔═╡ 25377598-ebac-4c52-9f71-afaea5735b51
begin
	print(π)
	print(ℯ)
end

# ╔═╡ 6be52879-6cdf-467a-b4de-366d41c25ca5
begin
	println(π)
	println(ℯ)
end

# ╔═╡ 64ae103e-beb3-4913-918d-a01ba6168f54
md"""
## 4. Data types
"""

# ╔═╡ 3efac976-948f-4d87-8f62-0c077a31469e
print(join(tt(Signed), ""))

# ╔═╡ 2c3455cd-5e5d-46bc-9cf7-cf8650b6bc68
print(join(tt(Number), ""))

# ╔═╡ 980552a1-1aa6-4e70-8bd3-34e8252a0646
print(join(tt(Any), ""))

# ╔═╡ 21665973-d846-4968-a0b0-141cbfb905d8
d::Int64 = 1000

# ╔═╡ e84914ce-3f71-4ee5-9de0-67aa0f94b4c7
typeof(d)

# ╔═╡ e4d69a3a-a0d9-4595-b6de-df341957688b
d isa Int64

# ╔═╡ c712423b-0216-40bb-bec6-e8a2ff58b967
δ = convert(UInt64, d)

# ╔═╡ ad3de390-6cbb-4489-b3c2-fa91b06781b5
g::Float64 = 1000

# ╔═╡ 1935cc41-a37d-40c1-b026-08012029a0ae
g

# ╔═╡ bd8422df-dd53-4038-b60f-db3d1c4c85e2
begin
	β = 7
	typeof(β)
end

# ╔═╡ 97332772-09e5-454d-8fc9-57c7ecee2ae3
β_1 = bitstring(β)

# ╔═╡ 77d44c4c-69ce-4a33-98ea-0dfdff891a9a
σ = "This is the greek letter sigma"

# ╔═╡ d8dfe4b6-03ca-455a-bca1-0f8c333799ec
typeof(σ)

# ╔═╡ 885cdf99-93dc-43b6-91b3-661239d08a3a
σ[13:17]

# ╔═╡ a92ba817-861a-4324-a47b-f93d15ed4fba
σ[1]

# ╔═╡ ae392cb9-6c3d-48fd-b795-5d785e471601
typeof(σ[1])

# ╔═╡ 13466385-7498-48c0-866b-a401ba882b26
my_char = 'π'

# ╔═╡ 57a6dfde-97e7-4d64-baaf-03d4d8c16783
begin
	my_int_char = '?'
	println(my_int_char)
	println(typeof(my_int_char))
	my_int_char = Int(my_int_char)
	println(my_int_char)
	println(typeof(my_int_char))
end

# ╔═╡ 6b9873db-7c6a-400e-99aa-544411b430a1
Char(my_int_char)

# ╔═╡ c0203f14-6ed6-4c69-b050-de8d7c71249b
begin
	b = true
	t = false
end

# ╔═╡ dc942f9a-546f-4b66-bef4-43d3c3784e5a
begin
	println(typeof(b))
	println(typeof(t))
end

# ╔═╡ 6123c2a9-f3d3-45b7-b3bf-784a04043aa0
b - 1

# ╔═╡ 4a7c3cae-7071-4a21-b8d5-a537e653c8e3
md"""
## 5. Data structures
"""

# ╔═╡ 18d65bfb-d179-40d5-a5a0-2954b49fc665
my_tuple = (1, "2", '3', "four", "🚀")

# ╔═╡ 1b6a4e5a-6e2d-4acf-bcd1-41cfab27202f
my_tuple[5]

# ╔═╡ 17b75674-1429-4dce-848a-536ff0e828d4
my_tuple[5] = λ

# ╔═╡ 0ab29709-fbe0-42ec-955e-af1dd8989232
for i in my_tuple
	println(i)
end

# ╔═╡ 97b087c1-dc17-420f-9861-6d5d1e5acb3a
my_range = 1:7

# ╔═╡ f8104d65-d76a-4612-a94c-c2ff9a680921
my_range[2]

# ╔═╡ ecae72bd-4c61-437d-98cf-037b575d6632
begin
	my_range_2 = 1:7
	println(my_range_2[7])
	
	for i in my_range_2
		println(i)
	end
end

# ╔═╡ 86f372ff-5b55-41ef-9019-7ac506287f9c
begin
	my_array_comp = [x for x in 1:7]
	println(my_array_comp)
end

# ╔═╡ f83af840-aa41-4d4c-b0e4-10c8faa77870
my_vector = [1, 2, 3]

# ╔═╡ d13e6927-2f04-49e2-8e07-712d5644813c
typeof(my_vector)

# ╔═╡ 9c8bf174-a63f-4780-b00e-d16d1ef1f3a9
begin
	my_vector_2 = [1, 2, "3"]
	typeof(my_vector_2)
end

# ╔═╡ 39083c08-72c6-4aa4-b92d-bd6f09818f13
begin
	my_matrix = [[1, 2] [3, 4] [5, 6]]
	println(typeof(my_matrix))
	println(my_matrix)
end

# ╔═╡ 65415628-a77c-4109-a0b9-34755f391671
begin
	my_matrix_2 = Matrix{Float64}(undef, 4, 2)
	println(typeof(my_matrix_2))
	println(my_matrix_2)
end

# ╔═╡ 9c319ac6-e41d-4c52-8814-5adb862d451c
begin
	my_matrix_zeros = zeros(4, 2)
	my_matrix_ones = ones(4, 2)
	println(my_matrix_zeros)
	println(my_matrix_ones)
end

# ╔═╡ c93d2ed4-449f-4f8f-b2cd-89b48f8c5b73
rand(5,5)

# ╔═╡ 1128ecc7-3889-4be7-87a7-12d778ced6c6
begin
	my_matrix_rand = rand(5,5)
	println(length(my_matrix_rand))
	println(ndims(my_matrix_rand))
	println(size(my_matrix_rand))
end

# ╔═╡ 56238cba-50cf-4614-a10c-964b40e7f79a
my_matrix_rand_2 = rand(2,5)

# ╔═╡ 7721bc28-b5df-4c58-be67-89c94b1b63fa
begin
	println(my_matrix_rand_2[1])
	println(my_matrix_rand_2[2, 1])
	println(my_matrix_rand_2[end])
end

# ╔═╡ fb25422c-1d75-4eb2-b0b5-29b22086c1d5
my_pair = "My Number" => 7

# ╔═╡ 45f4ba17-eaf2-4591-843a-af64d21de59e
begin
	println(first(my_pair))
	println(last(my_pair))
end

# ╔═╡ 290fe398-fb6e-4d8a-a8c8-13c02bcc9aea
my_dict = Dict("ONE" => 1, "TWO" => 2, "THREE" => 3)

# ╔═╡ eb7d1256-fce0-4ec5-baab-82ead6e2f342
begin
	my_dict_2 = Dict("ONE" => 1, "ONE" => 2, "THREE" => 3)
	println(my_dict_2)
end

# ╔═╡ 8327e8d6-7eb8-466a-ab0e-53980945fef6
my_dict["ONE"]

# ╔═╡ 6d10abcf-c594-42b3-9e0d-0c6f2b938507
begin
	my_dict["ONE"] = 7
	println(my_dict)
end

# ╔═╡ b751a9fa-c921-414c-ab2a-c6dc411526bf
for i in my_dict
	println(i)
end

# ╔═╡ 55ec175a-d35b-4c10-b82e-4e9e0851f78e
for (i, j) in my_dict
    println(i, " => ", j)
end

# ╔═╡ 0ad4f67a-5960-4967-bb4b-79f25181a29e
md"""
## 6. Mathematical operators
"""

# ╔═╡ d2e81a00-407e-4109-a7bd-4e8ea06d4c5e
begin
	my_num_1 = 7
	my_num_2 = 2
	my_vec_1 = [3, 4, 5]
	println(my_vec_1 * my_num_1)
end

# ╔═╡ 6f73ae7f-0a1b-431c-b381-f930b70b228f
md"""
## 7. Flow control
"""

# ╔═╡ 364c44c8-548c-4478-8e6d-e7f9e1765f5a
begin
	e = 1
	f = 2
	println(e>f)
end

# ╔═╡ e37983a4-f8db-434c-8e45-aa68f07888b3
begin
	for i in 1:10
		if i%2 != 0
			println("Odd number")
		else
			println("Even number")
		end
	end
end

# ╔═╡ 3589c802-26c5-4793-bda9-a7f2f9d228b0
begin
	for i in 0:9
		println(i+1)
	end
end

# ╔═╡ 6626fb27-b8f6-4a11-acf1-ea9cf706fc83
begin
	i = 7
	
	while i >= 1
		println(i)
	    i -= 1
	end
end

# ╔═╡ c8cd0b2a-cff6-466f-b50c-028d68718e72
md"""
## 8. Functions
"""

# ╔═╡ 1d055498-dc4e-452a-aaaa-e3e2f8856f0b
function my_fun(x,y)
	   x + y
   end

# ╔═╡ abdae22b-5e72-4338-bad1-307534240a6a
begin
	call_to_fun = my_fun(1, 2)
	println(call_to_fun)
end

# ╔═╡ 2075da8f-8fd0-4435-9a59-4819fb840a8a
my_fun_2(x,y) = x + y

# ╔═╡ 7baeb606-4423-4d3e-a400-23319fd90011
∑(x,y) = x + y

# ╔═╡ 3cb3cebc-6b4e-49dd-8fe0-91fa406bf56a
∑(7, 7)

# ╔═╡ 8bfcb05e-cb24-4da7-a9f5-21f78ae3494e
function my_fun_3(x, y)
	a = x*y
	b = x+y
	return a, b
end

# ╔═╡ 48402f64-8644-4721-8226-2dde8226c9e6
println(my_fun_3(7, 7))

# ╔═╡ 41df8430-b7a9-4828-b841-94996366aabb
my_matrix_b = rand(4, 4)

# ╔═╡ 643a03e6-95d7-4afb-9973-d5b2a48d315b
function my_fun_nb(x)
	return x^2
end

# ╔═╡ fdad27d9-f8cb-45c2-bb6a-a271ab19ad03
display(my_fun_nb(my_matrix_b))

# ╔═╡ cd3f1d92-93a7-4bf7-813b-31f33568d0ca
display(my_fun_nb.(my_matrix_b))

# ╔═╡ 70141d91-5cf7-4f72-ab94-2b8b6c800d45
begin
	my_vec_a = [1, 4, 5, 8, 3, 0]
	println(sort(my_vec_a))
	println(my_vec_a)
end

# ╔═╡ 85925734-c536-49ac-84bb-ec081850c36a
begin
	my_vec_b = [1, 4, 5, 8, 3, 0]
	println(sort!(my_vec_b))
	println(my_vec_b)
end

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
TypeTree = "04da0e3b-1cad-4b2c-a963-fc1602baf1af"

[compat]
TypeTree = "~0.3.0"
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

julia_version = "1.8.3"
manifest_format = "2.0"
project_hash = "3f4763f5218c5e2babd42e007032b0054a726c16"

[[deps.Base64]]
uuid = "2a0f44e3-6c83-55bd-87e4-b1978d98bd5f"

[[deps.InteractiveUtils]]
deps = ["Markdown"]
uuid = "b77e0a4c-d291-57a0-90e8-8db25a27a240"

[[deps.Markdown]]
deps = ["Base64"]
uuid = "d6f4376e-aef5-505a-96c1-9c027394607a"

[[deps.TypeTree]]
deps = ["InteractiveUtils"]
git-tree-sha1 = "c1adbb6b9d9374babe8975a456f383a37a8e02ec"
uuid = "04da0e3b-1cad-4b2c-a963-fc1602baf1af"
version = "0.3.0"
"""

# ╔═╡ Cell order:
# ╟─dd145092-afde-11ed-042f-4da8249ada73
# ╟─a11cfd20-1126-49f9-b258-3fe779625d20
# ╠═84900720-b902-4a60-ab1b-301ae8ae9e85
# ╠═c80e1930-92cf-47bd-b5b5-276e664a2854
# ╟─e46df2a1-72ed-4aeb-b2b0-ed75da8f2721
# ╠═1526e1e1-2472-42f3-975c-9ba17ffc2c08
# ╠═abd69392-ebaf-45ed-b3e6-eac36da98b59
# ╠═9d1ffffb-6bf6-4839-ae5b-d9c902d3a905
# ╟─21a00515-1262-437d-aac6-4cb81971e20e
# ╠═21a9d373-e130-464f-b72d-4ef2cdbe2af1
# ╠═25377598-ebac-4c52-9f71-afaea5735b51
# ╠═6be52879-6cdf-467a-b4de-366d41c25ca5
# ╟─64ae103e-beb3-4913-918d-a01ba6168f54
# ╠═72152220-9129-4a0f-8d87-66db36edb0c1
# ╠═3efac976-948f-4d87-8f62-0c077a31469e
# ╠═2c3455cd-5e5d-46bc-9cf7-cf8650b6bc68
# ╠═980552a1-1aa6-4e70-8bd3-34e8252a0646
# ╠═21665973-d846-4968-a0b0-141cbfb905d8
# ╠═e84914ce-3f71-4ee5-9de0-67aa0f94b4c7
# ╠═e4d69a3a-a0d9-4595-b6de-df341957688b
# ╠═c712423b-0216-40bb-bec6-e8a2ff58b967
# ╠═ad3de390-6cbb-4489-b3c2-fa91b06781b5
# ╠═1935cc41-a37d-40c1-b026-08012029a0ae
# ╠═bd8422df-dd53-4038-b60f-db3d1c4c85e2
# ╠═97332772-09e5-454d-8fc9-57c7ecee2ae3
# ╠═77d44c4c-69ce-4a33-98ea-0dfdff891a9a
# ╠═d8dfe4b6-03ca-455a-bca1-0f8c333799ec
# ╠═885cdf99-93dc-43b6-91b3-661239d08a3a
# ╠═a92ba817-861a-4324-a47b-f93d15ed4fba
# ╠═ae392cb9-6c3d-48fd-b795-5d785e471601
# ╠═13466385-7498-48c0-866b-a401ba882b26
# ╠═57a6dfde-97e7-4d64-baaf-03d4d8c16783
# ╠═6b9873db-7c6a-400e-99aa-544411b430a1
# ╠═c0203f14-6ed6-4c69-b050-de8d7c71249b
# ╠═dc942f9a-546f-4b66-bef4-43d3c3784e5a
# ╠═6123c2a9-f3d3-45b7-b3bf-784a04043aa0
# ╟─4a7c3cae-7071-4a21-b8d5-a537e653c8e3
# ╠═18d65bfb-d179-40d5-a5a0-2954b49fc665
# ╠═1b6a4e5a-6e2d-4acf-bcd1-41cfab27202f
# ╠═17b75674-1429-4dce-848a-536ff0e828d4
# ╠═0ab29709-fbe0-42ec-955e-af1dd8989232
# ╠═97b087c1-dc17-420f-9861-6d5d1e5acb3a
# ╠═f8104d65-d76a-4612-a94c-c2ff9a680921
# ╠═ecae72bd-4c61-437d-98cf-037b575d6632
# ╠═86f372ff-5b55-41ef-9019-7ac506287f9c
# ╠═f83af840-aa41-4d4c-b0e4-10c8faa77870
# ╠═d13e6927-2f04-49e2-8e07-712d5644813c
# ╠═9c8bf174-a63f-4780-b00e-d16d1ef1f3a9
# ╠═39083c08-72c6-4aa4-b92d-bd6f09818f13
# ╠═65415628-a77c-4109-a0b9-34755f391671
# ╠═9c319ac6-e41d-4c52-8814-5adb862d451c
# ╠═c93d2ed4-449f-4f8f-b2cd-89b48f8c5b73
# ╠═1128ecc7-3889-4be7-87a7-12d778ced6c6
# ╠═56238cba-50cf-4614-a10c-964b40e7f79a
# ╠═7721bc28-b5df-4c58-be67-89c94b1b63fa
# ╠═fb25422c-1d75-4eb2-b0b5-29b22086c1d5
# ╠═45f4ba17-eaf2-4591-843a-af64d21de59e
# ╠═290fe398-fb6e-4d8a-a8c8-13c02bcc9aea
# ╠═eb7d1256-fce0-4ec5-baab-82ead6e2f342
# ╠═8327e8d6-7eb8-466a-ab0e-53980945fef6
# ╠═6d10abcf-c594-42b3-9e0d-0c6f2b938507
# ╠═b751a9fa-c921-414c-ab2a-c6dc411526bf
# ╠═55ec175a-d35b-4c10-b82e-4e9e0851f78e
# ╟─0ad4f67a-5960-4967-bb4b-79f25181a29e
# ╠═d2e81a00-407e-4109-a7bd-4e8ea06d4c5e
# ╟─6f73ae7f-0a1b-431c-b381-f930b70b228f
# ╠═364c44c8-548c-4478-8e6d-e7f9e1765f5a
# ╠═e37983a4-f8db-434c-8e45-aa68f07888b3
# ╠═3589c802-26c5-4793-bda9-a7f2f9d228b0
# ╠═6626fb27-b8f6-4a11-acf1-ea9cf706fc83
# ╟─c8cd0b2a-cff6-466f-b50c-028d68718e72
# ╠═1d055498-dc4e-452a-aaaa-e3e2f8856f0b
# ╠═abdae22b-5e72-4338-bad1-307534240a6a
# ╠═2075da8f-8fd0-4435-9a59-4819fb840a8a
# ╠═7baeb606-4423-4d3e-a400-23319fd90011
# ╠═3cb3cebc-6b4e-49dd-8fe0-91fa406bf56a
# ╠═8bfcb05e-cb24-4da7-a9f5-21f78ae3494e
# ╠═48402f64-8644-4721-8226-2dde8226c9e6
# ╠═41df8430-b7a9-4828-b841-94996366aabb
# ╠═643a03e6-95d7-4afb-9973-d5b2a48d315b
# ╠═fdad27d9-f8cb-45c2-bb6a-a271ab19ad03
# ╠═cd3f1d92-93a7-4bf7-813b-31f33568d0ca
# ╠═70141d91-5cf7-4f72-ab94-2b8b6c800d45
# ╠═85925734-c536-49ac-84bb-ec081850c36a
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
