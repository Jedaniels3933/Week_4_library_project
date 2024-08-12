from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase2(TestCase):
    def test_1(self):
        self.assertEqual(solution(["T", "F", "F", "F" ]) ,"Outage")
    def test_2(self):
        self.assertEqual(solution(["T", "F", "T", "T"]), "Power")