class BayesCalculator:
    '''Calculator for calculating Bayes's Probablity'''

    def __init__(self, p_a=None, p_not_a=None, p_b=None, p_b_given_a=None, p_b_given_not_a=None):
        for name,value in locals().items():
            if name!='self':
                setattr(self,name,value)
        self._validate_inputs()

    def _validate_inputs(self):
        if not all(isinstance(v, (type(None), int, float)) for v in self.__dict__.values()):
            raise TypeError("Please make sure the entries are numerical.")
    
    # Only enforce 0-1 bounds for actual probabilities (P(A), P(not A), P(A|B))
        probability_keys = ['p_a', 'p_not_a']
        for k in probability_keys:
            val = getattr(self, k, None)
            if val is not None and not (0 <= val <= 1):
                raise ValueError(f"{k} must be between 0 and 1.")
        
    def compute(self):
        if self.p_a is None and self.p_not_a is None:
                raise ValueError("Please enter either P(A) or P(A')")
            
        self.p_a = 1-self.p_not_a if self.p_not_a is not None else self.p_a
        self.p_not_a = 1-self.p_a if self.p_a is not None else self.p_not_a
        
        #Law of total Probablity
        if self.p_b is None:
            try:
                self.p_b= (self.p_b_given_a * self.p_a) + (self.p_b_given_not_a * self.p_not_a)
            except:
                raise ValueError("Either give the total probablity P(B) or P(B|A) and P(B|A')")
        self.p_a_given_b = (self.p_b_given_a * self.p_a) / (self.p_b)
        return round(self.p_a_given_b,12)
