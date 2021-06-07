import request
    
  payload='<script>alert(XSS);<script>'

  req=request.post(target + payload)

  if payload in req.text:
    print("=vulnerability discovered")
    print("Attacking payload : "+payload)
  else:
    print("Secure")
