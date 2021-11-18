import numpy as np
import time
from opt import *
from model import *


class recommender():
    def __init__(self):
        self.max_len = opt.max_len
        self.model = self.init_model()

    def init_model(self):
        model = trans_to_cpu(CombineGraph(opt, opt.num_node))
        model.load_state_dict(torch.load(opt.model_path, map_location="cpu"))
        return model

    def get_data(self, sequence):
        u_input = sequence
        max_n_node = self.max_len
        node = []
        for i, it in enumerate(u_input):
            if it == 0:
                break
            if it not in node:
                node.append(it)
        node = np.array(node)
        items = node.tolist() + (max_n_node - len(node)) * [0]
        adj = np.zeros((max_n_node, max_n_node))
        for i in np.arange(len(u_input) - 1):
            u = np.where(node == u_input[i])[0][0]
            adj[u][u] = 1
            if u_input[i + 1] == 0:
                break
            v = np.where(node == u_input[i + 1])[0][0]
            if u == v or adj[u][v] == 4:
                continue
            adj[v][v] = 1
            if adj[v][u] == 2:
                adj[u][v] = 4
                adj[v][u] = 4
            else:
                adj[u][v] = 2
                adj[v][u] = 3

        return [torch.tensor(adj), torch.tensor(items)]

    def recommend(self, sequence):
        self.model.eval()
        data = self.get_data(sequence)
        scores = forward_recommender(self.model, data)
        ranks = scores.topk(opt.topk)[1] + 1
        ranks = ranks.detach().numpy().tolist()

        return ranks


if __name__ == '__main__':
    recommender = recommender()
    sequence = np.array([2, 4, 5, 6, 8, 2, 4, 5, 6, 8, 2, 4, 5, 6, 8])
    time1 = time.time()
    for _ in range(100):
        targets = recommender.recommend(sequence)
    time2 = time.time()
    print(time2 - time1)
