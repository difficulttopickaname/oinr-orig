# torch
import torch


# From LieConv
class Expression(torch.nn.Module):
    def __init__(self, func):
        """
        Creates a torch.nn.Module that applies the function func.
        :param func: lambda function
        """
        super().__init__()
        self.func = func

    def forward(self, x):
        return self.func(x)

    def extra_repr(self) -> str:
        return f"{self.func}"


def Sine():
    """
    out = sin(x)
    """
    # return Expression(lambda x: torch.sin(x))
    return Expression(torch.sin)
