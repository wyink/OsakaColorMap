from pickle import TRUE
from typing import List

class City:
    '''行政地区の情報を管理するクラス
    
    Attributes
    ----------
    citycode:int
        行政地区コード 
    prefec:str
        都道府県名
    branch:str
        支庁名
    county:str
        郡および政令指定都市名
    cityname:str
        市区町村名  
    areablocks:List[int]
        svgに出現したpathタグのカウンタリスト
        各行政地区に属するエリアを保持する．   
    order:int
        svgに出現した色指標の順番
        昇順に並べたとき，行政地区コードの昇順に対応．   
    colorcode:str
        エリアを塗りつぶすカラーコード
    '''

    def __init__(self,citycode,property,areablocks,order,colorcode='#FFFFFF'):
        self._citycode = citycode
        self._prefec = property[0]
        self._branch = property[1]
        self._county = property[2]
        self._cityname = property[3]
        self._areablocks = areablocks
        self._order = order
        self._colorcode = colorcode     #colorcodeのみ変更可能
    
    @property
    def citycode(self) :
        return self._citycode

    @property
    def prefec(self):
        return self._prefec
    
    @property
    def branch(self):
        return self._branch
    
    @property
    def county(self):
        return self._county

    @property
    def cityname(self):
        return self._cityname

    def areablocks(self):
        return self._areablocks
    
    @property
    def order(self):
        return self._order
    
    @property
    def colorcode(self):
        return self._colorcode
    
    @colorcode.setter
    def colorcode(self,colorcode):
        self._colorcode = colorcode

    
    def isCounty(self):
        '''cityが郡・政令指定都市に所属するかの判定

        Returns
        -------
        bool 
            True : cityが郡もしくは政令指定都市に所属する．
            False : 郡もしくは政令指定都市に所属しない．
        
        '''
        if self._county != '':
            return True
        else:
            return False
        
