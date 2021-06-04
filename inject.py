import request


def main():
  target=raw_input("Url inject: ")
  type=input('''
  [1]Javascipt
  [2]html
  [3]php
  
  > ''')
  if type=1:
    choice=input('''
    [1]injection.js
    
    > ''')
    if choice=1:
      inject_payload=open('injection.js','r').read()
  
  if type=="2":
    choice=input('''
    [1]template_injection.html
    [2]basic_injection.html
    [3]xss.html
    
    > ''')
    
    if choice=='1':
      inject_payload=open('template_injection.html','r').read()
      
      while True:
        print('payload injection is sucessful')
        break
      
      while False:
        print('payload injection fail')
        break
    
    if choice=='2':
      inject_payload=open('basic_injection.html','r').read()
      
      while True:
        print('payload injection is sucessful')
        break
      
      while False:
        print('payload injection fail')
        break
        
    if choice=='3':
      inject_payload=open('xss.html','r').read()
      
      while True:
        print('payload injection is sucessful')
        break
      
      while False:
        print('payload injection fail')
        break
    
  payload=inject_payload

  req=request.post(target + payload)

  if payload in req.text:
    print("=vulnerability discovered")
    print("Attacking payload : "+payload)
  else:
    print("Secure")
    
if __name__=="__main__":
  main()
