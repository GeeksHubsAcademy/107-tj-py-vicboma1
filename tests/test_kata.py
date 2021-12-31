import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):
    
    def test_apply_1(self):
        expected = "None";
        result = apply(None);
        assert(expected == result) 

    def test_apply_2(self):
        expected = "vacio";
        result = apply([])
        assert(expected == result) 

    def test_apply_3(self):
        expected = "a";
        result = apply(["a"])
        assert(expected == result) 

    def test_apply_4(self):
        expected = "az";
        result = apply(["a", "z"])
        assert(expected == result) 

    def test_apply_5(self):
        expected = "xy";
        result = apply(["x", "z", "y"])
        assert(expected == result) 

    def test_apply_6(self):
        expected = "hi!";
        result = apply(["h", "z", "i", "!"])
        assert(expected == result) 

    def test_apply_7(self):
        expected = "[%]";
        result = apply(["[", "o", "%", "a", "]"])
        assert(expected == result) 

    def test_apply_8(self):
        expected = "hl!";
        result = apply(["h", "o", "l", "a", "!"])
        assert(expected == result) 

    def test_apply_9(self):
        expected = "hola!";
        result = apply(["h", "o", "o", "l", "l", "a", "a", "!"])
        assert(expected == result) 

    def test_apply_10(self):
        expected = "casa!";
        result = apply(["c", "o", "a", "l", "s", "a", "a", "!"])
        assert(expected == result) 

    def test_apply_11(self):
        expected = "geeks!";
        result = apply(["g", "e", "e", "e", "e", "k", "k", "s", "s", "!"])
        assert(expected == result) 

    def test_apply_12(self):
        expected = "foo";
        result = apply(["f", "o", "o", "o"])
        assert(expected == result) 

    def test_apply_13(self):
        expected = "buu";
        result = apply(["b", "u", "u", "u"])
        assert(expected == result) 

    def test_apply_14(self):
        expected = "bu";
        result = apply(["b", "u", "u"])
        assert(expected == result) 
    

if __name__ == '__main__':
	unittest.main()