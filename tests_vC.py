import pytest
from ex01 import count_au

def test_count_au_0():
  assert(count_au(42)==0)

def test_count_au_1():
  assert(count_au('mai')==1)

def test_count_au_2():
  assert(count_au('MAYA')==2)

def test_count_au_3():
  assert(count_au('maui')==2)

def test_count_au_4():
  assert(count_au('moana')==2)

def test_count_au_5():
  assert(count_au('Auckland')==3)


from ex01 import maxOfTwoLists

def test_maxOfTwoLists_0():
  assert(maxOfTwoLists(42, [1])==False)

def test_maxOfTwoLists_1():
  assert(maxOfTwoLists(['ox'],['cat'])==['cat'])

def test_maxOfTwoLists_2():
  assert(maxOfTwoLists(['ox','bear'],['cat', 'cow'])==['cat', 'bear'])

def test_maxOfTwoLists_3():
  assert(maxOfTwoLists(['bear','cow'],['ox','cat'])==['bear', 'cow'])

def test_maxOfTwoLists_4():
  assert(maxOfTwoLists(['bear','cow','crow','sparrow'],\
                       ['ox','cat','mouse','ox'])==\
                       ['bear', 'cow','mouse','sparrow'])
  
def test_maxOfTwoLists_5():
  assert(maxOfTwoLists(['bear','cow','crow'],['ox','cat','mouse'])==\
         ['bear', 'cow','mouse'])

