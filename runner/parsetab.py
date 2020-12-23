
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTIONS ASSIGNMENT BOOL CBLOCK COLON DESCRIPTION END EOL EXPRESSION ID IN INT INTOUT ITEMS NATIVE_LIBRARY NUMBER OUT SHELFS SKEWERS SPACE START_SKEWER SVG TITLE TYPE VARIABLES WORDprogram : title EOL native_library EOL variables EOL actions shelfs end EOL skewersdescription : DESCRIPTION COLON SPACE string EOLskewers : SKEWERS COLON EOL skwrsskwrs : skewer EOL svg\n             | skewer EOL svg skwrssvg : SPACE SVG COLON EOL svgdef EOLsvgdef : SPACE string EOL\n              | SPACE string EOL svgdefskewer : SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string\n              | SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string SPACE ENDactions : ACTIONS COLON EOL EOLactions : ACTIONS COLON EOL actsshelfs : SHELFS COLON EOL\n              | SHELFS COLON EOL shlfsshlfs : shelf EOL\n             | shelf EOL shlfsacts : action EOL\n            | action EOL actsshelf : SPACE WORD COLON EOL SPACE DESCRIPTION COLON SPACE string SPACE ASSIGNMENT                SPACE string EOL SPACE EXPRESSION COLON SPACE WORD SPACE ASSIGNMENT SPACE string EOL svgaction : SPACE WORD COLON EOL SPACE description SPACE cblock EOL svgcblock : CBLOCK COLON SPACE methods EOLmethods : methoddef\n               | methods EOL SPACE methoddefmethoddef : stringvariables : VARIABLES COLON vars EOLvars :\n            | var\n            | vars EOL varinout : IN\n             | OUTvtype : INT\n             | BOOL var : SPACE inout SPACE WORD SPACE vtype SPACE stringtitle : TITLE COLON EOL SPACE description SPACE START_SKEWER COLON SPACE WORD EOL svgnative_library : NATIVE_LIBRARY COLON SPACE WORD EOLstring : WORDstring : string SPACE WORDend : END COLON EOL svg'
    
_lr_action_items = {'EOL':([2,4,8,15,19,21,24,27,28,30,31,35,36,44,45,46,47,49,50,51,56,63,69,71,72,76,83,86,89,92,98,100,104,105,110,111,116,120,123,124,125,128,129,133,134,135,145,147,],[5,6,11,20,24,-26,-35,36,-27,-36,40,46,-25,52,53,54,-28,-37,59,60,66,73,-34,-38,81,84,90,93,95,-33,104,106,-6,111,115,-7,-8,-20,128,-24,-22,-21,-9,136,-23,-10,146,-19,]),'INT':([68,],[79,]),'COLON':([1,7,12,16,23,26,34,43,62,67,74,80,94,102,109,117,138,],[4,10,17,21,32,35,45,51,72,76,83,86,100,108,114,121,139,]),'NATIVE_LIBRARY':([5,],[7,]),'TITLE':([0,],[1,]),'BOOL':([68,],[77,]),'START_SKEWER':([18,],[23,]),'WORD':([14,22,41,42,48,57,64,85,88,99,113,119,122,126,130,131,132,140,144,],[19,30,49,50,58,67,74,30,94,30,30,30,49,30,30,30,49,141,30,]),'SVG':([70,],[80,]),'EXPRESSION':([137,],[138,]),'CBLOCK':([103,],[109,]),'VARIABLES':([11,],[16,]),'END':([33,53,65,73,82,132,],[43,-13,-14,-15,-16,135,]),'ITEMS':([112,],[117,]),'IN':([29,],[38,]),'$end':([3,61,87,101,104,107,],[0,-1,-3,-4,-6,-5,]),'ACTIONS':([20,],[26,]),'SPACE':([6,10,13,17,21,30,31,32,36,37,38,39,40,46,49,53,58,59,60,66,73,77,78,79,81,84,90,92,93,95,97,101,104,105,106,108,111,114,115,118,121,124,127,128,129,133,136,139,141,143,145,146,],[9,14,18,22,29,-36,41,42,29,-30,-29,48,-2,57,-37,64,68,70,70,57,64,-32,85,-31,88,91,96,41,99,70,103,88,-6,41,112,113,99,119,70,122,126,41,130,131,132,41,137,140,142,144,41,70,]),'DESCRIPTION':([9,91,96,],[12,12,102,]),'SKEWERS':([52,],[62,]),'OUT':([29,],[37,]),'ASSIGNMENT':([122,142,],[127,143,]),'SHELFS':([25,54,55,66,75,],[34,-11,-12,-17,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'shelf':([53,73,],[63,63,]),'svgdef':([93,111,],[98,116,]),'string':([22,85,99,113,119,126,130,131,144,],[31,92,105,118,124,129,133,124,145,]),'inout':([29,],[39,]),'actions':([20,],[25,]),'program':([0,],[3,]),'title':([0,],[2,]),'native_library':([5,],[8,]),'methoddef':([119,131,],[125,134,]),'skewer':([81,101,],[89,89,]),'methods':([119,],[123,]),'variables':([11,],[15,]),'shelfs':([25,],[33,]),'shlfs':([53,73,],[65,82,]),'vars':([21,],[27,]),'skewers':([52,],[61,]),'action':([46,66,],[56,56,]),'skwrs':([81,101,],[87,107,]),'end':([33,],[44,]),'vtype':([68,],[78,]),'svg':([59,60,95,115,146,],[69,71,101,120,147,]),'var':([21,36,],[28,47,]),'acts':([46,66,],[55,75,]),'description':([9,91,],[13,97,]),'cblock':([103,],[110,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> title EOL native_library EOL variables EOL actions shelfs end EOL skewers','program',11,'p_program','view_parser.py',8),
  ('description -> DESCRIPTION COLON SPACE string EOL','description',5,'p_description','view_parser.py',19),
  ('skewers -> SKEWERS COLON EOL skwrs','skewers',4,'p_skewers','view_parser.py',24),
  ('skwrs -> skewer EOL svg','skwrs',3,'p_skwrs','view_parser.py',29),
  ('skwrs -> skewer EOL svg skwrs','skwrs',4,'p_skwrs','view_parser.py',30),
  ('svg -> SPACE SVG COLON EOL svgdef EOL','svg',6,'p_svg','view_parser.py',38),
  ('svgdef -> SPACE string EOL','svgdef',3,'p_svgdef','view_parser.py',43),
  ('svgdef -> SPACE string EOL svgdef','svgdef',4,'p_svgdef','view_parser.py',44),
  ('skewer -> SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string','skewer',9,'p_skewer','view_parser.py',52),
  ('skewer -> SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string SPACE END','skewer',11,'p_skewer','view_parser.py',53),
  ('actions -> ACTIONS COLON EOL EOL','actions',4,'p_actions_empty','view_parser.py',57),
  ('actions -> ACTIONS COLON EOL acts','actions',4,'p_action_full','view_parser.py',63),
  ('shelfs -> SHELFS COLON EOL','shelfs',3,'p_shelfs','view_parser.py',67),
  ('shelfs -> SHELFS COLON EOL shlfs','shelfs',4,'p_shelfs','view_parser.py',68),
  ('shlfs -> shelf EOL','shlfs',2,'p_shlfs','view_parser.py',76),
  ('shlfs -> shelf EOL shlfs','shlfs',3,'p_shlfs','view_parser.py',77),
  ('acts -> action EOL','acts',2,'p_acts','view_parser.py',85),
  ('acts -> action EOL acts','acts',3,'p_acts','view_parser.py',86),
  ('shelf -> SPACE WORD COLON EOL SPACE DESCRIPTION COLON SPACE string SPACE ASSIGNMENT SPACE string EOL SPACE EXPRESSION COLON SPACE WORD SPACE ASSIGNMENT SPACE string EOL svg','shelf',25,'p_shelf','view_parser.py',94),
  ('action -> SPACE WORD COLON EOL SPACE description SPACE cblock EOL svg','action',10,'p_action','view_parser.py',100),
  ('cblock -> CBLOCK COLON SPACE methods EOL','cblock',5,'p_cblock','view_parser.py',105),
  ('methods -> methoddef','methods',1,'p_methods','view_parser.py',109),
  ('methods -> methods EOL SPACE methoddef','methods',4,'p_methods','view_parser.py',110),
  ('methoddef -> string','methoddef',1,'p_methoddef','view_parser.py',114),
  ('variables -> VARIABLES COLON vars EOL','variables',4,'p_variables','view_parser.py',118),
  ('vars -> <empty>','vars',0,'p_vars','view_parser.py',122),
  ('vars -> var','vars',1,'p_vars','view_parser.py',123),
  ('vars -> vars EOL var','vars',3,'p_vars','view_parser.py',124),
  ('inout -> IN','inout',1,'p_inout','view_parser.py',128),
  ('inout -> OUT','inout',1,'p_inout','view_parser.py',129),
  ('vtype -> INT','vtype',1,'p_vtype','view_parser.py',133),
  ('vtype -> BOOL','vtype',1,'p_vtype','view_parser.py',134),
  ('var -> SPACE inout SPACE WORD SPACE vtype SPACE string','var',8,'p_var','view_parser.py',138),
  ('title -> TITLE COLON EOL SPACE description SPACE START_SKEWER COLON SPACE WORD EOL svg','title',12,'p_title','view_parser.py',142),
  ('native_library -> NATIVE_LIBRARY COLON SPACE WORD EOL','native_library',5,'p_native_library','view_parser.py',148),
  ('string -> WORD','string',1,'p_string_word','view_parser.py',152),
  ('string -> string SPACE WORD','string',3,'p_string_row','view_parser.py',157),
  ('end -> END COLON EOL svg','end',4,'p_end','view_parser.py',162),
]
