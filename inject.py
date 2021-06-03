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
      
      
  payload=inject

  req=request.post(target + payload) dd

  if payload in req.text:
    print("=vulnerability discovered")
    print("Attacking payload : "+payload)
  else:
    print("Secure")
    
if __name__=="__main__":
  main()
