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

tensor_int = torch.tensor([1,2,3], dtype=torch.int32)
print(tensor_int)

tensor_slice = torch.tensor([[1,2,3], [4,5,6]])
last_el = tensor_slice[1, 2] # 6
last_el2 = tensor_slice[1, 1] # 5
last_el3 = tensor_slice[0, 2] # 3
print(last_el, last_el2, last_el3)