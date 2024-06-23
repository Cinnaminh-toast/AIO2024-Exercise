import torch
from torch import nn

class Softmax(nn.Module):
  def __init__(self):
    super(Softmax, self).__init__()
    self.softmax = nn.Softmax(dim=0)

  def forward(self, data):
    return self.softmax(data)


class Softmax_stable(nn.Module):
  def __init__(self):
    super().__init__()

  def forward(self, data):
    c = data.max()
    e_xic = torch.exp(data-c)
    sum_e_xjc = torch.sum(e_xic)
    result = e_xic / sum_e_xjc
    return result
