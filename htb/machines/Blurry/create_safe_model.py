# safe_model.py
import torch

# Example of a simple, safe model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

# Save the model
model = SimpleModel()
torch.save(model.state_dict(), 'model.pth')
