import unittest
from Binary_Search_Tree import Binary_Search_Tree 

class Binary_Search_Tree_Tester(unittest.TestCase):
    
    def setUp(self):
        self._bst = Binary_Search_Tree()

############################################################################# empty tree        
    def test_empty_tree_height(self):
        self.assertEqual(0, self._bst.get_height())
    
    def test_empty_tree(self):
        self.assertEqual("[ ]", str(self._bst))

    def test_empty_tree_inorder(self):
        self.assertEqual("[ ]", self._bst.in_order())

    def test_empty_tree_preorder(self):
        self.assertEqual("[ ]", self._bst.pre_order())

    def test_empty_tree_postorder(self):
        self.assertEqual("[ ]", self._bst.post_order())
############################################################################# one node
    def test_one_tree_insert(self):
        self._bst.insert_element(50)
        self.assertEqual("[ 50 ]", str(self._bst))

    def test_one_tree_insert_height(self):
        self._bst.insert_element(50)
        self.assertEqual(1, self._bst.get_height())

    def test_one_string(self):
        self._bst.insert_element(50)
        self.assertEqual("[ 50 ]", str(self._bst))

    def test_one_inorder(self):
        self._bst.insert_element(50)
        self.assertEqual("[ 50 ]", self._bst.in_order())

    def test_one_preorder(self):
        self._bst.insert_element(50)
        self.assertEqual("[ 50 ]", self._bst.pre_order())

    def test_one_postorder(self):
        self._bst.insert_element(50)
        self.assertEqual("[ 50 ]", self._bst.post_order())

    def test_one_remove(self):
        self._bst.insert_element(50)
        self._bst.remove_element(50)
        self.assertEqual("[ ]",str(self._bst))

    def test_one_remove_height(self):
        self._bst.insert_element(50)
        self._bst.remove_element(50)
        self.assertEqual(0, self._bst.get_height())

    def test_one_remove_inorder(self):
        self._bst.insert_element(50)
        self._bst.remove_element(50)
        self.assertEqual("[ ]", self._bst.in_order())

    def test_one_remove_preorder(self):
        self._bst.insert_element(50)
        self._bst.remove_element(50)
        self.assertEqual("[ ]", self._bst.pre_order())

    def test_one_remove_postorder(self):
        self._bst.insert_element(50)
        self._bst.remove_element(50)
        self.assertEqual("[ ]", self._bst.post_order())
        
############################################################################# one child

    def test_two_left_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self.assertEqual(2,self._bst.get_height())
        
    def test_two_left_string(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self.assertEqual('[ 25, 50 ]',str(self._bst))
        
    def test_two_left_pre_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self.assertEqual('[ 50, 25 ]',self._bst.pre_order())

    def test_two_left_in_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self.assertEqual('[ 25, 50 ]',self._bst.in_order())

    def test_two_left_post_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self.assertEqual('[ 25, 50 ]',self._bst.post_order())
        
    def test_two_left_remove_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.remove_element(50)
        self.assertEqual(1,self._bst.get_height())
        
    def test_two_left_remove_string(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.remove_element(50)
        self.assertEqual("[ 25 ]", str(self._bst))
        
    def test_two_left_pre_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.remove_element(50)
        self.assertEqual('[ 25 ]',self._bst.pre_order())

    def test_two_left_in_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.remove_element(50)
        self.assertEqual('[ 25 ]',self._bst.in_order())

    def test_two_left_post_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.remove_element(50)
        self.assertEqual('[ 25 ]',self._bst.post_order())

    def test_two_right_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self.assertEqual(2,self._bst.get_height())
        
    def test_two_right_string(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self.assertEqual('[ 50, 75 ]',str(self._bst))

    def test_two_right_pre_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self.assertEqual('[ 50, 75 ]',self._bst.pre_order())

    def test_two_right_in_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self.assertEqual('[ 50, 75 ]',self._bst.in_order())

    def test_two_right_post_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self.assertEqual('[ 75, 50 ]',self._bst.post_order())

    def test_two_right_remove_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual(1,self._bst.get_height())
        
    def test_two_right_remove_string(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual("[ 75 ]", str(self._bst))
        
    def test_two_right_pre_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual('[ 75 ]',self._bst.pre_order())

    def test_two_right_in_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual('[ 75 ]',self._bst.in_order())

    def test_two_right_post_order(self):
        self._bst.insert_element(50)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual('[ 75 ]',self._bst.post_order())

############################################################################# two children balanced

    def test_two_both_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self.assertEqual(2,self._bst.get_height())
        
    def test_two_left_string(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self.assertEqual('[ 25, 50, 75 ]',str(self._bst))

    def test_two_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self.assertEqual('[ 25, 50, 75 ]', self._bst.in_order())

    def test_two_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self.assertEqual('[ 50, 25, 75 ]', self._bst.pre_order())

    def test_two_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self.assertEqual('[ 25, 75, 50 ]', self._bst.post_order())

    def test_two_removeRoot_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual(2, self._bst.get_height())

    def test_two_removeRoot_string(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual("[ 25, 75 ]", str(self._bst))

    def test_two_removeRoot_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual('[ 25, 75 ]', self._bst.in_order())
    
    def test_two_removeRoot_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual('[ 75, 25 ]', self._bst.pre_order())

    def test_two_removeRoot_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(50)
        self.assertEqual('[ 25, 75 ]', self._bst.post_order())

    def test_two_removeChild_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(25)
        self.assertEqual(2, self._bst.get_height())

    def test_two_removeChild_string(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(25)
        self.assertEqual("[ 50, 75 ]", str(self._bst))

    def test_two_removeChild_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(25)
        self.assertEqual('[ 50, 75 ]', self._bst.in_order())

    def test_two_removeChild_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(25)
        self.assertEqual('[ 50, 75 ]', self._bst.pre_order())

    def test_two_removeChild_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.remove_element(25)
        self.assertEqual('[ 75, 50 ]', self._bst.post_order())

############################################################################# three nodes

    def test_three_pos2neg1_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(70)
        self._bst.insert_element(60)
        self.assertEqual(2, self._bst.get_height())

    def test_three_pos2neg1_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(70)
        self._bst.insert_element(60)
        self.assertEqual('[ 50, 60, 70 ]', self._bst.in_order())

    def test_three_pos2neg1_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(70)
        self._bst.insert_element(60)
        self.assertEqual('[ 60, 50, 70 ]', self._bst.pre_order())

    def test_three_pos2neg1_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(70)
        self._bst.insert_element(60)
        self.assertEqual('[ 50, 70, 60 ]', self._bst.post_order())

    def test_three_neg2pos1_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual(2, self._bst.get_height())

    def test_three_neg2pos1_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual('[ 30, 40, 50 ]', self._bst.in_order())

    def test_three_neg2pos1_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual('[ 40, 30, 50 ]', self._bst.pre_order())

    def test_three_neg2pos1_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual('[ 30, 50, 40 ]', self._bst.post_order())

    #def test_three_pos2pos1_
    def test_three_pos2pos1_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(60)
        self._bst.insert_element(70)
        self.assertEqual(2, self._bst.get_height())

    def test_three_pos2pos1_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(60)
        self._bst.insert_element(70)
        self.assertEqual('[ 50, 60, 70 ]', self._bst.in_order())

    def test_three_pos2pos1_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(60)
        self._bst.insert_element(70)
        self.assertEqual('[ 60, 50, 70 ]', self._bst.pre_order())

    def test_three_pos2pos1_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(60)
        self._bst.insert_element(70)
        self.assertEqual('[ 50, 70, 60 ]', self._bst.post_order())

    #def test_three_neg2neg1_
    def test_three_neg2neg1_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self.assertEqual(2, self._bst.get_height())

    def test_three_neg2neg1_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self.assertEqual('[ 30, 40, 50 ]', self._bst.in_order())

    def test_three_neg2neg1_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self.assertEqual('[ 40, 30, 50 ]', self._bst.pre_order())

    def test_three_neg2neg1_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self.assertEqual('[ 30, 50, 40 ]', self._bst.post_order())   

############################################################################# multiple nodes

    #def test_mult_pos2neg1_
    def test_mult_pos2neg1_height(self):
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self._bst.insert_element(50)
        self._bst.insert_element(70)
        self._bst.insert_element(60)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_pos2neg1_inorder(self):
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self._bst.insert_element(50)
        self._bst.insert_element(70)
        self._bst.insert_element(60)
        self.assertEqual('[ 30, 40, 50, 60, 70 ]', self._bst.in_order())

    def test_mult_pos2neg1_preorder(self):
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self._bst.insert_element(50)
        self._bst.insert_element(70)
        self._bst.insert_element(60)
        self.assertEqual('[ 40, 30, 60, 50, 70 ]', self._bst.pre_order())

    def test_mult_pos2neg1_postorder(self):
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self._bst.insert_element(50)
        self._bst.insert_element(70)
        self._bst.insert_element(60)
        self.assertEqual('[ 30, 50, 70, 60, 40 ]', self._bst.post_order())

    def test_mult_pos2neg1_conflict1_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.insert_element(60)
        self._bst.insert_element(80)
        self._bst.insert_element(70)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_pos2neg1_conflict1_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.insert_element(60)
        self._bst.insert_element(80)
        self._bst.insert_element(70)
        self.assertEqual('[ 25, 50, 60, 70, 75, 80 ]', self._bst.in_order())

    def test_mult_pos2neg1_conflict1_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.insert_element(60)
        self._bst.insert_element(80)
        self._bst.insert_element(70)
        self.assertEqual('[ 60, 50, 25, 75, 70, 80 ]', self._bst.pre_order())

    def test_mult_pos2neg1_conflict1_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.insert_element(60)
        self._bst.insert_element(80)
        self._bst.insert_element(70)
        self.assertEqual('[ 25, 50, 70, 80, 75, 60 ]', self._bst.post_order())

    def test_mult_pos2neg1_conflict2_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.insert_element(60)
        self._bst.insert_element(80)
        self._bst.insert_element(55)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_pos2neg1_conflict2_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.insert_element(60)
        self._bst.insert_element(80)
        self._bst.insert_element(55)
        self.assertEqual('[ 25, 50, 55, 60, 75, 80 ]', self._bst.in_order())

    def test_mult_pos2neg1_conflict2_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.insert_element(60)
        self._bst.insert_element(80)
        self._bst.insert_element(55)
        self.assertEqual('[ 60, 50, 25, 55, 75, 80 ]', self._bst.pre_order())

    def test_mult_pos2neg1_conflict2_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(75)
        self._bst.insert_element(60)
        self._bst.insert_element(80)
        self._bst.insert_element(55)
        self.assertEqual('[ 25, 55, 50, 80, 75, 60 ]', self._bst.post_order())

    def test_mult_pos2neg1_remove_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(10)
        self._bst.insert_element(70)
        self._bst.insert_element(55)
        self._bst.insert_element(65)
        self._bst.remove_element(55)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_pos2neg1_remove_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(10)
        self._bst.insert_element(70)
        self._bst.insert_element(55)
        self._bst.insert_element(65)
        self._bst.remove_element(55)
        self.assertEqual('[ 10, 20, 50, 60, 65, 70 ]', self._bst.in_order())

    def test_mult_pos2neg1_remove_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(10)
        self._bst.insert_element(70)
        self._bst.insert_element(55)
        self._bst.insert_element(65)
        self._bst.remove_element(55)
        self.assertEqual('[ 50, 20, 10, 65, 60, 70 ]', self._bst.pre_order())

    def test_mult_pos2neg1_remove_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(10)
        self._bst.insert_element(70)
        self._bst.insert_element(55)
        self._bst.insert_element(65)
        self._bst.remove_element(55)
        self.assertEqual('[ 10, 20, 60, 70, 65, 50 ]', self._bst.post_order())


    #def test_mult_neg2pos1_
    def test_mult_neg2pos1_height(self):
        self._bst.insert_element(70)
        self._bst.insert_element(50)
        self._bst.insert_element(80)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_neg2pos1_inorder(self):
        self._bst.insert_element(70)
        self._bst.insert_element(50)
        self._bst.insert_element(80)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual('[ 30, 40, 50, 70, 80 ]', self._bst.in_order())

    def test_mult_neg2pos1_preorder(self):
        self._bst.insert_element(70)
        self._bst.insert_element(50)
        self._bst.insert_element(80)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual('[ 70, 40, 30, 50, 80 ]', self._bst.pre_order())

    def test_mult_neg2pos1_postorder(self):
        self._bst.insert_element(70)
        self._bst.insert_element(50)
        self._bst.insert_element(80)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual('[ 30, 50, 40, 80, 70 ]', self._bst.post_order())

    def test_mult_neg2pos1_conflict1_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(70)
        self._bst.insert_element(20)
        self._bst.insert_element(30)
        self._bst.insert_element(27)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_neg2pos1_conflict1_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(70)
        self._bst.insert_element(20)
        self._bst.insert_element(30)
        self._bst.insert_element(27)
        self.assertEqual('[ 20, 25, 27, 30, 50, 70 ]', self._bst.in_order())

    def test_mult_neg2pos1_conflict1_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(70)
        self._bst.insert_element(20)
        self._bst.insert_element(30)
        self._bst.insert_element(27)
        self.assertEqual('[ 30, 25, 20, 27, 50, 70 ]', self._bst.pre_order())

    def test_mult_neg2pos1_conflict1_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(25)
        self._bst.insert_element(70)
        self._bst.insert_element(20)
        self._bst.insert_element(30)
        self._bst.insert_element(27)
        self.assertEqual('[ 20, 27, 25, 70, 50, 30 ]', self._bst.post_order())

    def test_mult_neg2pos1_conflict2_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(70)
        self._bst.insert_element(10)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_neg2pos1_conflict2_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(70)
        self._bst.insert_element(10)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual('[ 10, 20, 30, 40, 50, 70 ]', self._bst.in_order())

    def test_mult_neg2pos1_conflict2_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(70)
        self._bst.insert_element(10)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual('[ 30, 20, 10, 50, 40, 70 ]', self._bst.pre_order())

    def test_mult_neg2pos1_conflict2_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(70)
        self._bst.insert_element(10)
        self._bst.insert_element(30)
        self._bst.insert_element(40)
        self.assertEqual('[ 10, 20, 40, 70, 50, 30 ]', self._bst.post_order())

    def test_mult_neg2pos1_removal_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(47)
        self._bst.remove_element(55)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_neg2pos1_removal_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(47)
        self._bst.remove_element(60)
        self.assertEqual('[ 30, 40, 45, 47, 50, 55 ]', self._bst.in_order())

    def test_mult_neg2pos1_removal_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(47)
        self._bst.remove_element(60)
        self.assertEqual('[ 45, 40, 30, 50, 47, 55 ]', self._bst.pre_order())

    def test_mult_neg2pos1_removal_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(47)
        self._bst.remove_element(60)
        self.assertEqual('[ 30, 40, 47, 55, 50, 45 ]', self._bst.post_order())
        

    #def test_mult_pos2pos1_
    def test_mult_pos2pos1_height(self):
        self._bst.insert_element(100)
        self._bst.insert_element(50)
        self._bst.insert_element(150)
        self._bst.insert_element(180)
        self._bst.insert_element(190)
        self._bst.insert_element(40)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_pos2pos1_inorder(self):
        self._bst.insert_element(100)
        self._bst.insert_element(50)
        self._bst.insert_element(150)
        self._bst.insert_element(180)
        self._bst.insert_element(190)
        self._bst.insert_element(40)
        self.assertEqual('[ 40, 50, 100, 150, 180, 190 ]', self._bst.in_order())

    def test_mult_pos2pos1_preorder(self):
        self._bst.insert_element(100)
        self._bst.insert_element(50)
        self._bst.insert_element(150)
        self._bst.insert_element(180)
        self._bst.insert_element(190)
        self._bst.insert_element(40)
        self.assertEqual('[ 100, 50, 40, 180, 150, 190 ]', self._bst.pre_order())

    def test_mult_pos2pos1_postorder(self):
        self._bst.insert_element(100)
        self._bst.insert_element(50)
        self._bst.insert_element(150)
        self._bst.insert_element(180)
        self._bst.insert_element(190)
        self._bst.insert_element(40)
        self.assertEqual('[ 40, 50, 150, 190, 180, 100 ]', self._bst.post_order())

    def test_mult_pos2pos1_conflict_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(55)
        self._bst.insert_element(70)
        self._bst.insert_element(80)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_pos2pos1_conflict_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(55)
        self._bst.insert_element(70)
        self._bst.insert_element(80)
        self.assertEqual('[ 20, 50, 55, 60, 70, 80 ]', self._bst.in_order())

    def test_mult_pos2pos1_conflict_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(55)
        self._bst.insert_element(70)
        self._bst.insert_element(80)
        self.assertEqual('[ 60, 50, 20, 55, 70, 80 ]', self._bst.pre_order())

    def test_mult_pos2pos1_conflict_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(55)
        self._bst.insert_element(70)
        self._bst.insert_element(80)
        self.assertEqual('[ 20, 55, 50, 80, 70, 60 ]', self._bst.post_order())

    def test_mult_pos2pos1_remove_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(10)
        self._bst.insert_element(70)
        self._bst.insert_element(55)
        self._bst.insert_element(65)
        self._bst.insert_element(80)
        self._bst.remove_element(55)
        self.assertEqual(4, self._bst.get_height())

    def test_mult_pos2pos1_remove_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(10)
        self._bst.insert_element(70)
        self._bst.insert_element(55)
        self._bst.insert_element(65)
        self._bst.insert_element(80)
        self._bst.remove_element(55)
        self.assertEqual('[ 10, 20, 50, 60, 65, 70, 80 ]', self._bst.in_order())

    def test_mult_pos2pos1_remove_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(10)
        self._bst.insert_element(70)
        self._bst.insert_element(55)
        self._bst.insert_element(65)
        self._bst.insert_element(80)
        self._bst.remove_element(55)
        self.assertEqual('[ 50, 20, 10, 70, 60, 65, 80 ]', self._bst.pre_order())

    def test_mult_pos2pos1_remove_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(20)
        self._bst.insert_element(60)
        self._bst.insert_element(10)
        self._bst.insert_element(70)
        self._bst.insert_element(55)
        self._bst.insert_element(65)
        self._bst.insert_element(80)
        self._bst.remove_element(55)
        self.assertEqual('[ 10, 20, 65, 60, 80, 70, 50 ]', self._bst.post_order())

    #def test_mult_neg2neg1_
    def test_mult_neg2neg1_height(self):
        self._bst.insert_element(100)
        self._bst.insert_element(50)
        self._bst.insert_element(150)
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self._bst.insert_element(120)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_neg2neg1_inorder(self):
        self._bst.insert_element(100)
        self._bst.insert_element(50)
        self._bst.insert_element(150)
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self._bst.insert_element(120)
        self.assertEqual('[ 30, 40, 50, 100, 120, 150 ]', self._bst.in_order())

    def test_mult_neg2neg1_preorder(self):
        self._bst.insert_element(100)
        self._bst.insert_element(50)
        self._bst.insert_element(150)
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self._bst.insert_element(120)
        self.assertEqual('[ 100, 40, 30, 50, 150, 120 ]', self._bst.pre_order())

    def test_mult_neg2neg1_postorder(self):
        self._bst.insert_element(100)
        self._bst.insert_element(50)
        self._bst.insert_element(150)
        self._bst.insert_element(40)
        self._bst.insert_element(30)
        self._bst.insert_element(120)
        self.assertEqual('[ 30, 50, 40, 120, 150, 100 ]', self._bst.post_order())

    def test_mult_neg2neg1_conflict_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(35)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_neg2neg1_conflict_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(35)
        self.assertEqual('[ 30, 35, 40, 45, 50, 60 ]', self._bst.in_order())

    def test_mult_neg2neg1_conflict_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(35)
        self.assertEqual('[ 40, 30, 35, 50, 45, 60 ]', self._bst.pre_order())

    def test_mult_neg2neg1_conflict_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(35)
        self.assertEqual('[ 35, 30, 45, 60, 50, 40 ]', self._bst.post_order())

    def test_mult_neg2neg1_remove_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(20)
        self._bst.remove_element(50)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_neg2neg1_remove_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(20)
        self._bst.remove_element(50)
        self.assertEqual('[ 20, 30, 40, 45, 55, 60 ]', self._bst.in_order())

    def test_mult_neg2neg1_remove_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(20)
        self._bst.remove_element(50)
        self.assertEqual('[ 40, 30, 20, 55, 45, 60 ]', self._bst.pre_order())

    def test_mult_neg2neg1_remove_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(20)
        self._bst.remove_element(50)
        self.assertEqual('[ 20, 30, 45, 60, 55, 40 ]', self._bst.post_order())

    def test_mult_neg2neg1_remove2_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(20)
        self._bst.remove_element(30)
        self.assertEqual(3, self._bst.get_height())

    def test_mult_neg2neg1_remove2_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(20)
        self._bst.remove_element(30)
        self.assertEqual('[ 20, 40, 45, 50, 55, 60 ]', self._bst.in_order())

    def test_mult_neg2neg1_remove2_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(20)
        self._bst.remove_element(30)
        self.assertEqual('[ 50, 40, 20, 45, 60, 55 ]', self._bst.pre_order())

    def test_mult_neg2neg1_remove2_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(45)
        self._bst.insert_element(55)
        self._bst.insert_element(20)
        self._bst.remove_element(30)
        self.assertEqual('[ 20, 45, 40, 55, 60, 50 ]', self._bst.post_order())

##################### additional removal

    def test_remove_connect_height(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(55)
        self._bst.insert_element(70)
        self._bst.insert_element(57)
        self._bst.remove_element(50)
        self.assertEqual(3, self._bst.get_height())

    def test_remove_connect_inorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(55)
        self._bst.insert_element(70)
        self._bst.insert_element(57)
        self._bst.remove_element(50)
        self.assertEqual('[ 30, 40, 55, 57, 60, 70 ]', self._bst.in_order())

    def test_remove_connect_preorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(55)
        self._bst.insert_element(70)
        self._bst.insert_element(57)
        self._bst.remove_element(50)
        self.assertEqual('[ 55, 40, 30, 60, 57, 70 ]', self._bst.pre_order())

    def test_remove_connect_postorder(self):
        self._bst.insert_element(50)
        self._bst.insert_element(40)
        self._bst.insert_element(60)
        self._bst.insert_element(30)
        self._bst.insert_element(55)
        self._bst.insert_element(70)
        self._bst.insert_element(57)
        self._bst.remove_element(50)
        self.assertEqual('[ 30, 40, 57, 70, 60, 55 ]', self._bst.post_order())    
        



 

if __name__ == "__main__":
    unittest.main()

