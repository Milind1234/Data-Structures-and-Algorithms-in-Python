import os
import importlib.util
import unittest


def load_graph_module():
    here = os.path.dirname(__file__)
    path = os.path.join(here, "05_Create_Graph.py")
    spec = importlib.util.spec_from_file_location("create_graph_mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestGraph(unittest.TestCase):
    def setUp(self):
        mod = load_graph_module()
        # make a deep-ish copy of the adjacency lists to avoid mutating module state
        self.graph = mod.Graph({k: v.copy() for k, v in mod.Dict.items()})

    def test_add_edge_existing_vertex(self):
        self.graph.addEdge("c", "d")
        self.assertIn("d", self.graph.graph_dict["c"])
        # ensure appended at end
        self.assertEqual(self.graph.graph_dict["c"][-1], "d")

    def test_add_edge_missing_vertex_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.graph.addEdge("x", "y")


if __name__ == "__main__":
    unittest.main()
