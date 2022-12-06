import calendar

#Makes

def monthly(s = '1 2018', *allelse):
    mmm = 0
    print('s=',s)
    try:
        s = s.replace(',', '')
        m,y = s.split(' ')
    except exception as e:
        print(e)
        try:
            m,y = s.spit(',')
        except exception as e:
            print(e)
            m = 1
            y = 2020
    
        
    print('>', m, y)
    
    if not (str.isnumeric((m[:1]))):
        try:
            mm = str(m[:3].lower())
            print('mm===', mm)
            if mm == 'jan': mmm = 1
            if mm == 'feb': mmm = 2 
            if mm == 'mar': mmm = 3
            if mm == 'apr': mmm = 4
            if mm == 'may': mmm = 5
            if mm == 'jun': mmm = 6
            if mm == 'jul': mmm = 7
            if mm == 'aug': mmm = 8
            if mm == 'sep': mmm = 9
            if mm == 'oct': mmm = 10
            if mm == 'nov': mmm = 11
            if mm == 'dec': mmm = 12
            if mmm == 0: mmm = int(m)
        
            y = int(y)
            m = int(mmm)

            cal = (calendar.month(y,m))
            return(cal,m,y)
        
        except Exception as e:
            print(e)
            return('There was a problem. Try again. \nExample: 12 2020')
            
    else:       
        if int(m) > 12: m = 1
        if int(m) == 0: m = 1
        if int(y) > 10000: y = 2020
        y = int(y)
        m = int(m)

        cal = (calendar.month(y,m))
        return(cal,m,y)

if __name__ == '__main__':

    i = input('enter month year, example: 12 1999 >')
    c,m,y = monthly(i)
    print(c)

    




