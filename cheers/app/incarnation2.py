
import math
import logging
import pdb
import sys
from decimal import Decimal, getcontext
from xml.etree import ElementTree, cElementTree
from xml.dom import minidom

x = 2.31

class MathMethod:
    
    def get_sin(self, r):
        return math.sin(r)
    
    
    def get_cos(self, r):
        return math.cos(r)
    
    
    def get_pi(self):
        '''
        Bailey–Borwein–Plouffe formula
        '''
        getcontext().prec=100
        pi = sum(1/Decimal(16)**k * 
                   (Decimal(4)/(8*k+1) - 
                    Decimal(2)/(8*k+4) - 
                    Decimal(1)/(8*k+5) -
                    Decimal(1)/(8*k+6)) for k in range(100))
        
        return round(pi,4)
    
        
    def convert_degree_radian(self, d):
        return math.radians(d)
    
    
    def convert_radian_degree(self, r):
        return math.degrees(r)


class Incarnation2:
    _math_method = MathMethod()

    def writexml(self, out, radiusValue, alphaValue, outputValue):
        cheers = ElementTree.Element('cheers')
        input = ElementTree.SubElement(cheers, 'input')
        output = ElementTree.SubElement(cheers, 'output')
        radius = ElementTree.SubElement(input, 'radius')
        alpha = ElementTree.SubElement(input, 'alpha')
        radius.text = str(radiusValue)
        alpha.text = str(alphaValue)
        output.text = str(outputValue)
        # tree = cElementTree.ElementTree(cheers) # wrap it in an ElementTree instance, and save as XML
        prettyOutput = minidom.parseString(ElementTree.tostring(
            cheers)).toprettyxml()  # Since ElementTree write() has no pretty printing support, used minidom to beautify the xml.
        finalTree = ElementTree.ElementTree(ElementTree.fromstring(prettyOutput))
        finalTree.write(out, encoding='utf-8', xml_declaration=False)



    def find_alpha(self):
        '''
        x - sinx = pi/2
        - sinx = pi/2 -x
        sinx = -(pi/2-x)
        sin(sinx) = sin(-(pi/2 -x))     ( sin(-x) = -sinx)
        sin(sinx) = -sin(pi/2 -x)
        sin(sinx) + sin(pi/2 -x)
        sin(sinx) + cos(x) = 0         ( sin(90 - x) = cos x)
        
        '''
        sin_value = self._math_method.get_sin(self._math_method.get_sin(x))
        cos_value = self._math_method.get_cos(x)
      
        if round(sin_value,2) + round(cos_value,2) == 0:
            print("Alpha: "+ str(x))
            return x
        else:
            print("x is not an alpha")
            return
    
    
    def get_length_of_segment(self, R):
        '''
        R radius of coasters
        '''
        try:
            if '--debugger' in sys.argv:
                pdb.set_trace()
            alpha = self.find_alpha()
            cos_value = self._math_method.get_cos(alpha/2)
            l = 2*R * (1 - cos_value)
            return l
        except Exception as e:
            print(e)
            return 
        

if __name__ == "__main__":
    
    # Logger
    logging.basicConfig(filename='cheers.log',
                        level=logging.INFO,
                        format='%(asctime)s: %(name)-4s: %(levelname)-4s: %(message)s',
                        datefmt='%Y-%m-%d %Hh %Mm %Ss')

    logging.info("start the process")
    _incarnationObj = Incarnation2()
    outputStream = open("out.xml", "wb")
    header = str('<?xml version="1.0" encoding="UTF-8" ?><!DOCTYPE cheers SYSTEM "cheers.dtd">\n')
    outputStream.write(str.encode(header))
    #while True:
    try:
            r = input("Please enter the value of radius: ") 
            l = round(_incarnationObj.get_length_of_segment(float(r)),2)
            print("length of segment of coasters: "+str(l)+ " whose radius "+ str(r))
            _incarnationObj.writexml(outputStream, r, x, l)

    except Exception as e:
            print("please enter the valid input")
            print(e)
            outputStream.close()