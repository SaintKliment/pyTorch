import torch

# tensor_1 = torch.tensor([1.2, 2.3, 4.5])
# print(tensor_1)

# #create tensor zero
# tensor_zeros = torch.zeros(4, 5)
# print(tensor_zeros)

# # tensor one
# tensor_ones = torch.ones(2,3)
# print(tensor_ones)

# # tensor rand
# tensor_rand = torch.rand(4, 4)
# print(tensor_rand)

# tensor_int = torch.tensor([1,2,3], dtype=torch.int32)
# print(tensor_int)

# tensor_test = torch.tensor([[1,2,3], [4,5,6]])
# last_el = tensor_test[1, 2] # 6
# el2 = tensor_test[1, 1] # 5
# el3 = tensor_test[0, 2] # 3
# print(last_el, el2, el3)

# el_slice1 = tensor_test[0:2, 2:3]
# el_slice2 = 
# print(el_slice1)

tensor_form = torch.tensor([1,2,3,4,5,6])

tensor_deform = tensor_form.view(3,2)
tensor_unsqueezed = tensor_form.unsqueeze(1)
print(tensor_unsqueezed)