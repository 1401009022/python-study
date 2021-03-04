#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
import base64

flagstr = "YnumCRmcnumBhvdnumCsnumCNnumBJkYTNhMSnumJnumBZDJmLTQxMDItYmRjNSnumAkYnumBInumDNzNiODknumANjVnumI"

flag = ""
flag = flag+flagstr.replace("numA",'1').replace("numB",'2').replace("numC",'3').replace("numD",'4').replace("numE",'5').replace("numF",'6').replace("numG",'7').replace("numH",'8').replace("numI",'9').replace("numJ",'0')
# flag = flag+flagstr.replace("numB",'2')
# flag = flag+flagstr.replace("numC",'3')
# flag = flag+flagstr.replace("numD",'4')
# flag = flag+flagstr.replace("numE",'5')
# flag = flag+flagstr.replace("numF",'6').replace("numG",'7').replace("numH",'8').replace("numI",'9').replace("numJ",'0')
# flag = flag+flagstr.replace("numG",'7')
# flag = flag+flagstr.replace("numH",'8')
# flag = flag+flagstr.replace("numI",'9')
# flag = flag+flagstr.replace("numJ",'0')
print(flag)
print(base64.b64decode(flag))