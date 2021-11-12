import unittest
from abc import ABC, abstractmethod

class Calculator(ABC):     #In diagram, we have mentioned calculator as interface, I have used calculator as abstract class. 
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
  
    @abstractmethod
    def calculate(self):   
        pass

# Classes for each operations
# In diagram, we have used getter for num1 and num2 but I didnt use it.
class Add(Calculator):

    def calculate(self):
        return self.num1 + self.num2
    
class Sub(Calculator):

    def calculate(self):
        return self.num1 - self.num2

class Mul(Calculator):

    def calculate(self):
        return self.num1 * self.num2

class Div(Calculator):

    def calculate(self):
        if(self.num2 == 0):
           raise Exception("DIVIDE BY ZERO: UNDEFINED")
        return self.num1 / self.num2
        
class Mod(Calculator):

    def calculate(self):
        if(self.num2== 0):
            raise Exception("MODULO BY ZERO: UNDEFINED")
        return self.num1 % self.num2

# In diagram, Display class we didnt mention readInput, storing result 
class Display():
    
    # continueCalculation method is created for performing operations on more than 2 numbers. In diagram we missed to mentioned about working on multiple numbers.
    def continueCalculation(self, num2, operator):
        self.readInput(self.result, num2 , operator)

    # readInput methods takes the input num1, num2 and operator
    def readInput(self, num1, num2, operator):
        #print(num1, num2, operator)
        if(operator == '+'):
            add_obj = Add(num1, num2)
            self.result = add_obj.calculate()

        elif(operator == '-'):
            sub_obj = Sub(num1, num2)
            self.result = sub_obj.calculate()

        elif(operator == '*'):
            mul_obj = Mul(num1, num2)
            self.result = mul_obj.calculate()

        elif(operator == '/'):
            div_obj = Div(num1, num2)
            self.result = div_obj.calculate()

        elif(operator == '%'):
            mod_obj = Mod(num1, num2)
            self.result = mod_obj.calculate()
        
        self.printResult()
# prints the result
    def printResult(self):
        print(self.result)

# clear button functionality
    def clear(self):
        self.result = 0

# Unit test class for testing from subtraction and divide from display class
class Test_Display(unittest.TestCase):
    # tests 10-5 = 5
    def test_subtraction1(self):
        display_object_test1 = Display()
        display_object_test1.readInput(10,5,'-')
        self.assertEqual(display_object_test1.result, 5)

    # tests 10/0 raises DIVIDE BY ZERO: UNDEFINED exception
    def test_divide_by_zero(self):
        try:
            display_object_test2 = Display()
            display_object_test2.readInput(10,0,'/')
        except Exception as e:
            self.assertEqual("DIVIDE BY ZERO: UNDEFINED", str(e))
        else:
            self.fail('DIVIDE BY ZERO exception not raised')
    
    #tests 10/5+2 = 4 
    def test_divide1_subtract(self):
        display_object_test3 = Display()
        display_object_test3.readInput(10,5,'/')
        self.assertEqual(display_object_test3.result, 2)
        display_object_test3.continueCalculation(2,'/')
        self.assertEqual(display_object_test3.result, 1)

    #tests 0/0 raises DIVIDE BY ZERO: UNDEFINED exception
    def test_divide2(self):
        try:
            display_object_test2 = Display()
            display_object_test2.readInput(0,0,'/')
        except Exception as e:
            self.assertEqual("DIVIDE BY ZERO: UNDEFINED", str(e))
        else:
            self.fail('DIVIDE BY ZERO exception not raised')

    # tests 2-5+(-1) = -4
    def test_subtraction2_addition(self):
        display_object_test5 = Display()
        display_object_test5.readInput(2,5,'-')
        self.assertEqual(display_object_test5.result, -3)
        display_object_test5.continueCalculation(-1,'-')
        self.assertEqual(display_object_test5.result, -2)
    
    # tests 0-0 = 0
    def test_subtraction3(self):
        display_object_test6 = Display()
        display_object_test6.readInput(0,0,'-')
        self.assertEqual(display_object_test6.result, 0)

# Unit test class for testing from Sub class
class Test_Sub(unittest.TestCase):

    # tests 2-1 = 1
    def test_sub1(self):
        SubObj_1 = Sub(2,1)
        self.assertEqual(SubObj_1.calculate(), 1)

    #tests 0-0 = 0
    def test_sub2(self):
        SubObj_2 = Sub(0,0)
        self.assertEqual(SubObj_2.calculate(), 0)

    #tests -3-(-4) = 1
    def test_sub3(self):
        SubObj_3 = Sub(-3,-4)
        self.assertEqual(SubObj_3.calculate(), 1)
    
    #tests 438833255083 - 336635816586895 = -336196983331812
    def test_sub4(self):
        SubObj_4 = Sub(438833255083,336635816586895)
        self.assertEqual(SubObj_4.calculate(), -336196983331812)

    #tests -3.456 - (-4.654) = 1.198
    def test_sub5(self):
        SubObj_5 = Sub(-3.456,-4.654)
        self.assertEqual(SubObj_5.calculate(), 1.198)

    #tests -567325325325342 - 87432532523532 = -654757857848874
    def test_sub6(self):
        SubObj_6 = Sub(-567325325325342,87432532523532)
        self.assertEqual(SubObj_6.calculate(), -654757857848874)

    #tests -945837543685.4356 -(-3454325435.42354) = -942383218250.012
    def test_sub7(self):
        SubObj_7 = Sub(-945837543685.4356,-3454325435.42354)
        self.assertEqual(SubObj_7.calculate(), -942383218250.012)

    # tests 0 - 1 = -1 
    def test_sub8(self):
        SubObj_8 = Sub(0,1)
        self.assertEqual(SubObj_8.calculate(), -1)

# Unit test class for testing from Div class
class Test_Div(unittest.TestCase):
    #tests 2 / 1 = 2
    def test_div1(self):
        DivObj_1 = Div(2,1)
        self.assertEqual(DivObj_1.calculate(), 2)

    #tests 0 / 0 raises DIVIDE BY ZERO: UNDEFINED exception 
    def test_div2(self):
        try:
            DivObj_2 = Div(0,0)
            DivObj_2.calculate()
        except Exception as e:
            self.assertEqual("DIVIDE BY ZERO: UNDEFINED", str(e))
        else:
            self.fail('DIVIDE BY ZERO exception not raised')

    #tests 2.56/1.45 =1.7655172413793105
    def test_div3(self):
        DivObj_3 = Div(2.56,1.45)
        self.assertEqual(DivObj_3.calculate(), 1.7655172413793105)

    #tests -4.5 / -9.5 = 0.47368421052631576
    def test_div4(self):
        DivObj_4 = Div(-4.5,-9.5)
        self.assertEqual(DivObj_4.calculate(), 0.47368421052631576)

    # tests 167880 / 0 raises DIVIDE BY ZERO: UNDEFINED exception 
    def test_div5(self):
        try:
            DivObj_2 = Div(167880,0)
            DivObj_2.calculate()
        except Exception as e:
            self.assertEqual("DIVIDE BY ZERO: UNDEFINED", str(e))
        else:
            self.fail('DIVIDE BY ZERO exception not raised')
    
    #tests -567325325325342/87432532523532 = -6.488721176784504
    def test_div6(self):
        DivObj_6 = Div(-567325325325342,87432532523532)
        self.assertEqual(DivObj_6.calculate(), -6.488721176784504)

    # tests -945837543685.4356 / -3454325435.42354 = 273.81251748489785
    def test_div7(self):
        DivObj_7 = Div(-945837543685.4356,-3454325435.42354)
        self.assertEqual(DivObj_7.calculate(), 273.81251748489785)

    # tests 0 / 1 = 0
    def test_div8(self):
        DivObj_8 = Div(0,1)
        self.assertEqual(DivObj_8.calculate(), 0)

# Driver/main function
if __name__== "__main__" :

    # Executing tests
    unittest.main(exit=False)

    display_object = Display()  
    display_object.readInput(10,0,'+')
    display_object.readInput(10,5,'/')
    display_object.continueCalculation(5,'/')
    display_object.continueCalculation(5,'+')
    display_object.continueCalculation(4,'/')

    SubObj = Sub(-10,11)
    print(SubObj.calculate())
    
    DivObj = Div(5,2)
    print(DivObj.calculate())
