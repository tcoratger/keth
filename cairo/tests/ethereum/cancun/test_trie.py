from hypothesis import given

from ethereum.base_types import Bytes
from ethereum.cancun.trie import bytes_to_nibble_list


class TestTrie:
    # def test_encode_internal_node(self, cairo_run, node):
    #     assert encode_internal_node(node) == cairo_run("encode_internal_node", node)

    # @given(node=...)
    # def test_encode_node(self, cairo_run, node: Node):
    #     assert encode_node(node, storage_root) == cairo_run(
    #         "encode_node", node, storage_root
    #     )

    # def test_copy_trie(self, cairo_run, trie):
    #     assert copy_trie(trie) == cairo_run("copy_trie", trie)

    # @given(key=..., value=...)
    # def test_trie_set(self, cairo_run, key: K, value: V):
    #     assert trie_set(trie, key, value) == cairo_run("trie_set", trie, key, value)

    # @given(key=...)
    # def test_trie_get(self, cairo_run, key: K):
    #     assert trie_get(trie, key) == cairo_run("trie_get", trie, key)

    # @given(a=..., b=...)
    # def test_common_prefix_length(self, cairo_run, a: Sequence, b: Sequence):
    #     assert common_prefix_length(a, b) == cairo_run("common_prefix_length", a, b)

    # @given(x=..., is_leaf=...)
    # def test_nibble_list_to_compact(self, cairo_run, x: Bytes, is_leaf: bool):
    #     assert nibble_list_to_compact(x, is_leaf) == cairo_run(
    #         "nibble_list_to_compact", x, is_leaf
    #     )

    @given(bytes_=...)
    def test_bytes_to_nibble_list(self, cairo_run, bytes_: Bytes):
        assert bytes_to_nibble_list(bytes_) == cairo_run("bytes_to_nibble_list", bytes_)

    # def test_root(self, cairo_run, trie, get_storage_root):
    #     assert root(trie, get_storage_root) == cairo_run("root", trie, get_storage_root)

    # @given(level=...)
    # def test_patricialize(self, cairo_run, level: Uint):
    #     assert patricialize(obj, level) == cairo_run("patricialize", obj, level)
