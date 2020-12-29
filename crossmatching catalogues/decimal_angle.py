def hms2dec(h, m, s):
  return 15*(h + m/60 + s/3600) 
def dms2dec(d, m, s):
  if d >= 0:
    return (abs(d) + m/60 + s/3600)
  else:
    return -(abs(d) + m/60 + s/3600)

