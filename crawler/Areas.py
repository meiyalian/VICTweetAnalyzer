# location data of each area represented by a central point + radius 
areas = {
         'Colac-Otway (S)': {'lat': -38.483006, 'lng': 143.6501903},
         'Corangamite (S)': {'lat': -38.1491105, 'lng': 143.1319209},
      
         'East Gippsland (S)': {'lat': -37.4975957, 'lng': 148.1892921},
        
         'Gannawarra (S)': {'lat': -35.6867808, 'lng': 144.1128981},
         
         'Glenelg (S)': {'lat': -37.9078291, 'lng': 141.5150077},
         'Golden Plains (S)': {'lat': -37.8943285, 'lng': 143.6501903},
         'Hindmarsh (S)': {'lat': -35.97520799999999, 'lng': 141.852273},
       
         'Indigo (S)': {'lat': -36.2306763, 'lng': 146.6962857},
   
       
         'Loddon (S)': {'lat': -36.4175636, 'lng': 143.9106594},
         'Mansfield (S)': {'lat': -37.0625288, 'lng': 146.0821493},
        
         'Maroondah (C)': {'lat': -37.80966, 'lng': 145.2590707},
         'Melbourne (C)': {'lat': -37.8136276, 'lng': 144.9630576},
        
         'Moira (S)': {'lat': -35.9897244, 'lng': 145.5801757},
         'Monash (C)': {'lat': -37.9109574, 'lng': 145.1371751},
         'Moonee Valley (C)': {'lat': -37.7465015, 'lng': 144.9061342},
         'Moorabool (S)': {'lat': -37.6334256, 'lng': 144.1720041},
         'Moreland (C)': {'lat': -37.7411231, 'lng': 144.9700317},
       
         'Moyne (S)': {'lat': -38.1886081, 'lng': 142.4465474},
         'Murrindindi (S)': {'lat': -37.36184069999999, 'lng': 145.53928},
         'Nillumbik (S)': {'lat': -37.597667, 'lng': 145.2701235},
         'Northern Grampians (S)': {'lat': -36.9044244, 'lng': 142.9599661},
         'Port Phillip (C)': {'lat': -37.8464983, 'lng': 144.9666905},
         'Pyrenees (S)': {'lat': -37.3879637, 'lng': 143.4770359},
         'Northern Grampians (S)': {'lat': -36.9044244, 'lng': 142.9599661},
         'Port Phillip (C)': {'lat': -37.8464983, 'lng': 144.9666905},
         'Pyrenees (S)': {'lat': -37.3879637, 'lng': 143.4770359},
   
         'South Gippsland (S)': {'lat': -38.5884838, 'lng': 146.1142253},
         'Southern Grampians (S)': {'lat': -37.4535972, 'lng': 141.852273},
         'Stonnington (C)': {'lat': -37.8595876, 'lng': 145.0328017},
         'Strathbogie (S)': {'lat': -36.879426, 'lng': 145.7113079},
         'Surf Coast (S)': {'lat': -38.3128176, 'lng': 143.9976775},
         'Swan Hill (RC)': {'lat': -35.1588446, 'lng': 143.1319209},
         'Towong (S)': {'lat': -36.1303027, 'lng': 147.9752136},
         
         'Wellington (S)': {'lat': -38.078841, 'lng': 147.1013188},
         'West Wimmera (S)': {'lat': -36.6091473, 'lng': 141.1794546},
         'Whitehorse (C)': {'lat': -37.8286371, 'lng': 145.1486206},
         'Whittlesea (C)': {'lat': -37.5382852, 'lng': 145.093449},
         'Yarra (C)': {'lat': -37.7979219, 'lng': 144.9887218},
         'Yarra Ranges (S)': {'lat': -37.7450808, 'lng': 145.7133909},
         'Yarriambiack (S)': {'lat': -35.9703773, 'lng': 142.4465474}}



#  'Alpine (S)': {'lat': -36.7532313, 'lng': 147.0111681},
#          'Ararat (RC)': {'lat': -37.5401763, 'lng': 142.8741407},
#          'Ballarat (C)': {'lat': -37.5621587, 'lng': 143.8502556},
#          'Banyule (C)': {'lat': -37.7314254, 'lng': 145.082419},
#          'Bass Coast (S)': {'lat': -38.5087582, 'lng': 145.5358152},
#          'Baw Baw (S)': {'lat': -37.8320547, 'lng': 146.3068671},
#          'Bayside (C)': {'lat': -37.9333402, 'lng': 145.016269},
#          'Benalla (RC)': {'lat': -36.4122615, 'lng': 145.9358581},
#          'Boroondara (C)': {'lat': -37.8390146, 'lng': 145.0618816},
#          'Brimbank (C)': {'lat': -37.7594793, 'lng': 144.8071366},
#          'Buloke (S)': {'lat': -36.1736195, 'lng': 143.2180495},
#          'Campaspe (S)': {'lat': -36.308533, 'lng': 144.6972774},
#          'Cardinia (S)': {'lat': -38.147, 'lng': 145.423},
#          'Casey (C)': {'lat': -38.1105316, 'lng': 145.2922335},
#          'Central Goldfields (S)': {'lat': -36.9802447, 'lng': 143.6935405},
#          'Colac-Otway (S)': {'lat': -38.483006, 'lng': 143.6501903},
#          'Corangamite (S)': {'lat': -38.1491105, 'lng': 143.1319209},
#          'Darebin (C)': {'lat': -37.727768, 'lng': 145.016269},
#          'East Gippsland (S)': {'lat': -37.4975957, 'lng': 148.1892921},
#          'Frankston (C)': {'lat': -38.1466246, 'lng': 145.135722},
#          'Gannawarra (S)': {'lat': -35.6867808, 'lng': 144.1128981},
#          'Glen Eira (C)': {'lat': -37.9034811, 'lng': 145.0383133},
#          'Glenelg (S)': {'lat': -37.9078291, 'lng': 141.5150077},
#          'Golden Plains (S)': {'lat': -37.8943285, 'lng': 143.6501903},
#          'Greater Bendigo (C)': {'lat': -36.7570157, 'lng': 144.2793906},
#          'Greater Dandenong (C)': {'lat': -38.00611079999999, 'lng': 145.2038278},
#          'Greater Geelong (C)': {'lat': -37.9697434, 'lng': 144.3904526},
#          'Greater Shepparton (C)': {'lat': -36.376568, 'lng': 145.3993654},
#          'Hepburn (S)': {'lat': -37.3118233, 'lng': 144.125661},
#          'Hindmarsh (S)': {'lat': -35.97520799999999, 'lng': 141.852273},
#          'Hobsons Bay (C)': {'lat': -37.8360799, 'lng': 144.8401227},
#          'Horsham (RC)': {'lat': -36.715634, 'lng': 142.1988988},
#          'Hume (C)': {'lat': -37.5986911, 'lng': 144.8291259},
#          'Indigo (S)': {'lat': -36.2306763, 'lng': 146.6962857},
#          'Kingston (C) (Vic.)': {'lat': -37.366667, 'lng': 143.95},
#          'Knox (C)': {'lat': -37.8714657, 'lng': 145.2480193},
#          'Latrobe (C) (Vic.)': {'lat': -37.7206639, 'lng': 145.0483389},
#          'Loddon (S)': {'lat': -36.4175636, 'lng': 143.9106594},
#          'Macedon Ranges (S)': {'lat': -37.3663141, 'lng': 144.6972774},
#          'Manningham (C)': {'lat': -37.7949407, 'lng': 145.1774309},
#          'Mansfield (S)': {'lat': -37.0625288, 'lng': 146.0821493},
#         'Maribyrnong (C)': {'lat': -37.7695602, 'lng': 144.8820803},
#          'Maroondah (C)': {'lat': -37.80966, 'lng': 145.2590707},
#          'Melbourne (C)': {'lat': -37.8136276, 'lng': 144.9630576},
#          'Melton (C)': {'lat': -37.6881754, 'lng': 144.6533747},
#          'Mildura (RC)': {'lat': -34.1734864, 'lng': 142.1365351},
#          'Mitchell (S)': {'lat': -37.1847484, 'lng': 145.0493375},
#          'Moira (S)': {'lat': -35.9897244, 'lng': 145.5801757},
#          'Monash (C)': {'lat': -37.9109574, 'lng': 145.1371751},
#          'Moonee Valley (C)': {'lat': -37.7465015, 'lng': 144.9061342},
#          'Moorabool (S)': {'lat': -37.6334256, 'lng': 144.1720041},
#          'Moreland (C)': {'lat': -37.7411231, 'lng': 144.9700317},
#          'Mornington Peninsula (S)': {'lat': -38.2854053, 'lng': 145.093449},
#          'Mount Alexander (S)': {'lat': -37.0353437, 'lng': 144.1720041},
#          'Moyne (S)': {'lat': -38.1886081, 'lng': 142.4465474},
#          'Murrindindi (S)': {'lat': -37.36184069999999, 'lng': 145.53928},
#          'Nillumbik (S)': {'lat': -37.597667, 'lng': 145.2701235},
#          'Northern Grampians (S)': {'lat': -36.9044244, 'lng': 142.9599661},
#          'Port Phillip (C)': {'lat': -37.8464983, 'lng': 144.9666905},
#          'Pyrenees (S)': {'lat': -37.3879637, 'lng': 143.4770359},
#          'Northern Grampians (S)': {'lat': -36.9044244, 'lng': 142.9599661},
#          'Port Phillip (C)': {'lat': -37.8464983, 'lng': 144.9666905},
#          'Pyrenees (S)': {'lat': -37.3879637, 'lng': 143.4770359},
#         'Queenscliffe (B)': {'lat': -38.2677746, 'lng': 144.6286897},
#          'South Gippsland (S)': {'lat': -38.5884838, 'lng': 146.1142253},
#          'Southern Grampians (S)': {'lat': -37.4535972, 'lng': 141.852273},
#          'Stonnington (C)': {'lat': -37.8595876, 'lng': 145.0328017},
#          'Strathbogie (S)': {'lat': -36.879426, 'lng': 145.7113079},
#          'Surf Coast (S)': {'lat': -38.3128176, 'lng': 143.9976775},
#          'Swan Hill (RC)': {'lat': -35.1588446, 'lng': 143.1319209},
#          'Towong (S)': {'lat': -36.1303027, 'lng': 147.9752136},
#          'Wangaratta (RC)': {'lat': -36.3547503, 'lng': 146.3230693},
#          'Warrnambool (C)': {'lat': -38.3686779, 'lng': 142.4982086},
#          'Wellington (S)': {'lat': -38.078841, 'lng': 147.1013188},
#          'West Wimmera (S)': {'lat': -36.6091473, 'lng': 141.1794546},
#          'Whitehorse (C)': {'lat': -37.8286371, 'lng': 145.1486206},
#          'Whittlesea (C)': {'lat': -37.5382852, 'lng': 145.093449},
#          'Wodonga (C)': {'lat': -36.1583417, 'lng': 146.8985944},
#          'Wyndham (C)': {'lat': -37.9119003, 'lng': 144.6533747},
#          'Yarra (C)': {'lat': -37.7979219, 'lng': 144.9887218},
#          'Yarra Ranges (S)': {'lat': -37.7450808, 'lng': 145.7133909},
#          'Yarriambiack (S)': {'lat': -35.9703773, 'lng': 142.4465474}