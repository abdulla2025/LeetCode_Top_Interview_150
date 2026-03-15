MOD=int(1e9+7)
class Node:
    def __init__(self,left,right):
        self.left_child=None;self.right_child=None;self.left=left;self.right=right;self.mid=(left+right)>>1;self.val=0;self.lazy_add=0;self.lazy_mul=1
class SegTree:
    def __init__(self):
        self.root=Node(1,int(1e5+1))
    def range_add(self,left,right,inc,node=None):
        if left>right:return
        if node is None:node=self.root
        if node.left>=left and node.right<=right:
            node.val=(node.val+(node.right-node.left+1)*inc)%MOD;node.lazy_add+=inc;return
        self.pushdown(node)
        if left<=node.mid:self.range_add(left,right,inc,node.left_child)
        if right>node.mid:self.range_add(left,right,inc,node.right_child)
        self.pushup(node)
    def range_mul(self,left,right,mul,node=None):
        if left>right:return
        if node is None:node=self.root
        if node.left>=left and node.right<=right:
            node.val=(node.val*mul)%MOD;node.lazy_add=(node.lazy_add*mul)%MOD;node.lazy_mul=(node.lazy_mul*mul)%MOD;return
        self.pushdown(node)
        if left<=node.mid:self.range_mul(left,right,mul,node.left_child)
        if right>node.mid:self.range_mul(left,right,mul,node.right_child)
        self.pushup(node)
    def query(self,left,right,node=None):
        if left>right:return 0
        if node is None:node=self.root
        if node.left>=left and node.right<=right:return node.val
        self.pushdown(node);total=0
        if left<=node.mid:total=(total+self.query(left,right,node.left_child))%MOD
        if right>node.mid:total=(total+self.query(left,right,node.right_child))%MOD
        return total
    def pushup(self,node):
        node.val=(node.left_child.val+node.right_child.val)%MOD
    def pushdown(self,node):
        if node.left_child is None:node.left_child=Node(node.left,node.mid)
        if node.right_child is None:node.right_child=Node(node.mid+1,node.right)
        lc,rc=node.left_child,node.right_child
        if node.lazy_add!=0 or node.lazy_mul!=1:
            lc.val=(lc.val*node.lazy_mul+(lc.right-lc.left+1)*node.lazy_add)%MOD
            rc.val=(rc.val*node.lazy_mul+(rc.right-rc.left+1)*node.lazy_add)%MOD
            lc.lazy_add=(lc.lazy_add*node.lazy_mul+node.lazy_add)%MOD;rc.lazy_add=(rc.lazy_add*node.lazy_mul+node.lazy_add)%MOD
            lc.lazy_mul=(lc.lazy_mul*node.lazy_mul)%MOD;rc.lazy_mul=(rc.lazy_mul*node.lazy_mul)%MOD
            node.lazy_add=0;node.lazy_mul=1
class Fancy:
    def __init__(self):
        self.size=0;self.tree=SegTree()
    def append(self,val:int)->None:
        self.size+=1;self.tree.range_add(self.size,self.size,val)
    def addAll(self,inc:int)->None:
        self.tree.range_add(1,self.size,inc)
    def multAll(self,mul:int)->None:
        self.tree.range_mul(1,self.size,mul)
    def getIndex(self,idx:int)->int:
        return -1 if idx>=self.size else self.tree.query(idx+1,idx+1)
