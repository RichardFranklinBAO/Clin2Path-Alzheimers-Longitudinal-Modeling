"""Small BiLSTM example with fully synthetic sequences; not Clin2Path validation."""
import torch
from torch import nn
from torch.nn.utils.rnn import pack_padded_sequence


class BidirectionalSequenceRegressor(nn.Module):
    def __init__(self, n_features=6, hidden_size=12):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=n_features, hidden_size=hidden_size,
            batch_first=True, bidirectional=True
        )
        self.head = nn.Linear(hidden_size * 2, 1)

    def forward(self, sequences, lengths):
        packed = pack_padded_sequence(
            sequences, lengths.cpu(), batch_first=True, enforce_sorted=False
        )
        _, (h_n, _) = self.lstm(packed)
        return self.head(torch.cat((h_n[-2], h_n[-1]), dim=1)).squeeze(1)


def run_demo(seed=42):
    torch.manual_seed(seed)
    n, max_visits, n_features = 48, 8, 6
    lengths = torch.randint(3, max_visits + 1, (n,))
    sequences = torch.randn(n, max_visits, n_features)
    for i, length in enumerate(lengths.tolist()):
        sequences[i, length:] = 0  # padding, not clinical observations
    targets = torch.stack([
        sequences[i, :length, 0].mean() + 0.3 * sequences[i, :length, 1].mean()
        for i, length in enumerate(lengths.tolist())
    ])
    model = BidirectionalSequenceRegressor(n_features=n_features)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    for _ in range(15):
        optimizer.zero_grad()
        predictions = model(sequences, lengths)
        loss = nn.functional.mse_loss(predictions, targets)
        loss.backward()
        optimizer.step()
    print(f"Synthetic-data training MSE: {loss.item():.4f}")
    return float(loss.item())


if __name__ == "__main__":
    run_demo()
