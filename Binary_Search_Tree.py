class Binary_Search_Tree:

  class _BST_Node:
    
    def __init__(self, value):
      self._value = value
      
      self._left= None
      self._right= None
      self._height=1

  def __init__(self):
    
    self._root = None


  #AVL TREE
  def _calc_bal(self,root):
    if root._left is None and root._right is not None:
      balance = root._right._height

    elif root._right is None and root._left is not None:
      balance = 0-root._left._height

    elif root._right is not None and root._left is not None:
      balance = root._right._height - root._left._height

    else:
      balance = 0

    return balance


  def _correct_pos2pos1(self, root):
    a=root
    c=root._right
    d=root._right._left #could be a child or None
    root=root._right
    c._left=a
    a._right=d
    return root

  def _correct_neg2neg1(self, root):
    a=root
    c=root._left
    d=root._left._right
    root=root._left
    c._right=a
    a._left=d
    return root
    
  
  def _balance(self, root):
    rootBal = self._calc_bal(root)
    if rootBal == 2:
      rightBal = self._calc_bal(root._right)
      
      if rightBal == -1: #+2 -1
        a=root
        b=root._right
        c=b._left
        d=c._right
        b._left=None
        a._right=c
        c._right=b #here things should be +2 +1
        b._left=d
        root=self._correct_pos2pos1(root)
      else: #+2 +1 also covers +2 0 in removal
        root=self._correct_pos2pos1(root)

      
    elif rootBal== -2:
      leftBal = self._calc_bal(root._left)
      if leftBal== 1: #-2 +1
        a=root
        b=root._left
        c=b._right
        d = c._left
        b._right=None
        a._left=c
        c._left=b #here things should be -2 -1
        b._right=d
        root=self._correct_neg2neg1(root)
      else: #-2 -1
        root=self._correct_neg2neg1(root)

    
    if root._left is not None:
      self._update_node_height(root._left)
    if root._right is not None:
      self._update_node_height(root._right)
    self._update_node_height(root)
      
    return root
    
  
  def _update_node_height(self, root):
    
    if root._left==None and root._right!=None:
      root._height=root._right._height+1
 
    elif root._right==None and root._left!=None:
      root._height=root._left._height+1
  
    elif root._right!=None and root._left!=None:
      root._height=max(root._left._height,root._right._height)+1
   
    else: 
      root._height=1


  def _insert_element_rec(self, value, root):
    if root is None:
      root=self._BST_Node(value)
    elif value<root._value: #go left
      root._left=self._insert_element_rec(value,root._left)
      
    else: #go right
      root._right=self._insert_element_rec(value,root._right)
      
    self._update_node_height(root)
    return self._balance(root)
    
 
  def insert_element(self, value):
    
    self._root=self._insert_element_rec(value,self._root)
    

  def _find_min(self,root):
    if root._left==None:
      return root._value
    else:
      return self._find_min(root._left)

  
  def _remove_element_rec(self,value,  target):
    if value==target._value:
      #perform delete
      #if no child
      if target._left==None and target._right==None:
        return None    # if target has no children
        
      elif target._left==None and target._right!=None: #has 1 right child
        return target._right
       
      elif target._right==None and target._left!=None: #has 1 left child
        return target._left
        
      else: #has 2 child
        replace=self._find_min(target._right) #replace is a value, not a node
        
        target._value=replace
        target._right=self._remove_element_rec(replace,target._right)

    elif value<target._value: #go left
     
      target._left=self._remove_element_rec(value,target._left)


    else:#go right
     
      target._right=self._remove_element_rec(value,target._right)

    self._update_node_height(target)
    return self._balance(target)    

    
  def remove_element(self, value):
    
    self._root=self._remove_element_rec(value,self._root)
    
  def _in_order_rec(self, root,line):
    if root._left!=None:
      line=self._in_order_rec(root._left,line)+", "
    line=line+str(root._value)
    if root._right!=None:
      line=self._in_order_rec(root._right,line+", ")
    return line
    
  def in_order(self): #left, root, right

    if self._root==None:
      return "[ ]"
    else:
      return "[ "+self._in_order_rec(self._root,"")+" ]"

  def _pre_order_rec(self,root,line): #root left right
    line=line+str(root._value)
    if root._left!=None:
      line=self._pre_order_rec(root._left,line+", ")
    if root._right!=None:
      line=self._pre_order_rec(root._right,line+", ")
    return line

  def pre_order(self):
    
    if self._root==None:
      return "[ ]"
    else:
      return "[ "+self._pre_order_rec(self._root,"")+" ]"
  
  
  def _post_order_rec(self,root,line): #left right root
    
    if root._left!=None:
      line=self._post_order_rec(root._left,line)+", "
    if root._right!=None:
      line=self._post_order_rec(root._right,line)+", "
    line=line+str(root._value)
    return line    
    
  def post_order(self):

    if self._root==None:
      return "[ ]"
    else:
      return "[ "+self._post_order_rec(self._root,"")+" ]"

  def get_height(self):
    
    if self._root==None:
      return 0
    else:
      return self._root._height

  def __str__(self):
    return self.in_order()
    
    def reverse(self):
    self._root=self._reverse_rec(self._root)
  
  def _reverse_rec(self,root):
    if root is None:
      return None
    else:
      root._left=self._reverse_rec(root._left)
      root._right=self._reverse_rec(root._right)
      
      left=root._left
      right=root._right
      root._left=right
      root._right=left
      
      return root

if __name__ == '__main__':
  pass
