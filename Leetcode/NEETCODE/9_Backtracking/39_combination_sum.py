class Solution:
    def combinationSum(self, candidates, target: int): 
        _s = []
        def _combinationSum():
            l = []
            m = []
            k = 0
            for i in range(candidates):
                while _target > 0:
                    if len( l != 0 ):
                        for j in range(l):
                            



                    if _target == 0:
                        _s.append(_m)
                        _m = []
            
            
            
            
            
                k = 0
                _l = []
                _m = []
                while _target > 0:
                    k = k + candidates[i]
                    _target = _target - k
                    _l.append(_target)
                    _m.append(candidates[i])
                    if _target == 0:
                        _s.append(_m)
                        _m = []