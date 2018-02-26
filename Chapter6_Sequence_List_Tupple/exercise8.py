#!/usr/bin/env python
#-*- coding : utf-8 -*-
import string
'''数字转换为英文单词'''


unit = ['one','two','three','four','five','six','seven','eight','nine','zero']
tens_units = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def num2Eng(int(number)):
    if number < 0 or number > 1000:
        print 'Input number error!'
        return 0
#    elif number == 0:
#        return repr(num)+"zero"
    elif number == 1000:
        return repr(num)+':one-thousand'
    else:  
        num_hun,num_ten,num_unit=str(num).rjust(3,'0')[0:3]  
        num_unit,num_ten,num_hun=int(num_unit),int(num_ten),int(num_hun)  
        if num_hun==1:  
            Eng_num=Eng_num+' one-hundred'  
        elif (num_hun)>1:  
            Eng_num=Eng_num+' '+unit[num_hun-1]+'-hundreds'  
  
        if num_hun!=0 and (num_ten or num_unit):  
            Eng_num=Eng_num+' and'  
  
        if num_ten==0:  
            Eng_num=Eng_num+' '+unit[num_unit-1]  
        elif num_ten==1:  
            Eng_num=Eng_num+' '+tens_units[num_unit]  
        else:  
            Eng_num=Eng_num+' '+tens[num_ten]  
            if num_unit!=0:  
                Eng_num=Eng_num+'-'+unit[num_unit-1]  
        print repr(num)+':'+Eng_num
